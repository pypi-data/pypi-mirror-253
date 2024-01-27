#!/usr/bin/env python3
# vasttrafik-cli
# Copyright (C) 2012-2024 Salvo "LtWorf" Tomaselli
#
# vasttrafik-cli is free software: you can redistribute it and/or modify
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

import sys
import datetime
import os
from typing import Optional, Literal
from pathlib import Path

from vasttrafik import Vasttrafik, Stop, Location


CONFIGDIR = Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config'))
CACHEDIR = Path(os.environ.get('XDG_CACHE_HOME', Path.home() / '.cache'))


def init() -> None:
    '''
    Create expected files and directories
    '''
    if not CACHEDIR.exists():
        CACHEDIR.mkdir(parents=True)


def get_key() -> str:
    '''
    This function tries to load the API key from some configuration files.
    It will try, in the order:
        - /etc/vasttrafik-cli.conf
        - ~/.vasttrafik-cli

    If the files aren't found or they don't contain the key attribute then
    None will be returned, otherwise, a string containing the key will be
    returned.
    '''
    paths = (
        Path.home() / '.vasttrafik-cli',
        CONFIGDIR / 'vasttrafik-cli.conf',
        Path('/etc/vasttrafik-cli.conf'),
    )

    path = None
    for i in paths:
        if i.exists():
            path = i
            break
    if path is None:
        # No configuration, using this hardcoded token
        return 'b2hWUmlXc192b0pYMENabTh6WmNfUlBFRGFZYTpjYjZ1U2MzSnp4ZlozRnU1V0tLZlVBSVlGNVFh'

    config = {}
    with open(path, 'rt') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, value = line.split('=', 1)
            key = key.strip()
            value = value.strip()
            config[key] = value
    return config['key']


init()
key = get_key()
vast = Vasttrafik(key, CACHEDIR / 'vasttrafik-cli-token')


def save_completion(name: str) -> None:
    """
    Saves the name of the stop in the completion file
    """
    # Trim up to the part completion can manage
    for char in ' ,':
        if char in name:
            name = name.split(char, 1)[0]
    # Only lower
    name = name.lower()

    # Read file or presume empty
    path = CACHEDIR / 'vasttrafik-cli-stops'
    if path.exists():
        with path.open('rt') as f:
            lines = [i.strip() for i in f]
    else:
        lines = []

    # Do nothing if completion is there already
    if name in lines:
        return

    # Append new stop to completion
    lines.append(name)

    # Remove old completions, if necessary
    if len(lines) > 100:
        lines.pop(0)

    # Write the file again
    with path.open('wt') as f:
        f.write('\n'.join(lines))


def get_stop(prompt: str, stops_only: bool, preset: str|None=None):
    if preset:
        r = vast.location(preset)
        if stops_only:
            r = [i for i in r if isinstance(i, Stop)]
        save_completion(r[0].name)
        return r[0]

    while True:
        try:
            line = input(prompt)
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        if not line:
            return None

        stops = vast.location(line)

        for i in range(len(stops)):
            print("%d: %s" % (i, stops[i].name))
            if i > 8:
                break

        while True:
            try:
                line = input('> ')
            except (KeyboardInterrupt, EOFError):
                sys.exit(0)
            try:
                save_completion(stops[int(line)].name)
                return stops[int(line)]
            except:
                break


def get_time(default):
    if default:
        return datetime.datetime.now(datetime.timezone.utc).astimezone()
    try:
        line = input('Insert time? [N/y]')
    except KeyboardInterrupt:
        sys.exit(0)
    except EOFError:
        line = ''
    if line != 'y':
        return datetime.datetime.now(datetime.timezone.utc).astimezone()

    try:
        hour = input('Hour: ')
        minute = input('Minutes: ')
    except (KeyboardInterrupt, EOFError):
        sys.exit(0)

    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    r = now.replace(minute=int(minute), hour=int(hour))

    if (r - now).total_seconds() < 0:
        # Must increment one day
        r += datetime.timedelta(days=1)
    return r


def tripmain():
    if len(sys.argv) not in {1, 3, 5}:
        sys.exit('Invalid number of parameters')
    orig = sys.argv[1] if len(sys.argv) > 1 else None
    dest = sys.argv[2] if len(sys.argv) > 1 else None

    origstop = get_stop('FROM: > ', False, orig)
    deststop = get_stop('TO: > ', False, dest)

    if origstop is None or deststop is None:
        return


    if len(sys.argv) == 5:
        if sys.argv[3] not in {'depart', 'arrive'}:
            sys.exit(f'Invalid parameter {sys.argv[3]}')
        arrive_depart: Literal['arrival', 'departure'] = 'arrival' if sys.argv[3] == 'arrive' else 'departure'

        try:
            hour, minute = sys.argv[4].replace('.', ':').split(':', 1)
            now = datetime.datetime.now(datetime.timezone.utc).astimezone()
            time = now.replace(minute=int(minute), hour=int(hour))
        except Exception:
            sys.exit(f'Unable to parse {sys.argv[4]} as HH:MM')
        if (time - now).total_seconds() < 0:
            # Must increment one day
            time += datetime.timedelta(days=1)
    else:
        time = None
        arrive_depart = 'arrival'


    print('\t%s → %s' % (origstop.name, deststop.name))
    for i in vast.trip(origstop, deststop, arrive_depart, time):
        print(i.toTerm())
        print(f'Duration: {i.duration} minutes')
        print("=========================")


def stopsmain():
    if len(sys.argv) > 2:
        sys.exit('Invalid number of parameters')
    preset = sys.argv[1] if len(sys.argv) == 2 else ''
    stop = get_stop('> ', True, preset)
    trams = vast.board(stop, time_span=120, departures=4)

    print(f"\t\t{stop.name}\n")

    prev_track = None
    for i in trams:
        if prev_track != i.track:
            print("   == Platform %s ==" % i.track)
        prev_track = i.track
        print(i.toTerm())
