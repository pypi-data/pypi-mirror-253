# Copyright (C) 2021 Matthias Nadig

import os
import sys
import time
import threading
import queue
import traceback
import atexit
import yaml
from datetime import datetime

from ._codes import ERASE_LINE, CARRIAGE_RETURN
from ._codes import COLOR_DEFAULT_FONT_FG, COLOR_DEFAULT_FONT_BG
from ._codes import RESET
from ._codes import RED, LIGHT_GRAY
from ._codes import PROGBAR_INIT, PROGBAR_ACTIVE, PROGBAR_DONE
from ._codes import DEFAULT_STR_INFO, DEFAULT_CHANNEL
from ._codes import DEBUG, INFO, WARN, ERROR
from ._channels import Channel
from ._progbars import ProgbarKnownLength, ProgbarUnknownLength
from ._timeformat import format_time

from ._cli import activate_esc, deactivate_esc


exception = None
global_channels = []

t_start = time.time()


def _print(s):
    # sys.stdout.write(s)
    print(s, end='')


def _get_print_thread(target):
    return threading.Thread(target=target, daemon=True)


class Logger:
    def __init__(self, path_logfiles, filename_main_channel, layout_leading_line='oneliner'):
        # FOR DEBUGGING
        # print('Logger.__init__')

        self._path_logfiles = path_logfiles

        # Refresh rate and timer for calculating minimum interval between terminal outputs
        self.refresh_interval = 0  # will be overwritten by refresh rate set below
        self.set_refresh_rate(25)
        self.t_last_update = time.time() - self.refresh_interval

        # Output event handling
        # self.lock_output = threading.Lock()
        # self.event_wait_interval = threading.Event()
        self.event_print_requested = threading.Event()
        # self.cond_print_requested = threading.Condition()

        # Channels that can be registered, e.g. by different modules
        default_channel = Channel(name=DEFAULT_CHANNEL, show_prefix_module=False, show_prefix_level=False, filename=filename_main_channel, path_logfile=self._path_logfiles)
        self.channels = {
            DEFAULT_CHANNEL: default_channel,
        }

        # Progress bars will always be printed into the most recent line
        # self.progbars = []
        if layout_leading_line == 'table':
            self.leading_line = LeadingLineTable()
        elif layout_leading_line == 'oneliner':
            self.leading_line = LeadingLineOneliner()
        else:
            raise ValueError(layout_leading_line)

        # Activate ANSI escape codes if necessary
        activate_esc()
        _print(COLOR_DEFAULT_FONT_FG + COLOR_DEFAULT_FONT_BG)

        self._q = queue.Queue()
        self._event_stop = threading.Event()

        self._th_print = threading.Thread(target=self._on_print, daemon=True)
        self._th_print.start()

    def is_running(self):
        return not self._event_stop.is_set()

    def on_exit(self):
        """
        Prints total runtime when Python exits
        Note:
            Does not make sense to make this a method of logger. Logger will be cleaned up first (?).
            The Method would then still be executed but can not access attributes of logger anymore.
            Thus, we need to use globals anyway.
        """

        # print('_on_exit 1')
        self._stop_print_daemon()
        # print('_on_exit 2')

        # if exception is None:
        t_elapsed = time.time() - t_start
        str_timer_info = ('\n\nTotal runtime: {} ' + LIGHT_GRAY + '(since logbox import)' + RESET + '\n').format(
            format_time(t_elapsed))
        _print(str_timer_info)

        # Explicitly log time to all channels
        for channel in global_channels:
            channel.on_log(str_timer_info + ' ' + format_time(time.time() - t_start))

        # Deactivate ANSI escape codes if necessary
        # _print(RESET)
        # time.sleep(0.1)
        deactivate_esc()

    def on_exception(self, exc_type, exc_value, exc_traceback):
        """
        Callback for exceptions
        Exceptions will be logged to each channel and then reraised.
        """
        global exception

        # Get current exception
        # exc_type, exc_value, exc_traceback = sys.exc_info()
        # print(exc_type, exc_value, exc_traceback)

        # Handle exception in case there is one
        if exc_type is not None:
            # Note the exception for exit handling (global)
            exception = (exc_type, exc_value, exc_traceback)

            # Parse the traceback
            str_traceback = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
            str_traceback = RED + str_traceback

            self.leading_line.stop_on_exit()

            # Write error report to channels
            # print('\n\nLogger traceback:\n', str_traceback)
            # print('\n' + str_traceback)
            for _, channel in self.channels.items():
                channel.on_error('\n\n' + str_traceback)

            # Wait until all outputs have been printed
            self._stop_print_daemon()
            # print('on_exception', exc_type)

            return self._reraise(exc_type, exc_value, exc_traceback)

        # Wait until all outputs have been printed
        # print('on_exception', exc_type)
        self._stop_print_daemon()

    # def __del__(self):
    #     print('__del__')
    #     # Wait until all outputs have been printed
    #     self._wait_for_print_finished()

    def _stop_print_daemon(self):
        self._event_stop.set()
        self._q.join()
        self._th_print.join()

    def print_time_since_start(self, *args):
        """ Print the total runtime since the logger has been started """
        t_elapsed = time.time() - t_start
        self.print_time(*args, t_elapsed)

    def print_time(self, *args):
        t = args[-1]
        str_time = format_time(t)
        self.print(*args[:-1], str_time)

    def _reraise(self, exc_type, exc_value, exc_traceback):
        # Re-raise the exception
        return sys.__excepthook__(exc_type, exc_value, exc_traceback)

    def set_refresh_rate(self, refresh_rate):
        """ Calculate refresh interval [s] given a refresh rate [Hz] """
        self.refresh_interval = 1 / refresh_rate

    def print(self, *str_new, level=INFO, channel=DEFAULT_CHANNEL, use_style=True):
        """ Method that will be invoked by logger.info(...) or logger.warn(...) """

        # Can be given multiple arguments to be joined into one string (as Python's standard print-function)
        str_new = ' '.join([str(item) for item in str_new])

        # Get channel (in case name is given)
        channel = self._get_channel(channel)

        # Apply style if requested
        if use_style:
            str_new = self._apply_params(str_new, level, channel)
        else:
            str_new += '\n'

        # Write to enabled logfiles
        channel.on_log_tree(str_new)

        # Queue to terminal outputs
        # with self.lock_output:
        #     self.outputs.append(str_new)
        self._q.put(str_new)

        # self.notify_print()

    def notify_print(self):
        """ Serves as callback for progbar to request a print update """
        self.event_print_requested.set()

    def _get_channel(self, channel):
        """ Chooses corresponding channel if specified by name """

        # In case string is given, select channel by name
        if isinstance(channel, str):
            for channel_name, channel_check in self.channels.items():
                if channel_name == channel:
                    channel = channel_check
                    break
            else:
                raise ValueError('Channel could not be found by name: \'{}\''.format(channel))

        return channel

    def _apply_params(self, str_new, level, channel):
        """ Given string will be added prefixes, colors, etc. based on channel parameters """

        # Prefix to be added to every line of output
        prefix_line = ''
        prefix_line = channel.prefix_line_debug if level == DEBUG else prefix_line
        prefix_line = channel.prefix_line_info if level == INFO else prefix_line
        prefix_line = channel.prefix_line_warn if level == WARN else prefix_line
        prefix_line = channel.prefix_line_error if level == ERROR else prefix_line

        # Appendix to be added to every line of output
        appendix_line = ''
        appendix_line = channel.appendix_line_debug if level == DEBUG else appendix_line
        appendix_line = channel.appendix_line_info if level == INFO else appendix_line
        appendix_line = channel.appendix_line_warn if level == WARN else appendix_line
        appendix_line = channel.appendix_line_error if level == ERROR else appendix_line

        # Disassemble output into lines
        lines = str_new.split('\n')

        # Reassemble lines
        #   1. Set font and background color
        #   2. Concatenate lines by inserting prefix and appendix for each line
        #   3. Reset all parameters
        # print(appendix_line+'\n'+prefix_line, lines)
        str_new = \
            prefix_line + \
            str(appendix_line+RESET+prefix_line).join(lines) + \
            appendix_line + RESET

        return str_new

    def _on_print(self):
        """
        Print current output
        First check refresh timer, sleep if necessary and then print.
        """

        while self.is_running():
            # Sleep until end of refresh interval
            t_wait = max(0.0, self.refresh_interval - (time.time() - self.t_last_update))
            time.sleep(t_wait)

            outputs = []
            # try:
            #     outputs.append(self._q.get(block=True, timeout=self.refresh_interval))
            # except queue.Empty():
            #     continue
            while not self._q.empty():
                outputs.append(self._q.get(block=False))
                self._q.task_done()

            # Print only if outputs had been queued or the print-request was set by any of the progbars
            if len(outputs) > 0 or self.event_print_requested.is_set():
                # Reset event
                self.event_print_requested.clear()

                # Assemble strings for leading line
                leading_line_done, leading_line_active = self.leading_line.get_leading_line()

                # Update timer and reset flag
                self.t_last_update = time.time()

                # Remove previous leading line and add the current one
                str_out = ERASE_LINE + CARRIAGE_RETURN + RESET + leading_line_done + ''.join(outputs) + leading_line_active

                if len(outputs) > 0:
                    self.leading_line.is_headline_overwritten = True
                else:
                    self.leading_line.is_headline_overwritten = False

                # Print to terminal
                _print(str_out)

    def register(self, name, mode='sub', name_parent=DEFAULT_CHANNEL, **params):
        """ Method that will be invoked by logger.register(...) to set up a new channel """

        if name in self.channels:
            raise RuntimeError(f'Channel with name "{name}" already registered')

        if mode == 'parallel':
            # Channel without parent (does not report to default main channel)
            channel = Channel(name=name, path_logfile=self._path_logfiles, **params)
        elif mode == 'sub':
            # Channel is child of another channel (typically default main channel)
            if name_parent not in self.channels:
                raise RuntimeError(f'Parent channel "{name_parent}" does not exist')
            parent = self.channels[name_parent]
            channel = Channel(name=name, path_logfile=self._path_logfiles, **params, parent=parent)
            parent.note_new_child(channel)
        else:
            raise ValueError(mode)

        global global_channels
        global_channels.append(channel)
        self.channels[name] = channel

        return channel

    def register_progbar(self, limit_updates=None, str_info=DEFAULT_STR_INFO, channel=DEFAULT_CHANNEL):
        """ Method that will be invoked by logger.register_progbar(...) to set up a new progbar """
        channel = self._get_channel(channel)
        return self.leading_line.register_progbar(channel,
                                                  limit_updates=limit_updates,
                                                  str_info=str_info)


