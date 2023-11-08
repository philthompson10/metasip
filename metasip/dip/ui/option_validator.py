# Copyright (c) 2013 Riverbank Computing Limited.
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


from ..model import implements, Model

from .i_validator import IValidator


@implements(IValidator)
class OptionValidator(Model):
    """ The OptionValidator class implements an editor validator for option
    values that cannot be ``None``.
    """

    def configure(self, editor):
        """ Configure an editor to use this validator.

        :param editor:
            is the editor.
        """

    def validate(self, editor):
        """ Validate an editor.

        :param editor:
            is the editor.
        :return:
            a string describing why the value is invalid.  An empty string is
            returned if the value is valid.
        """

        return "no option chosen" if editor.value is None else ''