#!/usr/bin/env python3
# vim: fileencoding=utf8
# SPDXVersion: SPDX-2.3
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © Copyright 2022, 2023 by Christian Dönges
# SPDXID: SPDXRef-littlejonny-py
"""Format output to a text table.

   In case you have been wondering, the name is a reference to
   https://xkcd.com/327/.
"""

# Postpone type hint evaluation until after the entire class has been parsed.
# This was to become standard in 3.10 but will probably never be.
# @see https://stackoverflow.com/a/33533514
# @see https://mail.python.org/archives/list/python-dev@python.org/thread/CLVXXPQ2T2LQ5MP2Y53VVQFCXYWQJHKZ/
from __future__ import annotations


import enum
from dataclasses import dataclass, field
from typing import Any

from pymisclib.ansiterminal import AnsiControl, BgColor, FgColor, TextStyle
from pymisclib.unicodechars import UC


# Box drawing characters.
# The beauty of Namespace makes it possible to access a character like so:
# box_drawings.light.horizontal.
box_drawings = UC.box_drawings

# Type definition: a Text is a collection of lines, each of which is a string.
Text = list[str]
"""Type definition: a Text is a collection of lines, each of which is a string.

    The lines are organized by row, so the first string in the list is the first text line.
"""


@enum.unique
class LineStyle(enum.Enum):
    """Rendering style for lines."""
    double = box_drawings.double
    light = box_drawings.light
    heavy = box_drawings.heavy


@enum.unique
class OutputFormat(enum.Enum):
    """Format for rendering the output."""
    ANSI = enum.auto()  # Render on an ANSI terminal.
    TEXT = enum.auto()  # Render as plain text.


@dataclass
class Point:
    """Coordinate in column (x) / row (y) space."""
    column: int = 1
    row: int = 1

    def __str__(self) -> str:
        """Return a string representation of the instance."""
        return f'({self.column};{self.row})'


