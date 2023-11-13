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


from PyQt6.QtWidgets import (QCheckBox, QComboBox, QFormLayout, QGroupBox,
        QLineEdit, QVBoxLayout)

from ..Annos import split_annos
from ..Encoding import Encoding

from .base_dialog import BaseDialog


class VariablePropertiesDialog(BaseDialog):
    """ This class implements the dialog for a variables's properties. """

    def populate(self):
        """ Populate the dialog's layout. """

        layout = self.layout()

        group_box = QGroupBox("Annotations")
        layout.addWidget(group_box)
        group_box_layout = QVBoxLayout()
        group_box.setLayout(group_box_layout)

        form = QFormLayout()
        group_box_layout.addLayout(form)

        self._doc_type = QLineEdit()
        form.addRow('DocType', self._doc_type)

        encoding = QComboBox()
        self._encoding_helper = Encoding(encoding)
        form.addRow('Encoding', encoding)

        self._no_setter = QCheckBox('NoSetter')
        group_box_layout.addWidget(self._no_setter)

        self._no_type_hint = QCheckBox('NoTypeHint')
        group_box_layout.addWidget(self._no_type_hint)

        self._py_int = QCheckBox('PyInt')
        group_box_layout.addWidget(self._py_int)

        form = QFormLayout()
        group_box_layout.addLayout(form)

        self._py_name = QLineEdit()
        form.addRow('PyName', self._py_name)

        self._type_hint = QLineEdit()
        form.addRow('TypeHint', self._type_hint)

    def set_fields(self):
        """ Set the dialog's fields from the API item. """

        for name, value in split_annos(self.api_item.annos):
            if name == 'DocType':
                self._doc_type.setText(value)
            elif name == 'Encoding':
                self._encoding_helper.setAnnotation(value)
            elif name == 'NoSetter':
                self._no_setter.setChecked(True)
            elif name == 'NoTypeHint':
                self._no_type_hint.setChecked(True)
            elif name == 'PyInt':
                self._py_int.setChecked(True)
            elif name == 'PyName':
                self._py_name.setText(value)
            elif name == 'TypeHint':
                self._type_hint.setText(value)

    def get_fields(self):
        """ Update the API item from the dialog's fields. """

        annos_list = []

        self._encoding_helper.annotation(annos_list)

        doc_type = self._doc_type.text().strip()
        if doc_type:
            annos_list.append(f'DocType="{doc_type}"')

        if self._no_setter.isChecked():
            annos_list.append('NoSetter')

        if self._no_type_hint.isChecked():
            annos_list.append('NoTypeHint')

        if self._py_int.isChecked():
            annos_list.append('PyInt')

        py_name = self._py_name.text().strip()
        if py_name:
            annos_list.append('PyName=' + py_name)

        type_hint = self._type_hint.text().strip()
        if type_hint:
            annos_list.append(f'TypeHint="{type_hint}"')

        self.api_item.annos = ','.join(annos_list)
