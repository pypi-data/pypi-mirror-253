# Copyright (C) 2021 Matthias Nadig

import os

from ._codes import _parse_font_color_from_rgb, _parse_background_color_from_rgb
from ._codes import COLOR_DEFAULT_FONT_FG, COLOR_DEFAULT_FONT_BG
from ._codes import ORANGE
from ._codes import RESET
from ._codes import ENCODING_LOGFILES


_n_chars_name_max = 0
_fn_update = []


def _update_all():
    for fn in _fn_update:
        fn()


class Channel:
    def __init__(self,
                 name=None,
                 color_font=None, color_bg=None,
                 show_prefix_module=True,
                 show_prefix_level=True,
                 path_logfile=None,
                 filename=None,
                 parent=None):
        global _n_chars_name_max
        global _fn_update

        self.name = name
        self.color_font = COLOR_DEFAULT_FONT_FG if color_font is None else _parse_font_color_from_rgb(color_font)
        self.color_bg = COLOR_DEFAULT_FONT_BG if color_bg is None else _parse_background_color_from_rgb(color_bg)
        self.show_prefix_module = show_prefix_module
        self.show_prefix_level = show_prefix_level

        self._path_logfile = path_logfile

        _n_chars_name_max = max(_n_chars_name_max, len(self.name))
        _fn_update.append(self._update_style)
        _update_all()

        self._parent = parent
        self._children = []

        self.f = None
        if filename is not None:
            self.open_logfile(filename=filename)

    def open_logfile(self, filename):
        if self.f is not None:
            raise RuntimeError('Logfile already specified')
        if not os.path.isabs(filename):
            filename = os.path.join(self._path_logfile, filename)
        self.f = _open_logfile(filename=filename)

    # The method create_child might be handy, but for now this creates too much spaghetti code:
    # Handy because could be used to create child from channel by user directly.
    # Spaghetti code because it must somehow report to logger, that child has been created.
    '''
    def create_child(self, **params):
        child = Channel(**params, parent=self)
        self.note_new_child(child)
        return child
    '''

    def note_new_child(self, child):
        self._children.append(child)

    def _update_style(self):
        self.prefix_line_debug = ''
        self.prefix_line_info = ''
        self.prefix_line_warn = ''
        self.prefix_line_error = ''
        
        if self.show_prefix_module and self.name is not None:
            # Start with channel-specific color, then write name of channel to beginning of line and reset font color
            prefix_name = (
                self.color_font + self.color_bg +
                self.name + (' ' * (_n_chars_name_max - len(self.name))) + ' |' +
                RESET + ' '
            )
            self.prefix_line_debug += prefix_name
            self.prefix_line_info += prefix_name
            self.prefix_line_warn += prefix_name
            self.prefix_line_error += prefix_name

        if self.show_prefix_level:
            self.prefix_line_debug += '(D) '
            self.prefix_line_info += '(I) '
            self.prefix_line_warn += '(W) '
            self.prefix_line_error += '(E) '

        self.prefix_line_warn += ORANGE + 'WARNING: '

        self.appendix_line_debug = '\n'
        self.appendix_line_info = '\n'
        self.appendix_line_warn = RESET + '\n'
        self.appendix_line_error = '\n'

    def __del__(self):
        if self.f is not None:
            self.f.close()

    def _on_log(self, str_log):
        if self.f is not None:
            self.f.write(str_log)

    def on_log_tree(self, str_log):
        self._on_log(str_log)

        if self._parent is not None:
            self._parent.on_log(str_log)

    def on_log(self, str_log):
        self._on_log(str_log)

    def on_error(self, str_log):
        self._on_log(str_log)


def _open_logfile(filename):
    filename_appendix = '.log'
    if not filename.endswith(filename_appendix):
        filename += filename_appendix
    (path_logfile, _) = os.path.split(filename)
    if path_logfile != '':
        os.makedirs(path_logfile, exist_ok=True)
    '''
    n_conflicts = 0
    filename_unique = filename
    while os.path.exists(filename_unique):
        n_conflicts += 1
        filename_unique = filename[:-len(filename_appendix)] + '_conflict{}'.format(n_conflicts) + filename_appendix
    filename = filename_unique
    '''
    return open(filename, 'a+', encoding=ENCODING_LOGFILES)
