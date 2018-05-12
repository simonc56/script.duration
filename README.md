script.duration
===============

Displays movies duration in hours and minutes instead of only minutes while navigating in Kodi 17 movies library. Kodi skin has to be tweaked, see exemple below.

Exemple: __108 minutes__ is now displayed __1h48__.

When launched the script provides those properties :

* `Window(Home).Property(Durations.HoursMinutes)`
* `Window(Home).Property(Durations.Hours)`
* `Window(Home).Property(Durations.Minutes)`
* `Window(Home).Property(Durations.DBID)`

### Exemple of integration in Estuary skin

2 files need to be modified as follow :

#### Variables.xml

Add this new variable at the end of the file (before the `</include>`) :
```
<variable name="ItemDuration">
    <value condition="System.HasAddon(script.duration)+
        [Window.IsVisible(Videos) | Window.IsVisible(Movieinformation)] +
        !String.IsEmpty(Window(Home).Property(Durations.Hours)) +
        !String.IsEqual(Window(Home).Property(Durations.Hours),0) +
        !String.IsEmpty(Window(Home).Property(Durations.DBID)) +
        String.IsEqual(Window(Home).Property(Durations.DBID),ListItem.DBID)">$INFO[Window(Home).Property(Durations.HoursMinutes)]</value>
    <value>$INFO[ListItem.Duration] min</value>
</variable>
```

#### Includes.xml

Replace `<label>$INFO[ListItem.Duration,, $LOCALIZE[31132]]</label>` with `<label>$VAR[ItemDuration]</label>`

______________________
