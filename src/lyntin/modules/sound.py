import os.path
import sound_lib
from lyntin import exported
from lyntin.modules import modutils

# this will hold the command information for adding to
# Lyntin later on
commands_dict = {}

_volume = 50
_ambiance = None

sources = []

def play(sound):
    global sources, _volume
    src = sound_lib.stream.FileStream(file=os.path.abspath(sound))
    src.volume=int(_volume)/100.0
    src.play()
    sources.append(src)
    for src in sources[:]:
      if not src.is_playing:
        sources.remove(src)

def play_cmd(ses, args, input):
    """
    Play a sound. The sound should be in the sounds folder, located in the mudder path.

Examples:
#sound.play myfile.ogg
#sound.play mysound.ogg volume=50
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

commands_dict["sound.play"] = (play_cmd, "filename= volume=50 loop:boolean=false")

def volume_cmd(ses, args, input):
    """
    Set default volume. The default volume will be used for all played sounds, unless otherwise specified. Volume must be in range 0-100.
    """
    global _volume
    try:
        v = int(args["volume"])
        if 0 <= v <= 100:
            _volume = v
            exported.write_message("sound volume set to %s" % args["volume"])
        else:
            raise
    except:
        exported.write_message("couldn't set volume: %s must be an integer from 0 to 100" % args["volume"])

commands_dict["sound.volume"] = (volume_cmd, "volume")

def play_ambiance_cmd(ses, args, input):
    """
    Play an environmental sound (for example, ambient sound in a room). It's the same than sound.play but it will loop the sound. There is only one sound allowed. When playing the next sound, the previous one will be stopped.
    """
    global _ambiance
    filename = args["filename"]
    if "/" in filename:
        fileparts = filename.split("/")
        fileparts.insert(0, "sounds")
    else:
        fileparts = ["sounds", filename]
    volume = args["volume"]
    _ambiance = sound_lib.stream.FileStream(file=os.path.abspath(os.path.join(*fileparts)))
    _ambiance.volume=int(_volume)/100.0
    _ambiance.looping = True
    _ambiance.play()

commands_dict["sound.play_ambiance"] = (play_ambiance_cmd, "filename= volume=50")

def stop_ambiance_cmd(ses, args, input):
    """
    Stop the current ambient sound.
"""
    global _ambiance
    if _ambiance != None and _ambiance.is_playing:
        _ambiance.stop()
        _ambiance = None

commands_dict["sound.stop_ambiance"] = (stop_ambiance_cmd, "")

def load():
    """ Initializes the module by binding all the commands."""
    sound_lib.output.Output()
    modutils.load_commands(commands_dict)

def unload():
    """ Unbinds the commands (for when we reimport the module)."""
    modutils.unload_commands(commands_dict)
