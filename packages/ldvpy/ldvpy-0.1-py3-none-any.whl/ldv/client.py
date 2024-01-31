import requests

from . import apps, consts

class Client:
    '''
    Represents a connection to the LDV portal.
    '''
    
    def __init__(self, address: str, password: str, login: bool = True) -> None:
        '''
        Initialises a new Client connection.
        '''
        
        self.logged = False
        self.address = address
        self._password = password
        
        self.session = requests.Session()
        
        # Connect apps
        self.rooms = apps.rooms.App(self)
        self.presence = apps.presence.App(self)
        
        ...
        
        if login:
            self.login()
    
    def _call(self, func: str, method: str = 'GET', data: dict = None) -> requests.Response:
        '''
        Send a request to the LDV servers.
        '''
        
        if not '://' in func:
            func = consts.ROOT + func
        
        response = self.session.request(
            method = method,
            url = func,
            data = data
        )
        
        response.raise_for_status()
        return response
    
    def login(self) -> None:
        '''
        Attempts to login.
        '''

        # Send analyse query
        analyser = self._call(
            'ajax.inc.php', 'POST',
            {'act': 'ident_analyse', 'login': self.address}
        )
        
        backend_url = consts.ROOT + consts.regex.get_lssop_url(analyser.text)
        
        # Authenfificate to SSO
        authorized_url = self._call(backend_url).url
        
        sso = self._call(
            authorized_url, 'POST',
            {
                'UserName': self.address,
                'Password': self._password,
                'AuthMethod': 'FormsAuthentication'
            }
        ).text
        
        # Authentificate to SAML
        saml_backend = consts.regex.get_saml_form(sso)
        saml_token = consts.regex.get_saml_token(sso)
        
        self._call(
            saml_backend, 'POST',
            {'SAMLResponse': saml_token}
        )
                
        self.logged = True

# EOF        