class LeadingLineOneliner:
    def __init__(self):
        self.delimiter_progbars = ' | '
        self.str_leading_line = ''

        self.is_headline_overwritten = True

        self.progbars = []
        self.channels = []

    def register_progbar(self, channel, limit_updates=None, str_info=DEFAULT_STR_INFO):
        """ Method that will be invoked by logger.register_progbar(...) to set up a new progbar """

        if limit_updates is None:
            progbar = ProgbarUnknownLength(callback_on_update=_notify_print, str_info=str_info, style=COLOR_DEFAULT_FONT_FG+COLOR_DEFAULT_FONT_BG)
        else:
            progbar = ProgbarKnownLength(limit_updates=limit_updates, callback_on_update=_notify_print, str_info=str_info, style=COLOR_DEFAULT_FONT_FG+COLOR_DEFAULT_FONT_BG)
        self.progbars.append(progbar)
        self.channels.append(channel)

        return progbar

    def stop_on_exit(self):
        """ Handle exit when exception has been raised """

        # Write to log files
        for channel, progbar in zip(self.channels, self.progbars):
            str_progbar_canceled = \
                progbar.parse_leading_line() + \
                '\n\t\u2ba9 Process "{}" stopped due to error (see traceback below).\n'.format(progbar.str_info)
            channel.on_log_tree(str_progbar_canceled)

        # Remove all progbars
        for progbar in self.progbars:
            progbar.stop()

    def get_leading_line(self):
        return self._get_leading_line()

    def _get_leading_line(self):
        """
        Leading line contains progress bar
        This line is always removed and again appended to the output (while any progbar is active).
        """

        indices_active = []
        indices_done = []

        for index_progbar, progbar in enumerate(self.progbars):
            if progbar.state == PROGBAR_ACTIVE:
                indices_active.append(index_progbar)
            elif progbar.state == PROGBAR_DONE:
                indices_done.append(index_progbar)

        leading_line_active = self._parse_leading_line_active(indices_active)
        leading_line_done = self._parse_leading_line_done(indices_done)

        # Remove progbars that are done
        for index_progbar in reversed(indices_done):
            del self.progbars[index_progbar]
            del self.channels[index_progbar]

        # When any progbar is active, always append the "logbox symbol" to the end of the leading line
        if len(leading_line_active) > 0:
            style = COLOR_DEFAULT_FONT_FG + COLOR_DEFAULT_FONT_BG
            leading_line_active = style + leading_line_active + ' |\u02E1\u1d52\u1d4d\u1d47\u1d52\u02e3' + RESET

        return leading_line_done, leading_line_active

    def _parse_leading_line_active(self, indices_progbar):
        leading_line = []
        delimiter = self.delimiter_progbars
        for index_progbar in indices_progbar:
            leading_line.append(self.progbars[index_progbar].parse_leading_line())
        leading_line = delimiter.join(leading_line)
        return leading_line

    def _parse_leading_line_done(self, indices_progbar):
        leading_line = ''
        style = COLOR_DEFAULT_FONT_FG + COLOR_DEFAULT_FONT_BG
        newline = '\n' + RESET
        appendix = newline + style + '\t\u2ba9 {}, time elapsed: {}'
        for index_progbar in indices_progbar:
            channel, progbar = self.channels[index_progbar], self.progbars[index_progbar]
            str_readiness = 'Complete' if progbar.is_complete() else 'Stopped prematurely'
            str_time_elapsed = format_time(progbar.t_stop - progbar.t_start)
            # str_leading_line = progbar.parse_leading_line() + appendix.format(progbar.str_info, str_time_elapsed)
            str_leading_line = (
                style + progbar.parse_leading_line() +
                # ' |\u02E1\u1d52\u1d4d\u1d47\u1d52\u02e3' +
                appendix.format(str_readiness, str_time_elapsed))
            leading_line += str_leading_line + newline
            channel.on_log_tree(str_leading_line + '\n')
        return leading_line


