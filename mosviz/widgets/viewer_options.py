from __future__ import print_function, division, absolute_import

from qtpy.QtWidgets import QWidget

__all__ = ["OptionsWidget"]


class OptionsWidget(QWidget):
    def __init__(self, parent=None, data_viewer=None):
        super(OptionsWidget, self).__init__(parent=parent)
