from typing import Iterator
from datetime import datetime
from bs4 import BeautifulSoup as Soup
from functools import cached_property
from dataclasses import dataclass, field

from . import base

class App(base.App):
    '''
    App for the presences.
    '''
    
    @cached_property
    def _soup(self) -> Soup:
        '''
        Fetch all of today's presences.
        '''
        
        assert self.client.logged
        
        soup = Soup(self.client._call('student/presences').text, 'html.parser')
        return soup.find('tbody', {'id': 'body_presences'})
        
    @cached_property
    def current(self) -> str:
        '''
        Get the current presence status.
        '''
        
        current_class = self._soup.find('tr', {'class': 'warning'})
        current_class_url = current_class.find('a', {'class': 'btn-primary'}).get('href')

        current_class_document = self.client_call(current_class_url).text
        current_class_soup = Soup(current_class_document, 'html.parser')
        
        button = current_class_soup.find('div', {'id': 'body_presence'}).text
        button = ' '.join(button.strip().split())
        
        return button

# EOF