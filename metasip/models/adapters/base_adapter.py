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


from abc import ABC, abstractmethod
from enum import auto, Enum
from xml.sax.saxutils import escape

from .adapt import adapt


class AttributeType(Enum):
    """ The different types of element and model attributes. """

    BOOL = auto()
    LITERAL = auto()
    STRING = auto()
    STRING_LIST = auto()


class BaseAdapter(ABC):
    """ This is the base class for all adapters and provides the ability to
    load and save a model to a project file and to provide a user-friendly, one
    line string representation.
    """

    # The default attribute type map.
    ATTRIBUTE_TYPE_MAP = {}

    def __init__(self, model):
        """ Initialise the adapter. """

        self.model = model

    def load(self, element, ui):
        """ Load the model from the XML element.  An optional user interface
        may be available to inform the user of progress.
        """

        # This default implementation loads attributes define by
        # ATTRIBUTE_TYPE_MAP.
        for name, attribute_type in self.ATTRIBUTE_TYPE_MAP.items():
            if attribute_type is AttributeType.BOOL:
                value = bool(int(element.get(name, '0')))
            elif attribute_type is AttributeType.LITERAL:
                for subelement in element:
                    if subelement.tag == name:
                        value = subelement.text.strip()
                        break
                else:
                    value = ''
            elif attribute_type is AttributeType.STRING:
                value = element.get(name, '')
            elif attribute_type is AttributeType.STRING_LIST:
                value = element.get(name, '').split()

            setattr(self.model, name, value)

    @abstractmethod
    def save(self, output):
        """ Save the model to an output file. """

        ...

    @classmethod
    def save_attribute(cls, name, value, output):
        """ Save an attribute. """

        output.write(f' {name}="{cls._escape(value)}"')

    @classmethod
    def save_bool(cls, name, output):
        """ Save a bool. """

        value = getattr(self.model, name)

        if value:
            cls.save_attribute(name, '1', output)

    @classmethod
    def save_literal(cls, name, output):
        """ Save the value of a literal text attribute. """

        value = getattr(self.model, name)

        if value != '':
            output.write(f'<Literal type="{name}">\n{cls._escape(value)}\n</Literal>\n', indent=False)

    @classmethod
    def save_str(cls, name, output):
        """ Save a string. """

        value = getattr(self.model, name)

        if value != '':
            cls.save_attribute(name, value, output)

    @classmethod
    def save_str_list(cls, name, output):
        """ Save a list of strings. """

        value = getattr(self.model, value)

        if len(value) != 0:
            cls.save_attribute(name, ' '.join(value), output)

    @staticmethod
    def _escape(s):
        """ Return an XML escaped string. """

        return escape(s, {'"': '&quot;'})


class BaseApiAdapter(BaseAdapter):
    """ This is the base class for all adapters for models that are written to
    a .sip file and provide a user-friendly, one line string representation.
    """

    @abstractmethod
    def as_str(self):
        """ Return the standard string representation. """

        ...

    @staticmethod
    def expand_type(type, name=None):
        """ Return the full type with an optional name. """

        # Handle the trivial case.
        if type == '':
            return ''

        # SIP can't handle every C++ fundamental type.
        # TODO: add the SIP support.
        s = type.replace('long int', 'long')

        # Append any name.
        if name:
            if s[-1] not in '&*':
                s += ' '

            s += name

        return s

    @abstractmethod
    def generate_sip(self, output):
        """ Generate the .sip file content. """

        ...
