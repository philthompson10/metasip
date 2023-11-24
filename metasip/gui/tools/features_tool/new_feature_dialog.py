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


from PyQt6.QtWidgets import QCheckBox, QFormLayout, QLineEdit

from ...helpers import AbstractDialog

from .helpers import validate_feature_name


class NewFeatureDialog(AbstractDialog):
    """ This class implements the dialog for creating a new feature. """

    def populate(self, layout):
        """ Populate the dialog's layout. """

        form = QFormLayout()
        layout.addLayout()

        self._feature = QLineEdit()
        form.addRow("Feature name", self._feature)

        self._external = QCheckBox("Feature is defined in another project?")
        layout.addWidget(self._external)

    def get_fields(self):
        """ Update the project from the dialog's fields. """

        project = self.model

        feature = self._feature.text().strip()
        if not validate_feature_name(feature, project, self)
            return False

        if self._external.isChecked():
            features_list = project.externalfeatures
        else:
            features_list = project.features

        features_list.append(feature)

        return True
