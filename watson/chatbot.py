import logging, traceback
import unicodedata

from watson.stateful import State
from watson.grammar import create_grammars, match_grammars

logging.basicConfig(filename='/var/log/chatbot.log',level=logging.DEBUG)


class Chatbot(object):
    
    default_phrase = 'I... have no idea what you\'re talking about. Try the command "help" for a list of my functions'
    welcome_phrase = "Hello, %s here, how may I assist you?"
    goodbye_phrase = "Oh what a world, what a world..."
    
    def __init__(self, name = "Watson", command_names = ()):
        self._modules = {}
        self._commands = {}
        self.state = State(self)
        self.welcome_phrase = self.welcome_phrase % name
        self.command_grammars = create_grammars("/".join(command_names) + " <phrase>")
    
    def speak(self, message, user):
        raise NotImplementedError
    
    def connect(self):
        raise NotImplementedError
    
    def disconnect(self):
        raise NotImplementedError

    def error(self):
        raise NotImplementedError

    def add_module(self, module):
        if not self._modules.has_key(module.__module_name__):
            for dependency in module.__module_dependencies__:
                if not self._modules.has_key(dependency):
                    raise ValueError('Module dependency missing! Module "{0}" requires module "{1}", which has not been added yet.'.format(module.__module_name__,dependency))
            self._modules[module.__module_name__] = module
            module.bot = self
            
            for command in module.command_functions:
                self._commands[command.__name__] = command
        else:
            raise ValueError("Duplicate module added. Cannot have multiple modules with the same name: " + module.__module_name__)
    
    def get_module(self, name):
        return self._modules.get(name,None)
    
    def get_all_modules(self):
        return self._modules.values()
    
    def get_command(self, name):
        return self._commands.get(name,None)
    
    def perform_action(self, user, message):
        try:
            message = unicodedata.normalize('NFKD', unicode(message)).encode('ascii','ignore')
            self.state.check_answer(user, message)
            
            hit = False
            parsed = match_grammars(str(message),self.command_grammars)
            if parsed:
                phrase = parsed['phrase'].lower()
                for module in self._modules.values():
                    hit |= module.perform_action(user, phrase)
                    if hit:
                        break
                if not hit:
                    self.speak(user,self.default_phrase)
            
        except Exception, _:
            logging.error(traceback.format_exc())
            try:
                self.speak(user,"Whoops, looks like that caused me to crash. Check my log files to see what happened!")
            except:
                logging.error(traceback.format_exc())
