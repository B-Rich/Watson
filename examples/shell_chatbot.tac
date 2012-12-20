from watson.shellbot import Shellbot

from watson.modules.images import ImageModule
from watson.modules.quips import QuipsModule
from watson.modules.help import HelpModule
from watson.modules.mathchallenge import MathChallengeModule
from watson.modules.articles import ArticleModule
from watson.modules.adventuregame import AdventureGameModule
from watson.modules.stop import StopModule

bot = Shellbot("Watson",(""))
bot.add_module(ImageModule())
bot.add_module(HelpModule())
bot.add_module(MathChallengeModule())
bot.add_module(ArticleModule())
bot.add_module(QuipsModule())
bot.add_module(AdventureGameModule())
bot.add_module(StopModule())
application = bot.connect()