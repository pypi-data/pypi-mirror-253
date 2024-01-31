## LDVPY - A Python API for the LDV portal

Python unofficial API for the LDV dashboard.

Supported apps:
- Presence
- Rooms

Sample usage:
```py
import ldv
import time

client = ldv.Client('user@address', 'password')

while 1:
    
    client.presence.refresh()
    status = client.presence.current
    
    if 'pas encore ouvert' in status:
        print('*', status)
        time.sleep(10)
        continue
    
    le = len(status) + 2
    
    print('\033[91m+' + '-' * le + '+')
    print('| ' + status + ' |')
    print('+' + '-' * le + '+\033[0m')
```
