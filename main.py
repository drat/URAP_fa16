import urllib
import urllib2
import cookielib
import re
import webbrowser

class fbScrap:
    def __init__(self):
        
        self.target='https://www.facebook.com/limanner?ref=br_rs'
        self.values = {'email' : 'afreemans226@gmail.com',  
        'password' : '19951027' }
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  

        self.headers = { 'User-Agent' : 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)' ,
                        'Referer':'http://www.facebook.com'}

    def getPage(self):
        try:
            url = self.target
            user_agent = self.user_agent  
            values = self.values
            headers = self.headers
            data = urllib.urlencode(self.values)
            request = urllib2.Request(url, data, headers)  
            response = urllib2.urlopen(request)  
            page = response.read() 
            url = self.target
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print response.read()
            return response
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"Error:",e.reason
                return None


task = fbScrap()
task.getPage()

# class TokenHandler:
#     """
#     Class used to handle Facebook oAuth
#     """
#     def __init__(self, a_id, a_secret):
#         self._id = a_id
#         self._secret = a_secret

#     def get_access_token(self):
#         """
#          Fetches the access key using an HTTP server to handle oAuth
#          requests
#             Args:
#                 appId:      The Facebook assigned App ID
#                 appSecret:  The Facebook assigned App Secret
#         """

#         ACCESS_URI = ('https://www.facebook.com/dialog/' 
#             + 'oauth?client_id=' +self._id + '&redirect_uri='
#             + REDIRECT_URL + "&scope=ads_management")

#         open_new(ACCESS_URI)
#         httpServer = HTTPServer(
#                 ('localhost', PORT),
#                 lambda request, address, server: HTTPServerHandler(
#                     request, address, server, self._id, self._secret))
#         #This function will block until it receives a request
#         httpServer.handle_request()
#         #Return the access token
#         return httpServer.access_token 