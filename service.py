# -*- coding: UTF-8 -*-

import xbmc, xbmcaddon, xbmcgui

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

def get_hours_and_minutes(minutes_string):
    try:
        full_minutes = int(minutes_string)
        minutes = full_minutes % 60
        hours   = full_minutes // 60
        return str(hours) + 'h' + str(minutes).zfill(2)
    except:
        return ''

def get_hours_only(minutes_string):
    try:
        full_minutes = int(minutes_string)
        hours   = full_minutes // 60
        return str(hours)
    except:
        return ''

def get_minutes_only(minutes_string):
    try:
        full_minutes = int(minutes_string)
        minutes = full_minutes % 60
        return str(minutes).zfill(2)
    except:
        return ''

class Main:
    def __init__( self ):
        log("version %s started" % __version__)
        self.previousitem = ""
        self.monitor = xbmc.Monitor()
        self.run_service()

    def run_service(self):
        while not self.monitor.abortRequested():
            if self.monitor.waitForAbort(0.2):
                break
            if ((xbmc.getCondVisibility("Window.IsActive(Videos)") and xbmc.getCondVisibility("Window.Is(Videos)")) or (xbmc.getCondVisibility("Window.IsActive(MovieInformation)") and xbmc.getCondVisibility("Window.Is(MovieInformation)"))) and not xbmc.getCondVisibility("Container.Scrolling"):
                self.selecteditem = xbmc.getInfoLabel("ListItem.DBID")
                if (self.selecteditem and self.selecteditem != self.previousitem):
                    self.previousitem = self.selecteditem
                    
                    if (xbmc.getInfoLabel("ListItem.DBID") > -1 and not xbmc.getCondVisibility("ListItem.IsFolder")) and xbmc.getInfoLabel("ListItem.Duration") and int(float(xbmc.getInfoLabel("ListItem.Duration"))) > 0:
                        self.duration = xbmc.getInfoLabel("ListItem.Duration")
                        self.dbid = xbmc.getInfoLabel("ListItem.DBID")
                        self.set_duration_values()
            else:
                my_container_id = xbmc.getInfoLabel("Window(Home).Property(Durations.WidgetContainerId)")
                my_container_window = xbmc.getInfoLabel("Window(Home).Property(Durations.WidgetContainerWindowName)")
                
                if (my_container_id and my_container_window and (xbmc.getCondVisibility("Control.HasFocus("+my_container_id+")") and xbmc.getCondVisibility("Window.IsActive("+my_container_window+")") and xbmc.getCondVisibility("Window.Is("+my_container_window+")")) and not xbmc.getCondVisibility("Window.IsActive(Videos)") and not xbmc.getCondVisibility("Window.IsActive(MovieInformation)")) and not xbmc.getCondVisibility("Container("+my_container_id+").Scrolling"):
                    self.selecteditem = xbmc.getInfoLabel("Container("+my_container_id+").ListItem.DBID")
                    if (self.selecteditem and self.selecteditem != self.previousitem):
                        self.previousitem = self.selecteditem
                        if (xbmc.getInfoLabel("Container("+my_container_id+").ListItem.DBID") > -1 and not xbmc.getCondVisibility("Container("+my_container_id+").ListItem.IsFolder")) and xbmc.getInfoLabel("Container("+my_container_id+").ListItem.Duration") and int(float(xbmc.getInfoLabel("Container("+my_container_id+").ListItem.Duration"))) > 0:
                            self.duration = xbmc.getInfoLabel("Container("+my_container_id+").ListItem.Duration")
                            self.dbid = xbmc.getInfoLabel("Container("+my_container_id+").ListItem.DBID")
                            self.set_duration_values()
    #run_service end

    def set_duration_values(self):
        log('Converts: '+self.duration+' min')
        # HoursMinutes
        hours_and_minutes = get_hours_and_minutes(self.duration)
        xbmc.executebuiltin('SetProperty(Durations.HoursMinutes,"'+hours_and_minutes+'",home)')
        # Hours
        hours_only = get_hours_only(self.duration)
        xbmc.executebuiltin('SetProperty(Durations.Hours,"'+hours_only+'",home)')
        # Minutes
        minutes_only = get_minutes_only(self.duration)
        xbmc.executebuiltin('SetProperty(Durations.Minutes,"'+minutes_only+'",home)')
        # DBID
        xbmc.executebuiltin('SetProperty(Durations.DBID,"'+self.dbid+'",home)')
        # InputDurationMinutes
        xbmc.executebuiltin('SetProperty(Durations.InputDurationMinutes,"'+self.duration+'",home)')

if (__name__ == "__main__"):
    Main()
log('script finished.')
