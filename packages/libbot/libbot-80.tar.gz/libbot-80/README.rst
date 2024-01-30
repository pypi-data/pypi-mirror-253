NAME

::

    LIBBOT - the python3 bot namespave

SYNOPSIS

::

    bot <cmd> [key=val] 
    bot <cmd> [key==val]
    bot [-c] [-v] [-d]


DESCRIPTION

::



    LIBBOT is a python3 library implementing the 'bot' package. It
    provides all the tools to program a bot, such as disk perisistence
    for configuration files, event handler to handle the client/server
    connection, code to introspect modules for commands, deferred
    exception handling to not crash on an error, a parser to parse
    commandline options and values, etc.

    LIBBOT provides a demo bot, it can connect to IRC, fetch and
    display RSS feeds, take todo notes, keep a shopping list
    and log text. You can also copy/paste the service file and run
    it under systemd for 24/7 presence in a IRC channel.

    LIBBOT is a contribution back to society and is Public Domain.


INSTALL


::

    $ pipx install libbot


USAGE

::

    without any argument the bot does nothing

    $ bot
    $

    see list of commands

    $ bot cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ bot mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use mod=<name1,name2> to load additional
    modules

    $ bot cfg mod=irc

    start a console

    $ bot -c mod=irc,rss
    >

    use -v for verbose

    $ bot -cv mod=irc
    BOT started CV started Sat Dec 2 17:53:24 2023
    >

    start daemon

    $ bot -d
    $ 


CONFIGURATION


::

    irc

    $ bot cfg server=<server>
    $ bot cfg channel=<channel>
    $ bot cfg nick=<nick>

    sasl

    $ bot pwd <nsvnick> <nspass>
    $ bot cfg password=<frompwd>

     rss

    $ bot rss <url>
    $ bot dpl <url> <item1,item2>
    $ bot rem <url>
    $ bot nme <url< <name>


COMMANDS


::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    req - reconsider
    rss - add a feed
    thr - show the running threads


SYSTEMD


::

    save the following it in /etc/systems/system/botd.service and
    replace "<user>" with the user running pipx


    [Unit]
    Description=24/7 channel daemon
    Requires=network.target
    After=network.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.bot
    ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/bot -d
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target


    then run this

    $ mkdir ~/.bot
    $ sudo systemctl enable botd --now

    default channel/server is #bot on localhost


FILES

::

    ~/.bot
    ~/.local/bin/bot
    ~/.local/bin/botd
    ~/.local/pipx/venvs/libbot/


AUTHOR


::

    libbotx <libbotx@gmail.com>


COPYRIGHT


::

    LIBBOT is Public Domain.
