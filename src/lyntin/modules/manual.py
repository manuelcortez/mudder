#########################################################################
# This file is part of Lyntin.
#
# Lyntin is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# Lyntin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# copyright (c) Free Software Foundation 2001-2007
#
# $Id: manual.py,v 1.5 2007/07/24 00:39:03 willhelm Exp $
#########################################################################
"""
This module holds the README manual text.
"""
from lyntin import exported

bugs = """
Mudder is written by Manuel Cortez (manuel@manuelcortez.net). You can send your bug reports to the provided email address. All types of feedback are welcome.

Inevitably you will either run across a bug in mudder or the Lyntin framework; or the need 
for a feature to be implemented.  When this happens, we ask you 
to provide as much information as you can:

  - Operating system and version of Mudder
    (from #diagnostics).
  - Stacktrace (if it's a bug and kicked up a stacktrace).
  - Explanation of what happened vs. what should be happening.
  - Any other pertinent information.

Enter this in the issue tracker (https://github.com/manuelcortez/mudder/issues) or send it to manuel@manuelcortez.net.  

category: readme
"""

command = """
Mudder uses Lyntin as the framework for connecting to MUD games. Mudder uses Lyntin commands to allow you to setup your session with aliases, variables, actions, 
and such.  Commands start with the command character--by default 
this is "#".  It can be changed with the "#config" command.  The 
command character can also do some other special things:

1. You can execute commands in another session by typing the 
   command character and then the sesion name then the command.
   example:

      #3k say hello       - will say hello in session 3k
      #a #info            - will run the #info command in session a

2. You can switch to another session by typing the command 
   character and then the session name.  examples:

      #a                  - will switch to session a (if it exists)
      #3k                 - will switch to session 3k (if it exists)

3. You can execute a command in all sessions by typing the 
   command character then all.  examples:

      #all say hello      - will run "say hello" in all sessions

4. You can execute a command a number of times by typing the 
   command character then a number, then the command.  examples:

      #5 say hello        - will run "say hello" 5 times
      
Commands are separated by the semicolon.  Semicolons can be 
escaped with the \ character.  examples:

   say hello;wave         - will run "say hello" then "wave"
   say hi!  \;)           - will run "say hi!  ;)"

Command arguments can be enclosed with { }.  This enables you to 
specify arguments that have multiple words in them.  exaples:

   #alias a b             - executes #alias with args "a" and "b"
   #alias {a} {b}         - executes #alias with args "a" and "b"
   #alias {a} {say hi}    - executes #alias with args "a" and "say hi"
   #alias a say hi        - executes #alias with args "a", "say", 
                            and "hi" which will kick up an error
                            (since the #alias command doesn't accept
                            a third string argument)


{, } and \ can all be escaped with the \ character: \{, \}, and \\.

category: readme
"""

contribute = """
Development and maintenance is entirely managed in github. Please send any pull request to https://github.com/manuelcortez/mudder

category: readme
"""

errata = """
For now, there are no built versions of mudder available for donwload. We will change it soon!

When communicating bugs or feature requests INCLUDE AS MUCH 
INFORMATION AS POSSIBLE.  If you don't, I'll just ask you for
it anyhow.

In-game help is accessed by typing ``#help``.  When you start 
Lyntin for the first time, type ``#help general`` and that'll 
get you started.  Read through the various help files at your 
leisure.

category: readme
"""

