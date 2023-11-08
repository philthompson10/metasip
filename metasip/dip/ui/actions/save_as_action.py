# Copyright (c) 2018 Riverbank Computing Limited.
#
# This file is part of dip.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


from ..toolkits import UIToolkit

from .. import Action, IAction


class SaveAsAction(Action):
    """ The SaveAsAction class implements the well known :term:`action` to save
    an object under a different name.
    """

    def create(self):
        """ Create the action.

        :return:
            the action.
        """

        if self.id is None:
            self.id = 'dip.ui.actions.save_as'

        return IAction(UIToolkit.save_as_action())