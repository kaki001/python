import urllib
import urllib2
import cookielib

cookie = cookielib.CookieJar()

handler=urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value


filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookie.save(ignore_discard=True, ignore_expires=True)


cookie = cookielib.MozillaCookieJar()

cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

req = urllib2.Request("http://www.baidu.com")

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
print response.read()


filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'stuid':'201200131012', 'pwd':'23342321'})

loginUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'

result = opener.open(loginUrl,postdata)

cookie.save(ignore_discard=True, ignore_expires=True)

gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'

result = opener.open(gradeUrl)
print result.read()




