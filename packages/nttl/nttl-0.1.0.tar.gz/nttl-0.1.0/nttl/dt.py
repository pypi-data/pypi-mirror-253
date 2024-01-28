# Copyright (C)  2024  Robert Labudda
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Datetime/str utilities"""
import datetime


def parse_when(value):
    now = datetime.datetime.now()
    if value is None or len(value.strip()) == 0:
        return now

    value = value.strip()

    if value[0] == 'T':
        return now + parse_timedelta(value[1:])
    elif value[0] in '-+':
        return now + parse_timedelta(value)
    elif len(value) == 5:
        return datetime.datetime.strptime(value,
                                          '%H:%M').replace(year=now.year,
                                                           month=now.month,
                                                           day=now.day)
    elif len(value) == 8:
        return datetime.datetime.strptime(value,
                                          '%H:%M:%S').replace(year=now.year,
                                                              month=now.month,
                                                              day=now.day)
    elif len(value) == 17:
        return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M')
    elif len(value) == 19:
        return datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

    raise ValueError(f"Don't know the time format '{value}'")


def dt_as_str(value):
    return value.strftime("%Y-%m-%dT%H:%M:%S")


def parse_dt(value):
    try:
        return datetime.datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError:
        pass

    return (datetime.datetime.now() + parse_timedelta(value)).date()


def parse_timedelta(text):
    if text[0] == 'T':
        text = text[1:]

    sign = -1 if text[0] == '-' else 1
    if text[0] in '-+':
        text = text[1:]

    value = ''
    duration = datetime.timedelta(0)
    for letter in text:
        if letter == '_' or letter.isspace():
            continue
        if letter.isdigit():
            value += letter
        if letter in 'hmsdw':
            if len(value) == 0:
                continue

            if letter == 'h':
                duration += datetime.timedelta(hours=int(value))
            elif letter == 'm':
                duration += datetime.timedelta(minutes=int(value))
            elif letter == 's':
                duration += datetime.timedelta(seconds=int(value))
            elif letter == 'd':
                duration += datetime.timedelta(days=int(value))
            elif letter == 'w':
                duration += datetime.timedelta(days=7*int(value))

            value = ''

    if len(value) > 0:
        duration += datetime.timedelta(minutes=int(value))

    return sign * duration
