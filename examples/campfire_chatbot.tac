from watson.firebot import Firebot

from watson.modules.images import ImageModule
from watson.modules.quips import QuipsModule
from watson.modules.help import HelpModule
from watson.modules.mathchallenge import MathChallengeModule
from watson.modules.articles import ArticleModule
from watson.modules.adventuregame import AdventureGameModule
from watson.modules.stackoverflow import StackOverflowModule

SUBDOMAIN="SUBDOMAIN"
AUTH_TOKEN="AUTHTOKEN"
COMMAND_NAMES=("watson","watson,")
NAME = "Watson"
ROOM_NAME = "ROOMNAME"

bot = Firebot(NAME,COMMAND_NAMES,AUTH_TOKEN,SUBDOMAIN,ROOM_NAME)
bot.add_module(ImageModule())
bot.add_module(QuipsModule())
bot.add_module(HelpModule())
bot.add_module(MathChallengeModule())
bot.add_module(ArticleModule())
bot.add_module(AdventureGameModule())
bot.add_module(StackOverflowModule())
application = bot.connect()
