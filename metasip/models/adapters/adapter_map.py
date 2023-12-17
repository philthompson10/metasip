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


from ..access import Access
from ..annos import Annos
from ..argument import Argument
from ..callable import Callable
from ..code import Code
from ..code_container import CodeContainer
from ..constructor import Constructor
from ..destructor import Destructor
from ..enum import Enum
from ..enum_value import EnumValue
from ..extended_access import ExtendedAccess
from ..function import Function
from ..header_directory import HeaderDirectory
from ..header_file import HeaderFile
from ..header_file_version import HeaderFileVersion
from ..klass import Class
from ..manual_code import ManualCode
from ..method import Method
from ..module import Module
from ..opaque_class import OpaqueClass
from ..operator_cast import OperatorCast
from ..operator_function import OperatorFunction
from ..operator_method import OperatorMethod
from ..project import Project
from ..sip_file import SipFile
from ..tagged import Tagged
from ..typedef import Typedef
from ..variable import Variable
from ..workflow import Workflow

from .access import AccessAdapter
from .annos import AnnosAdapter
from .argument import ArgumentAdapter
from .callable import CallableAdapter
from .code import CodeAdapter
from .code_container import CodeContainerAdapter
from .constructor import ConstructorAdapter
from .destructor import DestructorAdapter
from .enum import EnumAdapter
from .enum_value import EnumValueAdapter
from .extended_access import ExtendedAccessAdapter
from .function import FunctionAdapter
from .header_directory import HeaderDirectoryAdapter
from .header_file import HeaderFileAdapter
from .header_file_version import HeaderFileVersionAdapter
from .klass import ClassAdapter
from .manual_code import ManualCodeAdapter
from .method import MethodAdapter
from .module import ModuleAdapter
from .opaque_class import OpaqueClassAdapter
from .operator_cast import OperatorCastAdapter
from .operator_function import OperatorFunctionAdapter
from .operator_method import OperatorMethodAdapter
from .project import ProjectAdapter
from .sip_file import SipFileAdapter
from .tagged import TaggedAdapter
from .typedef import TypedefAdapter
from .variable import VariableAdapter
from .workflow import WorkflowAdapter


# The map of adaptable models to adapters.
ADAPTER_MAP = {
    Access:             AccessAdapter,
    Annos:              AnnosAdapter,
    Argument:           ArgumentAdapter,
    Callable:           CallableAdapter,
    Class:              ClassAdapter,
    Code:               CodeAdapter,
    CodeContainer:      CodeContainerAdapter,
    Constructor:        ConstructorAdapter,
    Destructor:         DestructorAdapter,
    Enum:               EnumAdapter,
    EnumValue:          EnumValueAdapter,
    ExtendedAccess:     ExtendedAccessAdapter,
    Function:           FunctionAdapter,
    HeaderDirectory:    HeaderDirectoryAdapter,
    HeaderFile:         HeaderFileAdapter,
    HeaderFileVersion:  HeaderFileVersionAdapter,
    ManualCode:         ManualCodeAdapter,
    Method:             MethodAdapter,
    Module:             ModuleAdapter,
    Namespace:          NamespaceAdapter,
    OperatorCast:       OperatorCastAdapter,
    OperatorFunction:   OperatorFunctionAdapter,
    OperatorMethod:     OperatorMethodAdapter,
    OpaqueClass:        OpaqueClassAdapter,
    Project:            ProjectAdapter,
    SipFile:            SipFileAdapter,
    Tagged:             TaggedAdapter,
    Typedef:            TypedefAdapter,
    Variable:           VariableAdapter,
    Workflow:           WorkflowAdapter,
}
