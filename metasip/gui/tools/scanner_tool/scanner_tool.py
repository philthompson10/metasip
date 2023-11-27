# Copyright (c) 2023 Riverbank Computing Limited.
#
# This file is part of metasip.
#
# This file may be used under the terms of the GNU General Public License v3
# as published by the Free Software Foundation which can be found in the file
# LICENSE-GPL3.txt included in this package.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.



from ...shell_tool import ShellTool, ShellToolLocation

from .gui import ScannerWidget


class ScannerTool(ShellTool):
    """ This class implements a tool for handling the scanning of a project's
    header directories.
    """

    def __init__(self, shell):
        """ Initialise the tool. """

        super().__init__(shell)

        self._scanner_widget = ScannerWidget(self)

    def event(self, event_type, event_arg):
        """ Reimplemented to handle project-specific events. """

        #if event_type is EventType.PROJECT_NEW:
        #    self._api_editor.set_project(self.shell.project)

    @property
    def location(self):
        """ Get the location of the tool in the shell. """

        return ShellToolLocation.RIGHT

    @property
    def name(self):
        """ Get the tool's name. """

        return 'metasip.tool.scanner'

    def restore_state(self, settings):
        """ Restore the tool's state from the settings. """

        #state = settings.value(self.name)
        #if state is not None:
        #    self._api_editor.widget_state = state

    def save_state(self, settings):
        """ Save the tool's state in the settings. """

        #settings.setValue(self.name, self._api_editor.widget_state)

    @property
    def title(self):
        """ Get the tool's title. """

        return "Scanner"

    @property
    def widget(self):
        """ Get the tool's widget. """

        return self._scanner_widget
