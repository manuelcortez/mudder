# mudder

Modified Lyntin with a completely accessible graphical user interface.

Mudder is a software to allow playing of MUD (multi user domain) games in an easy and accessible way. Its goal is to integrate some good known open source projects for making a mud client that can fits everyone. Mudder, in fact, is a Graphical User interface around [Lyntin,](https://pypi.python.org/pypi/Lyntin/4.2) a Python based MUD client that is modular and allows people to write their own modules to improve its performance. Once finished, mudder should include the following features:

* Translatable interface and all Lyntin texts.
* Access all Lyntin commands from a graphical user interface wich will allow screen readers to read automatically updates in some elements.
* Easy creation and management of triggers (string matching, regular expressions and even triggers coded in pure Python thanks to the Lyntin API).
* Creation and management of packs (packs will be created per game and can have their own set of triggers, actions, sounds and python code as modules). Packs will be able to be created, exported and installed from the Mudder Window.
* Aliases, actions, gags, highlights, variables, substitutes...
* Handles regular expressions and ignorecase in action triggers.
* Highly configurable speedwalking system.
* Data logging.
* User input history with replacements.
* Most Tintin macro commands: if, math, loop...
* Has a Lyntin and Tintin evaluation modes--the Tintin mode will work with Tintin command files and Tintin syntax.
* In-game help 
* Dynamically loaded modules for additional functionality.