@dataclass
class Box:
    """A box consisting of a frame with content.

        Constructor arguments:
            :param int origin_column: Top left corner column.
            :param int origin_row: Top left corner row.
            :param int width: Width in columns.
            :param int height: Height in rows.
            :param LineStyle line_style: Border line style.
            :param str border_style: Border color and font style expressed as ANSI format codes.
            :param str text_style: Content text color and font style expressed as ANSI format codes.
    """
    origin_column: int = 1  # starting x-coordinate
    """X-coordinate of the upper left corner of the box."""
    origin_row: int = 1  # starting y coordinate
    """Y-coordinate of the upper left corner of the box."""
    width: int = 40
    """Width of the box in columns."""
    height: int = 20
    """Height of the box in rows."""
    line_style: LineStyle = LineStyle.light
    """Style of the border characters."""
    border_style: str = FgColor.Black.value + BgColor.White.value
    """Rendering style (color and font style) of the border."""
    text_style: str = FgColor.Blue.value + BgColor.BrightYellow.value + TextStyle.Bold.value
    """Text style (color and font) of the content."""
    _text: Text = field(default_factory=list)

    @classmethod
    def make_from_points(cls, top_left: Point,
                         bottom_right: Point,
                         line_style: LineStyle = LineStyle.light) -> Box:
        """Create a new Box instance with the given top left and bottom right
        points.

        :param Point top_left: starting point in the upper left corner.
        :param Point bottom_right: ending point (inclusive) in the lower right
            corner.
        :param LineStyle line_style: Style to use when rendering the box.
        :return: An initialized instance.
        :rtype Box:
        """
        if top_left.column < 1:
            raise ValueError('left column too small')
        if top_left.row < 1:
            raise ValueError('top row too small')
        if bottom_right.column <= top_left.column:
            raise ValueError('right column too small')
        if bottom_right.row <= top_left.row:
            raise ValueError('bottom column too small')
        width = bottom_right.column - top_left.column
        height = bottom_right.row - top_left.row
        return Box(top_left.row, top_left.column, width, height, line_style)

    @property
    def text(self) -> Text:
        """Text contained in the box."""
        return self._text

    @text.setter
    def text(self, text: Text, truncate: bool = True):
        """Set the text contained in the box."""
        self._text = []
        if len(text) > self.height:
            if truncate:
                edited_text = text[:self.height]
            else:
                raise ValueError('too many lines')
        else:
            edited_text = text
        for line in edited_text:
            if len(line) > self.width:
                if truncate:
                    line = line[:self.width]
                else:
                    ValueError('line too wide')
            else:
                line = line + ' ' * (self.width - len(line))
            self._text.append(line)

    def render(self, output_format: OutputFormat) -> Text:
        """Render the box in the given output_format.

        :param OutputFormat output_format: Rendering format.
        :return: A list of lines rendering the instance.
        :rtype Text:
        """
        if output_format == OutputFormat.ANSI:
            return self._render_ansi()
        elif output_format == OutputFormat.TEXT:
            return self._render_text()
        raise ValueError('unknown output output_format')

    def _render_ansi(self) -> Text:
        """Render the instance on an ANSI terminal."""
        lines = []
        if self.origin_column > 1:
            prefix = AnsiControl.move_cursor_forward(self.origin_column - 1)
        else:
            prefix = ''
        box = self.line_style.value
        s = self.border_style + box.down_and_right + box.horizontal * self.width + \
            box.down_and_left + TextStyle.Reset.value
        if self.origin_column > 1 or self.origin_row > 1:
            s = AnsiControl.move_cursor_to(self.origin_column, self.origin_row) + s
        else:
            s = prefix + s
        lines.append(s)
        s = prefix + self.border_style + box.vertical + \
            self.text_style + (' ' * self.width) + TextStyle.Reset.value + \
            self.border_style + box.vertical + TextStyle.Reset.value
        for i in range(self.height):
            if i < len(self._text):
                lines.append(prefix + self.border_style + box.vertical +
                             self.text_style + self._text[i] + TextStyle.Reset.value +
                             self.border_style + box.vertical + TextStyle.Reset.value)
            else:
                lines.append(s)
        s = prefix + self.border_style + box.up_and_right + \
            box.horizontal * self.width + box.up_and_left + TextStyle.Reset.value
        lines.append(s)

        return lines

    def _render_text(self) -> Text:
        """Render the instance on dumb terminal (e.g. as plain text).

        The origin column and row are created using spaces and blank lines.

        :return: A list of lines, each of which is a string that contains no
            formatting characters.
        :rtype list[str]:
        """
        lines = []
        if self.origin_row > 1:
            for i in range(self.origin_row - 1):
                lines.append('')
        prefix = ' ' * (self.origin_column - 1)
        box = self.line_style.value
        s = prefix + box.down_and_right + box.horizontal * self.width + box.down_and_left
        lines.append(s)
        s = prefix + box.vertical + ' ' * self.width + box.vertical
        for i in range(self.height):
            if i < len(self._text):
                lines.append(prefix + box.vertical + self._text[i] + box.vertical)
            else:
                lines.append(s)
        s = prefix + box.up_and_right + box.horizontal * self.width + box.up_and_left
        lines.append(s)

        return lines


