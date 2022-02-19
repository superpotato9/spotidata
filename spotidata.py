cmd = True
import lyr
import os
from urllib.request import unquote
from sty import fg, bg, ef, rs
print(bg.li_green + fg.black + 'welcome to spotidata' + fg.rs + bg.rs)
from html import unescape
import webbrowser
def between(start, end):
        
    start = raw.find(start) + len(start)
    end = raw.find(end)
    return raw[start:end]
os.system('cd /Users/nathankoliha/Desktop/')
while True:
    url = str(input('input spotify song share link: '))
    
    if 'https://open.spotify.com/track/' in url:
        break
    else:
        print('error malformed input please input a spotify web address') 
        
filename = url.replace('https://open.spotify.com/track/', '').split('?')
os.system("wget --no-check-certificate --adjust-extension -O " + filename[0] + ' ' + url)

filename = filename[0]
title = ''

with open(filename, 'r') as file:
    raw = file.read()
image_url = between('<meta property="og:image" content="', '" /><meta property="og:type"')

title = between('<title>', '| Spotify</title>')
released = between('· Song ·', '." /><meta')
song_length = between('</div><div class="Type__TypeElement-goli3j-0 bWzOVV T3C0eBxRoJcpqMNCpLT6"', '</div></div></div></div><div data-testid="action-bar-container" ').split('T3C0eBxRoJcpqMNCpLT6">')
preTitle = unescape(unquote(title)).split('-')
title = preTitle[0]
label = between('</p><p dir="auto" class="Type__TypeElement-goli3j-0 eEsqRZ">', '</p></div></div></div></div></div></div></div></div></div></div><aside class="App__ModalLayer-sc-hckv0t-1 iRxyhF"></aside></div><script type="application/json" id="initial-state">')

artist = preTitle[1].replace(' song by ', '')
lyrics = lyr.lyrics(title + artist)
if lyrics == None:
    lyrics = 'None'
    

data = {'title':title, 'artist': artist, 'lyrics':lyrics, 'released':released, 'length':song_length[1], 'label':label, 'image':image_url}




if cmd == True:           
    print( fg.green + data['title']  + fg.rs)
    print( fg.blue + data['artist']  + fg.rs)
    print(bg.magenta + data['lyrics']  + bg.rs)
    print(fg.yellow + data['released'] + fg.rs)
    print(fg.cyan + data['length'] + fg.rs)
    print(fg.green + data['label'] + fg.rs)
    print(fg.blue + data['image'] + fg.rs)
    input('press enter/return to open image in browser')
    print('opening image in browser')
    webbrowser.open(data['image'])




