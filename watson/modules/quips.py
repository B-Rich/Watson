import datetime

from watson.modules.chatmodule import ChatModule, command_function

class QuipsModule(ChatModule):
    
    __module_name__ = "quips"
    __module_description__ = "A bunch of one-liners"

    @command_function("what's brown and sounds like a bell[?]")
    def joke(self,user):
        self.speak(user,"Dung!")
        
    @command_function("what time is it[?]")
    def whattime(self,user):
        self.speak(user,"Hammer time, of course")

    @command_function("seriously[,] what time is it[?]")
    def whattimereally(self,user):
        self.speak(user,datetime.datetime.utcnow().strftime("%m/%d/%y %H:%M GMT"))

    @command_function("what are the rules[?]")
    def rules(self,user):
        self.speak(user,"I'll be honest, I can't bring myself to actually make the Fight Club joke.")

    @command_function("status")
    def status(self,user):
        self.speak(user,"believe me I am still alive. I'm doing Science and I'm still alive. I feel FANTASTIC and I'm still alive. While you're dying I'll be still alive. And when you're dead I will be still alive.")

    @command_function("[<sudo>] make me a sandwich")
    def sandwich(self,user,sudo=""):
        if sudo == "sudo":
            self.speak(user,"Okay.")
        else:
            self.speak(user,"No, make it yourself.")


    @command_function("be creepy")
    def creepy(self,user):
        self.speak(user,"http://gifsforum.com/images/gif/happy/grand/Ill-eat-your-childern.gif")

