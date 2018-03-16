# mudder

Modified Lyntin with a completely accessible graphical user interface.

Mudder is a software to allow playing of MUD (multi user domain) games in an easy and accessible way. Its goal is to integrate some good known open source projects for making a mud client that can fits everyone. Mudder, in fact, is a Graphical User interface around [Lyntin,](https://pypi.python.org/pypi/Lyntin/4.2) a Python based MUD client that is modular and allows people to write their own modules to improve its performance. Once finished, mudder should include the following features:

* Translatable interface and all Lyntin texts.
* Access all Lyntin commands from a graphical user interface wich will allow screen readers to read  updates in some elements automatically.
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

## Running from sources

1. You will need [Python 2.7](https://python.org)
2. Install requirements from the requirements file: pip install -r requirements.txt
3. Run "python src/run.py"
4. If you have made a settings file (.ini) you can import it at startup by running something like: "python run.py file.ini".
5. Or you can import it once Mudder has been started with the #read command (type #help read for more info).

## Status

Currently, there are no available builds ready to download. Theoretically py2exe should be able to build a Windows binary version of the program. However I have decided to keep working in Lyntin's internals a bit and improve the GUI for mudder before releasing something. If you want to try it out, I suggest to do it from sources.