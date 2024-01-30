**R  S  S  B  O  T**


!!


**NAME**

|
| RSSBOT - 24/7 feed fetcher.
|

**DESCRIPTION**

|
| RSSBOT is a python3 bot able to display rss feeds in your channel.
|
| It provides all the tools to program a bot, such as disk perisistence
| for configuration files, event handler to handle the client/server
| connection, code to introspect modules for commands, deferred
| exception handling to not crash on an error, a parser to parse
| commandline options and values, etc.
|
| You can copy/paste the service file and run it under systemd for
| 24/7 presence in a IRC channel.
|

**SYNOPSIS**

|
| rssbot <cmd> [key=val]
| rssbot [-c] [-v] 
| rssbotd
|

**INSTALL**

|
| pipx install rssbot
|

**USAGE**

|
| default action is doing nothing
|
| $ rssbot
| $

first argument is a command

|
| $ rssbot cmd
| cfg,cmd,dpl,mre,nme,pwd,rem,rss,ver

starting a console requires an option

|
| $ rssbot -c
| >

to start the rssbot as daemon

|
| $ rssbot -d
| $ 

add -v if you want to have verbose logging

|
| $ rssbot -cv
| RSSBOT started Wed Nov 8 15:38:56 2023 CVI
| >
|

**CONFIGURATION**


irc configuration is done with the cli interface
using the ``cfg`` command

|
| $ rssbot cfg server=<server>
| $ rssbot cfg channel=<channel>
| $ rssbot cfg nick=<nick>

sasl need a nickserv nick/password pair to generate
a password for sasl

|
| $ rssbot pwd <nsnick> <nspass>
| $ rssbot cfg password=<frompwd>

rss has several configuration commands

|
| $ rssbot rss <url>
| $ rssbot dpl <url> <item1,item2>
| $ rssbot rem <url>
| $ rssbot nme <url> <name>
|

**COMMANDS**

here is a list of the commands (use rssbot <cmd>)

|
| cfg - irc configuration
| cmd - commands
| dpl - sets display items
| mre - displays cached output
| pwd - sasl nickserv name/pass
| rem - removes a rss feed
| rss - add a feed
|

**SYSTEMD**

save the following it in /etc/systems/system/rssbot.service and
replace "<user>" with the user running pipx

|
| [Unit]
| Description=24/7 feed fetcher
| Requires=network.target
| After=network.target
|
| [Service]
| Type=simple
| User=<user>
| Group=<user>
| WorkingDirectory=/home/<user>/.rssbot
| ExecStart=/home/<user>/.local/pipx/venvs/rssbot/bin/rssbotd
| RemainAfterExit=yes
|
| [Install]
| WantedBy=multi-user.target
|
|

if you don't have a ~/.rssbot directory you need to create it

|
| $ mkdir ~/.rssbot
|

then run this

|
| $ sudo systemctl enable rssbot --now
|
| default channel/server is #rssbot on localhost
|

**FILES**

|
| ~/.rssbot
| ~/.local/bin/rssbot
| ~/.local/bin/rssbotd
| ~/.local/pipx/venvs/rssbot/
|

**AUTHOR**

|
| Bart Thate <objx@proton.me>
|

**COPYRIGHT**

|
| RSSBOT is Public Domain.
