import requests
import socket
import time

#-----------------------
#color script

def outer_func(color):
    def inner_func(msg):
        print(f'{color}{msg}')
    return inner_func

GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')

#-----------------------
#banner

banner='''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@*                           (@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@,                                     #@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@                                         ,@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@                                               @@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@                                                 @@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@,                                                 &@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@                                                   @@@@@@@@@@@@@@
@@@@@@@@@@@@@@&                                                   @@@@@@@@@@@@@@
@@@@@@@@@@@@@@.                                                   &@@@@@@@@@@@@@
@@@@@@@@@@@@@@                                                    .@@@@@@@@@@@@@
@@(*/@@@@@@@@@                                                     @@@@@@@@&**#@
@           .@                                                     &            
@@.                                                                           (@
@@@@@                                                                       @@@@
@@@@@@@@@%                                                             &@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%%%%%##(((((////***///((((((##%%%&&@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&.&@@@@@@%*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@, @@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%@%#@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%@@@& @@@@@@@@@/(@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,        /@@/        /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@&  @@@@@@@@@&                            @@@@@@@@@   &@@@@@@@@@@@@@
@@@@@@@@@@& &@@@@@@@@@&                                 (@@@@@@@@@@% &@@@@@@@@@@
@@@@@@@@@@  &@@@@@@(                                        @@@@@@@,  @@@@@@@@@@
@@@@@@@@@@(                                                          %@@@@@@@@@@
@@@@@@@@@@@@@*                       #@@@@@                        @@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%(**/#&@@@@@@@@@@@@@@@@@@@@%(*****%@@@@@@@@@@@@@@@@@@@@@@
\n\n\n'''

print(banner)

#-----------------------


#-----------------------
uname = input("UserName to monocle:\t")

ebay = f'https://www.ebay.com/usr/{uname}'
giphy = f'https://giphy.com/explore/{uname}'
imgur = f'https://imgur.com/user/{uname}'
gravatar = f'https://en.gravatar.com/{uname}'
askfm = f'https://ask.fm/{uname}'
spotify = f'https://open.spotify.com/user/{uname}'
steam = f'https://steamcommunity.com/id/{uname}'
A500px = f'https://500px.com/{uname}'
youpic = f'https://youpic.com/photographer/{uname}/'
itchio = f'https://{uname}.itch.io'
aboutme = f'https://about.me/{uname}'
btcforum = f'https://bitcoinforum.com/profile/{uname}'
tripadvisor = f'https://www.tripadvisor.com/members/{uname}'
vsco = f'https://vsco.co/{uname}/images'
wiki = f'https://en.wikipedia.org/wiki/User:{uname}'
bandcamp = f'https://bandcamp.com/{uname}'
A9gag = f'https://9gag.com/u/{uname}'
pornhub = f'https://www.pornhub.com/{uname}'
facebook = f'https://www.facebook.com/{uname}'
instagram = f'https://www.instagram.com/{uname}/'
youtube  = f'https://www.youtube.com/user/{uname}'
twitch = f'https://www.twitch.tv/{uname}'
tumbler = f'https://{uname}.tumblr.com/'
linkedin = f'https://il.linkedin.com/pub/dir?firstName={uname}&lastName=&trk=people-guest_people-search-bar_search-submit'
telegram = f'https://t.me/{uname}'
fliker = f'https://www.flickr.com/people/{uname}'
tiktok = f'https://www.tiktok.com/@{uname}'
pinterest = f'https://www.pinterest.com/{uname}/'
kik = f'https://ws2.kik.com/user/{uname}'
tinder = f'https://www.gotinder.com/@{uname}'
meetme = f'https://www.meetme.com/{uname}'
github = f'https://github.com/{uname}'
gitlab = f'https://gitlab.com/{uname}'
codepen = f'https://codepen.io/{uname}'
pastebin = f'https://pastebin.com/u/{uname}'
codecademy = f'https://www.codecademy.com/{uname}'
tryhackme = f'https://tryhackme.com/p/{uname}'
hackerone = f'https://hackerone.com/{uname}'
medium = f'https://medium.com/@{uname}'
reddit = f'https://www.reddit.com/user/{uname}'
ycombinator = f'https://news.ycombinator.com/user?id={uname}'
quora = f'https://www.quora.com/profile/{uname}'
vk = f'https://vk.com/{uname}'
goodreads = f'https://www.goodreads.com/{uname}'
patreon = f'https://www.patreon.com/{uname}'
producthun = f'https://www.producthunt.com/@{uname}'
independent = f'https://independent.academia.edu/{uname}'
angel = f'https://angel.co/{uname}'
ask = f'https://ask.fm/{uname}'
blip = f'https://blip.fm/{uname}'
badoo = f'https://badoo.com/profile/{uname}'
bandcamp = f'https://bandcamp.com/{uname}'
behance = f'https://www.behance.net/{uname}'
bitbucket = f'https://bitbucket.org/{uname}/'
buzzfeed = f'https://www.buzzfeed.com/{uname}'
canva = f'https://www.canva.com/{uname}'
cash = f'https://cash.me/{uname}'
cloob = f'https://www.cloob.com/name/{uname}'
codecadema = f'https://www.codecademy.com/{uname}'
codementor = f'https://www.codementor.io/{uname}'
codepen = f'https://codepen.io/{uname}'
coderwall = f'https://coderwall.com/{uname}'
colourlovers = f'https://www.colourlovers.com/lover/{uname}'
coroflot = f'https://www.coroflot.com/{uname}'
ceatrivemarket = f'https://creativemarket.com/{uname}'
crunchyroll = f'https://www.crunchyroll.com/user/{uname}'
dev = f'https://dev.to/{uname}'
dailymotion = f'https://www.dailymotion.com/{uname}'
designspiration = f'https://www.designspiration.net/{uname}/'
deviantart = f'https://www.deviantart.com/{uname}'
disqus = f'https://disqus.com/{uname}'
dribble = f'https://dribbble.com/{uname}'
ello = f'https://ello.co/{uname}'
etsy = f'https://www.etsy.com/shop/{uname}'
eyeem = f'https://www.eyeem.com/u/{uname}'
fliker = f'https://www.flickr.com/people/{uname}'
flipboard = f'https://flipboard.com/@{uname}'
foursquare = f'https://foursquare.com/{uname}'
gitlab = f'https://gitlab.com/{uname}'
gitee = f'https://gitee.com/{uname}'
gumroad =f'https://www.gumroad.com/{uname}'
hackerone = f'https://hackerone.com/{uname}'
housemid = f'https://www.house-mixes.com/profile/{uname}'
houzz = f'https://houzz.com/user/{uname}'
hubpage = f'https://hubpages.com/@{uname}'
homescreen = f'https://homescreen.me/{uname}'
ifttt = f'https://www.ifttt.com/p/{uname}'
imageshack = f'https://imageshack.us/user/{uname}'
instractables = f'https://www.instructables.com/member/{uname}'
investing = f'https://www.investing.com/traders/{uname}'
issuu = f'https://issuu.com/{uname}'
kaggle = f'https://www.kaggle.com/{uname}'
kano = f'https://api.kano.me/progress/user/{uname}'
keybase = f'https://keybase.io/{uname}'
kik = f'https://ws2.kik.com/user/{uname}'
kongregate = f'https://www.kongregate.com/accounts/{uname}'
launchpad = f'https://launchpad.net/~{uname}'
letterboxd = f'https://letterboxd.com/{uname}'
mastodon = f'https://mastodon.social/@{uname}'
meetme = f'https://www.meetme.com/{uname}'
mixcould = f'https://www.mixcloud.com/{uname}'
myanimelist = f'https://myanimelist.net/profile/{uname}'
namemc = f'https://namemc.com/name/{uname}'
pastebin = f'https://pastebin.com/u/{uname}'
pexels = f'https://www.pexels.com/@{uname}'
photobucket = f'https://photobucket.com/user/{uname}/library'
pinterest = f'https://www.pinterest.com/{uname}/'
pixabay = f'https://pixabay.com/en/users/{uname}'
repl = f'https://repl.it/@{uname}'
reverbnation = f'https://www.reverbnation.com/{uname}'
roblox = f'https://www.roblox.com/user.aspx?username={uname}'
scribd = f'https://www.scribd.com/{uname}'




