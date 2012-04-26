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


from dip.model import Bool, Instance, Str

from .i_access import IAccess
from .i_class import IClass
from .i_code import ICode


class IDestructor(ICode, IAccess):

    container = Instance(IClass)

    methcode = Str()

    name = Str()

    virtcode = Str()

    virtual = Bool(False)