@dataclass
class ColumnTable:
    """Table with data arranged by column."""
    _headings: list[str] = field(default_factory=list)  # row or column heading
    _formats: list[str] = field(default_factory=list)  # cell formats
    _cells: list[list[Any]] = field(default_factory=list)  # column[row]
    _num_columns: int = 0
    _num_rows: int = 0

    @property
    def cell_formats(self) -> list[str]:
        """Return cell formats by columns."""
        return self._formats

    @property
    def headings(self) -> list[str]:
        """Return headings by column."""
        return self._headings

    @property
    def num_columns(self):
        """Number of columns in the table."""
        return self._num_columns

    @property
    def num_rows(self):
        """Number of rows in the table."""
        return self._num_rows

    def set_table(self,
                  headings: list[str],
                  cell_formats: list[str],
                  cells: list[list[str]]):
        """Set the content of the table with cells specified by column.

            :param list[str] headings: List of headings.
            :param list[str] cell_formats: List of cell formats for each column.
                The formats use the same format-language as Python format strings.
            :param list[str] cells: Matrix of cell contents, specified column[row].

            Example
            ---------

            .. code-block:: python

                ct2 = ColumnTable()
                ct2.set_table(
                    headings=['First', 'Second', 'Third', 'Fourth'],
                    cell_formats=['3d', '08x', 's', '>s'],
                    cells=[[1, 2, 12, 123, 1000],
                           [0x12345678, 0xffffee01, -1, 0, 23],
                           ['abc def geh', '12345', 'minus one', 'zero', 'First'],
                           ['this is a sample text', 'Short', 'negative hex number',
                            'Zero hexadecimal number', 'The first column is too large.']]
                )
                print_lines(ct2.draw(LineStyle.light))

            Output::

                ┌───────┬──────────┬─────────────┬────────────────────────────────┐
                │ First │ Second   │ Third       │ Fourth                         │
                ├───────┼──────────┼─────────────┼────────────────────────────────┤
                │   1   │ 12345678 │ abc def geh │ this is a sample text          │
                │   2   │ ffffee01 │ 12345       │ Short                          │
                │  12   │ -0000001 │ minus one   │ negative hex number            │
                │ 123   │ 00000000 │ zero        │ Zero hexadecimal number        │
                │ 1000  │ 00000017 │ First       │ The first column is too large. │
                └───────┴──────────┴─────────────┴────────────────────────────────┘
        """
        if len(headings) != len(cell_formats):
            raise ValueError('number columns in headings and formats do not match')
        if len(headings) != len(cells):
            raise ValueError('number of columns in headings and cells do not match')
        self._num_columns = len(headings)
        self._num_rows = len(cells[0])
        self._headings = headings
        self._formats = cell_formats
        self._cells = cells

    def set_table_transposed(self,
                             headings: list[str],
                             cell_formats: list[str],
                             cells: list[list[str]]):
        """Set the content of the table with cells specified by row.

            :param list[str] headings: List of headings.
            :param list[str] cell_formats: List of cell formats for each column.
            :param list[str] cells: Matrix of cell contents, specified row[column].

            Example
            ---------

            .. code-block:: python

                ct1 = ColumnTable()
                ct1.set_table_transposed(
                    headings=['First', 'Second', 'Third', 'Fourth'],
                    cell_formats=['3d', '08x', 's', '>s'],
                    cells=[[1, 0x12345678, 'abc def geh', 'this is a sample text'],
                           [2, 0xffffee01, '12345', 'Short'],
                           [12, -1, 'minus one', 'negative hex number'],
                           [123, 0, 'zero', 'Zero hexadecimal number'],
                           [1000, 23, 'First', 'The first column is too large.']]
                )
                print_lines(ct1.draw(LineStyle.light))

            Output::

                ┌───────┬──────────┬─────────────┬────────────────────────────────┐
                │ First │ Second   │ Third       │ Fourth                         │
                ├───────┼──────────┼─────────────┼────────────────────────────────┤
                │   1   │ 12345678 │ abc def geh │ this is a sample text          │
                │   2   │ ffffee01 │ 12345       │ Short                          │
                │  12   │ -0000001 │ minus one   │ negative hex number            │
                │ 123   │ 00000000 │ zero        │ Zero hexadecimal number        │
                │ 1000  │ 00000017 │ First       │ The first column is too large. │
                └───────┴──────────┴─────────────┴────────────────────────────────┘
        """
        transposed_cells = [list(x) for x in zip(*cells)]
        self.set_table(headings, cell_formats, transposed_cells)

    def draw(self, style: LineStyle) -> Text:
        """Render the table to a list of lines.

            :param LineStyle style: The line style to use for the table.
            :rtype Text:
            :return: A list of rows which make up the rendered table.
        """
        formatted_cells = []
        column_widths = []
        for c in range(self.num_columns):
            column_width = len(self._headings[c])
            column_data = self._cells[c]
            fmt = self._formats[c]
            formatted_column = []
            for cell in column_data:
                formatted_cell = f'{cell:{fmt}}'
                formatted_column.append(formatted_cell)
                column_width = max(column_width,  len(formatted_cell))
            formatted_cells.append(formatted_column)
            column_widths.append(column_width)

        box = style.value
        lines = []
        first = True
        s = ''
        for c in range(self.num_columns):
            column_width = column_widths[c]
            if first:
                s = box.down_and_right + box.horizontal * (column_width + 2)
                first = False
            else:
                s += box.down_and_horizontal + box.horizontal * (column_width + 2)
        s += box.down_and_left
        lines.append(s)

        s = ''
        for c in range(self.num_columns):
            column_width = column_widths[c]
            s += box.vertical + f' {self._headings[c]:{column_width}s} '
        s += box.vertical
        lines.append(s)

        first = True
        s = ''
        for c in range(self.num_columns):
            column_width = column_widths[c]
            if first:
                s = box.vertical_and_right + box.horizontal * (column_width + 2)
                first = False
            else:
                s += box.vertical_and_horizontal + box.horizontal * (column_width + 2)
        s += box.vertical_and_left
        lines.append(s)

        for r in range(self.num_rows):
            s = ''
            for c in range(self.num_columns):
                column_width = column_widths[c]
                s += box.vertical + f' {formatted_cells[c][r]:{column_width}s} '
            s += box.vertical
            lines.append(s)

        first = True
        s = ''
        for c in range(self.num_columns):
            column_width = column_widths[c]
            if first:
                s = box.up_and_right + box.horizontal * (column_width + 2)
                first = False
            else:
                s += box.up_and_horizontal + box.horizontal * (column_width + 2)
        s += box.up_and_left
        lines.append(s)

        return lines


