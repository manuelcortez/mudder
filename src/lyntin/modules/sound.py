import os.path
from lyntin import exported
from lyntin.modules import modutils

# this will hold the command information for adding to
# Lyntin later on
commands_dict = {}

import sound_lib

volume = 50

sources = []

def play(sound):
    global sources, volume
    src = sound_lib.stream.FileStream(file=os.path.abspath(sound))
    src.volume=int(volume)/100.0
    src.play()
    sources.append(src)
    for src in sources[:]:
      if not src.is_playing:
        sources.remove(src)

def sound_cmd(ses, args, input):
    """
    This command allows you to play a sound.

Example:
#sound myexample.ogg volume=50 loop=false
    """
    filename = args["filename"]
    if "/" in filename:
        fileparts = filename.split("/")
        fileparts.insert(0, "sounds")
    else:
        fileparts = ["sounds", filename]
    volume = args["volume"]
    loop = args["loop"]
#    try:
    play(os.path.join(*fileparts))
#    except:
#        exported.write_message("couldn't play sound: %s" % filename)

commands_dict["sound"] = (sound_cmd, "filename= volume=50 loop:boolean=false")

def soundvolume_cmd(ses, args, input):
    """
    This command allows you to set the sound volume (from 0 to 100).
    """
    global volume
    try:
        v = int(args["volume"])
        if 0 <= v <= 100:
            volume = v
            exported.write_message("sound volume set to %s" % args["volume"])
        else:
            raise
    except:
        exported.write_message("couldn't set volume: %s must be an integer from 0 to 100" % args["volume"])

commands_dict["soundvolume"] = (soundvolume_cmd, "volume")

def load():
    """ Initializes the module by binding all the commands."""
    sound_lib.output.Output()
    modutils.load_commands(commands_dict)

def unload():
    """ Unbinds the commands (for when we reimport the module)."""
    modutils.unload_commands(commands_dict)
