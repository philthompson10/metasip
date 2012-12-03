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


from dip.model import Bool, Interface, List, Str

from .i_header_file_version import IHeaderFileVersion


class IHeaderFile(Interface):
    """ The IHeaderFile interface is implemented by models that represent a
    C/C++ .h file.
    """

    # This is set if the header file is being ignored, i.e. it will never be
    # assigned to a module.
    ignored = Bool(False)

    # The name of the optional module that the header file is assigned to.
    module = Str()

    # The basename of the header file.
    name = Str()

    # The individual versions of the header file.  Note that these are
    # unordered.
    versions = List(IHeaderFileVersion)
