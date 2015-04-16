script.duration
===============

Displays movies duration in the format __hours:minutes__ instead of __minutes__ while navigating in Kodi movies library.

Exemple: __108 minutes__ is now displayed __1h48__

When launched it provides those properties :

* Window(videolibrary).Property(Duration)
* Window(movieinformation).Property(Duration)

To use it in your skin, just call it this way :

* RunScript(script.duration,duration=$INFO[ListItem.Duration]) for a one shot request
* RunScript(script.duration,backend=True) to run in background

##Integration in your skin

###MyVideoNav.xml

Add <onload>RunScript(script.duration,backend=True)</onload> at the beginning

###variables.xml

Add $INFO[window.Property(Duration)] labels as an alternative to $INFO[ListItem.Duration] with a System.HasAddon(script.duration) condition

###DialogVideoInfo.xml

Add <onload>RunScript(script.duration,duration=$INFO[ListItem.Duration])</onload> at the beginning

Add $INFO[window.Property(Duration)] label as an alternative to $INFO[ListItem.Duration] with a System.HasAddon(script.duration) condition

______________________

_This is my first kodi addon, for any suggestions, do not hesitate to email me :)_