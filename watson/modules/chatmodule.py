import logging

from watson.grammar import create_grammars, match_grammars


def command_function(*syntaxes):
    def g(f):
        if not syntaxes:
            raise ValueError("Must provide at least one valid syntax for each command")
        f.command_syntaxes = syntaxes
        f.command_grammars = []
        for syntax in syntaxes:
            f.command_grammars += create_grammars(syntax)
        return f
    return g

class ChatModuleMeta(type):
    def __new__(cls, name, bases, dct):
        clss = super(ChatModuleMeta, cls).__new__(cls, name, bases, dct)
        clss.command_functions = [x for x in dct.values() if hasattr(x,"command_grammars")]
        return clss

class ChatModule(object):
    __metaclass__ =  ChatModuleMeta
    
    __module_name__ = None
    __module_description__ = None
    __module_dependencies__ = []
    
    def __init__(self):
        self.bot = None
    
    def perform_action(self, user, command):
        hit = False
        for fun in self.command_functions:
            kwargs = match_grammars(command, fun.command_grammars)
            if kwargs is not False:
                logging.info("Grammar Parsed:\n\tcommand: {0}\n\tmodule: {1}\n\targs: {2}".format(command, self.__module_name__ + " - " + fun.__name__, kwargs))
                fun(self,user,**kwargs)
                hit = True
        return hit
    
    def speak(self,user,message):
        return self.bot.speak(user,message)
