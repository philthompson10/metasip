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


from PyQt6.QtWidgets import QComboBox, QFormLayout, QLineEdit

from ...helpers import AbstractDialog

from ..helpers import tagged_items

from .helpers import init_feature_selector, validate_feature_name


class RenameFeatureDialog(AbstractDialog):
    """ This class implements the dialog for renaming a feature. """

    def populate(self, layout):
        """ Populate the dialog's layout. """

        self._feature = QComboBox()
        layout.addWidget(self._feature)

        form = QFormLayout()
        layout.addLayout(form)

        self._new_name = QLineEdit()
        form.addRow("New name", self._new_name)

    def set_fields(self):
        """ Set the dialog's fields from the project. """

        init_feature_selector(self._feature, self.model)

    def get_fields(self):
        """ Update the project from the dialog's fields. """

        project = self.model

        old_name = self._feature.currentText()

        new_name = self._new_name.text().strip()
        if not validate_feature_name(new_name, project, self):
            return False

        # Rename in each API item it appears.
        for api_item, _ in tagged_items(project):
            # TODO - this should probably generate a lot more events.
            for i, f in enumerate(api_item.features):
                if f[0] == '!':
                    if f[1:] == old_name:
                        api_item.features[i] = '!' + new_name
                elif f == old_name:
                    api_item.features[i] = new_name

        # Rename in the project's list.
        if old_name in project.externalfeatures:
            feature_list = project.externalfeatures
        else:
            feature_list = project.features

        feature_list[feature_list.index(old_name)] = new_name

        return True
