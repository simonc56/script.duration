script.duration
===============

Displays movies duration in hours and minutes instead of only minutes while navigating in Kodi movies library. Kodi skin has to be tweaked.

Exemple: __108 minutes__ is now displayed __1h48__.

When launched the script provides those properties :

* `Window(Home).Property(Duration.HoursMinutes)`
* `Window(Home).Property(Duration.Hours)`
* `Window(Home).Property(Duration.Minutes)`
* `Window(Home).Property(Duration.DBID)`

##Exemple of integration in Estuary skin

2 files need to be modified as follow :

###Variables.xml

Add this new variable at the end of the file (before the `</include>`) :
```
<variable name="ItemDuration">
    <value condition="System.HasAddon(script.duration)+
                            [Window.IsVisible(Videos) | Window.IsVisible(Movieinformation)] +
                            !String.IsEmpty(Window(Home).Property(Duration.Hours)) +
                            !String.IsEqual(Window(Home).Property(Duration.Hours),0) +
                            !String.IsEmpty(Window(Home).Property(Duration.DBID)) + String.IsEqual(Window(Home).Property(Duration.DBID),ListItem.DBID)">$INFO[Window(Home).Property(Duration.HoursMinutes)]
        </value>
	<value>$INFO[ListItem.Duration] min</value>
</variable>
```

###Includes.xml

Replace `<label>$INFO[$PARAM[infolabel_prefix]ListItem.Duration]</label>` with `<label>$VAR[ItemDuration]</label>`

______________________