class LeadingLineTable:
    def __init__(self):
        self.delimiter_progbars = ' | '
        self.str_headline = ''
        self.str_leading_line = ''

        self.is_headline_overwritten = True

        self.progbars = []

        raise NotImplementedError('Usage of logger.LeadingLineTable not recommended and might behave differently than Oneliner')

    def register_progbar(self, limit_updates=None, str_info=DEFAULT_STR_INFO):
        """ Method that will be invoked by logger.register_progbar(...) to set up a new progbar """

        if limit_updates is None:
            progbar = ProgbarUnknownLength(callback_on_update=_notify_print, str_info=str_info)
        else:
            progbar = ProgbarKnownLength(limit_updates=limit_updates, callback_on_update=_notify_print, str_info=str_info)
        self.progbars.append(progbar)

        return progbar

    def get_leading_line(self):
        return self._get_leading_line()

    def _get_leading_line(self):
        """
        Leading line contains progress bar
        This line is always removed and again appended to the output (while any progbar is active).
        """

        indices_active = []
        indices_done = []

        for index_progbar, progbar in enumerate(self.progbars):
            if progbar.state == PROGBAR_ACTIVE:
                indices_active.append(index_progbar)
            elif progbar.state == PROGBAR_DONE:
                indices_done.append(index_progbar)

        headline_active, leading_line_active = self._parse_leading_line(indices_active)
        headline_done, leading_line_done = self._parse_leading_line(indices_done)

        # Remove progbars that are done
        for index_progbar in reversed(indices_done):
            del self.progbars[index_progbar]

        # Compare "active" headline with currently printed one
        n_chars_min = min(len(self.str_headline), len(headline_active))
        if ((self.str_headline == '' or headline_active[:n_chars_min] != self.str_headline[:n_chars_min]) and \
            headline_active[n_chars_min:] != ' ' * len(headline_active[n_chars_min:])) or \
            self.is_headline_overwritten:
            # Headlines differ, append to reprint
            leading_line_active = headline_active + '\n' + leading_line_active  # + ' |\u02E1\u1d52\u1d4d\u1d47\u1d52\u02e3'
            self.str_headline = headline_active

        # Reprint headline of progbars that are done, if not empty
        if headline_done != ' ' * len(headline_done) and (self.is_headline_overwritten or len(indices_active) > 0):
            leading_line_done = headline_done + '\n' + leading_line_done

        # Concatenate leading lines
        if len(leading_line_done) == 0:
            leading_line = leading_line_active
        else:
            leading_line = leading_line_done + '\n' + leading_line_active

        return leading_line

    def _parse_leading_line(self, indices_progbar):
        headline = []
        leading_line = []

        for index_progbar in indices_progbar:
            headline.append(self.progbars[index_progbar].parse_headline())
            leading_line.append(self.progbars[index_progbar].parse_leading_line())

        headline = self.delimiter_progbars.join(headline)
        leading_line = self.delimiter_progbars.join(leading_line)

        return headline, leading_line


