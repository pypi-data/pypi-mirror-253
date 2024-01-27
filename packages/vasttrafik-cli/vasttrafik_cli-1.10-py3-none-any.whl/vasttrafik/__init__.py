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

from dataclasses import dataclass, field
import urllib.request
import urllib.parse
import datetime
from enum import Enum
import json
import re
from time import time
from typing import Dict, List, Optional, NamedTuple, Union, Literal
from pathlib import Path

from wcwidth import wcswidth as ulen  # type: ignore
from typedload import load, dump
from xtermcolor import colorize  # type: ignore


@dataclass
class Location:
    '''
    Generic location
    '''
    name: str
    latitude: float
    longitude: float

    def __str__(self):
        return self.name


@dataclass
class Stop(Location):
    '''
    The object represents a stop or a position.
    '''
    locationType: Literal['stoparea', 'metastation', 'stoppoint']
    gid: str

@dataclass
class PointOfInterest(Location):
    locationType: Literal['pointofinterest']

@dataclass
class Address(Location):
    locationType: Literal['address']


@dataclass
class Token:
    expires_in: int
    access_token: str

    def expired(self) -> bool:
        return self.expires_in < time()


def _reportload(data, type_):
    try:
        return load(data, type_)
    except:
        print('FAILED TO PARSE DATA')
        print(data)
        raise


class Vasttrafik:

    def __init__(self, key: str, tokenfile: Path) -> None:
        '''
        key is the API key that must be sent on every request to obtain a reply.
        you can obtain one at api.vasttrafik.se, but it will be activated the
        night after registration.
        '''
        self.key = key
        self._tokenfile = tokenfile
        self._token: Optional[Token] = None

    def _get_token(self) -> Token:
        # Attempt to get cached token
        if self._token is None and self._tokenfile.exists():
            with self._tokenfile.open('rt') as f:
                self._token = load(json.load(f), Token)

        # If there is a token but it's expired, null it
        if self._token and self._token.expired():
            self._token = None

        if self._token is None:
            self._token = self._renew_token()

            with self._tokenfile.open('wt') as f:
                json.dump(dump(self._token), f)
        return self._token

    def _renew_token(self) -> Token:
        url = 'https://ext-api.vasttrafik.se/token'
        req = urllib.request.Request(url)
        req.data = b'grant_type=client_credentials'
        req.headers['Authorization'] = 'Basic ' + self.key
        with urllib.request.urlopen(req) as f:
            r = load(json.load(f), Token)
        r.expires_in += int(time())
        return r

    def _request(self, service: str, params: dict[str, str]):
        token = self._get_token().access_token

        url = f"https://ext-api.vasttrafik.se/pr/v4/{service}?{urllib.parse.urlencode(params)}"
        req = urllib.request.Request(url)
        req.headers['Authorization'] = 'Bearer ' + token
        req.headers['accept'] = 'text/plain'
        r = b''
        with urllib.request.urlopen(req) as f:
            while True:
                l = f.read()
                if len(l) == 0:
                    break
                r += l

        if r.strip().startswith(b'Invalid authKey'):
            raise Exception('Invalid authKey')

        return json.loads(r.decode('utf8'))

    def location(self, user_input: str) -> list[Stop | PointOfInterest | Address]:
        '''Returns a list of Stop objects, completing from the user input'''
        a = self._request("locations/by-text", {'q': user_input, 'limit':'10'})

        return _reportload(a['results'], list[Stop | PointOfInterest | Address])

    def board(self, stop: Stop, time_span:int|None=None, departures:int=2, datetime_obj: datetime.datetime | None=None) -> List['GroupedBoardItem']:
        '''Returns a departure board for a given station'''

        params: dict[str, str] = {}
        # TODO params['includeOccupancy'] = 'true'
        params['maxDeparturesPerLineAndDirection'] = str(departures)
        params['limit'] = '30'
        if datetime_obj:
            params['startDateTime'] = datetime_obj.isoformat()
        if time_span:
            params['timeSpanInMinutes'] = str(time_span)

        b = self._request(f'stop-areas/{stop.gid}/departures', params)

        boarditems = load(b['results'], List[BoardItem])
        return GroupedBoardItem.group(boarditems)


    def trip(
            self,
            origin: Location,
            dest: Location,
            datetime_relates: Literal['arrival', 'departure'],
            datetime_obj: datetime.datetime | None,
    ) -> list['Trip']:
        params = {}

        params['limit'] = '10'
        params['onlyDirectConnections'] = 'false'
        params['includeNearbyStopAreas'] = 'false'
        params['includeOccupancy'] = 'false'

        if hasattr(origin, 'gid'):
            params['originGid'] = origin.gid
        else:
            params['originLatitude'] = str(origin.latitude)
            params['originLongitude'] = str(origin.longitude)

        if hasattr(dest, 'gid'):
            params['destinationGid'] = dest.gid
        else:
            params['destinationLatitude'] = str(dest.latitude)
            params['destinationLongitude'] = str(dest.longitude)

        if datetime_obj:
            params['dateTimeRelatesTo'] = datetime_relates
            params['dateTime'] = datetime_obj.isoformat()

        # Request
        b = self._request('journeys', params)
        trips = _reportload(b['results'], list[Trip])

        # Clear empty trips… yes it's a thing
        return [i for i in trips if i.allLegs]


