from watson.modules.chatmodule import ChatModule, command_function, overhear_function


class CampfireModule(ChatModule):
    '''
    This is a module to contains functions that really only make sense in Campfire, pretty much only audio commands.
    '''

    __module_name__ = "campfire"
    __module_description__ = "Contains Miscellaneous Campfire Functions"

    def _get_sexy_user_list(self):
        return getattr(self.bot.state,"sexy_user_list",set())

    def _set_sexy_user_list(self, sexy_user_list):
        self.bot.state.sexy_user_list = sexy_user_list

    @command_function("sexify <target>")
    def sexify(self, user, target):
        '''
        Gives a soundtrack to the target user. The target cannot be the user speaking, though!
        '''
        if target == user:
            self.speak(user, "Sorry, you cannot sexify yourself. Get someone else to do it!")
        
        sexy_users = self._get_sexy_user_list()
        
        target = target.lower()
        if target not in sexy_users:
            sexy_users.add(target)
            self._set_sexy_user_list(sexy_users)
            self.speak(user,"{0} is officially bringing sexy back.".format(target))
        else:
            self.speak(user,"It looks like {0} is already sexy.".format(target))


    @command_function("unsexify <target>")
    def unsexify(self, user, target):
        '''
        Removes the sexyback soundtrack from the target. The target cannot be the user speaking, though!
        '''
        if target == user:
            self.speak(user, "Sorry, you cannot unsexify yourself. Get someone else to do it!")
        
        sexy_users = self._get_sexy_user_list()
        
        target = target.lower()
        if target in sexy_users:
            sexy_users.remove(target)
            self._set_sexy_user_list(sexy_users)
            self.speak(user,"{0} is no longer bringing sexy back. Who will bring it back now?!".format(target))
        else:
            self.speak(user,"It looks like {0} is already unsexy.".format(target))

    @overhear_function(".*")
    def play_soundtrack(self, user):
        sexy_users = self._get_sexy_user_list()
        if user.lower() in sexy_users:
            self.speak(user,"/play sexyback")