'''
def _on_exit():
    """
    Prints total runtime when Python exits
    Note:
        Does not make sense to make this a method of logger. Logger will be cleaned up first (?).
        The Method would then still be executed but can not access attributes of logger anymore.
        Thus, we need to use globals anyway.
    """

    print('_on_exit 1')
    logger._event_stop.set()
    logger._q.join()
    logger._th_print.join()
    print('_on_exit 2')

    # if exception is None:
    t_elapsed = time.time() - t_start
    str_timer_info = ('\n\nTotal runtime: {} ' + LIGHT_GRAY + '(since logbox import)' + RESET + '\n').format(format_time(t_elapsed))
    _print(str_timer_info)

    # Explicitly log time to all channels
    for channel in global_channels:
        channel.on_log(str_timer_info + ' ' + format_time(time.time()-t_start), global_default_channel)
    
    # Deactivate ANSI escape codes if necessary
    # _print(RESET)
    # time.sleep(0.1)
    deactivate_esc()
'''


# Get directory for logfiles and filename for default channel
filename_params = os.path.join(os.path.dirname(__file__), 'params.yml')
# print(f'filename yaml: "{filename_params}"')
with open(filename_params, 'r') as f:
    c = yaml.load(f, yaml.Loader)
    # print(f'content yaml: {type(c)}, {c}')
