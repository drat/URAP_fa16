import urllib
import urllib2
import cookielib
import sys
import time

class Acc:
    jar = cookielib.CookieJar()
    cookie = urllib2.HTTPCookieProcessor(jar)       
    opener = urllib2.build_opener(cookie)
    headers = {
        "User-Agent" : "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.8.1.14) Gecko/20080609 Firefox/2.0.0.14",
        "Accept" : "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,text/png,*/*;q=0.5",
        "Accept-Language" : "en-us,en;q=0.5",
        "Accept-Charset" : "ISO-8859-1",
        "Content-type": "application/x-www-form-urlencoded",
        "Host": "m.facebook.com"
    }

    def login(self):
        try:
            params = urllib.urlencode({'email':'afreemans226@gmail.com','pass':'19951027','login':'Log+In'})
            req = urllib2.Request('http://m.facebook.com/login.php?m=m&refsrc=m.facebook.com%2F', params, self.headers)
            res = self.opener.open(req)
            html = res.read()

        except urllib2.HTTPError, e:
            print e.msg
        except urllib2.URLError, e:
            print e.reason[1]
        return False

    def fetch(self,url):
        req = urllib2.Request(url,None,self.headers)
        res = self.opener.open(req)
        # print res.read()
        return res.read()


names = ['serenayan0919', 'bradleywolfe', 'ali.kelley.94']

user = Acc()
user.login()
for n in names:
    f = open(n + '_' + "home" + '.html', "w")
    url = 'https://m.facebook.com/' + n
    s = user.fetch(url)
    f.write(s)
    f.close
    time.sleep(0.5)

    # f = open(n + '_' + 'likes' + '.html', "w")
    # url = 'https://m.facebook.com/' + n + '?v=likes'
    # s = user.fetch(url)
    # f.write(s)
    # f.close
    # time.sleep(0.5)

    # f = open(n + '_' + "timeline" + '.html', "w")
    # url = 'https://m.facebook.com/' + n + '?v=timeline'
    # s = user.fetch(url)
    # f.write(s)
    # f.close
    # time.sleep(0.5)

    # f = open(n + '_' + "friends" + '.html', "w")
    # url = 'https://m.facebook.com/' + n + '/friends'
    # s = user.fetch(url)
    # f.write(s)
    # f.close
    # time.sleep(0.5)


# name = 'serenayan0919'
# url = 'https://m.facebook.com/' + name
# user = Acc()
# user.login()
# s = user.fetch(url)
