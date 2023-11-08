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


from ..model import List

from .container_factory import ContainerFactory
from .menu import Menu
from .i_menu_bar import IMenuBar


class MenuBar(ContainerFactory):
    """ The MenuBar class implements a factory for menu bars that implement or
    can be adapted to :class:`~dip.ui.IMenuBar`.
    """

    # The contents of the view.
    contents = List(Menu)

    # The interface that the view can be adapted to.
    interface = IMenuBar

    # The name of the toolkit factory method.
    toolkit_factory = 'menu_bar'


# Register the view factory.
MenuBar.view_factories.append(MenuBar)