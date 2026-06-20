"""
Hirst Dot Painting Generator

This program creates a grid of colored dots inspired by
Damien Hirst's spot paintings using Python's Turtle module.

The color palette was extracted from an image using the
Colorgram library (code provided below but commented out).
"""

# Uncomment this section if you want to extract colors
# from a new image using the Colorgram library.

# import colorgram
#
# # Extract 38 colors from an image
# colors = colorgram.extract('image.jpg', 38)
#
# color_list = []
# for color in colors:
#     rgb = color.rgb
#     color_list.append((rgb.r, rgb.g, rgb.b))
#
# print(color_list)

import turtle as t
import random

# Create turtle object
painter = t.Turtle()

# Set the fastest drawing speed
painter.speed(0)

# Enable RGB color values (0-255)
t.colormode(255)

# Extracted RGB color palette
color_list = [
    (235, 252, 243), (198, 13, 32), (248, 236, 25),
    (40, 76, 188), (244, 247, 253), (39, 216, 69),
    (238, 227, 5), (227, 159, 49), (29, 40, 154),
    (212, 76, 15), (17, 153, 17), (241, 36, 161),
    (195, 16, 12), (223, 21, 120), (68, 10, 31),
    (61, 15, 8), (223, 141, 206), (11, 97, 62),
    (219, 159, 11), (54, 209, 229), (19, 21, 49),
    (238, 157, 216), (79, 74, 212), (10, 228, 238),
    (73, 212, 168), (93, 233, 198), (65, 231, 239),
    (217, 88, 51), (6, 68, 42), (176, 176, 233),
    (239, 168, 161), (249, 8, 48), (5, 246, 222),
    (15, 76, 110), (243, 15, 14), (38, 43, 221)
]

# Lift pen so no lines are drawn while moving
painter.penup()

# Move turtle to starting position
painter.setposition(-250, -250)


def draw_dot_painting(gap, dot_size, columns, rows):
    """
    Draw a grid of colored dots.

    Args:
        gap (int): Distance between dots.
        dot_size (int): Size of each dot.
        columns (int): Number of dots per row.
        rows (int): Number of rows.
    """

    for row in range(rows):

        # Save current row starting position
        start_x = painter.position()[0]
        start_y = painter.position()[1]

        next_x = start_x + gap

        for column in range(columns):
            # Draw a dot with a random color
            painter.dot(dot_size, random.choice(color_list))

            # Move to next position in the row
            painter.setposition(next_x, start_y)
            next_x += gap

        # Move to beginning of next row
        painter.setposition(start_x, start_y + gap)


# Draw a 10 x 10 dot painting
draw_dot_painting(
    gap=50,
    dot_size=20,
    columns=10,
    rows=10
)

# Hide turtle cursor after drawing
painter.hideturtle()

# Create screen object
screen = t.Screen()

# Print canvas height (optional debugging)
print(screen.canvheight)

# Close window when user clicks
screen.exitonclick()