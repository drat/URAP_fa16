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
        print res.read()
        return res.read()

    # def main(self):

    #     names = ['serenayan0919', 'bradleywolfe', 'ali.kelley.94']
    #     for name in names:

            # sys.stdout = open('file', 'w')
            # print 'test'

            # f = open(name + '_' + "home" + '.html', "w")            
            # f.write(user.fetch('https://m.facebook.com/' + name))
            # f.close
            # time.sleep(0.5)
            

            # f = open(name + '_' + 'likes' + '.html', "w")
            # f.write(user.fetch('https://m.facebook.com/' + name + '?v=likes'))
            # f.close
            # time.sleep(0.5)
            # sys.stdout = open (name + '_' + "likes" + '.html', "w")
            # print user.fetch('https://m.facebook.com/' + name + '?v=likes')

            # f = open(name + '_' + "timeline" + '.html', "w")
            # f.write(user.fetch('https://m.facebook.com/' + name + '?v=timeline'))
            # f.close
            # time.sleep(0.5)

            # f = open(name + '_' + "friends" + '.html', "w")
            # f.write(user.fetch('https://m.facebook.com/' + name + '/friends'))
            # f.close
            # time.sleep(0.5)

user = Acc()
user.login
# names = ['serenayan0919'] #, 'bradleywolfe', 'ali.kelley.94'
# for name in names:
user.fetch('https://m.facebook.com/serenayan0919')
    # f = open(name + '_' + "home" + '.html', "w")            
    # f.write(user.fetch('https://m.facebook.com/' + name))
    # f.close
    # time.sleep(0.5)