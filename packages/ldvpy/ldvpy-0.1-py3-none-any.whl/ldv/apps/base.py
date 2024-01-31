from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import Client

class App:
    '''
    Represents a base class for all apps.
    '''
    
    def __init__(self, client: Client) -> None:
        '''
        Initialise the app.
        '''
        
        self.client = client
        
        if hasattr(self, '__post_init__'):
            self.__post_init__()
        
        # Lock loaded keys
        self._lock = list(self.__dict__.keys()) + ['_lock']

    def refresh(self) -> None:
        '''
        Clear the app cache.
        '''
        
        for key in list(self.__dict__.keys()):
            if not key in self._lock:
                delattr(self, key)

# EOF