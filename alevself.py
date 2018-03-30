# -*- coding: utf-8 -*-
#ALEBOT

import ALEVAN
from ALEVAN.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

ale = ALEVAN.LINE()
#ale.login(qr=True)
ale.login(token='ErTeIv3EzHHJxx3C8Boc.e2nG9Laq77F43k02llldZa.mpNlTtinB1vWKdRcIPlIv1nHEd+sVHELilAY/tkSP5I=')
ale.loginResult()
print "Ale-Login Success\n"

reload(sys)
sys.setdefaultencoding('utf-8')


selfMessage ="""
╔════════════════
║      ❇ S E L F ❇
╠════════════════
╠✒ Hi
╠✒ Me
╠✒ Mid @
╠✒ Idline (ID LINE)
╠✒ Checkdate (DD/MM/YY)
╠✒ Kalender
╠✒ Steal contact
╠✒ Pp @
╠✒ Cover @
╠✒ Auto like
╠✒ Scbc Text
╠✒ Getbio @
╠✒ Getinfo @
╠✒ Getname @
╠✒ Getprofile @
╠✒ Getcontact @
╠✒ Getvid @
╠✒ Friendlist
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

botMessage ="""
╔═════════════════
║         ❇ B O T ❇
╠═════════════════
╠✒ Absen
╠✒  Respon 
╠✒  Runtime 
╠✒  Ale copy @ 
╠✒  Backup all 
╠✒  !bio Text 
╠✒  @bye (Usir Bot) 
╠✒  !bye (mengeluarkan bot) 
╠[ P R A N K ]
╠✒ Call (nomor tlfn)
╠✒ Test/Hula (no tlfn)
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

mediaMessage ="""
╔═════════════════
║       ❇ M E D I A ❇
╠═════════════════
╠✒  Gift 
╠✒  Gift1 @ s/d Gift10 @ 
╠✒  Giftbycontact 
╠✒  All gift 
╠✒  Gif gore 
╠✒  My info 
╠✒  Info @ 
╠✒  Status @ 
╠✒  Google: (Text) 
╠✒  Playstore NamaApp 
╠✒  Fancytext: Text 
╠✒  /musik Judul-Penyanyi 
╠✒  /lirik Judul-Penyanyi 
╠✒  /musrik Judul-Penyanyi 
╠✒  /ig UrsnameInstagram 
╠✒  Profileig 
╠✒  Checkig UsernameInstagram 
╠✒  /apakah Text 
╠✒  /kapan Text 
╠✒  /hari Text
╠✒  /berapa Text
╠✒  /berapakah Text 
╠✒  Youtubelink: Judul Video 
╠✒  Youtubevideo: Judul Video 
╠✒  Youtubesearch: Judul Video 
╠✒  Image NamaGambar 
╠✒  Say-id Text  Indonesia
╠✒  Say-en Text Inggris
╠✒  Say-jp Text  Jepang
╠✒  Say-ko Text Korea
╠✒  Image (nama gambar)  
╠✒  Spam on/off jmlh text   
╠✒  Up 
╠✒  Spamtag @(tag khusus yg
║ namanya pakai huruf biasa) 
╠✒  Wikipedia (Text) 
╠✒  Spamcontact @ 
╠✒  Raisa 
╠✒  Pap 
╠✒  Pap abs 
╠✒  Pap creator 
╠✒  Pap cecan 
╠✒  Pap cogan 
╠✒  Pap toket (for 18++:'v)
╠✒  Pap anu (for 18++:'v)
╠✒  Hay @tag (mengirim 7pesan di pc) 
╠✒  .quotes 
╠✒  love contoh: Siti love adi 
╠✒  kapan 
╠✒  .spm jmlh text 
╠✒  Spamcontact @ 
╠✒  .waktu 
╠✒  .cek 
╠✒  .wiki-id 
╠✒  .wiki-en 
╠✒  .apakah 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

groupMessage ="""
╔════════════════
║     ❇ G R O U P ❇
╠════════════════
╠✒  Welcome 
╠✒  Say welcome 
╠✒  Invite creator 
║ ⚫ CHECK SIDER⚫
╠✒  Setview/Cctv 
╠✒  Viewseen/Cyduk 
╠✒  Bintit 
╠✒  Tan 
║            SELESAI 
╠✒  Gn: (NamaGroup) 
╠✒  Tagall/Sleding 
╠✒  Recover 
╠✒  Cancel 
╠✒  Cancelall 
╠✒  Gcreator 
╠✒  Ginfo 
╠✒  Gurl 
╠✒  List group 
╠✒  Pict group: (NamaGroup) 
╠✒  Spam: (Text) 
╠✒  Spam 
╠✒  Add all 
╠✒  Kick: (Mid) 
╠✒  Invite: (Mid) 
╠✒  Invite 
╠✒  Memlist 
╠✒  Getgroup image 
╠✒  Urlgroup image 
╠✒  Help media 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

