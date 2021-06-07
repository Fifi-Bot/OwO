from flask import Flask, redirect
from threading import Thread

#app = Flask('')

def urlparse(url) -> str:
  url = str(url)
  url.replace(" ", "+")
  url.replace("`", "%60")
  url.replace("@", "%40")
  url.replace("#", "%23")
  url.replace("$", "%24")
  url.replace("%", "%25")
  url.replace("^", "%5E")
  url.replace("&", "%26")
  url.replace("+", "%2B")
  url.replace("=", "%3D")
  url.replace("|", "%7C")
  url.replace("\\", "%5C")
  url.replace("[", "%5B")
  url.replace("]", "%5D")
  url.replace("{", "%7B")
  url.replace("}", "%7D")
  url.replace(":", "%3A")
  url.replace(";", "%3B")
  url.replace("'", "%27")
  url.replace(",", "%2C")
  url.replace("/", "%2F")
  url.replace("?", "%3F")
  return url

def commandSignature(command):
  clean_prefix = "f."
  if not command.signature and not command.parent:
    return f'"{clean_prefix}{command.name}"'
  if command.signature and not command.parent:
    return f'"{clean_prefix}{command.name} {command.signature}"'
  if not command.signature and command.parent:
    return f'"{clean_prefix}{command.parent} {command.name}"'
  else:
    return f'"{clean_prefix}{command.parent} {command.name} {command.signature}"'

msInvite = "https://discord.gg/3c5kc8M"

class FifiServer(Flask):
  def __init__(self, bot):
    super().__init__('Fifi OwO')
    self.bot = bot
    #self.app = app
    self.route("/")(self.main)
    self.route("/status")(self.status)
    self.route("/redirect")(self._redirect)
    #self.route("/status")(self.status)
    self.route("/stats")(self.status)
    self.route("/commands")(self.commands)
    self.route("/command")(self.commands)
    self.route("/guild")(self.guildInvite)
    self.route("/server")(self.guildInvite)
    self.route("/suport")(self.guildInvite)
    self.route("/invite")(self.botInvite)
    self.route("/invites")(self.botInvite)

  def _redirect(self, url):
    url = urlparse(url)
    return redirect(url)

  def botInvite():
    return f"Fifi and any other bots that are part of Fifi is not open for other servers right now. If you we're expecting to have the guild invite, <a href={msInvite}>Click Here</a>!"

  def guildInvite(self):
    return redirect(f"{msInvite}")

  #@app.route("/")
  def main(self):
    name = "M.S. Lounge" #self.bot.get_guild(720991608425807932).name
    return f"Bot is online! View this bot in <a href='{msInvite}'>{str(name)}</a>"

  #@app.route("/status")
  def status(self):
    return redirect("https://status.fifi.ayomerdeka.com")

  def commands(self):
    s = "Note:<br>Arguments with <> means that the argument is required.<br>Arguments with [] means that the argument is optional.<br>DO NOT USE THESE WHEN TYPING COMMANDS<br><br>"
    for command in self.bot.commands:
      s += f"""
Command {command.name}: <br>- Syntax: {commandSignature(command)}<br>- Aliases: {' | '.join(command.aliases)[:-3]}<br>
      """
      if command.cog is None:
        s += "- Cog: No Category/None"
      else:
        s += f"- Cog: {command.cog.qualified_name}"
      s += "<br>"
      if command._buckets._cooldown is None:
        s += "- Cooldown: None"
      else:
        s += f"""
- Cooldown: <br>  - Rate (How long the cooldown lasts in seconds): {command._buckets._cooldown.rate} <br>  - Per (How many commands can be triggered before the cooldown hits): {command._buckets._cooldown.per} <br>  - Type: Each {str(command._buckets._cooldown.type).lower().replace('commands', '').replace('buckettype', '').replace('.', '').title()}
        """
      
      s += "<br><br>"
    return s

  def start(self):
    server = Thread(target=self.run)
    server.start()

  def run(self):
    super().run(host="0.0.0.0", port=8080)