import re, sys, os, select, types
import wx
from lyntin import ansi, engine, event, utils, exported, config
from lyntin.ui import base, message

myui = None

def get_ui_instance():
  global myui
  if myui == None:
    myui = wxui()
  return myui

HELP_TEXT = """
Mudder will allow you to play your MUD games easily.
"""

class window(wx.Frame):
  def __init__(self):
    super(window, self).__init__(parent=None, title="Mudder")
    self.panel = wx.Panel(self)
    self.sizer = wx.BoxSizer(wx.VERTICAL)
    self.sb = self.CreateStatusBar()
    label = wx.StaticText(self.panel, wx.NewId(),   "input")
    self.input = wx.TextCtrl(self.panel, wx.NewId())
    inputBox = wx.BoxSizer(wx.HORIZONTAL)
    inputBox.Add(label, 0, wx.ALL, 5)
    inputBox.Add(self.input, 0, wx.ALL, 5)
    label = wx.StaticText(self.panel, wx.NewId(),   "history")
    self.output = wx.TextCtrl(self.panel, wx.NewId(), style=wx.TE_MULTILINE|wx.TE_READONLY, size=(500, 300))
    outputBox = wx.BoxSizer(wx.HORIZONTAL)
    outputBox.Add(label, 0, wx.ALL, 5)
    outputBox.Add(self.output, 0, wx.ALL, 5)
    self.sizer.Add(inputBox, 0, wx.ALL, 5)
    self.sizer.Add(outputBox, 0, wx.ALL, 5)
    self.panel.SetSizer(self.sizer)
    self.SetClientSize(self.sizer.CalcMin())

  def write(self, text):
    point = self.output.GetInsertionPoint()
    self.output.AppendText(text)
    self.output.SetInsertionPoint(point)
#    if text != "" and text.isspace() == False:
#      output.speak(text)

class wxui(base.BaseUI):
  def __init__(self):
    base.BaseUI.__init__(self)
    exported.hook_register("shutdown_hook", self.shutdown)
    exported.hook_register("to_user_hook", self.write)
    exported.hook_register("config_change_hook", self.configChangeHandler)
    exported.hook_register("bell_hook", self.bell)
    exported.hook_register("prompt_hook",
      lambda x: self.write( {
        'message': message.Message(x["prompt"], message.MUDDATA, x["session"])
        } ) )
    self.app = wx.App()
    self.window = window()
    self.window.input.Bind(wx.EVT_CHAR_HOOK, self.process)

  def process(self, event):
    key = event.GetKeyCode()
    if key == wx.WXK_RETURN:
      self.input_data()
    event.Skip()

  def runui(self):
    global HELP_TEXT
    exported.add_help("mudder", HELP_TEXT)
    self.window.Show()
    self.app.MainLoop()

  def wantMainThread(self):
    return 1

  def shutdown(self, args):
    pass

  def bell(self, args):
    """ Handles incoming bell characters."""
    sys.stdout.write('\07')

  def configChangeHandler(self, args):
    """ Handles config changes (including mudecho)."""
    name = args["name"]
    newvalue = args["newvalue"]
    return

  def input_data(self, *args, **kwargs):
    """ This is the poll loop for user input."""
    try:
      data = self.window.input.GetValue()
      self.window.input.SetValue("")
      if data != None:
        self.handleinput(data)
    except select.error, e:
      (errno,name) = e
      if errno == 4:
        exported.write_message("system exit: select.error.")
        event.ShutdownEvent().enqueue()
        return

    except SystemExit:
      exported.write_message("system exit: you'll be back...")
      event.ShutdownEvent().enqueue()

    except:
      exported.write_traceback()
      event.ShutdownEvent().enqueue()

  def write(self, args):
    """
    Handles writing information from the mud and/or Lyntin
    to the user.
    """
    msg = args["message"]

    if type(msg) == types.StringType:
      msg = message.Message(msg, message.LTDATA)

    line = msg.data
    ses = msg.session

    if line == '' or self.showTextForSession(ses) == 0:
      return

    # we prepend the session name to the text if this is not the 
    # current session sending text.
    pretext = ""
    if ses != None and ses != exported.get_current_session():
      pretext = "[" + ses.getName() + "] "

    if msg.type == message.ERROR or msg.type == message.LTDATA:
      if msg.type == message.ERROR:
        pretext = "error: " + pretext

      line = pretext + utils.chomp(line).replace("\n", "\n" + pretext)
      self.window.write(line+"\n")
      return

    elif msg.type == message.MUDDATA:
      if "\n" not in msg.data: msg.data = msg.data + "\n"
      self.window.write(msg.data)
      return

    if exported.get_config("ansicolor") == 0:
      if pretext:
        if line.endswith("\n"):
          line = (pretext + line[:-1].replace("\n", "\n" + pretext) + "\n")
        else:
          line = pretext + line.replace("\n", "\n" + pretext)
      self.window.write(line)
      return

  def prompt(self):
    """ Prints a prompt to the user."""
    self.window.write(">\n")

  def flush(self):
    """ Flushes the stdout.  Not sure we really need this
    but it's here."""
    sys.stdout.flush()