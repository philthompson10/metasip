# Copyright (c) 2012 Riverbank Computing Limited.
#
# This file is part of metasip.
#
# This file may be used under the terms of the GNU General Public License v3
# as published by the Free Software Foundation which can be found in the file
# LICENSE-GPL3.txt included in this package.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


from dip.model import Bool, Str

from .i_access import IAccess
from .i_class_callable import IClassCallable


class IOperatorMethod(IClassCallable, IAccess):
    """ The IOperatorMethod is implemented by models representing a C++ class
    operator.
    """

    # This is set if the operator is abstract.
    abstract = Bool(False)

    # This is set if the operator is const.
    const = Bool(False)

    # The optional %VirtualCatcherCode.
    virtcode = Str()

    # This is set if the operator is virtual.
    virtual = Bool(False)
