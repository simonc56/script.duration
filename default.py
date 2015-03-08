# -*- coding: UTF-8 -*-

import xbmc, xbmcaddon, xbmcgui

# in MyVideoNav.xml add <onload>RunScript(script.duration,backend=True)</onload> at beginning

# in variables.xml find all movies labels containing Item.Duration and add !System.HasAddon(script.duration) condition
# then add a value using window.Property(Duration) with System.HasAddon(script.duration) condition

# in DialogVideoInfo.xml add <onload>RunScript(script.duration,duration=$INFO[ListItem.Duration])</onload> at beginning
# and also add <label>$INFO[window.Property(Duration)]</label> next to <label>$INFO[ListItem.Duration]</label>
# with <visible>System.HasAddon(script.duration)</visible> and <visible>!System.HasAddon(script.duration)</visible> to the original one

# Script constants
__addon__      = xbmcaddon.Addon()
__addonid__    = __addon__.getAddonInfo('id')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString
__cwd__        = __addon__.getAddonInfo('path')

def log(txt):
    if isinstance (txt,str):
        txt = txt.decode("utf-8")
    message = u'%s: %s' % (__addonid__, txt)
    xbmc.log(msg=message.encode("utf-8"), level=xbmc.LOGDEBUG)

def in_hours_and_min(minutes_string):
    full_minutes = int(minutes_string)
    minutes = full_minutes % 60
    hours   = full_minutes // 60
    return str(hours) + ':' + str(minutes).zfill(2)

class Main:
    def __init__( self ):
        log("version %s started" % __version__)
        self._init_vars()
        self._parse_argv()
        # don't run if already in backend
        if xbmc.getCondVisibility("IsEmpty(Window(videolibrary).Property(duration_backend_running))"):
            if self.backend:
                # run in backend if parameter was set
                xbmc.executebuiltin("SetProperty(duration_backend_running,true,videolibrary)")
                self.run_backend()
            if self.duration:
                self.display_duration()

    def _init_vars(self):
        #winid = xbmcgui.getCurrentWindowId()
        #log('window ID: ' + str(winid))
        self.window = xbmcgui.Window(10025) # MyVideoNav.xml (videolibrary)
        self.dialogwindow = xbmcgui.Window(12003) # DialogVideoInfo.xml (movieinformation)

    def _parse_argv( self ):
        try:
            params = dict( arg.split( '=' ) for arg in sys.argv[ 1 ].split( '&' ) )
        except:
            params = {}
        log("params: %s" % params)
        self.duration  = params.get( 'duration', False )
        self.backend = params.get( 'backend', False )

    def run_backend(self):
        self._stop = False
        self.previousitem = ""
        while not self._stop:
            if not xbmc.getCondVisibility("Container.Scrolling"):
                self.selecteditem = xbmc.getInfoLabel("ListItem.DBID")
                if (self.selecteditem != self.previousitem):
                    self.previousitem = self.selecteditem
                    if xbmc.getInfoLabel("ListItem.DBID") > -1 and not xbmc.getCondVisibility("ListItem.IsFolder"):
                        self.duration = xbmc.getInfoLabel("ListItem.Duration")
                        self.display_duration()
            xbmc.sleep(200)
            if not xbmc.getCondVisibility("Window.IsVisible(videolibrary)"):
                log('backend stopped.')
                xbmc.executebuiltin('ClearProperty(duration_backend_running,videolibrary)')
                self._stop = True

    def display_duration(self):
        log('Converts : '+self.duration+' min.')
        readable_duration = in_hours_and_min(self.duration)
        self.window.setProperty('Duration', readable_duration)
        self.dialogwindow.setProperty('Duration', readable_duration)

if (__name__ == "__main__"):
    Main()
log('script finished.')