env_dirname = os.environ['LOGBOX_LOGFILES_DIR'] if 'LOGBOX_LOGFILES_DIR' in os.environ else None
env_filename = os.environ['LOGBOX_MAIN_LOGFILE_NAME'] if 'LOGBOX_MAIN_LOGFILE_NAME' in os.environ else None
params_filename = c['DEFAULT_LOGFILE_NAME']
path_logfiles = None
str_warn_nodir = None
if 'LOGFILES_DIR' in c:
    params_dirname = c['LOGFILES_DIR']
    if params_dirname is not None:
        # Folder must exist
        if not os.path.isdir(params_dirname):
            raise NotADirectoryError(f'"{params_dirname}"')
        path_logfiles = params_dirname
elif env_dirname is not None:
    if env_dirname != '?':
        # Folder must exist
        if not os.path.isdir(env_dirname):
            raise NotADirectoryError(f'"{env_dirname}"')
        path_logfiles = env_dirname
else:
    str_warn_nodir = '\n'.join([
        f'No default directory specified for logfiles!',
        f'Disable warning by one of the following:',
        f'\t* set environment variable LOGBOX_LOGFILES_DIR=?',
        f'\t* uncomment line "LOGFILES_DIR: null" in {filename_params}',
    ])
if path_logfiles is None:
    path_logfiles = '.'
