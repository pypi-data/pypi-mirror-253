ProcessCheckerLib

Using

1.Create a new script on the device and paste it into it

import ProcessCheckerLib

ProcessCheckerLib.StartChecker('code','token','chatID')

Where token and chatId are variables that the bot holder will give you, and code can be obtained from the bot by sending it a command /code, a link to the bot will be given by its holder.

2.Run this script and keep it constantly active. (preferably demonize)

3.Paste at the beginning of all the scripts that you want to track

import ProcessCheckerLib

ProcessCheckerLib.scriptTracker()

Success!