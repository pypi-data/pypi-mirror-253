from typing import Iterator
from datetime import datetime
from bs4 import BeautifulSoup as Soup
from functools import cached_property
from dataclasses import dataclass, field

from . import base
from .. import consts

@dataclass
class Lesson:
    name : str
    start: datetime = field(repr = None)
    end  : datetime = field(repr = None)

@dataclass
class Room:
    name   : str
    size   : int
    desc   : str          = field(repr = None)
    lessons: list[Lesson] = field(repr = None)

def to_time(raw: str) -> datetime:
    '''
    Convert raw tome to date object.
    '''
    
    h, m = raw.split(':')
    
    return datetime.now().replace(
        hour = int(h),
        minute = int(m),
        second = 0,
        microsecond = 0
    )

class App(base.App):
    '''
    App for the classrooms.
    '''
    
    @cached_property
    def all(self) -> Iterator[Room]:
        '''
        Fetch all the rooms.
        '''
        
        assert self.client.logged

        soup = Soup(self.client._call('student/salles/').text, 'html.parser')
        lines: Iterator[Soup] = soup.find('tbody').find_all('tr')
        
        for line in lines:
            
            cells = line.find_all('td', {'class': 'success'})
            
            yield Room(
                name  = (name := line.find('a').text).split()[0],
                size  = int(consts.regex.get_room_size(name)),
                desc  = line.find('span').text,
                lessons = [
                    Lesson(
                        start = to_time((dt := (dr := cell.find('div').text).split('-'))[0]),
                        end = to_time(dt[1]),
                        name = cell.text.replace(dr, ''),
                    )
                    for cell in cells
                ]
            )
    
    def get(self, room: str) -> Room:
        '''
        Get a room by name.
        '''
        
        for room in self.all:
            if room.name == room:
                return room

# EOF