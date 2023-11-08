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


from .exceptions import ValidationTypeError
from .value_type_factory import ValueTypeFactory


class Int(ValueTypeFactory):
    """ The Int class encapsulates a Python integer. """

    def __init__(self, default=0, allow_none=False, allow_rebind=True, getter=None, setter=None, **metadata):
        """ Initialise the object.

        :param default:
            the default value of the integer.
        :param allow_none:
            ``True`` if ``None`` is a valid value.  The default is ``False``.
        :param allow_rebind:
            ``True`` if the attribute can be re-bound after the model has been
            instantiated.
        :param getter:
            is the optional attribute getter.
        :param setter:
            is the optional attribute setter.
        :param \*\*metadata:
            is additional meta-data stored with the type.
        """

        super().__init__(default, allow_none, allow_rebind, getter, setter,
                metadata)

    def validate(self, value):
        """ Validate an integer according to the constraints.  An exception is
        raised if the integer is invalid.

        :param value:
            the integer to validate.
        :return:
            the validated integer.
        """

        if self.validate_none(value):
            return value

        if not isinstance(value, int):
            try:
                value = int(value)
            except:
                raise ValidationTypeError(type(self), int, value)

        return value