# python_material_colors
A simple implementation of the material design colors in python.

- currently only supports 'rgb' format; more will be added soon

The values are from https://www.materialpalette.com/colors

Thanks to the creators of this page for providing this really helpful tool

# Usage:

from material_colors import MaterialColors

Colors = MaterialColors('rgb')

my_red_color = Colors.red()

my_purple_color = Colors.purple(300)
