# Victorian Building Generator

A Blender script for generating buildings in the style of late Victorian rural England, using Chat GPT extensively.

## Getting Started

To use the Victorian Building Generator, you will need to have Blender installed on your computer. You can download Blender for free from the [official website](https://www.blender.org/download/).

Once you have Blender installed, you can clone this repository and open the `sample.blend` file in Blender. The script is located in the `op.py` file and can be run by pressing `Run Script` in the Text Editor.

## Usage

To generate a building, run the `Generate Building` operator in the 3D Viewport. This will generate a building in the style of late Victorian rural England. The generated building will be selected by default, and you can use the standard Blender tools to modify it as desired.

## Contributing

If you would like to contribute to the development of the Victorian Building Generator, you can submit a pull request with your changes. Please make sure to follow the existing coding style and include appropriate documentation for your changes.

## Development

To run the Victorian Building Generator through the Visual Studio Blender Development plugin, you will need to have both Blender and Visual Studio installed on your computer.

Open Blender and install the Blender Development plugin by going to Edit > Preferences > Add-ons and searching for "Blender Development".
Enable the plugin by checking the checkbox next to it.
In Visual Studio, create a new project and add the op.py file to the project.
In Visual Studio, go to Tools > Blender Development > Set as Startup File. This will set the op.py file as the startup file for the plugin.
In Blender, go to Text Editor > Open. This will open the Text Editor panel.
In the Text Editor panel, open the op.py file.
In the Text Editor panel, press Run Script. This will run the script and generate the building.

To run the Generate Room operator in the Blender Python console, you will need to have the op.py file open in the Text Editor panel.

In Blender, go to Text Editor > Open. This will open the Text Editor panel.
In the Text Editor panel, open the op.py file.
In the Text Editor panel, press Run Script. This will run the script and make the Generate Room operator available in the Blender Python console.
In the Blender Python console, enter `bpy.ops.object.generate_room()` and hit <kbd>Enter</kbd>

For full details of using the Visual Studio Code Blender development plugin visit the projects github

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