evaluation = """
Variables get evaluated according to a new methodology we developed
after disliking the Tintin way of doing things.  This new methodology
provides maximum flexibility and provides for some things that
the Tintin variable evaluation did not provide for.

  * Variables and placement variables with a single $ or % are
    evaluated/expanded.  One layer of $s or %s is then stripped 
    off when this evaluation occurs.

  * Variables are matched by length of name.  So if you have two
    variables "a" and "ab", we'll test to see if the variable is
    "ab" before "a".  We also handle bracing of variable names
    like ${a} and ${ab} which will guarantee unambiguosity.

  * Variable expansion is always done on user input before 
    commands are evaluated.  This means variables can be used as 
    arguments to any commands, etc.  It also means that if you
    want the variable actually in the command, you have to prepend
    another $.

  * Variable expansion happens again when certain expressions are
    evaluated, such as action triggers, alias expansion, etc.
    Essentially, when any stored value gets expanded its variables
    will get expanded (typically whenever tintinmode would do its 
    sole expansion.) 

  * Placement vars in actions and aliases support an expanded 
    syntax based on python array slices.  %0:1 will evaluate to 
    the first and second arguments, while %0: will be all 
    arguments, and %:-1 will be all but the last argument, etc.

Examples:

1. #action {$Myvar} {woo} 

Will trigger whenever the value Myvar holds when this is entered 
passes by (the original value of Myvar - it will not change if 
Myvar's value changes)

2. #action {$$Myvar} {woo}

Will trigger whenever the current value of Myvar passes by.

3. #action {$$$Myvar} {woo}

Will trigger whenever the literal string $Myvar is seen.  Place 
more $s in if you wish to trigger on more of them, the first 2 
will be stripped by the variable expansion processes. 

4. #alias {hello} {$moo}

Will bind hello to $moo's current value.

5. #alias {hello} {$$moo}

Will bind hello to always expand to moo's current value at the
time of expansion.

6. #alias {hello} {$$$moo}

Will bind hello to expand to the literal string "$moo"

7. #alias {hello} {$${moo}}

Will bind hello to expand to moo's current value at the time of
expansion.

category: readme
"""

general = """
Type "#help help" for help on how to use the in-game help system.

Read through the "#help readme" topics.  These will help as they 
will walk you through how Mudder and Lyntin work, how to get additional 
help, where to go for answers, and what to do if you find a bug.  
These are also exported into the README file.

You should read through the topics in "#help commands" for all 
the currently registered Mudder commands.

To start, the "#session" command will allow you to start a 
session.  When you're done, "#end" will close Mudder.

category: readme
"""

gettingstarted = """
Mudder uses Lyntin to provide all client's functionality. Lyntin incorporates the _look and feel_ of Tintin, so if you've used
Tintin or a variant it should be pretty easy to make the transition.  
It offers all the major features of Tintin, including multiple 
sessions, but leaves some things out.

There are *in-game* help files covering the commands and most 
other things we could think of which can be accessed with the "#help"
command.

category: readme
"""

osnotes = """
for now, Mudder works only in Windows, but it should be relatively easy to get it to work in other operating systems.
category: readme
"""

regexp = """
Mudder allows the use of regular expressions in various arguments
for commands like #action, #highlight, and such.  It uses a 
specific format to trigger using raw regular expressions rather 
than having your argument get escaped so it can be compiled into 
a regular expression.  This allows you to write arguments using 
the simplest form that you can without having to adjust toggles 
and such.

For example:

  #highlight {red} {*says:}

is the same as:

  #highlight {red} {r[^.*?says:]}

The first one will undergo escaping and get transformed into 
"^.*?says\:" (without the quotes) before being compiled into a
regular expression.

The second one gets compiled without being escaped.

If you want to pass an "ignorecase" flag, do so after the end
]:

  #highlight {red} {r[krynor]i}

will highlight all instances of "krynor" (ignoring case) as red.

For regular expression documentation, refer to the Python 
documentation at:

  http://www.python.org/doc/current/lib/re-syntax.html

Note: It may have moved since this was written.

category: readme
"""

def load():
  exported.add_help("bugs", bugs)
  exported.add_help("command", command)
  exported.add_help("contribute", contribute)
  exported.add_help("errata", errata)
  exported.add_help("evaluation", evaluation)
  exported.add_help("general", general)
  exported.add_help("gettingstarted", gettingstarted)
  exported.add_help("osnotes", osnotes)
  exported.add_help("regexp", regexp)