def draw_box(x, y, style) -> Text:
    """Construct a box of size x * y with style."""
    box = style.value

    lines = []
    s = box.down_and_right + box.horizontal * x + box.down_and_left
    lines.append(s)
    s = box.vertical + ' ' * x + box.vertical
    for i in range(y):
        lines.append(s)
    s = box.up_and_right + box.horizontal * x + box.up_and_left
    lines.append(s)

    return lines


def print_lines(lines: Text):
    """Print lines stored as a list of strings to stdout."""
    for line in lines:
        print(line)


if __name__ == '__main__':
    print_lines(draw_box(5, 3, LineStyle.light))
    print_lines(draw_box(1, 1, LineStyle.double))
    print_lines(draw_box(40, 3, LineStyle.heavy))

    b1 = Box(8, 3, 17, 9, LineStyle.light,
             FgColor.Green.value + BgColor.White.value,
             FgColor.Blue.value + BgColor.BrightYellow.value + TextStyle.Italic.value)
    b1.text = [
        '(8;7)      (17;8)',
        '',
        '',
        '',
        '        *       ',
        '',
        '',
        '',
        '(8;16)    (17;16)',
    ]
    b2 = Box(1, 1, 64, 13, LineStyle.double,
             FgColor.Black.value + BgColor.Green.value,
             FgColor.Red.value + BgColor.BrightWhite.value + TextStyle.Bold.value)
    b2.text = [
        '         1         2         3         4         5         6    ',
        '1234567890123456789012345678901234567890123456789012345678901234',
        '',
        '                                                           right',
        'left',
        '                               center',
        UC.box_drawings.light.horizontal * b2.width,
        'ABC DEF GHI JKL MNO PRQ STU VWX YZ!',
        'ABC DEF GHI JKL MNO PRQ STU VWX YZ!',
        UC.box_drawings.light.horizontal * b2.width,
    ]
    print_lines(b1.render(OutputFormat.ANSI))
    print_lines(b2.render(OutputFormat.ANSI))

    print_lines(b1.render(OutputFormat.TEXT))
    print_lines(b2.render(OutputFormat.TEXT))

    # row[column]
    ct1 = ColumnTable()
    ct1.set_table_transposed(
        headings=['First', 'Second', 'Third', 'Fourth'],
        cell_formats=['3d', '08x', 's', '>s'],
        cells=[[1, 0x12345678, 'abc def geh', 'this is a sample text'],
               [2, 0xffffee01, '12345', 'Short'],
               [12, -1, 'minus one', 'negative hex number'],
               [123, 0, 'zero', 'Zero hexadecimal number'],
               [1000, 23, 'First', 'The first column is too large.']]
    )
    print_lines(ct1.draw(LineStyle.light))

    # column[row]
    ct2 = ColumnTable()
    ct2.set_table(
        headings=['First', 'Second', 'Third', 'Fourth'],
        cell_formats=['3d', '08x', 's', '>s'],
        cells=[[1, 2, 12, 123, 1000],
               [0x12345678, 0xffffee01, -1, 0, 23],
               ['abc def geh', '12345', 'minus one', 'zero', 'First'],
               ['this is a sample text', 'Short', 'negative hex number',
                'Zero hexadecimal number', 'The first column is too large.']]
    )
    print_lines(ct2.draw(LineStyle.light))
