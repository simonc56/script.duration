script.duration
===============

Displays movies duration in hours and minutes instead of only minutes while navigating in Kodi movies library.

Exemple: __108 minutes__ is now displayed __1h48__.

When launched the script provides those properties :

* `Window(videolibrary).Property(Duration)`
* `Window(movieinformation).Property(Duration)`

To use it in your skin, just call it this way :

* `RunScript(script.duration,duration=$INFO[ListItem.Duration])` for a one shot request
* `RunScript(script.duration,backend=True)` to run in background

##Integration in your skin

3 files need to be modified as follow :

###MyVideoNav.xml

Add `<onload>RunScript(script.duration,backend=True)</onload>` at the beginning.

###variables.xml

Add this new variable at the end of the file (before the `</include>`) :
```
<variable name="MovieDuration">
    <value condition="System.HasAddon(script.duration)">$INFO[window.Property(Duration)]</value>
	<value>$INFO[ListItem.Duration]</value>
</variable>
```
Then, still in variables.xml, do those replacements :

`$INFO[ListItem.Duration]`                         replaced by `$VAR[MovieDuration]`

`$INFO[ListItem.Duration,, $LOCALIZE[12391]]`      replaced by `$VAR[MovieDuration]`

`$INFO[ListItem.Duration, • , $LOCALIZE[12391]]`   replaced by ` • $VAR[MovieDuration]` (one space before and after the dot)

###DialogVideoInfo.xml

Add `<onload>RunScript(script.duration,duration=$INFO[ListItem.Duration])</onload>` at the beginning.

Replace `$INFO[ListItem.Duration]` with `$VAR[MovieDuration]`

______________________

_This is my first kodi addon, for any suggestions, do not hesitate to email me :)_