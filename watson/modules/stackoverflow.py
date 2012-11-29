import urllib2, json, urllib
from chatmodule import ChatModule, command_function
import itertools
import gzip
import StringIO

import logging
logging.basicConfig(filename='/var/log/chatbot.log',level=logging.DEBUG)



class StackOverflowModule(ChatModule):
    __module_name__ = "stackoverflow"
    __module_description__ = "Module that finds relevant questions on stackoverflow"

    def _decompress(self, compressed_data):
        stream = StringIO.StringIO(compressed_data)
        gzipper = gzip.GzipFile(fileobj=stream)
        return gzipper.read()

    @command_function("stackoverflow <query>")
    def search_questions(self, user, query):
        '''
        Searches questions on StackOverflow
        '''
        self.speak(user, "Looking up information...")
        request = urllib2.Request("http://api.stackexchange.com/2.1/search?" + urllib.urlencode({
                    "tagged": ";".join(query.split()),
                    "sort" : "relevance",
                    "order" : "desc",
                    "site" : "stackoverflow"
                    }))
        opener = urllib2.build_opener()
        response = opener.open(request)

        data = response.read()
        info = response.info()
        if "Content-Encoding" in info and info['Content-Encoding'] == 'gzip':
            data = self._decompress(data)
        results = json.loads(data)

        # todo: filter based on answers or etc
        questions = results["items"]
        good_questions = itertools.ifilter(lambda x: "accepted_answer_id" in x, questions)

        good_questions = itertools.islice(good_questions, 0, 5)
        def pluralize(count, noun):
            if count == 1:
                return "1 %s" % noun
            else:
                return "%s %ss" % (count, noun)

        count = 0
        for question in good_questions:
            s = "%s - %s - %s" % (question["title"], pluralize(int(question["answer_count"]), "answer"), question["link"])
            self.speak(user, s)
            count += 1
        self.speak(user, "Displaying %s" % pluralize(count, "question"))
            








