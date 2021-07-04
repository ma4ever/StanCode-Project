"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program demonstrates the popularity of name from year 1900 to 2010.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_position = GRAPH_MARGIN_SIZE + year_index * ((width - GRAPH_MARGIN_SIZE) / len(YEARS))
    return x_position


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        canvas.create_text(TEXT_DX + get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    num = 0  # use num to control color of text and line
    for name in lookup_names:
        year_point_x = []  # list for adding x coordinate
        year_point_y = []  # list for adding y coordinate

        # get position of x and y
        for i in range(len(YEARS)):
            year = YEARS[i]
            x_position = get_x_coordinate(CANVAS_WIDTH, i)
            if year in name_data[name]:
                rank = name_data[name][year]
                y_position = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000 * int(rank) + GRAPH_MARGIN_SIZE
            else:
                rank = "*"
                y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            # create text
            canvas.create_text(TEXT_DX + x_position, y_position, text=name + " " + rank, anchor=tkinter.SW,
                               fill=COLORS[num])

            # add all coordinates to list
            year_point_x.append(x_position)
            year_point_y.append(y_position)

        # create line
        for j in range(len(YEARS) - 1):
            canvas.create_line(year_point_x[j], year_point_y[j], year_point_x[j + 1], year_point_y[j + 1],
                               fill=COLORS[num], width=LINE_WIDTH)

        # change color of text and line
        num += 1
        if num > 3:
            num = 0


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
