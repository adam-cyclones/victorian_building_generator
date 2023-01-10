import csv
import bpy
import os
from .src import rooms
from .src.utils import geom, math_extra, strings

# Run with:
# bpy.ops.object.generate_room()


def generate_room(
    parent,
    width=6,
    height=10,
    depth=6,
    wall_thickness=1,
    floor_thickness=1,
    collection="Scene Collection",
    z=0
):
    # Width is equal too: |E| <-- x/2 --> |W|
    # Walls have origin center but to total width, height, depth we gave needs to be achieved, we need to offset the wall thickness by math.half via subtraction
    # The East and West wall will slot within the North and South walls
    # _____
    # -----
    # ||
    # ||
    # _____
    # -----
    #
    # East wall
    geom.cube_ft(
        parent,
        name=f"{collection}.East wall",
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2 + z,
        x=math_extra.half(math_extra.pos_neg(width)["pos"]) - math_extra.half(wall_thickness))
    # West wall
    geom.cube_ft(
        parent,
        name=f"{collection}.West wall",
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2 + z,
        x=math_extra.half(math_extra.pos_neg(width)["neg"]) + math_extra.half(wall_thickness))
    # North wall
    geom.cube_ft(
        parent,
        name=f"{collection}.North wall",
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2 + z,
        y=math_extra.half(math_extra.pos_neg(depth)[
            "pos"]) - math_extra.half(wall_thickness)
    )
    # South wall
    geom.cube_ft(
        parent,
        name=f"{collection}.South wall",
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2 + z,
        y=math_extra.half(math_extra.pos_neg(depth)["neg"]) + math_extra.half(wall_thickness))
    # Floor
    geom.cube_ft(
        parent,
        name=f"{collection}.Floor",
        width=width - wall_thickness * 2,
        height=floor_thickness - wall_thickness * 2,
        depth=depth - wall_thickness * 2,
        z=floor_thickness / 2 + z,
        y=0
    )


def generate_building(
    preset='Lower Class',
    floors=1
):
    def generate(data):
        rooms.load(data)

        bpy.ops.object.empty_add(
            type='PLAIN_AXES',
            align='WORLD',
            location=(0, 0, 0),
            scale=(1, 1, 1),
        )
        bpy.context.active_object.name = f'{preset} Building'
        building_root = bpy.data.objects[f'{preset} Building']
        for floor in range(floors):
            if (floor == 0):
                floor = (floor, '0 Ground')
            else:
                floor = (floor, strings.add_floor_suffix(floor))
            # Add an empty
            bpy.ops.object.empty_add(
                type='PLAIN_AXES',
                align='WORLD',
                location=(0, 0, 0),
                scale=(1, 1, 1),
            )
            # Set a Name for the empty
            bpy.context.active_object.name = f'{floor[1]} Floor'
            # Assign parent to the building
            bpy.data.objects[f'{floor[1]} Floor'].parent = building_root
            generate_room(
                parent=bpy.data.objects[f'{floor[1]} Floor'],
                width=30,
                depth=40,
                height=10,
                wall_thickness=.75,
                collection=f"Floor {floor[1]}",
                z=floor[0] * 10
            )
    match preset:
        case "Lower Class":
            data = os.path.join(os.path.dirname(
                os.path.abspath(__file__)) + "/models/lower class/rooms.csv")
            generate(data)
        case "Middle Class":
            data = os.path.join(os.path.dirname(
                os.path.abspath(__file__)) + "/models/middle class/rooms.csv")
            generate(data)
        case "Upper Class":
            data = os.path.join(os.path.dirname(
                os.path.abspath(__file__)) + "/models/upper class/rooms.csv")
            generate(data)
        case _:
            print(f"{preset} is not a supported preset")


class Generate_Room_Operator(bpy.types.Operator):
    bl_idname = "object.generate_room"
    bl_label = "generate_room"

    def execute(self, context):
        generate_building(floors=3)
        # geom.cube_ft(width=6, height=6, depth=6)

        return {'FINISHED'}