subfolder_template = f'log_{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}' + '_{}'
counter = 1
path_logfiles = os.path.join(path_logfiles, subfolder_template.format(counter))
while os.path.isdir(path_logfiles):
    counter += 1
    path_logfiles = os.path.join(path_logfiles, subfolder_template.format(counter))
filename_main_channel = None
if params_filename is not None:
    if os.path.isabs(params_filename):
        path_filename_main_channel = os.path.dirname(params_filename)
        # Folder must exist
        if not os.path.isdir(path_filename_main_channel):
            raise NotADirectoryError(f'"{path_filename_main_channel}"')
    filename_main_channel = params_filename
elif env_filename is not None:
    if os.path.isabs(env_filename):
        path_filename_main_channel = os.path.dirname(env_filename)
        # Folder must exist
        if not os.path.isdir(path_filename_main_channel):
            raise NotADirectoryError(f'"{path_filename_main_channel}"')
    filename_main_channel = env_filename
if filename_main_channel is not None and os.path.isfile(filename_main_channel):
    # raise FileExistsError(f'"{filename_main_channel}"')
    # File will be appended
    pass

# Logger is started here to handle output to the terminal and can be used by functions below
logger = Logger(path_logfiles=path_logfiles, filename_main_channel=filename_main_channel)

# Exceptions should always be given to the logger
sys.excepthook = logger.on_exception

# When program exits (with or without exception) the logger should be informed
atexit.register(logger.on_exit)


def _info(*str_out, channel=DEFAULT_CHANNEL):
    """ Print multiple arguments (info level) """
    logger.print(*str_out, level=INFO, channel=channel, use_style=True)


def _warn(*str_out, channel=DEFAULT_CHANNEL):
    """ Print multiple arguments (warn level) """
    logger.print(*str_out, level=WARN, channel=channel, use_style=True)


def _register(name_channel, mode='sub', **params):
    """
    Register a new channel
    E.g. different modules can set up their own channels for logging.
    """
    return logger.register(name_channel, mode=mode, **params)


def _register_progbar(limit_updates=None, str_info=DEFAULT_STR_INFO, channel=DEFAULT_CHANNEL):
    """
    Register a new progbar
    E.g. done by log_range(...) and other iterators.
    """
    return logger.register_progbar(limit_updates=limit_updates,
                                   str_info=str_info,
                                   channel=channel)


def _notify_print():
    """ Invoke notify_print() to force print of most recent output """
    return logger.notify_print()


def _print_time_since_start(*str_out):
    """
    Print the total runtime since the logger has been started
    Note: The time will automatically be appended to the given output string.
    """
    logger.print_time_since_start(*str_out)


def _print_time(*args):
    """
    Print the given time interval (last item of args)
    """
    logger.print_time(*args)


# Notify user of paths
if str_warn_nodir is not None:
    _warn(str_warn_nodir)
str_info_paths = f'Logbox paths:'
if filename_main_channel is None:
    str_info_paths += f'\n\t* All logfiles -> "{os.path.normpath(path_logfiles)}"'
else:
    str_info_paths += f'\n\t* Main channel -> "{os.path.normpath(filename_main_channel)}"'
    str_info_paths += f'\n\t* Sub-channels -> "{os.path.normpath(path_logfiles)}' + os.path.sep + '"'
_info(str_info_paths)
