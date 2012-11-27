import httplib2
from pyquery import PyQuery

from watson.modules.chatmodule import ChatModule, command_function


class ArticleModule(ChatModule):
    
    __module_name__ = "articles"
    __module_description__ = "Module that provides interactions with Wikipedia."

    @command_function("[random] wikipedia")
    def wikipedia(self,user):
        '''
        Displays the title, summary, and link to a random Wikipedia article.
        '''
        http = httplib2.Http()
        resp, content = http.request('http://en.wikipedia.org/wiki/Special:Random')
        if resp.status != 200:
            self.speak(user,"Looks like Wikipedia is down. You should have donated.")
            return
        page = PyQuery(content)
        title = page('h1#firstHeading').text().encode('utf-8')
        summary = page('div#mw-content-text > p:first').text().encode('utf-8')
        article_url = resp['content-location']
        self.speak(user,"\n".join([x.decode('UTF-8') for x in [title,summary,article_url] if x]))
