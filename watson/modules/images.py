import urllib, urllib2, json, random

from watson.modules.chatmodule import ChatModule, command_function


class ImageModule(ChatModule):

    __module_name__ = "images"
    __module_description__ = "Displays often-humorous images to chat"

    @command_function("m[o]ustachify <name>")
    def moustachify(self, user, name):
        '''
        Displays a picture of the named celebrity with a mustache on their face.
        '''
        params = {"q": name,
                  "v": "1.0",
                  "safe": "active",
                  "imgtype": "face"}
        response = urllib2.urlopen("http://ajax.googleapis.com/ajax/services/search/images?" + urllib.urlencode(params))
        data = json.load(response)
        try:
            images = data['responseData']['results']
            if not images:
                self.speak(user, "Some things just cannot be moustachified...")
            else:
                url = images[0]['unescapedUrl']
                self.speak(user, "http://mustachify.me/?src=" + url)
        except:
            self.speak(user, "Looks like I couldn't find any images of that person. You may want to try again, since I'm really bad at finding images sometimes.")

    @command_function("xkcd [me]", "xkcdme")
    def xkcd(self, user):
        '''
        Displays a random xkcd comic
        '''
        result = json.load(urllib2.urlopen("http://xkcd.com/info.0.json"))
        comic = random.randint(1, result['num'])
        result = json.load(urllib2.urlopen("http://xkcd.com/{0}/info.0.json".format(comic)))
        self.speak(user, result["img"])
        self.speak(user, result["alt"])

    @command_function("pugme")
    def pugme(self, user):
        '''
        Displays a random pug picture
        '''
        response = urllib2.urlopen("http://pugme.herokuapp.com/random")
        pugs = json.load(response)
        self.speak(user, pugs["pug"])