setMessage ="""
╔══════════════════
║              ❇ S E T ❇
╠══════════════════
╠✒  Sambutan on/off 
╠✒  Url on/off 
╠✒  Alwaysread on/off 
╠✒  Sider on/off 
╠✒  Contact on/off 
╠✒  Simisimi on/off 
╠✒  Like on/off 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

creatorMessage ="""
╔══════════════════
║     ❇ C R E A T O R ❇
╠══════════════════
╠✒  Admin add @ 
╠✒  Admin remove @ 
╠✒  /cnAle 
╠✒  Crash 
╠✒  Kickall 
╠✒  Bc: (Text) 
╠✒  !bc (Text)
╠✒  Cbc (Text) 
╠✒  Nk: @ 
╠✒  Ulti @ 
╠✒  Join group: (NamaGroup 
╠✒  Leave group: (NamaGroup 
╠✒  Leave all group 
╠✒  Bot restart 
╠✒  Turn off 
╠✒  Kernel 
╠✒  Cpu 
╠✒  Ifconfig 
╠✒  System 
╠✒  Self like 
╠✒  Like temen 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

adminMessage ="""
╔══════════════════
║          ❇ A D M I N ❇
╠══════════════════
╠✒  Admin list 
╠✒  Ban 
╠✒  Unban 
╠✒  Ban @ 
╠✒  Unban @ 
╠✒  Ban list 
╠✒  Clear ban 
╠✒  Kill 
╠✒  Kick @ 
╠✒  Set member: (Jumblah) 
╠✒  Ban group: (NamaGroup 
╠✒  Del ban: (NamaGroup 
╠✒  List ban 
╠✒  Kill ban 
╠✒  Glist 
╠✒  Glistmid 
╠✒  Details group: (Gid) 
╠✒  Cancel invite: (Gid) 
╠✒  Invitemeto: (Gid) 
╠✒  Ale acc invite 
╠✒  Removechat 
╠✒  Join on/off 
╠✒  Joincancel on/off 
╠✒  Respon on/off 
╠✒  Responkick on/off 
╠✒  Leave on/off 
╠✒  Help admin 
╠✒  Help creator 
╠✒  Help set 
╠✒  Help protect 
╠✒  Status 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

helpMessage ="""
╔═══════════════════
║    ❇ H E L P U B L I K❇
╠═══════════════════
╠✒  Help group 
╠✒  Help media 
╠✒  Help trans 
╠✒  Help self 
╠✒  Owner 
╠✒  Admin 
╠✒  Speed/Spd 
╠✒  Speedt/Spt
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""
keyMessage ="""
╔═══════════════════
║❇ H E L P C R E A T O R❇
╠═══════════════════
╠✒  Help creator 
╠✒  Help protect 
╠✒  Help bot 
╠✒  Help admin 
╠✒  Help set 
╠✒  Status 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""
alevan="u136360f65010efb7f8dcad362cb2c3cc"

transMessage ="""
╔════════════════
║       ❇ TRANSLATE ❇
╠════════════════
╠✒Tr-id = Indonesia
╠✒Tr-ja = Jepang
╠✒Tr-en = Inggris
╠✒Tr-es = Spanyol
╠✒Tr-th = Thailand
╠✒Tr-ko = Korea
╠✒Tr-jw = Jawa
╠✒Tr-ru = Rusia
╠✒Tr-ms = Malaysia
╠✒Tr-ar = Arab
╠✒Tr-fr = Perancis
╠✒Tr-it = Itali
╠✒Tr-de = Jerman
╠✒Tr-tr = Turki
╠✒Tr-la = Latin
╠✒Tr-vi = Vietnam
╠✒Tr-hi = India
╠✒Tr-su = Sunda
╠✒Tr-zh = Chinese
╠✒Tr-af = afrika
╠✒Translate-id
╠✒Translate-en
╠✒Translate-ar
╠✒Translate-jp
╠✒Translate-ko
╠✒Id@en Text (Translate ID Ke En 
╠✒Id@th Text (Translate ID Ke TH 
╠✒Th@id Text (Translate Th Ke ID 
╠✒En@id Text (Translate En Ke ID 
╠✒Ko@id Text (Translate Ko Ke ID 
╠✒Id@ko Text (Translate ID Ke ko 
╠✒Id@jw Text (Translate ID Ke jw 
╠✒Jw@id Text (Translate Jw Ke ID 
╠✒Id@su Text (Translate ID Ke Su 
╠✒Su@id Text (Translate Sunda Ke ID 
╠✒Id@ar Text (Translate ID Ke Arab 
╠✒Ar@id Text (Translate Ar Ke ID 
║      BEBERAPA ADA PERBAIKAN
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""

protectMessage ="""
╔═════════════════
║         ❇ P R O T E C T ❇
╠═════════════════
╠✒  Allprotect on/off 
╠✒  Autocancel on/off 
╠✒  Qr on/off 
╠✒  Autokick on/off 
╠✒  Ghost on/off 
╠✒  Invitepro on/off 
╠══════════════════
║    CREATOR: Alevan 
╠══════════════════
║ ⚪ line.me/ti/p/~shandiap 
╚══════════════════
"""


KAC=[ale]
mid = ale.getProfile().mid
Amid = ale.getProfile().mid
Bmid = ale.getProfile().mid
Cmid = ale.getProfile().mid
Dmid = ale.getProfile().mid
Emid = ale.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid]
Creator=["u136360f65010efb7f8dcad362cb2c3cc"]
admin=["u136360f65010efb7f8dcad362cb2c3cc"]

contact = ale.getProfile()
backup1 = ale.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = ale.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "AutoJoinCancel":True,
    "memberscancel":10,
    "Members":1,
    "AutoCancel":{},
    "AutoCancelon":False,  
    "joinkick":False,
    "AutoKick":{},
    "AutoKickon":False,
    'pap':True,
    'invite':True,
    'steal':{},
    'gift':{},
    'likeOn':True,
    'Leave':{},    
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,      
    'timeline':True,
    "Timeline":True,
    "comment1":"lb ya kak ke #punyaalevan",
  #  "comment2":"Wkwkwk ＼（○＾ω＾○）／",
#    "comment3":"Lucu Banget!!! ヘ(^_^)ヘ",
#    "comment4":"Nice Kak (^_^)",
    "comment5":"Bot Auto Like ©By : Alevan\nAdd oa kita, buat mengetahui bot lainnya : 👉 http://line.me/ti/p/%40bqs0815l",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":{},
    "Qron":False,
    "Contact":False,
    "Sambutan":True,
    "Ghost":False,
    "inviteprotect":False,   
    "alwaysRead":False,    
    "atjointicket":True,
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"


def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    years, month = divmod(month,12)
    return '\n╠▶ %02d Years \n╠▶ %02d Month\n╠▶ %02d Days\n╠▶ %02d нσυяѕ\n╠▶ %02d мιиυтє\n╠▶ %02d ѕє¢σи∂」' %(years, month, days ,hours, mins,secs)
#def waktu(secs):
#    mins, secs = divmod(secs,60)
#    hours, mins = divmod(mins,60)
#    return '%02d нσυяѕ %02d мιиυтє %02d ѕє¢σи∂」' % (hours, mins, secs)     
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              ale.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                ale.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      

        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ale.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            contact = ale.getContact(op.param2)
                            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            c = Message(to=op.param1, from_=None, text=None, contentType=13)
                            c.contentMetadata={'mid':op.param2}
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n╠✒" + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                    	ale.sendMessage(c)
                                        ale.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgintip Aja Niih. . .\nAyo gabung sini kak  ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                    	ale.sendMessage(c)
                                        ale.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nBetah Banget Jadi Penonton. . .\nJangan doyang ngintip, pantes jones:'v  ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                	ale.sendMessage(c)
                                        ale.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nNgapain Kak Ngintip Aja???\nSini Gabung Chat...   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass    

	      

        if op.type == 22:
            ale.leaveRoom(op.param1)

        if op.type == 21:
            ale.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Creator:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Creator:
		    ale.acceptGroupInvitation(op.param1)
 
            if op.param3 in mid:
		if op.param2 in Amid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Bmid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
		if op.param2 in Cmid:
		    ale.acceptGroupInvitation(op.param1)
 
            if op.param3 in Amid:
		if op.param2 in mid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    ale.acceptGroupInvitation(op.param1)
 
            if op.param3 in Bmid:
		if op.param2 in mid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    ale.acceptGroupInvitation(op.param1)
 
            if op.param3 in Cmid:
		if op.param2 in mid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Cmid:
		    ale.acceptGroupInvitation(op.param1)
 
            if op.param3 in Dmid:
		if op.param2 in mid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Amid:
		    ale.acceptGroupInvitation(op.param1)
            if op.param3 in Dmid:
		if op.param2 in Bmid:
		    ale.acceptGroupInvitation(op.param1)
		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = ale.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        ale.acceptGroupInvitation(op.param1)
                        ale.sendText(op.param1,"Maaf " + ale.getContact(op.param2).displayName + "\nMember Kurang Dari 10 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':alevan}
                        ale.sendMessage(c)                        
                        ale.leaveGroup(op.param1)                        
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = ale.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        ale.rejectGroupInvitation(op.param1)
		    else:
                        ale.acceptGroupInvitation(op.param1)
			#G = ale.#getGroup(op.#param1)
			#G.preventJoinByTicket #= #False
			#ale.updateGroup#(G#)
			#Ti #= #ale.reissueGroupTicket#(op.#param1)
			#ale.acceptGroupInvitationByTicket#(op.#param1,Ti#)
			#ale.acceptGroupInvitationByTicket#(op.#param1,Ti#)
			#ale.acceptGroupInvitationByTicket#(op.#param1,Ti#)
			#ale.acceptGroupInvitationByTicket#(op.#param1,Ti#)
			#G.preventJoinByTicket #= #True
			#ale.updateGroup#(G#)
			ale.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
			ale.sendText(op.param1,"☆Jika terjadi sesuatu hubungi own☆\n☆https://line.me/ti/p/%40bqs0815l")
	    else:
                if wait["AutoCancel"][op.param1] == True:
		    if op.param3 in admin:
			pass
		    else:
                        ale.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			ale.cancelGroupInvitation(op.param1, [op.param3])
			ale.sendText(op.param1, "Blacklist Detected")
		    else:
			pass


        if op.type == 19:
		if wait["AutoKick"][op.param1] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    G = ale.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ale.updateGroup(G)
                    Ti = ale.reissueGroupTicket(op.param1)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ale.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ale.updateGroup(X)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ale.kickoutFromGroup(op.param1,[op.param2])
                        ale.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = ale.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    Ti = ale.reissueGroupTicket(op.param1)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ale.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ale.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ale.kickoutFromGroup(op.param1,[op.param2])
                        ale.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = ale.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    Ti = ale.reissueGroupTicket(op.param1)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ale.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ale.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ale.kickoutFromGroup(op.param1,[op.param2])
                        ale.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = ale.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    Ti = ale.reissueGroupTicket(op.param1)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ale.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ale.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
                            
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ale.kickoutFromGroup(op.param1,[op.param2])
                        ale.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True

                    X = ale.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    Ti = ale.reissueGroupTicket(op.param1)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    ale.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ale.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ale.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True                            
 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True


        if op.type == 11:
            if wait["Qr"][op.param1] == True:
                if op.param2 not in Bots:
                  if op.param2 not in admin:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(KAC).updateGroup(G)


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ginfo = ale.getGroup(op.param1)
            contact = ale.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ale.sendMessage(c)
            ale.sendText(op.param1,"Hallo "+"@"+ ale.getContact(op.param2).displayName + " \nWelcome To ☞ " + str(ginfo.name) + " ☜" + "\nBudayakan Cek Note\nDan Semoga Betah Disini ^_^")
            ale.sendImageWithURL(op.param1,image)
            print "MEMBER JOIN TO GROUP"
            
            
        if op.type == 17:
          if wait["joinkick"] == True:
            if op.param2 in admin:
              if op.param2 in Bots:
                return
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            print "MEMBER JOIN KICK TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ale.sendText(op.param1,"Good Bye " + ale.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP"


        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    ale.cancelGroupInvitation(op.param1,[op.param3])
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19:
	 if wait["Ghost"] == True:
          if op.param2 in admin:
           if op.param2 in Bots:
               pass
          else:
            try:
              G = ale.getGroup(op.param1)
              G.preventJoinByTicket = False
              ale.updateGroup(G)
              Ticket = ale.reissueGroupTicket(op.param1)
              ale.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ale.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ale.sendMessage(c)
              ale.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              ale.updateGroup(G)
              wait["blacklist"][op.param2] = True
            except:
              G = ale.getGroup(op.param1)
              G.preventJoinByTicket = False
              ale.updateGroup(G)
              Ticket = ale.reissueGroupTicket(op.param1)
              ale.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              ale.kickoutFromGroup(op.param1,[op.param2])
              c = Message(to=op.param1, from_=None, text=None, contentType=13)
              c.contentMetadata={'mid':op.param2}
              ale.sendMessage(c)
              ale.leaveGroup(op.param1)
              G.preventJoinByTicket = True
              ale.updateGroup(G)
              wait["blacklist"][op.param2] = True



        if op.type == 25:
            msg = op.message
            if "My info" in msg.text:
              kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong","Kalau pagi cowo","Kalau pagi cewe")
              wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur","Kembaran miper","Tidak beraturan")
              status = ("Menikah","Pacaran","Jones","Gamon dari mantan")
              k = random.choice(kelamin)
              w = random.choice(wajah)
              s = random.choice(status)
              ale.sendText(msg.to,"╠✒Nama : "+ale.getContact(msg.from_).displayName+"\n╠✒Kelamin : "+k+"\n╠✒Wajah : "+w+"\n╠✒Status Kehidupan : "+s)

            if "Info @" in msg.text:
                _name = msg.text.replace("Info @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong","Kalau pagi cowo","Kalau pagi cewe")
                        wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur","Kembaran miper","Tidak beraturan")
                        status = ("Menikah","Pacaran","Jones","Gamon dari mantan")
                        k = random.choice(kelamin)
                        w = random.choice(wajah)
                        s = random.choice(status)
                        ale.sendText(msg.to,"╠✒Nama : "+xname+"\n╠✒Kelamin : "+k+"\n╠✒Wajah : "+w+"\n╠✒Status Kehidupan : "+s)

            if "Status @" in msg.text:
                _name = msg.text.replace("Status @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        kelamin = ("Keturunan darah biru","Keturunan darah kotor","Saudaranya miper","Keturunan kerajaan","Keturunan ubab","Anaknya miper","Kembaran dijjah")
                        wajah = ("Gajelas","Digantungin doi","Status ngambang kek anu","Pacaran","Bentar lagi Nikah","Menikah","Jomblo","Jonez seumur hidup","Menyedihkan")
                        status = ("Jodohnya miper","Jodohnya Dijjah","Jodohnya artis","Jodohnya dari khayangan","Gapunya jodoh","Jodohnya ganti ganti","Kan jonez gapunya jodoh:'v")
                        k = random.choice(kelamin)
                        w = random.choice(wajah)
                        s = random.choice(status)
                        ale.sendText(msg.to,"╠✒Nama : "+xname+"\n╠✒Keturunan : "+k+"\n╠✒Status : "+w+"\n╠✒Jodoh : "+s)

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    ale.sendChatChecked(msg.from_,msg.id)
                else:
                    ale.sendChatChecked(msg.to,msg.id)
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     ale.like(url[25:58], url[66:], likeType=1005)
                     ale.like(url[25:58], url[66:], likeType=1002)
                     ale.like(url[25:58], url[66:], likeType=1004)
                     ale.like(url[25:58], url[66:], likeType=1003)
                     ale.like(url[25:58], url[66:], likeType=1001)
                     ale.comment(url[25:58], url[66:], wait["comment1"])
                     ale.comment(url[25:58], url[66:], wait["comment2"])
                     ale.comment(url[25:58], url[66:], wait["comment3"])
                     ale.comment(url[25:58], url[66:], wait["comment4"])
                     ale.comment(url[25:58], url[66:], wait["comment5"])
                     ale.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False

        if op.type == 25:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ale.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ale.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  ale.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break                                  
                           if mention['M'] in Bots:
                                  ale.sendText(msg.to,ret_)
                                  random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
                                  break 
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = ale.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Tag Mulu Lo Anjirr!","Dia Lagi Off", cName + " Kenapa Tag? Kangen?","Dia Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in admin:
                                  ale.sendText(msg.to,ret_)
                                  break                                  
                           if mention['M'] in Bots:
                                  ale.sendText(msg.to,ret_)
                                  break   
                                  
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = ale.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Sekali lagi nge tag gw sumpahin jomblo seumur hidup!","Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Woii " + cName + " Jangan Ngetag, Riibut!"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ale.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "20001316",
                                                       "STKPKGID": "1582380",
                                                       "STKVER": "1" }
                                  ale.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = ale.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["Woii " + cName + ", Dasar Jones Ngetag Mulu!"]
                    balas1 = "Ini Foto Sii Jones Yang Suka Ngetag. . ."
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  ale.sendText(msg.to,ret_)
                                  ale.sendText(msg.to,balas1)
                                  ale.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "11764508",
                                                       "STKPKGID": "6641",
                                                       "STKVER": "1" }
                                  ale.sendMessage(msg)                                
                                  break  

            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            random.choice(KAC).sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            random.choice(KAC).sendText(msg.to,"Ditambahkan")
		    else:
			ale.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        random.choice(KAC).sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        random.choice(KAC).sendText(msg.to,"Tidak Ada Black List")

 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ale.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        ale.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        ale.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ale.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': alevan}
                ale.sendMessage(msg)
		ale.sendText(msg.to,"Itu Majikan Kami yang unchh")
		
            elif msg.text in ["Admin","admin"]:
                msg.contentType = 13
                admin1 = "u6b3f7e3b124ad8d9ed9261d351c91abf"
                admin2 = "u8b2bb5214c1afc77d06901a535c23e30"
                admin3 = "uee350d1db0e0079e88b53017439e24b0"
                msg.contentMetadata = {'mid': alevan}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': admin1}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': admin2}
                random.choice(KAC).sendMessage(msg)
                msg.contentMetadata = {'mid': admin3}
                random.choice(KAC).sendMessage(msg)                
		random.choice(KAC).sendText(msg.to,"Itu Admin Kami (^_^)")	
		
 
                
            elif "Admin add @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            ale.sendText(msg.to,"Admin Unity Ditambahkan")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ale.sendText(msg.to,"Command Denied.")
                ale.sendText(msg.to,"Creator Permission Required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in Creator:
                print "[Command]Admin Remove Executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                gs = ale.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact Tidak Di Temukan")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ale.sendText(msg.to,"Admin Unity Dihapus")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ale.sendText(msg.to,"Command Denied.")
                ale.sendText(msg.to,"Creator Permission Required.")
                
            elif msg.text in ["Admin list","admin list","List admin"]:
              if admin == []:
                  ale.sendText(msg.to,"The Admin List Is Empty")
              else:
                  ale.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════════════════\n║        ☆☞ ADMIN UNITY  ☆\n╠═════════════════════════\n"
                  for mi_d in admin:
                      mc += "╠••> " +ale.getContact(mi_d).displayName + "\n"
                  ale.sendText(msg.to,mc + "╚═════════════════════════")
                  print "[Command]Admin List executed"
				  
            elif msg.text.lower() == 'Runtime':
                eltime = time.time() - mulai
                van = "║  Bot sudah berjalan selama"+waktu(eltime)
                ale.sendText(msg.to,"╔═══════════════\n║☆☞ UNITY RUNTIME══════════════\n " + van + "\n╚═══════════════")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = ale.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                ale.sendMessage(msg)
		ale.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ale.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ale.findAndAddContactsByMid(target)
                                contact = ale.getContact(target)
                                cu = ale.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ale.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                ale.sendText(msg.to,"Profile Picture " + contact.displayName)
                                ale.sendImageWithURL(msg.to,image)
                                ale.sendText(msg.to,"Cover " + contact.displayName)
                                ale.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ale.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ale.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                ale.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break


            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = ale.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             ale.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 ale.findAndAddContactsByMid(target)
                                 ale.inviteIntoGroup(msg.to,[target])
                                 ale.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      ale.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["Key creator","help creator","Help creator"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,creatorMessage)

            elif msg.text in ["Key group","help group","Help group"]:
                ale.sendText(msg.to,groupMessage)

            elif msg.text in ["Key","help","Help"]:
                ale.sendText(msg.to,helpMessage)
                
            elif msg.text in ["!!!!","-!-","Help1"]:
                ale.sendText(msg.to,keyMessage)
				
            elif msg.text in ["Trans","help trans","Help trans"]:
                ale.sendText(msg.to,transMessage)

            elif msg.text in ["Key self","help self","Help self"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,selfMessage)

            elif msg.text in ["Key bot","help bot","Help bot"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,botMessage)

            elif msg.text in ["Key set","help set","Help set"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,setMessage)

            elif msg.text in ["Key media","help media","Help media"]:
                ale.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["Key admin","help admin","Help admin"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,adminMessage)    
                
            elif msg.text in ["Key protect","help protect","Help protect"]:
#              if msg.from_ in Admin:
                ale.sendText(msg.to,protectMessage)                 
                

 
            elif msg.text in ["List group"]:
                    gid = ale.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = ale.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    ale.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = ale.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = ale.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    ale.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    ale.sendText(msg.to, "Khusus Alevan")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        random.choice(KAC).sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +ale.getGroup(gid).name + "\n"
                        random.choice(KAC).sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    ale.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if ale.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    ale.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    ale.sendText(msg.to, "Khusus Alevan")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = ale.getGroupIdsJoined()
		gid = ale.getGroupIdsJoined()
		gid = ale.getGroupIdsJoined()
		gid = ale.getGroupIdsJoined()
		gid = ale.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = ale.getGroup(i).name
                            h = ale.getGroup(i).name
                            h = ale.getGroup(i).name
                            h = ale.getGroup(i).name
                            h = ale.getGroup(i).name
		            if h == ng:
		                random.choice(KAC).inviteIntoGroup(i,[Creator])
			        ale.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        ale.sendText(msg.to,"Khusus Alevan")
		except Exception as e:
		    ale.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = ale.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = ale.getGroup(i).name
		        if h == ng:
			    ale.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            ale.leaveGroup(i)
			    ale.leaveGroup(i)
			    ale.leaveGroup(i)
			    ale.leaveGroup(i)
			    ale.leaveGroup(i)
			    ale.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
 
	    elif "Leave all group" == msg.text:
		gid = ale.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			ale.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        ale.leaveGroup(i)
			ale.leaveGroup(i)
			ale.leaveGroup(i)
			ale.leaveGroup(i)
			ale.leaveGroup(i)
		    ale.sendText(msg.to,"Success Leave All Group")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = ale.getGroupIdsJoined()
                for i in gid:
                    h = ale.getGroup(i).name
                    gna = ale.getGroup(i)
                    if h == saya:
                        ale.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ale.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        ale.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    ale.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    ale.sendText(msg.to,"Url Sudah Aktif")
                else:
                    ale.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ale.updateGroup(X)
                    ale.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    ale.sendText(msg.to,"Can not be used outside the group")
                    
            elif '/ti/g/' in msg.text.lower():
	           if wait["atjointicket"] == True:
		          link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		          links = link_re.findall(msg.text)
		          n_links=[]
		          for l in links:
			                  if l not in n_links:
		                                 n_links.append(l)
		          for ticket_id in n_links:
			                  group = ale.findGroupByTicket(ticket_id)
			                  ale.acceptGroupInvitationByTicket(group.id,ticket_id)
			                  ale.sendMessage(to, "Sukses join ke grup %s" % str(group.name))
			
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    ale.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    ale.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    ale.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    ale.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")		    
		    
 
            elif msg.text in ["Respon on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["kickMention"] = False
                    ale.sendText(msg.to,"Auto Respon Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Respon off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    ale.sendText(msg.to,"Auto Respon Sudah Off")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")	

            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    ale.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    ale.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    ale.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    ale.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")	

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    ale.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    ale.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
		    
		    
 
            elif msg.text in ["Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    ale.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    ale.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")			  
 
            elif msg.text in ["Leave on"]:
		if msg.from_ in admin:
                    wait["Leave"] = True
                    ale.sendText(msg.to,"Leave Sudah Aktif")
		else:
		    ale.sendText(msg.to,"Khusus Alevan")
		    
 
	    elif msg.text in ["Autocancel on"]:
     	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = True
                wait["AutoCancelon"] = True
                ale.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")		

	    elif msg.text in ["Autocancel off"]:
    	     if msg.from_ in admin:	        
                wait["AutoCancel"][msg.to] = False
                wait["AutoCancelon"] = False
                ale.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")	


	    elif msg.text in ["Joinkick on"]:
    	     if msg.from_ in admin:	        
                wait["joinkick"] = True
                wait["Sambutan"] = False
                ale.sendText(msg.to,"Join Kick Sudah Aktif")
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")		

	    elif msg.text in ["Joinkick off"]:
    	     if msg.from_ in admin:	        
                wait["joinkick"] = False
                ale.sendText(msg.to,"Join Kick Sudah Di Nonaktifkan")
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")	

		    

	    elif msg.text in ["Invitepro on","Inviteprotect on"]:
    	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                ale.sendText(msg.to,"Invite Protect Sudah Aktif")
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")		

	    elif msg.text in ["Invitepro off","Inviteprotect off"]:
    	     if msg.from_ in admin:	        
                wait["inviteprotect"] = False
                ale.sendText(msg.to,"Invite Protect Sudah Di Nonaktifkan")
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")		    

	    elif "Qr on" in msg.text:
#            if msg.from_ in admin:	        
	        wait["Qr"][msg.to] = True
	        wait["Qron"] = True
	    	ale.sendText(msg.to,"QR Protect Sudah Aktif")
		print wait["Qr"]	    	
#	     else:
#		    ale.sendText(msg.to,"Khusus Alevan")	    	 #--------------------------------------------------
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		ale.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=ale.findGroupByTicket(ticket_id)
				ale.acceptGroupInvitationByTicket(group.mid,ticket_id)
				ale.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
#--------------------------------------------------


	    elif "Qr off" in msg.text:
#	        if msg.from_ in admin:	        
	    	wait["Qr"][msg.to] = False
	    	wait["Qron"] = False
	    	ale.sendText(msg.to,"Qr Protect Sudah Di Nonaktifkan")
		print wait["Qr"]	    	
#	     else:
#		    ale.sendText(msg.to,"Khusus Alevan")	    	
                        
	    elif msg.text in ["Autokick on"]:
    	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = True
                wait["AutoKickon"] = True
                ale.sendText(msg.to,"Auto Kick Sudah Aktif")
		print wait["AutoKick"]
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")		

	    elif msg.text in ["Autokick off"]:
    	     if msg.from_ in admin:	        
                wait["AutoKick"][msg.to] = False
                wait["AutoKickon"] = False
                ale.sendText(msg.to,"Auto Kick Sudah Di Nonaktifkan")
		print wait["AutoKick"]
	     else:
		    ale.sendText(msg.to,"Khusus Alevan")	


	    elif msg.text in ["Ghost on"]:
#	        if msg.from_ in admin:	        
                wait["Ghost"] = True
                ale.sendText(msg.to,"Ghost Sudah Aktif")
#	     else:
#		    ale.sendText(msg.to,"Khusus Alevan")		

	    elif msg.text in ["Ghost off"]:
#	        if msg.from_ in admin:	        
                wait["Ghost"] = False
                ale.sendText(msg.to,"Ghost Sudah Di Nonaktifkan")
#	     else:
#		    ale.sendText(msg.to,"Khusus Alevan")	     

            elif msg.text in ["Allprotect on"]:
           	   if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = True
                    wait["AutoCancelon"] = True
                    wait["inviteprotect"] = True 
                    wait["joinkick"] = True 
                    wait["AutoKick"][msg.to] = True
                    wait["AutoKickon"] = True
                    wait["Qr"][msg.to] = True
                    wait["Qron"] = True
                    wait["Ghost"] = True     
                    ale.sendText(msg.to,"All Protect Sudah Aktif Semua")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
#		else:
#		    ale.sendText(msg.to,"Khusus Alevan")

            elif msg.text in ["Allprotect off"]:
          	   if msg.from_ in admin:
                    wait["AutoCancel"][msg.to] = False
                    wait["AutoCancelon"] = False
                    wait["inviteprotect"] = False  
                    wait["joinkick"] = False
                    wait["AutoKick"][msg.to] = False
                    wait["AutoKickon"] = False
                    wait["Qr"][msg.to] = False
                    wait["Qron"] = False
                    wait["Ghost"] = False 
                    ale.sendText(msg.to,"All Protect Sudah Di Nonaktifkan Semua")
		    print wait["AutoCancel"]
		    print wait["AutoKick"]
		    print wait["Qr"]
#		else:                    
#		else:
#		    ale.sendText(msg.to,"Khusus Alevan")


            elif msg.text in ["K on","Contact on"]:
                wait["Contact"] = True
                ale.sendText(msg.to,"Contact Sudah Aktif")

            elif msg.text in ["K off","Contact off"]:
                wait["Contact"] = False
                ale.sendText(msg.to,"Contact Sudah Di Nonaktifkan")
                

            elif msg.text in ["Alwaysread on"]:
                wait["alwaysRead"] = True
                ale.sendText(msg.to,"Always Read Sudah Aktif")

            elif msg.text in ["Alwaysread off"]:
                wait["alwaysRead"] = False
                ale.sendText(msg.to,"Always Read Sudah Di Nonaktifkan")                


            elif msg.text in ["Sambutan on"]:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Sambutan Di Aktifkanヾ(*´∀｀*)ﾉ")
                else:
                    wait["Sambutan"] = True
                    wait["joinkick"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Sudah Onヽ(´▽｀)/")

            elif msg.text in ["Sambutan off"]:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Sambutan Di Nonaktifkan(　＾∇＾)")
                else:
                    wait["Sambutan"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Sudah Off(p′︵‵。)")
                        
                        
            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ale.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ale.sendText(msg.to, "Cek Sider Off")
                else:
                    ale.sendText(msg.to, "Heh Belom Di Set")                         


            elif msg.text in ["Status"]:
                md = ""
		if wait["Sambutan"] == True: md+="╠✒ ✔️ Sambutan : On\n"
		else:md+="╠✒ ❌ Sambutan : Off\n"
		if wait["joinkick"] == True: md+="╠✒ ✔️ Join Kick : On\n"
		else:md+="╠✒ ❌ Join Kick : Off\n"		
		if wait["AutoJoin"] == True: md+="╠✒ ✔️ Auto Join : On\n"
                else: md +="╠✒ ❌ Auto Join : Off\n"
		if wait["AutoJoinCancel"] == True: md+="╠✒ ✔️ Auto Join Cancel : On\n"
                else: md +="╠✒ ❌ Auto Join Cancel : Off\n"                
		if wait["Leave"] == True: md+="╠✒ ✔️ Leave : On\n"
                else: md +="╠✒ ❌ Leave : Off\n"                
		if wait["Contact"] == True: md+="╠✒ ✔️ Info Contact : On\n"
		else: md+="╠✒ ❌ Info Contact : Off\n"
                if wait["AutoCancelon"] == True:md+="╠✒ ✔️ Auto Cancel : On\n"
                else: md+= "╠✒ ❌ Auto Cancel : Off\n"
                if wait["inviteprotect"] == True:md+="╠✒ ✔️ Invite Protect : On\n"
                else: md+= "╠✒ ❌ Invite Protect : Off\n"                
		if wait["Qron"] == True: md+="╠✒ ✔️ Qr Protect : On\n"
		else:md+="╠✒ ❌ Qr Protect : Off\n"
		if wait["AutoKickon"] == True: md+="╠✒ ✔️ Auto Kick : On\n"
		else:md+="╠✒ ❌ Auto Kick : Off\n"
		if wait["Ghost"] == True: md+="╠✒ ✔️ Ghost : On\n"
		else:md+="╠✒ ❌ Ghost : Off\n"
		if wait["alwaysRead"] == True: md+="╠✒ ✔️ Always Read : On\n"
		else:md+="╠✒ ❌ Always Read: Off\n"
		if wait["detectMention"] == True: md+="╠✒ ✔️ Auto Respon : On\n"
		else:md+="╠✒ ❌ Auto Respon : Off\n"			
		if wait["detectMention2"] == True: md+="╠✒ ✔️ Auto Respon2 : On\n"
		else:md+="╠✒ ❌ Auto Respon2 : Off\n"	
		if wait["detectMention3"] == True: md+="╠✒ ✔️ Auto Respon3 : On\n"
		else:md+="╠✒ ❌ Auto Respon3 : Off\n"	
		if wait["kickMention"] == True: md+="╠✒ ✔️ Auto Respon Kick : On\n"
		else:md+="╠✒ ❌ Auto Respon Kick : Off\n"				
		if wait["Sider"] == True: md+="╠✒ ✔️ Auto Sider : On\n"
		else:md+="╠✒ ❌ Auto Sider: Off\n"	
		if wait["Simi"] == True: md+="╠✒ ✔️ Simisimi : On\n"
		else:md+="╠✒ ❌ Simisimi: Off\n"		
                ale.sendText(msg.to,"╔═════════════════════════\n""║           ☆☞ S T A T U S ☜☆\n""╠═════════════════════════\n"+md+"╚═════════════════════════")


            elif "Call " in msg.text:
                no = msg.text.replace("Call ","")
                r = requests.get("http://apisora.herokuapp.com/prank/call/?no="+str(no))
		    
            elif "Test " in msg.text:
                no = msg.text.replace("Test ","")
                r = requests.get("http://apisora.herokuapp.com/prank/sms/?no="+str(no))

            elif "Hula " in msg.text:
                no = msg.text.replace("Hula ","")
                r = requests.get("http://apisora.herokuapp.com/prank/sms2/?no="+str(no))

            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                ale.sendMessage(msg)
                ale.sendMessage(msg)
                ale.sendMessage(msg)

            elif msg.text in ["TC1 Gift","TC1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text in ["TC2 Gift","TC2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text in ["TC3 Gift","TC3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                ale.sendMessage(msg)
                
                
            elif "Gift1 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift1 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift2 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift2 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '1360738'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift3 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift3 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '1395389'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift4 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift4 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1329191'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift5 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift5 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '9057'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift6 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift6 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '2',
                                                         'STKPKGID': '9167'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift7 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift7 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '3',
                                                         'STKPKGID': '7334'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift8 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift8 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1380280'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift9 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift9 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '4',
                                                         'STKPKGID': '1405277'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}

            elif "Gift10 " in msg.text:
                       msg.contentType = 13
                       nk0 = msg.text.replace("Gift10 ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = ale.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ale.sendText(msg.to,_name + " Check Your Gift")
                                    msg.contentType = 9
                                    msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                    msg.to = target
                                    msg.text = None
                                    ale.sendMessage(msg)
                                except:
                                    msg.contentMetadata = {'mid': target}


            elif msg.text.lower() in ["wkwkwk","wkwk","hahaha","haha"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '100',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["hehehe","hehe"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '10',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["galau"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '9',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["you","kau","kamu"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '7',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["marah","hadeuh","hadeh"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '6',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["please","pliss","mohon","tolong"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '4',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["haa","haaa","kaget"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '3',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["lucu","ngakak","lol"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '110',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["hmm","hmmm"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '101',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["tidur"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '1',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["gemes"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '2',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["cantik","imut"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '5',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["nyanyi","lalala"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '11',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["gugup"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '8',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["ok","oke","okay","oce","okee","sip","siph"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '13',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["mantab","mantap","nice","keren"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '14',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["ngejek"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '15',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["nangis","sedih"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '16',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["woi","kampret"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '102',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

            elif msg.text.lower() in ["huft"]:
                msg.contentType = 7
                msg.contentMetadata={'STKID': '104',
                                    'STKPKGID': '1',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)
                
        


            elif msg.text in ["Tagall","Tag all","Sleding"]:
                  group = ale.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ale.sendMessage(msg)
                  except Exception as error:
                      print error


            elif msg.text in ["Setview","Setpoint","Cctv"]:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                ale.sendText(msg.to, "☆Checkpoint Checked☆")
                print "Setview"

            elif msg.text in ["Viewseen","Check","Ciduk","Cyduk"]:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = ale.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        tukang = "╔═════════════════════════\n║         ☆☞ LIST VIEWERS ☜☆\n╠═════════════════════════\n╠✒ "
                        grp = '\n╠✒  '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠✒  Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        ale.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                        ale.sendText(msg.to, "Viewers dari group " + gs.name)
                        subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                        ale.sendText(msg.to, "☆Auto Checkpoint☆")                        
                    else:
                        ale.sendText(msg.to, "☆Belum Ada Viewers☆")
                    print "Viewseen"
#--------------------------CEK SIDER------------------------------

            elif "Bintit" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                ale.sendText(msg.to, "sabar")
                ale.sendText(msg.to, "lg di proses")                
                print "@setview"

            elif "Tan" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = ale.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        gs = ale.getGroup(msg.to)
                        tukang = "╔═════════════════════════\n║  ☆☞ VIEWERS ☜☆\n╠═════════════════════════\n╠✒ "
                        grp = '\n╠✒  '.join(str(f) for f in dataResult)
                        total = '\n╠═════════════════════════\n╠✒  Total %i Viewers (%s)' % (len(dataResult), datetime.now().strftime('%H:%M:%S')) + "\n╚═════════════════════════"
                        ale.sendText(msg.to, "Viewers dari group " + gs.name)
                        ale.sendText(msg.to, "%s %s %s" % (tukang, grp, total))
                    else:
                        ale.sendText(msg.to, "Belum ada viewers")
                    print "@viewseen"
#--------------------------------------------------------



	    elif "Kick " in msg.text:
		if msg.from_ in admin:	        
		    if 'MENTION' in msg.contentMetadata.keys()!= None:
		        names = re.findall(r'@(\w+)', msg.text)
		        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
		        mentionees = mention['MENTIONEES']
		        print mentionees
		        for mention in mentionees:
			    ale.kickoutFromGroup(msg.to,[mention['M']])

	    elif "Set member: " in msg.text:
		if msg.from_ in admin:	 	        
		    jml = msg.text.replace("Set member: ","")
		    wait["memberscancel"] = int(jml)
		    ale.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)

	    elif "Add all" in msg.text:
		    thisgroup = ale.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    ale.findAndAddContactsByMids(mi_d)
		    ale.sendText(msg.to,"Success Add all")


#==============================================
            elif "Spamcontact @" in msg.text:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam") 
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam") 
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam") 
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam") 
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam") 
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(g.mid,"Spam")
                       ale.sendText(msg.to, "Bwehehehe")
                       print " Spammed !"

#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                ale.sendText(msg.to,"Send Contact")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                ale.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                ale.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                ale.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Already")
                
                

            elif msg.text in ["Auto like"]:
                wait["likeOn"] = True
                ale.sendText(msg.to,"Shere Post Kamu Yang Mau Di Like!")                


            elif msg.text in ["Steal contact"]:
                wait["steal"] = True
                ale.sendText(msg.to,"Send Contact")
                

            elif msg.text in ["Giftbycontact"]:
                wait["gift"] = True
                ale.sendText(msg.to,"Send Contact") 
                

	    elif "Recover" in msg.text:
		thisgroup = ale.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		ale.createGroup("Recover", mi_d)
		ale.sendText(msg.to,"Success recover")



            elif ("Gn: " in msg.text):
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    X.name = msg.text.replace("Gn: ","")
                    ale.updateGroup(X)
                else:
                    ale.sendText(msg.to,"It can't be used besides the group.")

            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
		kicker = [ki,kk,kc]
		if midd not in admin:
		    random.choice(kicker).kickoutFromGroup(msg.to,[midd])
		else:
		    ale.sendText(msg.to,"Admin Detected")

#--------------------------------------------------------
            elif "Invite: " in msg.text:
                midd = msg.text.replace("Invite: ","")
                ale.findAndAddContactsByMid(midd)
                ale.inviteIntoGroup(msg.to,[midd])
#--------------------------------------------------------

            elif "Invite creator" in msg.text:
                midd = "u136360f65010efb7f8dcad362cb2c3cc"
                random.choice(KAC).inviteIntoGroup(msg.to,[midd]) 

            elif msg.text in ["Welcome","welcome","Welkam","welkam","Wc","wc"]:
                gs = ale.getGroup(msg.to)
                ale.sendText(msg.to,"Selamat Datang Di "+ gs.name)
                msg.contentType = 7
                msg.contentMetadata={'STKID': '247',
                                    'STKPKGID': '3',
                                    'STKVER': '100'}
                msg.text = None
                ale.sendMessage(msg)

	    elif "Bc: " in msg.text:
		bc = msg.text.replace("Bc: ","")
		gid = ale.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
			ale.sendText(i,"=======[NUMPANG BROADCAST]=======\n\n"+bc+"\n\nContact Me : line.me/ti/p/~shandiap")
		    ale.sendText(msg.to,"Success BC BosQ")
		else:
		    ale.sendText(msg.to,"Khusus Admin")
	
#--------------------------------------------------------
	    elif msg.text in ["Self Like","Self like"]:
		try:
		    print "activity"
		    url = ale.activity(limit=1)
		    print url
		    ale.like(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], likeType=1001)
		    ale.comment(url['result']['posts'][0]['userInfo']['mid'], url['result']['posts'][0]['postInfo']['postId'], "Auto like by:ALEVAN lb ke #punyaalevan\nhttp://line.me/ti/p/~shandiap")
		    ale.sendText(msg.to, "Success~")
		except Exception as E:
		    try:
			ale.sendText(msg.to,str(E))
		    except:
			pass

#--------------------------------------------------------
                #---------------
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     ale.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     ale.sendText(msg.to,"Command denied.")
                     ale.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"

            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = ale.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ale.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        ale.sendText(msg.to,"No one is inviting")
                else:
                    ale.sendText(msg.to,"Can not be used outside the group")
#--------------------------------------------------------
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = ale.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ale.updateGroup(x)
                    gurl = ale.reissueGroupTicket(msg.to)
                    ale.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ale.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ale.sendText(msg.to,"Not for use less than group")

            elif msg.text in ["timeline"]:
		try:
                    url = ale.activity(limit=5)
		    ale.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E

            elif msg.text in ["!bye"]:
              if wait["Leave"] == True:		    
                    ale.leaveGroup(msg.to)
                    ale.leaveGroup(msg.to)
                    ale.leaveGroup(msg.to)
                    ale.leaveGroup(msg.to)
              else:
		          ale.sendText(msg.to,"Leavenya Belum On")                    

            elif "Profileig " in msg.text:
                    try:
                        instagram = msg.text.replace("Profileig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        ale.sendImageWithURL(msg.to, profileIG)
                        ale.sendText(msg.to, str(text))
                    except Exception as e:
                        ale.sendText(msg.to, str(e))

            elif "!bc " in msg.text:
                bc = msg.text.replace("!bc ","")
                group = ale.getGroup(msg.to)
                gid = ale.getGroupIdsJoined()
                for i in gid:
                    ale.sendText(i,"<==B R O A D C A S T==>\n\n"+bc+"\n\nFromGroup; "+group.name+"\n\nBC by;"+ale.getContact(msg.from_).displayName)


            elif msg.text in ["@bye","@Bye"]:
              if wait["Leave"] == True:	
		    ale.leaveGroup(msg.to)
		    wait["Leave"] = False
              else:
		          ale.sendText(msg.to,"Bilang Dulu Sama Admin Ku")		    
		    

            elif msg.text in ["Absen"]:
		ale.sendText(msg.to,"Pasukan Absen!!")
                ale.sendText(msg.to,"Unity1 Hadiir  \(ˆ▿ˆ)/")
                ale.sendText(msg.to,"Unity2 Hadiir  \(ˆ▿ˆ)/")
                ale.sendText(msg.to,"Unity3 Hadiir  \(ˆ▿ˆ)/")
                ale.sendText(msg.to,"Hadiir Semua Ale  \(ˆ▿ˆ)/")
                
                
            elif msg.text in ["Test","Tes"]:
		ale.sendText(msg.to,"Masuk boss")
                ale.sendText(msg.to,"Masuk Ale")
                ale.sendText(msg.to,"Masuk  \(ˆ▿ˆ)/")
                ale.sendText(msg.to,"Keluar  \(ˆ▿ˆ)/")
                ale.sendText(msg.to,"Apasi luu  \(ˆ▿ˆ)/")


            elif msg.text.lower() in ["respon"]:
                ale.sendText(msg.to,responsename)
                ale.sendText(msg.to,responsename2)
                ale.sendText(msg.to,responsename3)
                ale.sendText(msg.to,responsename4)
                ale.sendText(msg.to,responsename5)

            elif msg.text in ["Spt","Speedt"]:
                start = time.time()
                print("Speed")                
                elapsed_time = time.time() - start
		ale.sendText(msg.to, "Progress...")
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))
                
            elif msg.text in ["Speed","Spd"]:
                start = time.time()
                ale.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                random.choice(KAC).sendText(msg.to, "%sseconds" % (elapsed_time))           

 #           elif msg.text in ["SPeed","SP"]:
 #               start = time.time()
#                ale.sendText(msg.to, "Progress...")
#                elapsed_time = time.time() - start
                #random.choice(KAC).sendText(msg.to,"╔═════════════════════════\n║        ☆☞ ADMIN UNITY  ☆\n╠═════════════════════════"\n╠••>"%sseconds" % (elapsed_time) \n"╚═════════════════════════")

            elif "Nk: " in msg.text:
		if msg.from_ in Creator:
                    X = ale.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ale.updateGroup(X)
                    invsend = 0
                    Ti = ale.reissueGroupTicket(msg.to)
                    ale.acceptGroupInvitationByTicket(msg.to,Ti)
                    G = ale.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    ale.updateGroup(G)

                    nk0 = msg.text.replace("Nk: ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
			    if target not in admin:
                                ale.kickoutFromGroup(msg.to,[target])
                                ale.leaveGroup(msg.to)
                                ale.sendText(msg.to,"Succes BosQ")
                                ale.sendText(msg.to,"Pakyu~")
			    else:
			        ale.sendText(msg.to,"Admin Detected")
		else:
		    ale.sendText(msg.to,"Lu sape!")
 
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    ale.sendText(msg.to,"send contact")

            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    ale.sendText(msg.to,"send contact")
 
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                  if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    gs = ale.getGroup(msg.to)
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
			    if target not in admin:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ale.sendText(msg.to,"Succes BosQ")
                                except:
                                    ale.sendText(msg.to,"Error")
			    else:
				ale.sendText(msg.to,"Admin Detected~")
 
            elif msg.text in ["Banlist","Ban list"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada")
                else:
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +ale.getContact(mi_d).displayName + "\n"
                    random.choice(KAC).sendText(msg.to,"===[Blacklist User]===\n"+mc)

 
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    print "@Unban by mention"
                if msg.from_ in admin:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    gs = ale.getGroup(msg.to)
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                ale.sendText(msg.to,"Succes BosQ")
                            except:
                                ale.sendText(msg.to,"Succes BosQ")
                                
                                
            elif msg.text.lower() == 'clear ban':
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    ale.sendText(msg.to,"ヽ( ^ω^)ﾉ└ ❉Unbanned All Success❉ ┐") 

            elif msg.text.lower() in ["bot","Unity"]:
                ale.sendText(msg.to,"Kenapa manggil-manggil?\nKangen? pc sini:'v") 
                ale.sendText(msg.to,"☆Ketik ☞Help☜ Untuk Bantuan☆") 

 
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        group = ale.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ale.sendText(msg.to,"There was no blacklist user")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        ale.sendText(msg.to,"Blacklist emang pantas tuk di usir")
		else:
		    ale.sendText(msg.to, "Khusus creator")
 
            elif msg.text in ["Kill"]:
                    if msg.toType == 2:
                      if msg.from_ in admin:
                        group = ale.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            ale.sendText(msg.to,"Fuck You")
                            ale.sendText(msg.to,"Fuck You")
                            return
                        for jj in matched_list:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass

 
            elif "Kickall" == msg.text:
		    if msg.from_ in Creator:
                     if msg.toType == 2:
                        print "Kick all member"
                        _name = msg.text.replace("Kickall","")
                        gs = ale.getGroup(msg.to)
                        gs = ale.getGroup(msg.to)
                        gs = ale.getGroup(msg.to)
                        ale.sendText(msg.to,"Sampai jumpaa~")
                        ale.sendText(msg.to,"Dadaaah~")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ale.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
				if target not in admin:
                                    try:
                                        klist=[ki,kk,kc]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except Exception as e:
                                        ale.sendText(msg.to,str(e))
			    ale.inviteIntoGroup(msg.to, targets)
 

	    elif msg.text in ["Bot restart","Reboot"]:
		if msg.from_ in Creator:
		    ale.sendText(msg.to, "Bot Has Been Restarted...")
		    restart_program()
		    print "@Restart"
		else:
		    ale.sendText(msg.to, "No Access")
		    
            elif msg.text in ["Turn off"]: 
	        if msg.from_ in Creator:                
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass 		    


            elif 'Crash' in msg.text:
              if msg.from_ in Creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u136360f65010efb7f8dcad362cb2c3cc"}
                ale.sendMessage(msg)

 
            elif "Ale copy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Ale copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ale.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ale.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ale.CloneContactProfile(target)
                               ale.sendText(msg.to, "Copied (^_^)")
                            except Exception as e:
                                print e

            elif msg.text in ["Backup all"]:
                try:
                    ale.updateDisplayPicture(backup1.pictureStatus)
                    ale.updateProfile(backup1)
                    ale.sendText(msg.to, "All Done (^_^)")
                except Exception as e:
                    ale.sendText(msg.to, str(e))
                    
	    elif "/musik " in msg.text:
					songname = msg.text.replace("/musik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						ale.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						ale.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ale.sendAudioWithURL(msg.to,abc)
						ale.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
	
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ale.sendText(msg.to, hasil)
                except Exception as wak:
                        ale.sendText(msg.to, str(wak))
                        
	    elif "/musrik " in msg.text:
					songname = msg.text.replace("/musrik ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						hasil = 'Lyric Lagu ('
						hasil += song[0]
						hasil += ')\n\n'
						hasil += song[5]
						ale.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ale.sendAudioWithURL(msg.to,abc)
						ale.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4] +"\n\n" + hasil)
						ale.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
             
            
            
            elif "Fancytext: " in msg.text:
                    txt = msg.text.replace("Fancytext: ", "")
                    ale.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"


            elif "cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ale.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ale.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ale.sendText(msg.to,"Upload image failed.")

            elif "Cover @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Cover @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ale.channel.getHome(target)
                                objId = h["result"]["homeInfo"]["objectId"]
                                ale.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/myhome/c/download.nhn?userid=" + target + "&oid=" + objId)
                            except Exception as error:
                                print error
                                ale.sendText(msg.to,"Upload image failed.")
                                
                                
            elif "pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ale.getContact(target)
                                ale.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ale.sendText(msg.to,"Upload image failed.")

            elif "Pp @" in msg.text:
                if msg.toType == 2:
                    cover = msg.text.replace("Pp @","")
                    _nametarget = cover.rstrip('  ')
                    gs = ale.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ale.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                            try:
                                h = ale.getContact(target)
                                ale.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            except Exception as error:
                                print error
                                ale.sendText(msg.to,"Upload image failed.")

            elif "Pap creator" in msg.text:
                tanya = msg.text.replace("Pap creator","")
                link = ["https://i.pinimg.com/736x/4b/50/30/4b5030b3481beaaeaa75164fa9c9c2e3.jpg","https://i.pinimg.com/736x/43/bd/7d/43bd7d03d8b6e3837463f1efa4eff032.jpg","https://images.spot.im/image/upload/f_auto,q_70,fl_lossy,dpr_3,c_limit/v200/291e0f08a158efad957c65c848b21d41","https://i.pinimg.com/736x/39/46/70/3946708f4fdb7a582ae6329159deb949.jpg","https://i.pinimg.com/236x/74/5f/f4/745ff4860a715c428a50d688051a379a.jpg","http://dl.profile.line-cdn.net/0hKDWMzmtEFGtqNDhqhuxrPFZxGgYdGhIjEgYPD0s1H1sSV1JpV1NdBRs9QwhDBlI9UFdZBRs3TwhG","https://i.pinimg.com/736x/f5/92/3a/f5923a99bfd83e0d8f7c0362e649c33a.jpg","https://i.pinimg.com/736x/ea/7b/4d/ea7b4d364c0150060e6b9bca249527b9.jpg","http://dl.profile.line-cdn.net/0hKDWMzmtEFGtqNDhqhuxrPFZxGgYdGhIjEgYPD0s1H1sSV1JpV1NdBRs9QwhDBlI9UFdZBRs3TwhG"]
                pilih = random.choice(link)
                ale.sendImageWithURL(msg.to,pilih)
#----------------------
            elif "Pap cecan" in msg.text:
                tanya = msg.text.replace("Pap cecan","")
                jawab = ("https://i.pinimg.com/736x/fa/b0/de/fab0def5ba3108d51ba40747791bb089.jpg","https://i.pinimg.com/736x/8b/c6/0e/8bc60e8fd6fb5d142a074b6d2cf5c7ed.jpg","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQAa0KQ8XfoVfKRh82Ys63AX3VcuPml1JJFLk7iTEtMpmd7OzbN-yk_MGK6","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPMwr1Igswf8wgrTURHbGAt9jn54SvimA6Ps6W6lCtItkrh4I-kA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRg5SRVDjILsjUyBeLkBnbV96kX22_1mplLyjfCKws6nv8E_VtMDyV07e56bw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOXZ4yFF8R8vPVmEl21Txhvzh4YpUJkJ2uuO3KQLUzYIEVsuT9")
                jawaban = random.choice(jawab)
                ale.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
#----------------------
            elif "Pap cogan" in msg.text:
                tanya = msg.text.replace("Pap cogan","")
                jawab = ("https://i.pinimg.com/736x/41/9b/a5/419ba5606edf61dbab6dfdcc8014624d.jpg","https://i.pinimg.com/736x/38/9c/b1/389cb1203841730a1a8ba322daa7ecb0.jpg","https://i.pinimg.com/736x/76/e3/dc/76e3dc311ddbd61f666083b963910cea.jpg","https://i.pinimg.com/736x/e4/96/67/e496676ca6ea785c8ca5d28f514f9b69.jpg","https://i.pinimg.com/736x/c7/c9/d6/c7c9d6ee5e7d5214d89e3d8bab964497.jpg","https://i.pinimg.com/736x/98/79/5c/98795c07ad9b84ef22e4a6c2cdb135cc.jpg","https://i.pinimg.com/736x/63/fe/b0/63feb07620c1fab54e98ed2139be8aae.jpg","https://i.pinimg.com/736x/66/fc/f2/66fcf2d7d405398f8f163c4ea61aafbf.jpg","https://i.pinimg.com/736x/d9/52/ca/d952caf7b7de45d70f058be2b44e28b3.jpg","https://i.pinimg.com/736x/34/59/c5/3459c5208c819675eff6273210eed009.jpg","https://i.pinimg.com/736x/2a/55/76/2a557666df14a2594f6f3aade212021e.jpg","https://i.pinimg.com/736x/f0/b7/d5/f0b7d5140ec2fb65e58a53bef4506b52.jpg","https://i.pinimg.com/736x/ea/7b/4d/ea7b4d364c0150060e6b9bca249527b9.jpg","https://i.pinimg.com/736x/05/45/a4/0545a45040b9e368726bc134abf78075.jpg","https://i.pinimg.com/736x/f5/92/3a/f5923a99bfd83e0d8f7c0362e649c33a.jpg")
                jawaban = random.choice(jawab)
                ale.sendImageWithURL(msg.to,jawaban)
#----------------------
            elif "Pap abs" in msg.text:
                tanya = msg.text.replace("Pap abs","")
                jawab = ("https://i.pinimg.com/736x/80/1f/e8/801fe86de5b3768ac2994230b1a579e2.jpg","https://i.pinimg.com/736x/a0/e4/89/a0e489d5aeb8cc33c902f49b3b1f8006.jpg","https://i.pinimg.com/736x/91/b0/ee/91b0ee956c46b29f74b0e6d015be3255.jpg","https://i.pinimg.com/736x/f4/92/4d/f4924d75fe3170a73929fa3408592c86.jpg","https://i.pinimg.com/736x/d5/31/ba/d531ba0b7e72056eaedffa54620707e9.jpg","https://i.pinimg.com/736x/51/9b/99/519b9954e1b2ca5f4ab18a4e7c325619.jpg","https://i.pinimg.com/736x/3c/31/8c/3c318cae8e2a5e41ea1ed326737bf12f.jpg","https://i.pinimg.com/736x/87/d3/cb/87d3cb48f2e8eef33a49cd28d971d14b.jpg","https://i.pinimg.com/736x/0d/a3/57/0da357eeeeb9711317f2755a525d07db.jpg","https://i.pinimg.com/736x/09/7a/22/097a2296802dc6535edf1f10d35e64e8.jpg","https://i.pinimg.com/736x/e7/75/cc/e775cc97b9d52777f561daf284ace68b.jpg","https://i.pinimg.com/736x/76/bd/bf/76bdbfa728dcc6dfdd90cb816310af75.jpg","https://i.pinimg.com/736x/49/3a/98/493a988a4872216568844b319f022ac9.jpg","https://i.pinimg.com/736x/f0/f1/cf/f0f1cf3a347dd44c7416ca7baf2da7ed.jpg")
                jawaban = random.choice(jawab)
                ale.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
#----------------------
            elif "Pap toket" in msg.text:
                tanya = msg.text.replace("Pap toket","")
                jawab = ("https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTilO50kExe4q_t-l8Kfn98sxyrHcbWPWCu2GP2SNgg8XWGMaZc8h5zaxAeVA","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKgSYYgB33GP3LAvVSYxKjDlbPokmtzSWjbWJogz8lbZMNSyvqJTE3qWpwBg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgwKO_CAdZpSlXVVfA29qglGQR00WHkeqq4JakyYDuzIW2tKhvGg","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSC3ZMq4PnCX5dj7Fc_N6HOG6R_XrmOM7r6uBtpEcBfbO4hMEXQirK_lU_ePw","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgynJUxS4uYgaIiV_R6e4FY62QfhYRUEgYZg6psfJzWH_ci4dFng")
                jawaban = random.choice(jawab)
                ale.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------#----------------------
            elif "Pap anu" in msg.text:
                tanya = msg.text.replace("Pap anu","")
                jawab = ("https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQFFKdXErF56KzAa4oWnWQT34jmGKJ66lj1g0hnN4zwYh9GgW0dHWZfRnuM","https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQTn4_JMD1ZAg-XIk6JZ1Crhz9gtXEIS8AcjTA3SYmazAutt7ekHw","https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTIVuITo7KicaU6UwPhol1Rvkq4aQwznly8Xl2SiTlAa_1FrSHuwhwV5XoElA")
                jawaban = random.choice(jawab)
                ale.sendImageWithURL(msg.to,jawaban)
#-----------------------------------------------
 
            elif "Spam: " in msg.text:
                  bctxt = msg.text.replace("Spam: ", "")
                  t = 10
                  while(t):
                    random.choice(KAC).sendText(msg.to, (bctxt))
                    t-=1

            elif "Scbc " in msg.text:
                if msg.from_ in admin:
                  bctxt = msg.text.replace("Scbc ", "")
                  orang = ale.getAllContactIds()
                  t = 20
                  for manusia in orang:
                    while(t):
                      ale.sendText(manusia, (bctxt))
                      t-=1

            elif '!ig ' in msg.text.lower():
                try:
                    search = text.lower().replace("!ig ","")
                    r = requests.get("https://Farzain.xyz/api/ig_profile.php?apikey=3zeNkhvkplSALRAnmpk4G5lvHtl1RH&id={}".format(urllib.parse.quote(search))) 
                    data = r.text
                    data = json.loads(data)
                    info = data["info"]
                    hasil = "「 Hasil Instagram」\n"
                    hasil += "\nUsername : {}".format(str(info["username"]))
                    hasil += "\nBio : {}".format(str(info["bio"]))
                    hasil += "\nName : {}".format(str(info["full_name"]))
                    hasil += "\nFollowers : {}".format(str(info["followers"]))
                    hasil += "\nFollowing : {}".format(str(info["following"]))
                    hasil += "\nPost : {}".format(str(info["post"]))
                    ale.sendImageWithURL(msg.to, str(data["profile_pict"]))
                    ale.sendMessage(msg.to, str(hasil))
                except Exception as error:
                    ale.sendMessage(msg.to, "「 Result Error 」\n" + str(error))
                            
                	
            elif "Checkig " in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                ale.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                ale.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)                	


            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ale.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ale.sendText(msg.to,"Could not find it")
                    
#-----------------------------------------------
            if msg.text in ["Raisa"]:
                    try:
                        ale.sendImageWithURL(msg.to, "https://cdn.brilio.net/news/2017/05/10/125611/750xauto-selalu-tampil-cantik-memesona-ini-harga-10-sepatu-raisa-andriana-170510q.jpg")
                    except Exception as e:
                        ale.sendMessage(msg.to, str(e))
                        
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ale.sendMessage(msg)
                profile = ale.getProfile(receiver)
                xname = profile.displayName
                xlen = str(len(xname)+1)
                msg.contentType = 0
                msg.text = "@"+xname+" :)"
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                ale.sendMessage(msg)
#-----------------------------------------------
            elif "kapan " in msg.text:
                tanya = msg.text.replace("kapan ","")
                jawab = ("Besok","Tahun Depan","Minggu Depan","Satu Abad Lagi")
                jawaban = random.choice(jawab)
                ale.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif ".waktu" in msg.text:
	    	       wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	               ale.sendText(msg.to, "         Waktu/Tanggal\n\n" + (wait2['setTime'][msg.to]))
	               ale.sendText(msg.to, "Mungkin Tidak Sesuai Atau Sesuai Dengan Tanggal/Waktu Sekrang Dikarenakan Ini Robot Bukan Manusia :v")
#-----------------------------------------------
#-----------------------------------------------
            elif ".quotes" in msg.text:
                tanya = msg.text.replace(".quotes","")
                jawab = ("Don't cry because it's over, smile because it happened.\nDr. Seuss","I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.\nMarilyn Monroe","Be yourself; everyone else is already taken.\nOscar Wilde","Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.\nAlbert Einstein","Jangan makan, berat\nNanti kamu gendutan:'v","Nggak perlu orang yang sexy maupun rupawan untukku\nCukup kamu yang bisa buat aku bahagia")
                jawaban = random.choice(jawab)
                ale.sendText(msg.to,jawaban)
#----------------------------------------------------------------                  
            elif ".apakah " in msg.text:
                  tanya = msg.text.replace("/apakah ","")
                  jawab = ("ya","tidak","Bisa jadi","mungkin")
                  jawaban = random.choice(jawab)
#-------------------------------------------------
#-----------------------------------------------
            elif msg.text in ["pap","Pap"]:
                        ale.sendImageWithURL(msg.to, "https://i.pinimg.com/736x/d1/93/25/d19325b71789e33bedb054468c1fd134--girls-generation-tiffany-girls-generation.jpg")
            elif msg.text in ["kam"]:
				if msg.from_ in admin:
					ale.sendText(msg.to,"Selamat datang di Group")
					ale.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
#--------------------------------- DUGEM ------------------------------------
            elif ".kedapkedip " in msg.text.lower():
                txt = msg.text.replace(".kedapkedip ", "")
                ale.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#--------------------------------------------------------------------------
            elif "Hay @" in msg.text:
                _name = msg.text.replace("Hay @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")  
                       ale.sendText(g.mid,"Your Account Has Been Spammed !")
                       ale.sendText(msg.to, "Done")
                       print " Spammed !"
#---------------------------- SPAM CHAT -------------------------------------
            elif ".spm " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[1])
                    teks = msg.text.replace(".spm " + str(jmlh) + " ","")
                    if jmlh <= 9999:
                        for x in range(jmlh):
                            ale.sendText(msg.to,teks)
#-------------------------------------------------
            elif '.wiki-id ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(".wiki-id ","")
                      wikipedia.set_lang("id")
                      wiki = WikiApi({'locale':'id'})
                      results = wiale.find("search")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ale.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Text Nya Kepanjagan Klik Link Ini Saja\n"
                              pesan+=wikipedia.page(wiki).url
                              ale.sendText(msg.to, pesan)
                          except Exception as e:
                              ale.sendText(msg.to, str(e))                             
 #-------------------------------------------------
            elif '.wiki-en ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace(".wiki-en ","")
                      wikipedia.set_lang("en")
                      wiki = WikiApi({'locale':'en'})
                      results = wiale.find("search")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ale.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              ale.sendText(msg.to, pesan)
                          except Exception as e:
                              ale.sendText(msg.to, str(e))
#-----------------------------------------------
#---------------------------------- SONG ------------------------------------
#--------------------------------- YOUTUBE ----------------------------------
            elif "Youtubevideo: " in msg.text:
                query = msg.text.replace("Youtubevideo: ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    ale.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
#----------------------------------------------------------------------------
#-----------------------------------------------------
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      ale.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              ale.sendText(msg.to, pesan)
                          except Exception as e:
                              ale.sendText(msg.to, str(e))

 
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say-su " in msg.text:
                say = msg.text.replace("Say-su ","")
                lang = 'su'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jw " in msg.text:
                say = msg.text.replace("Say-jw ","")
                lang = 'jw'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = ale.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")
                

            elif msg.text.lower() in ["hi","hai","halo","hallo"]:
                    beb = "Hi Sayang 😘 " +ale.getContact(msg.from_).displayName + " 􀸂􀆇starry heart􏿿"
                    ale.sendText(msg.to,beb)



            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                ale.sendText(msg.to,"Sedang Mencari...")
                ale.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLink : https://play.google.com/store/search?q=" + tob)
                ale.sendText(msg.to,"Tuh Linknya Kak (^_^)")


            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass


            elif "!bio " in msg.text:
               if msg.from_ in Creator:
                    string = msg.text.replace("!bio ","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = ale.getProfile()
                        profile.statusMessage = string
                        ale.updateProfile(profile)
                        ale.updateProfile(profile)
                        ale.updateProfile(profile)
                        ale.updateProfile(profile)
                        ale.updateProfile(profile)
                        ale.sendText(msg.to,"All Done")

            elif "/cnAle" in msg.text:
		if msg.from_ in Creator:
                    string = msg.text.replace("/cnAle","Ganti Ale")
                    if len(string.decode('utf-8')) <= 5000:
                        profile = ale.getProfile()
                        profile.displayName = string
                        ale.updateProfile(profile)
                        ale.sendText(msg.to,"Done")

            elif "Ulti " in msg.text:
              if msg.from_ in Creator:
                ulti0 = msg.text.replace("Ulti ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = ale.getGroup(msg.to)
                ginfo = ale.getGroup(msg.to)
                gs.preventJoinByTicket = False
                ale.updateGroup(gs)
                invsend = 0
                Ticket = ale.reissueGroupTicket(msg.to)
                ale.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        ale.kickoutFromGroup(msg.to,[target])
                                        ale.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        ale.sendText(msg.t,"Ter ELIMINASI....")
                                        ale.sendText(msg.to,"WOLES brooo....!!!")
                                        ale.leaveGroup(msg.to)
                                        gs = ale.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        ale.updateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        ale.updateGroup(gs)


            elif msg.text.lower() in ["Mymid","myid"]:
                middd = "Name : " +ale.getContact(msg.from_).displayName + "\nMid : " +msg.from_
                ale.sendText(msg.to,middd)

            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ale.sendMessage(msg)

            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")                


            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ale.sendAudio(msg.to,"hasil.mp3")

 
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ale.sendText(msg.to," Simisimi Di Aktifkan")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ale.sendText(msg.to,"Simisimi Di Nonaktifkan")

 
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ale.sendImageWithURL(msg.to,path)
                except:
                    pass
 
            elif "Youtubesearch: " in msg.text:
                    query = msg.text.replace("Youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html.parser')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        ale.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'

#-------------------------------------------------------
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ale.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ale.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                ale.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                ale.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                ale.sendText(msg.to, A)
            
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                ale.sendText(msg.to,str(trans))
            elif "Tr-th " in msg.text:
                nk0 = msg.text.replace("Tr-th ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'th')
                ale.sendText(msg.to,str(trans))
            elif "Tr-ja " in msg.text:
                nk0 = msg.text.replace("Tr-ja ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ja')
                ale.sendText(msg.to,str(trans))
            elif "Tr-en " in msg.text:
                nk0 = msg.text.replace("Tr-en ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'en')
                ale.sendText(msg.to,str(trans))
            elif "Tr-ar " in msg.text:
                nk0 = msg.text.replace("Tr-ar ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ar')
                ale.sendText(msg.to,str(trans))
            elif "Tr-ko " in msg.text:
                nk0 = msg.text.replace("Tr-ko ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ko')
                ale.sendText(msg.to,str(trans))
            elif "Tr-es " in msg.text:
                nk0 = msg.text.replace("Tr-es ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'es')
                ale.sendText(msg.to,str(trans))
            elif "Tr-fr " in msg.text:
                nk0 = msg.text.replace("Tr-fr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'fr')
                ale.sendText(msg.to,str(trans))
            elif "Tr-jw " in msg.text:
                nk0 = msg.text.replace("Tr-jw ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'jw')
                ale.sendText(msg.to,str(trans))
            elif "Tr-it " in msg.text:
                nk0 = msg.text.replace("Tr-it ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'it')
                ale.sendText(msg.to,str(trans))
            elif "Tr-de " in msg.text:
                nk0 = msg.text.replace("Tr-de ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'de')
                ale.sendText(msg.to,str(trans))
            elif "Tr-ru " in msg.text:
                nk0 = msg.text.replace("Tr-ru ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ru')
                ale.sendText(msg.to,str(trans))
            elif "Tr-tr " in msg.text:
                nk0 = msg.text.replace("Tr-tr ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'tr')
                ale.sendText(msg.to,str(trans))
            elif "Tr-hi " in msg.text:
                nk0 = msg.text.replace("Tr-hi ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'hi')
                ale.sendText(msg.to,str(trans))
            elif "Tr-vi " in msg.text:
                nk0 = msg.text.replace("Tr-vi ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'vi')
                ale.sendText(msg.to,str(trans))
            elif "Tr-ms " in msg.text:
                nk0 = msg.text.replace("Tr-ms ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'ms')
                ale.sendText(msg.to,str(trans))
            elif "Tr-la " in msg.text:
                nk0 = msg.text.replace("Tr-la ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'la')
                ale.sendText(msg.to,str(trans))
            elif "Tr-id " in msg.text:
                nk0 = msg.text.replace("Tr-id ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name, 'id')
                ale.sendText(msg.to,str(trans))
            elif "Tr-su " in msg.text:
                nk0 = msg.text.replace("Tr-su ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name,'su')
                ale.sendText(msg.to,str(trans))
            elif "Tr-zh " in msg.text:
                nk0 = msg.text.replace("Tr-zh ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name,'zh')
                ale.sendText(msg.to,str(trans))
				
            elif "Tr-af " in msg.text:
                nk0 = msg.text.replace("Tr-af ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("","")
                nk3 = nk2.rstrip()
                _name = nk3
                trans = translate(_name,'af')
                ale.sendText(msg.to,str(trans))         

            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)


            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)

            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Korea----\n" + "" + result)

            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Korea----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)

            elif "Id@su" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'su'
                kata = msg.text.replace("Id@su ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Sunda----\n" + "" + result)
                
            elif "Su@id" in msg.text:
                bahasa_awal = 'su'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Su@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Sunda----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)

            elif "Id@jw" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'jw'
                kata = msg.text.replace("Id@jw ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Jawa----\n" + "" + result)

            elif "Jw@id" in msg.text:
                bahasa_awal = 'jw'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jw@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----DarJawa----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
            
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Thailand----\n" + "" + result)
                
            
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----Dari Thailand----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)                
               
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ale.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
 
            elif msg.text in ["Friendlist"]:    
                contactlist = ale.getAllContactIds()
                kontak = ale.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                ale.sendText(msg.to, msgs)

            elif msg.text in ["Memlist"]:   
                kontak = ale.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═�����═══════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                ale.sendText(msg.to, msgs)

#-----------------------------------------------
            elif "love " in msg.text:
                tanya = msg.text.replace("love ","")
                jawab = ("10%\nCoba lah untuk melupakan","20%\nKu tak tau lagi:'","30%\nButuh perjuangan yang berat inih","40%\nCobalah saling mencimtai dengan tulus\nIngatlah kenangan indah kalian","50%\nSegeralah mengerti satu sama lain","60%\nLebih perhatian lagi oke","70%\nAyo sedikit lagi","80%\nWahhh, ada kemungkinan kalian jodoh","90%\nAyo sedikit lgi kak","100%\nKeterangan Moga - Moga Langgeng Ya Kak","0%\nKeterangan Ngak Cinta Sama Sekali :v")
                jawaban = random.choice(jawab)
                ale.sendText(msg.to,jawaban)
#-----------------------------------------------
            elif msg.text in ["Ajg","Bgst","Bacot","Tai","Bazeng","Anjir","Fck","Fuck","Najiz","Bego","Najis"]:
#              if msg.from_ in admin:
                ale.sendText(msg.to,"Hayo jangan ngomong kasar kak")
                ale.sendText(msg.to,"Acu kik nih.gg")

#==============================================
            elif "Spamtag @" in msg.text:
#              if msg.from_ in admin:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = ale.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                        ale.sendMessage(msg)
                    else:
                        pass

#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   ale.sendText(msg.to, teks)
                        else:
                               ale.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               ale.sendText(msg.to, tulisan)
                         else:
                               ale.sendText(msg.to, "Out of range! ")
#-------------------------------------------------------------------#
            elif msg.text in ["Up"," up"]:
#              if msg.from_ in admin:
                ale.sendText(msg.to,"Ha? ada apa nih")
                ale.sendText(msg.to,"Di up in bos")
                ale.sendText(msg.to,"Butuh balon udara nggak?")
                ale.sendText(msg.to,"Buat di up in nih")
                ale.sendText(msg.to,"Gausah lah ya")
                ale.sendText(msg.to,"Up atuh")
                ale.sendText(msg.to,"Panjat bos")
                ale.sendText(msg.to,"Jangan panjat sosyal aja")
                ale.sendText(msg.to,"Panjat panjat pohon")
                ale.sendText(msg.to,"yiha")
                ale.sendText(msg.to,"Pohon aja di panjat")
                ale.sendText(msg.to,"Apalagi kamu.gg unch")
                ale.sendText(msg.to,"Maaf, harus kita up in")
                ale.sendText(msg.to,"Demi kebaikan bersama sayang")
                ale.sendText(msg.to,"Iya sayang")
                ale.sendText(msg.to,"Opo koe krungu?")
                ale.sendText(msg.to,"Jerite atiku")
                ale.sendText(msg.to,"Oaoee..")
                ale.sendText(msg.to,"Males lanjutin ah")
                ale.sendText(msg.to,"Sepi bat")
                ale.sendText(msg.to,"Iya sepi udah udah")
                ale.sendText(msg.to,"Gaada yang denger juga")
                ale.sendText(msg.to,"Yaiyalah, ini kan ketik ogeb")
                ale.sendText(msg.to,"Mending gua nyari BBG dulu")
                ale.sendText(msg.to,"Sono huss")
                ale.sendText(msg.to,"Up unch")
                ale.sendText(msg.to,"Up in dulu bos")
                ale.sendText(msg.to,"Ada apa nih")
                ale.sendText(msg.to,"Up atuh")
                ale.sendText(msg.to,"Maaf di up bos")

            elif msg.text in ["Spam"]:
#              if msg.from_ in admin:
                ale.sendText(msg.to,"Aku belum mandi")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Tapi masih cantik juga")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"apalagi kalau sudah mandi")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Pasti cantik sekali")
                ale.sendText(msg.to,"yiha")
                ale.sendText(msg.to,"Kalau orang lain melihatku")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Badak aku taba bana")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Tak tuntuang")
                ale.sendText(msg.to,"Tapi kalau langsuang diidu")
                ale.sendText(msg.to,"Tak tun tuang")
                ale.sendText(msg.to,"Atagfirullah baunya")
                ale.sendText(msg.to,"Males lanjutin ah")
                ale.sendText(msg.to,"Sepi bat")
                ale.sendText(msg.to,"Iya sepi udah udah")
                ale.sendText(msg.to,"Gaada yang denger juga kita nyanyi")
                ale.sendText(msg.to,"Nah")
                ale.sendText(msg.to,"Mending gua makan dulu")
                ale.sendText(msg.to,"Siyap")
                ale.sendText(msg.to,"Okeh")
                ale.sendText(msg.to,"Katanya owner kita Jomblo ya")
                ale.sendText(msg.to,"Iya emang")
                ale.sendText(msg.to,"Denger denger si lagi nyari pacar doi")
                ale.sendText(msg.to,"Udah ah gosip mulu doain aja biar dapet")
 
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = ale.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    ale.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = ale.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            ale.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"


            elif "Getgroup image" in msg.text:
                group = ale.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ale.sendImageWithURL(msg.to,path)

            elif "Urlgroup image" in msg.text:
                group = ale.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                ale.sendText(msg.to,path)
 
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ale.getContact(key1)
                cu = ale.channel.getCover(key1)
                try:
                    ale.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    ale.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)


            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ale.getContact(key1)
                cu = ale.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    ale.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    ale.sendText(msg.to,"Profile Picture " + contact.displayName)
                    ale.sendImageWithURL(msg.to,image)
                    ale.sendText(msg.to,"Cover " + contact.displayName)
                    ale.sendImageWithURL(msg.to,path)
                except:
                    pass


            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = ale.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                ale.sendMessage(msg)

            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ale.getContact(key1)
                cu = ale.channel.getCover(key1)
                try:
                    ale.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    ale.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
                  
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                ale.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass


            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = ale.getContact(key1)
                cu = ale.channel.getCover(key1)
                try:
                    ale.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    ale.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)


            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "║「вσт яυииιиg "+waktu(eltime)
                ale.sendText(msg.to,"╔═════════════════\n║ ☆☞ UNITY RUNTIME ☆\n╠════════════════\n" + van + "\n╚════════════════")
                
                 
            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                ale.sendText(msg.to,"========== I N F O R M A S I ==========\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n========== I N F O R M A S I ==========")
                
   
            elif msg.text in ["Kalender","Time","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                ale.sendText(msg.to, rst)                
                 
                
            elif "Idline: " in msg.text:
                userid = msg.text.replace("Idline: ","")
                contact = ale.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ale.sendMessage(msg)
                
            elif "Idline " in msg.text:
                userid = msg.text.replace("Idline ","")
                contact = ale.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ale.sendMessage(msg)       
                
                
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ale.removeAllMessages(op.param2)
                        ale.removeAllMessages(op.param2)
                        ale.removeAllMessages(op.param2)
                        ale.removeAllMessages(op.param2)
                        ale.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ale.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        ale.sendText(msg.to,"Error")      
                        
                        
            elif "Invitemeto: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Invitemeto: ","")
                    if gid == "":
                        ale.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            ale.findAndAddContactsByMid(msg.from_)
                            ale.findAndAddContactsByMid(msg.from_)
                            ale.findAndAddContactsByMid(msg.from_)
                            ale.findAndAddContactsByMid(msg.from_)
                            ale.findAndAddContactsByMid(msg.from_)
                            random.choice(KAC).inviteIntoGroup(gid,[msg.from_])
                        except:
                            ale.sendText(msg.to,"Mungkin Saya Tidak Di Dalaam Grup Itu")


            elif msg.text in ["Glist"]:
                ale.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = ale.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠✒ " + "%s\n" % (ale.getGroup(i).name +" ~> ["+str(len(ale.getGroup(i).members))+"]")
                ale.sendText(msg.to,"╔══════════════════════\n║      ☆☞ LIST GROUPS☜☆\n╠══════════════════════\n" + h + "╠═════════���═════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚══════════════════════")

            elif msg.text in ["Glistmid"]:   
                gruplist = ale.getGroupIdsJoined()
                kontak = ale.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                ale.sendText(msg.to, msgs)



            elif "Google: " in msg.text:
                    a = msg.text.replace("Google: ","")
                    b = urllib.quote(a)
                    ale.sendText(msg.to,"Sedang Mencari...")
                    ale.sendText(msg.to, "https://www.google.com/" + b)
                    ale.sendText(msg.to,"Itu Dia Linknya. . .")     


            elif "Details group: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Details group: ","")
                    if gid in [""," "]:
                        ale.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = ale.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            ale.sendText(msg.to,h)
                        except Exception as error:
                            ale.sendText(msg.to,(error))
            
            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = ale.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                ale.rejectGroupInvitation(i)
                            except:
                                ale.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        ale.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        ale.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Ale acc invite"]:
                if msg.from_ in admin:
                    gid = ale.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = ale.getGroup(i)
                            _list += gids.name
                            ale.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        ale.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        ale.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")  

            elif "Gif gore" in msg.text:
            	gif = ("https://media.giphy.com/media/l2JHVsQiOZrNMGzYs/giphy.gif","https://media.giphy.com/media/OgltQ2hbilzJS/200w.gif")
                gore = random.choice(gif)
                ale.sendGifWithURL(msg.to,gore)


        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = ale.fetchOps(ale.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ale.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ale.Poll.rev = max(ale.Poll.rev, Op.revision)
            bot(Op)