#------------------------



WEBSITES = [ebay,giphy,imgur,gravatar,askfm,spotify,steam,A500px,youpic,itchio,
            aboutme,btcforum,tripadvisor,vsco,wiki,bandcamp,A9gag,facebook,
            instagram,youtube,twitch,tumbler,telegram,linkedin,fliker,tiktok,
            pinterest,kik,tinder,meetme,github,gitlab,codepen,pastebin,codecademy,tryhackme,hackerone,pornhub,aboutme,btcforum,tripadvisor,vsco,wiki,bandcamp,A9gag,pornhub,facebook,instagram,youtube,twitch,tumbler,linkedin,telegram,fliker,tiktok,pinterest,kik,tinder,meetme,github,gitlab,codepen,pastebin,codecademy,tryhackme,hackerone,medium,reddit,ycombinator,quora,vk,goodreads,patreon,producthun,independent,angel,ask,blip,badoo,behance,bitbucket,buzzfeed,canva,cash,cloob,codecadema,codementor,coderwall,colourlovers,coroflot,ceatrivemarket,crunchyroll,dev,dailymotion,designspiration,deviantart,disqus,dribble,ello,etsy,eyeem,flipboard,foursquare,gitee,gumroad,houzz,hubpage,homescreen,ifttt,imageshack,instractables,investing,issuu,kaggle,kano,keybase,kongregate,launchpad,letterboxd,mastodon,mixcould,myanimelist,namemc,pexels,photobucket,pixabay,repl,reverbnation,roblox,scribd,]




def search():
    GREEN(f'[+] Searching for:\t{uname}')
    match = True
    FAILED = []
    SUCCESS = []
    try:
        for url in WEBSITES:
            requests.Timeout(0.5)
            r = requests.get(url)
            #r.close()
            if r.status_code == 200:
                GREEN(f"[+] {r.status_code}! {url} - Valid! ")
                SUCCESS.append(url)
            elif r.status_code != 200:
                RED(f"[-] {r.status_code}! {url} -  Failed! maybe this is a false positive")
                FAILED.append(url)
    except Exception as e:
        RED(f'Error has occurred {e}')



    YELLOW(f'[X] TOTAL = {len(WEBSITES)}')
    YELLOW(f'[X] SUCCESS = {len(SUCCESS)}')
    YELLOW(f'[X] FAILED = {len(FAILED)}')

    if (input('Show "SUCCESS" websites?:[y\\n]\t')) == 'Y' or 'y':
        x=0
        for i in SUCCESS:
            x += 1
            print(f'{x}) ',i)

search()
input()