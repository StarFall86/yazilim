import os
import sys
import time
import mechanize
import getpass

twitter_tweet__sender_bot_ico = """
#############################################################
#    PYTHON - Twetter Tweet Sender Bot - GH0ST S0FTWARE     #
############################################################# 
#                      ######################################
""";

print twitter_tweet__sender_bot_ico

time.sleep(5)

os.system('cls' if http://os.name == 'nt' else 'clear')

star = "#############################################################"

twitter_terminal_login_panel_ico = """
#############################################################
#                Twitter Terminal Login Panel               #
#############################################################
"""

print twitter_terminal_login_panel_ico

def twitter_tweet__sender_bot():
twitter_kullanici_adi_veya_eposta = raw_input("Twitter kullanıcı adı veya eposta adresinizi giriniz : ")
twitter_sifre = getpass.getpass("Twitter şifrenizi giriniz : ")
print star 
site_url = "https://mobile.twitter.com/session/new"
tarayici = mechanize.Browser()
http://tarayici.open(site_url)
http://tarayici.select_form(nr=0)
tarayici["session[username_or_email]"] = twitter_kullanici_adi_veya_eposta
tarayici["session[password]"] = twitter_sifre
tarayici.submit()
twitter_tweet_mesaj = raw_input("Göndereceğiniz tweetinizi giriniz : ")
twitter_tweet_url_adresi = http://tarayici.open("https://mobile.twitter.com/account").read()
tweet_url = "https://mobile.twitter.com/compose/tweet"
http://tarayici.open(tweet_url)
http://tarayici.select_form(nr=0)
tarayici["tweet[text]"] = 
m=1
n=5 
while m&lt;n:

        twitter_tweet_mesaj
        tarayici.submit()
                    gonderilen_mesaj_onayi_ico = """
#############################################################
#                   Twettiniz Gönderildi :)                 #
#############################################################
"""
print gonderilen_mesaj_onayi_ico

islemler_ico = """
(1) Twitter Tweet Gönderici
(2) Bilgi
(3) İletişim
(4) Çıkış
"""

print islemler_ico

print star

islem = input("Yapılacak işlem numarasını giriniz : ")

print star

if islem == 1:
twitter_tweet__sender_bot()

elif islem == 2:
info_ico = """
Linux işletim sistemleri için geliştirilmiş ve python dili 
ile yazılmışdır. Linux Terminali üzerinden Twitter'a giriş 
yaptıktan sonra tweet atmamızı sağlayan bir bot yazılımıdır.
""" 
print info_ico

elif islem == 3:
contact_ico = """
############################################################# 
#                      
#############################################################
"""
print contact_ico

elif islem == 4:
sys.exit()
print star
