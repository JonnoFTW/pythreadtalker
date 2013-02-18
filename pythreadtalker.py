import json, urllib2, re, pyttsx, time, sys, HTMLParser
board = raw_input("BOARD: ")
thread = raw_input("THREAD: ")
engine = pyttsx.init()
h = HTMLParser.HTMLParser()
def saytext(t):
    t = re.sub('<[^<]+?>', ' ', h.unescape(t))
    print  t
    engine.say(t)
    engine.runAndWait()
url = "http://api.4chan.org/%s/res/%s.json"%(board,thread)
oldest = 0
while True:
    page = json.load(urllib2.urlopen(url))
    for i in page['posts']:
        if i['time'] > oldest and 'com' in i:
            saytext(i["com"])
        oldest = i['time']
    time.sleep(20)

    
