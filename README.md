### Live ControlSurface Starter

My go-to template to bootstrap ControlSurface scripts for Ableton.  
Tested on Live 11.0 but should also work on Live 10.1.x

### Usage
Make sure to create ```log.txt``` in the same directory as log.py after cloning your repo!

### Features:
1. An interpreter-like debug server! run ```python debug/client.py``` in a shell when Ableton is running (with your control script enabled) to get interpreter-like access using Python's ```eval```. Just be mindful of the scope.
2. Logging. AFAIK, Ableton does not provide an easy way to do custom logging(the functions write to ```Log.txt``` in their Preferences folder).
Use ```self.log``` to log to ```log.txt``` which remains in the current dir! Logs are cleared on re-initialization of the control surface or on Live restart

### Warning:
**Do NOT** send untrusted code into the "interpreter" client as **it uses** ``eval`` on the server!

### Contributing
Open to ideas/suggestions/feedback and pull requests.
