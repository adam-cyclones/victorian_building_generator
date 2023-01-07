import bpy
import csv


def half(n):
    return n / 2


def pos_neg(n):
    calculated = {
        "pos": n,
        "neg": n * -1
    }
    return calculated


def foot(imperial_value):
    return imperial_value * 0.3048

# Run with:
# bpy.ops.object.generate_room()


def cube_ft(width=1, depth=1, height=1, x=0, y=0, z=0, name='cube_ft'):
    # x, y, x are half
    bpy.ops.mesh.primitive_cube_add(
        size=foot(1),
        location=(foot(x),
                  foot(y),
                  foot(z)),
    )
    bpy.context.active_object.name = name
    bpy.context.object.scale = (1 * width, 1 * depth, 1 * height)


def add_floor_suffix(number):
    if number % 100 in (11, 12, 13):
        return f"{number}th"
    elif number % 10 == 1:
        return f"{number}st"
    elif number % 10 == 2:
        return f"{number}nd"
    elif number % 10 == 3:
        return f"{number}rd"
    else:
        return f"{number}th"


def generate_room(
        width=6,
        height=10,
        depth=6,
        wall_thickness=1,
        floor_thickness=1,
        collection="Scene Collection"
):
    # Width is equal too: |E| <-- x/2 --> |W|
    # Walls have origin center but to total width, height, depth we gave needs to be achieved, we need to offset the wall thickness by half via subtraction
    # The East and West wall will slot within the North and South walls
    # _____
    # -----
    # ||
    # ||
    # _____
    # -----
    #
    # East wall
    cube_ft(
        name=f"{collection}.East wall",
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2,
        x=half(pos_neg(width)["pos"]) - half(wall_thickness))
    # West wall
    cube_ft(
        name=f"{collection}.West wall",
        width=wall_thickness,
        height=height,
        depth=depth - (wall_thickness * 2),
        z=height / 2,
        x=half(pos_neg(width)["neg"]) + half(wall_thickness))
    # North wall
    cube_ft(
        name=f"{collection}.North wall",
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2,
        y=half(pos_neg(depth)["pos"]) - half(wall_thickness)
    )
    # South wall
    cube_ft(
        name=f"{collection}.South wall",
        width=width,
        height=height,
        depth=wall_thickness,
        z=height / 2,
        y=half(pos_neg(depth)["neg"]) + half(wall_thickness))
    # Floor
    cube_ft(
        name=f"{collection}.Floor",
        width=width - wall_thickness * 2,
        height=floor_thickness - wall_thickness * 2,
        depth=depth - wall_thickness * 2,
        z=floor_thickness / 2,
        y=0
    )


def generate_building(
    preset='Lower Class',
    floors=1
):
    def generate(data):
        bpy.ops.object.empty_add(
            type='PLAIN_AXES',
            align='WORLD',
            location=(0, 0, 0),
            scale=(1, 1, 1),
        )
        bpy.context.active_object.name = f'{preset} Building'
        for floor in range(floors):
            if (floor == 0):
                floor = (floor, 'Ground')
            else:
                floor = (floor, add_floor_suffix(floor))
            generate_room(
                width=30,
                depth=40,
                height=10,
                wall_thickness=.75,
                collection=f"Floor {floor[1]}"
            )
    match preset:
        case "Lower Class":
            data = "models/lower class/rooms.csv"
            generate(data)
        case "Middle Class":
            data = "models/middle class/rooms.csv"
            generate(data)
        case "Upper Class":
            data = "models/upper class/rooms.csv"
            generate(data)
        case _:
            print(f"{preset} is not a supported preset")


class Generate_Room_Operator(bpy.types.Operator):
    bl_idname = "object.generate_room"
    bl_label = "generate_room"

    def execute(self, context):
        generate_building(floors=3)
        # cube_ft(width=6, height=6, depth=6)

        return {'FINISHED'}