@dataclass
class Note:
    type: str
    severity: Literal['unknown', 'low', 'normal', 'high']
    text: str

    def toTerm(self):
        if self.severity == 'high':
            return colorize(self.text, ansi=1)
        if self.severity == 'normal':
            return colorize(self.text, ansi=3)
        return self.text


class VehicleType(Enum):
    TRAM = 'tram'
    BUS = 'bus'
    TRAIN = 'train'
    FERRY = 'ferry'
    TAXI = 'taxi'
    WALK = 'walk'
    UNKNOWN = 'unknown'
    NONE = 'none'
    BIKE = 'bike'
    CAR = 'car'

    @property
    def symbol(self) -> str:
        s = {
            self.TRAIN: '🚅',
            self.TRAM: '🚋',
            self.BUS: '🚌',
            self.FERRY: '⛴',
            self.TAXI: '🚕',
            self.WALK: '🚶‍♂️',
            self.UNKNOWN: '',
            self.NONE: '',
            self.BIKE: '🚴',
            self.CAR: '🚗',
        }
        return s[self]  # type: ignore


@dataclass
class Line:
    name: str
    shortName: str
    backgroundColor: str
    foregroundColor: str
    borderColor: str
    transportMode: VehicleType

@dataclass
class Journey:
    direction: str
    line: Line

@dataclass
class StopPoint:
    name: str
    gid: str
    platform: str = ''


@dataclass
class BoardItem:

    '''
    This represents one item of the panel at a stop
    has a bunch of attributes to represent the stop
    '''
    plannedTime: datetime.datetime
    isCancelled: bool
    isPartCancelled: bool
    serviceJourney: Journey
    stopPoint: StopPoint
    estimatedTime: datetime.datetime | None = None

