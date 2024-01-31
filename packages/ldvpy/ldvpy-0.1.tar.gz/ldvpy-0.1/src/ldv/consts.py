import re
from typing import Callable

ROOT = 'https://www.leonard-de-vinci.net/'

def re_findone(pattern: str, flags: int = 0) -> Callable[[str, bool], str | None]:
    '''
    Compile a single find regex.
    '''
    
    rule = re.compile(pattern, flags)
    
    def wrap(string: str, throw: bool = True) -> str | None:
        
        matches = rule.findall(string)
        if throw and len(matches) < 1:
            raise Exception('Regex error: No match found.')
        
        return matches[0]
    
    return wrap

class regex:
    '''
    Useful regexes.
    '''
    
    # Autfhentification regexes
    get_lssop_url  = re_findone( r'\"\/(lssop\/.*?)\"\);'          )
    get_saml_form  = re_findone( r'action=\"(https.*?)\"'          )
    get_saml_token = re_findone( r'SAMLResponse\" value=\"(.*?)\"' )

    # Rooms regexes
    get_room_size = re_findone( r'\[(\d+?)\]' )

# EOF