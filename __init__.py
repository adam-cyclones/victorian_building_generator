# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# some_file.py
import bpy
from . import auto_load
from . import op

bl_info = {
    "name": "victorian_building_generator",
    "author": "Adam Crockett",
    "description": "",
    "blender": (3,),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic"
}


auto_load.init()


def register():
    # Register the operator class
    bpy.utils.register_class(op.Generate_Room_Operator)
    auto_load.register()


def unregister():
    # Unregister the operator class
    bpy.utils.unregister_class(op.Generate_Room_Operator)
    auto_load.unregister()
