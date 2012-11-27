from watson.gbot import Gbot

from watson.modules.images import ImageModule
from watson.modules.quips import QuipsModule
from watson.modules.help import HelpModule
from watson.modules.mathchallenge import MathChallengeModule
from watson.modules.articles import ArticleModule
from watson.modules.adventuregame import AdventureGameModule

bot = Gbot("Watson",("watson","watson,"),"YOUREMAILHERE@gmail.com","PASSWORD")
bot.add_module(ImageModule())
bot.add_module(QuipsModule())
bot.add_module(HelpModule())
bot.add_module(MathChallengeModule())
bot.add_module(ArticleModule())
bot.add_module(AdventureGameModule())
application = bot.connect()