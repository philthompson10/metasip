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


from PyQt6.QtWidgets import (QDialog, QDialogButtonBox, QSizePolicy,
        QSpacerItem, QVBoxLayout)


class BaseDialog(QDialog):
    """ A base class for other dialogs that handles common functionality. """

    def __init__(self, api_item, title, parent, project=None):
        """ Initialise the dialog. """

        self.api_item = api_item
        self.project = project

        super().__init__(parent)

        self.setWindowTitle(title)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.populate()

        spacer = QSpacerItem(1, 1, QSizePolicy.Policy.Minimum,
                QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        button_box = QDialogButtonBox(
                QDialogButtonBox.StandardButton.Cancel |
                QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def populate(self):
        """ Reimplemented by a sub-class to populate the dialog's layout. """

        raise NotImplementedError

    def update(self):
        """ Return True if the API item was updated or False if the dialog was
        cancelled.
        """

        self.set_fields()

        if self.exec() == int(QDialog.DialogCode.Rejected):
            return False

        self.get_fields()

        return True

    def set_fields(self):
        """ Normally reimplemented by a sub-class to set the dialog's fields
        from the API item.
        """

        # This default implementation does nothing.
        pass

    def get_fields(self):
        """ Reimplemented by a sub-class to update the API item from the
        dialog's fields.
        """

        raise NotImplementedError
