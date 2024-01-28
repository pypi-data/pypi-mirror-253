#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""TODO"""


# This file is part of Vhatable cli.
#
# Vhatable cli is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Vhatable cli is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Vhatable cli.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2019 Frédéric MARTIN
#
# Contributors list :
#
#  Frédéric MARTIN frederic.martin.fma@gmail.com
#


import datetime
import logging

from humanfriendly import format_size


class CellFactory:
    """TODO"""
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes

    def __init__(self, raw=False, vertical=False, debug=0):
        self.raw = raw
        self.debug = debug
        self.vertical = vertical
        classname = str(self.__class__.__name__.lower())
        self.log = logging.getLogger("vhatablecli.cell." + classname)
        self.date_cells = [
            "creationDate",
            "modificationDate",
            "expirationDate",
            "uploadDate"
        ]
        self.size_cells = ["size"]
        self.custom_cells = {}

    def __call__(self, name, value, row=None):
        if name in self.custom_cells:
            clazz = self.custom_cells.get(name)
        elif name in self.date_cells:
            clazz = DateCell
        elif name in self.size_cells:
            clazz = SizeCell
        elif isinstance(value, bool):
            clazz = BCell
        elif isinstance(value, int):
            clazz = ICell
        elif isinstance(value, list):
            clazz = ComplexCell
        elif isinstance(value, dict):
            clazz = ComplexCell
        else:
            clazz = SCell
        if self.debug >= 2:
            self.log.debug("building cell ...")
            self.log.debug("property: %s", name)
            self.log.debug("value type: %s", type(value))
            self.log.debug("value: %s", value)
            self.log.debug("raw: %s", self.raw)
            self.log.debug("vertical: %s", self.vertical)
        cell = clazz(value)
        cell.name = name
        cell.raw = self.raw
        cell.vertical = self.vertical
        if row is not None:
            cell.row = row
        if self.debug >= 3:
            self.log.debug("cell type: %s", type(cell))
            # str method from all cell must return encoded strings
            self.log.debug("cell rendering: %s", str(cell))
            self.log.debug("cell built.")
        return cell


class BaseCell:
    """TODO"""

    value = None
    raw = False
    row = {}
    vertical = False
    extended = False
    hidden = False
    name = None
    _format = None
    _format_vertical = None
    _format_filter = None
    none = "-"

    def __init__(self, value):
        self.value = value

    @property
    def formatt(self):
        """TODO"""
        return self._format

    @formatt.setter
    def formatt(self, formatt):
        """TODO"""
        self._format = formatt

    @property
    def formatv(self):
        """TODO"""
        return self._format_vertical

    @formatv.setter
    def formatv(self, formatv):
        """TODO"""
        self._format_vertical = formatv

    @property
    def formatf(self):
        """TODO"""
        return self._format_filter

    @formatf.setter
    def formatf(self, formatf):
        """TODO"""
        self._format_filter = formatf

    def match(self, regex):
        """Apply the input regext to the current object"""
        if self._format_filter:
            if regex.match(self._format_filter.format(**self.value)):
                return True
        if regex.match(str(self)):
            return True
        return False

    def __unicode__(self):
        """TODO"""
        if self.raw:
            return str(self.value)
        return str(self.value)

    def __str__(self):
        """TODO"""
        return self.__unicode__()

    def __eq__(self, item):
        return self.value == item

    def __lt__(self, value):
        if value is None:
            return True
        if self.value is None:
            return True
        return self.value < value

    def __le__(self, value):
        if value is None:
            return True
        if self.value is None:
            return True
        return self.value <= value

    def __gt__(self, value):
        if value is None:
            return False
        if self.value is None:
            return False
        return self.value > value

    def __ge__(self, value):
        if value is None:
            return False
        if self.value is None:
            return False
        return self.value >= value


class SCell(BaseCell):
    """This class is used to emulate str type for veryprettytable.
    VeryPrettyTable will call the __str__ method on non-unicode objects.
    It requires that the __str__ output is utf-8 encoded."""
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes

    def __unicode__(self):
        """TODO"""
        if self.raw:
            if self.value is None:
                return "None"
            return str(self.value)
        if self.value is None:
            return self.none
        if self.vertical:
            if self._format_vertical:
                return self._format_vertical.format(value=self.value)
        if self._format:
            return self._format.format(value=self.value)
        return str(self.value)

    def __add__(self, item):
        return self.value + item

    def lower(self):
        """return a lower case version of the current value"""
        return self.value.lower()


class DateCell(BaseCell):
    """TODO"""

    millisecond = True

    # pylint: disable=too-few-public-methods
    def __init__(self, value):
        super().__init__(value)
        fmt = "{da:%Y-%m-%d %H:%M:%S}"
        self._format = fmt
        self._format_vertical = fmt
        # self._format_filter = fmt

    def __unicode__(self):
        if self.raw:
            return str(self.value)
        if self.value is not None:
            fmt = self._format
            if self.vertical:
                fmt = self._format_vertical
            div = 1
            if self.millisecond:
                div = 1000
            return fmt.format(
                da=datetime.datetime.fromtimestamp(self.value / div))
        return self.none

    def __div__(self, value):
        return self.value / value


class ICell(int, BaseCell):
    """TODO"""
    # pylint: disable=too-few-public-methods

    def __init__(self, value):
        super().__init__(value)
        self.value = value

    def __unicode__(self):
        if self.raw:
            return str(self.value)
        return str(self.value)


class BCell(BaseCell):
    """TODO"""
    # pylint: disable=too-few-public-methods

    def __unicode__(self):
        if self.raw:
            return str(self.value)
        return str(self.value)


class SizeCell(BaseCell):
    """TODO"""
    # pylint: disable=too-few-public-methods

    def __div__(self, value):
        return self.value / value

    def __unicode__(self):
        if self.raw:
            return str(self.value)
        if self.value is None:
            return self.none
        return format_size(self.value)


class TypeCell(BaseCell):
    """TODO"""

    def __str__(self):
        return str(type(self.value))


class ComplexCell(BaseCell):
    """TODO"""
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes

    def __unicode__(self):
        if self.raw:
            return str(self.value)
        if self.value is None:
            return self.none
        if self.vertical:
            if self._format_vertical:
                return self._format_vertical.format(**self.value)
        if self._format:
            return self._format.format(**self.value)
        return str(self.value)

    def keys(self):
        """TODO"""
        return list(self.value.keys())

    def __getitem__(self, key):
        return self.value[key]


class CellBuilder:
    """wrapper to build a Cell with extra parameters."""
    # pylint: disable=too-few-public-methods

    def __init__(self, formatt, formatv=None, formatf=None, cell=SCell):
        self._format = formatt
        self._formatv = formatt
        self._formatf = None
        if formatv:
            self._formatv = formatv
        if formatf:
            self._formatf = formatf
        self.clazz = cell

    def __call__(self, value):
        cell = self.clazz(value)
        cell.formatt = self._format
        cell.formatv = self._formatv
        cell.formatf = self._formatf
        return cell


class ComplexCellBuilder(CellBuilder):
    """wrapper to build a ComplexCell with extra parameters."""
    # pylint: disable=too-few-public-methods

    def __init__(self, formatt, formatv=None, formatf=None):
        super().__init__(formatt, formatv, formatf, cell=ComplexCell)
