import types
import output
from lyntin import exported, utils
from lyntin.ansi import filter_ansi
from lyntin.ui import message

def handle_recv_data(args):
    msg = args["message"]

    if type(msg) == types.StringType:
      msg = message.Message(msg, message.LTDATA)

    line = msg.data
    ses = msg.session

    output.speak(filter_ansi(line), 0)
    return line

def load():
    """Initializes the module by binding all the commands."""
    exported.hook_register("to_user_hook", handle_recv_data)

def unload():
    """Unbinds the commands (for when we reimport the module)."""
    exported.hook_unregister("to_user_hook", handle_recv_data)
