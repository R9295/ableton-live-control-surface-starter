### Live ControlSurface Starter

My go-to template to bootstrap ControlSurface scripts for Ableton.  
Tested on Live 11.0 but should also work on Live 10.1.x

### Features:
1. An interpreter-like debug server! run ```python debug/client.py``` in a shell when Ableton is running (with your control script enabled) to get interpreter-like access using python's ```eval```. Just be mindful of the scope.
2. Logging. AFAIK, Ableton does not provide an easy way to do custom logging(the functions provided are written to ```Log.txt``` in their Preferences folder).
Use ```self.log``` to log to ```log.txt``` which remains in the current dir! Logs are cleared on re-initialization of control surface or on Live restart