@dataclass
class GroupedBoardItem:
    boarditems: list[BoardItem]

    @staticmethod
    def group(items: list[BoardItem]) -> list['GroupedBoardItem']:

        # Sort platforms, so all trams from a platform appear together
        items.sort(key=lambda i: i.stopPoint.platform)

        r = [GroupedBoardItem([items.pop(0)])]

        for i in items:
            added = False
            for group in r:
                firstitem = group.boarditems[0]

                if i.stopPoint == firstitem.stopPoint and i.serviceJourney == firstitem.serviceJourney:
                    # Group
                    added = True
                    group.boarditems.append(i)
            if not added:
                r.append(GroupedBoardItem([i]))

        return r

    @property
    def track(self) -> str:
        return self.boarditems[0].stopPoint.platform

    def toTxt(self):
        return self.toTerm(color=False)

    def toTerm(self, color=True) -> str:
        '''Returns a string representing the BoardItem colorized using
        terminal escape codes.

        Servertime must be retrieved from the Vasttrafik class, and indicates
        the time on the server, it will be used to show the difference in
        minutes before the arrival.
        '''
        bus = self.getName(color)
        delta = self.departures()
        return '%s %0*d%s -> %s # %s' % (bus, 2, delta[0][0], delta[0][1], self.boarditems[0].serviceJourney.direction, ','.join(map(lambda i: str(i[0]) + i[1], delta)))

    def departures(self) -> List[tuple[int, str]]:
        delta = [((((i.estimatedTime if i.estimatedTime else i.plannedTime) - datetime.datetime.now(datetime.timezone.utc)).seconds // 60), ('👻' if i.isPartCancelled else '') + ('🪦' if i.isCancelled else '')) for i in self.boarditems]
        delta.sort()
        return delta

    def getName(self, color=False):
        '''Returns a nice version of the name
        If color is true, then 256-color escapes will be
        added to give the name the color of the line'''
        name = self.boarditems[0].serviceJourney.line.shortName + ' '

        name += self.boarditems[0].serviceJourney.line.transportMode.symbol

        while ulen(name) < 20:
            name = " " + name

        if not color:
            return name

        fgcolor = int('0x' + self.boarditems[0].serviceJourney.line.foregroundColor[1:], 16)
        bgcolor = int('0x' + self.boarditems[0].serviceJourney.line.backgroundColor[1:], 16)
        return colorize(name, fgcolor, bg=bgcolor)


@dataclass
class LegHalf:
    stopPoint: StopPoint

    # These fields are not needed, since they are duplicates of what is in the Leg class
    # plannedTime
    # estimatedTime
    # estimatedOtherwisePlannedTime
    # notes

@dataclass
class ConnectionLeg:
    origin: LegHalf
    destination: LegHalf
    transportMode: VehicleType
    plannedDepartureTime: datetime.datetime
    plannedArrivalTime: datetime.datetime
    plannedDurationInMinutes: int
    estimatedDepartureTime: datetime.datetime | None = None
    estimatedArrivalTime: datetime.datetime | None = None
    estimatedDurationInMinutes: int | None = None

    @property
    def hidden(self) -> bool:
        return hasattr(self.origin.stopPoint, 'gid') and hasattr(self.destination.stopPoint, 'gid') and self.origin.stopPoint.name == self.destination.stopPoint.name

    def toTerm(self) -> str:
        departure = str((self.estimatedDepartureTime if self.estimatedDepartureTime else self.plannedDepartureTime).time())[:5]
        arrival = str((self.estimatedArrivalTime if self.estimatedArrivalTime else self.plannedArrivalTime).time())[:5]

        name = 'go ' + self.transportMode.symbol
        while ulen(name) < 33:
            name = ' ' + name

        r = f'{name} {departure}\t{arrival}\t{self.origin.stopPoint.name} -> {self.destination.stopPoint.name}'
        return r

@dataclass
class Leg:
    origin: LegHalf
    destination: LegHalf
    serviceJourney: Journey
    isCancelled: bool
    isPartCancelled: bool
    plannedDepartureTime: datetime.datetime
    plannedArrivalTime: datetime.datetime
    plannedDurationInMinutes: int
    estimatedDepartureTime: datetime.datetime | None = None
    estimatedArrivalTime: datetime.datetime | None = None
    estimatedDurationInMinutes: int | None = None
    notes: tuple[Note, ...] = tuple()

    @property
    def hidden(self) -> bool:
        return False

    def toTerm(self) -> str:
        name = self.getName()
        departure = str((self.estimatedDepartureTime if self.estimatedDepartureTime else self.plannedDepartureTime).time())[:5]
        arrival = str((self.estimatedArrivalTime if self.estimatedArrivalTime else self.plannedArrivalTime).time())[:5]

        r = f'{name} {departure}\t{arrival}\t{self.origin.stopPoint.name} -> {self.destination.stopPoint.name}'
        if self.notes:
            r += '\n' + '\n'.join(i.toTerm() for i in self.notes)
        return r

    def getName(self) -> str:
        name = self.serviceJourney.line.shortName + ' '
        name += self.serviceJourney.direction + ' '

        if self.isCancelled:
            name = '🪦' + name
        elif self.isPartCancelled:
            name = '👻' + name

        if len(name) > 29:
            name = name[:29] + ' '

        name += self.serviceJourney.line.transportMode.symbol

        while ulen(name) < 33:
            name = ' ' + name

        fgcolor = int('0x' + self.serviceJourney.line.foregroundColor[1:], 16)
        bgcolor = int('0x' + self.serviceJourney.line.backgroundColor[1:], 16)
        return colorize(name, fgcolor, bg=bgcolor)


@dataclass
class Trip:
    tripLegs: list[Leg] = field(default_factory=list)
    isDeparted: bool = False
    connectionLinks: list[ConnectionLeg] = field(default_factory=list)

    @property
    def allLegs(self) -> list[Leg | ConnectionLeg]:
        r: list[Leg | ConnectionLeg] = self.tripLegs + self.connectionLinks
        r.sort(key=lambda i: i.plannedDepartureTime)
        return r

    def toTerm(self) -> str:
        return '\n'.join(i.toTerm() for i in self.allLegs if i.hidden == False)

    @property
    def duration(self) -> int:
        if not self.tripLegs:
            return 0
        start = self.tripLegs[0].estimatedDepartureTime if self.tripLegs[0].estimatedDepartureTime else self.tripLegs[0].plannedDepartureTime
        end = self.tripLegs[-1].estimatedArrivalTime if self.tripLegs[-1].estimatedArrivalTime else self.tripLegs[-1].plannedArrivalTime

        delta = end - start
        return delta.seconds // 60
