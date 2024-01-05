# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:06:36 2023

@author: ASUS
"""
from abc import ABC, abstractmethod
from login import login


class Person(ABC): #ABSTRACT CLASS
    
    def __init__(self,name,surname,tc,phone,address):
        self.name=name
        self.surname=surname
        self.tc=tc
        self.phone=phone
        self.address=address
        
        
class Customer(Person): #INHERITANCE
    
    def __init__(self,name,surname,tc,phone,address):
        Person.__init__(self,name,surname,tc,phone,address)


class User(Person,login): #MULTIPLE INHERITANCE
    
    ulist=[]    # user sınıfına ait tüm örnekleri tutacak liste
    
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        self.ssn=ssn
        Person.__init__(self,name,surname,tc,phone,address)
        login.__init__(self,username,password,typex)
        

class Admin(User):
    
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        User.__init__(self,name,surname,tc,phone,address,ssn,username,password,typex)

    
    def add_OfficeWorker(self):
        name1=input("isim bilgisi giriniz:")
        surname1=input("soyisim bilgisi giriniz:")
        tc1=input("tc bilgisi giriniz:")
        phone1=input("telefon bilgisi giriniz:")
        address1=input("adres bilgisi giriniz:")
        ssn1=input("ssn bilgisi giriniz:")
        username1=input("username bilgisi giriniz:")
        password1=input("password bilgisi giriniz:")
        typex1=1
        ow = OfficeWorker(name1,surname1,tc1,phone1,address1,ssn1,username1,password1,typex1)
        print(ow)
        
        return ow
    
    def add_Carrier(self):
        # Kullanıcıdan temel kullanıcı bilgilerini al
        name2 = input("İsim: ")
        surname2 = input("Soyisim: ")
        tc2 = input("TC: ")
        phone2 = input("Telefon: ")
        address2 = input("Adres: ")
        ssn2= input("SSN: ")
        username2 = input("Kullanıcı Adı: ")
        password2 = input("Şifre: ")
        typex2=2

        # Kullanıcıdan taşıyıcı (Carrier) özelliklerini al
        carrier_name = input("Taşıyıcı Adı: ")
        capacity = input("Kapasite: ")

        # Carrier sınıfından bir örnek oluştur
        crr = Carrier(name2, surname2, tc2, phone2, address2, ssn2, username2, password2, typex2, carrier_name, capacity)

        # Oluşturulan taşıyıcı örneğini ekrana yazdır
        print(crr)

        # Taşıyıcı örneğini User sınıfına ait ulist listesine ekle
        self.ulist.append(crr)

        return crr
        
    def print_OfficeWorker(self,userlist):
        ow_users = [x for x in userlist if (x.typex == 1 )]
        for usr in ow_users:
            print(usr.name+" "+usr.surname)
            ##istediğiniz başka bilgileri de printe ekleyebilirsiniz...

    def print_Carrier(self):
        pass
        #BU METHOD SİZİN ÖDEVİNİZ  
        
    def delete_OfficeWorker(self,userlist,tc1):
        ow_user = [x for x in userlist if (int(x.tc) == int(tc1) )]
        userlist.remove(ow_user[0])
        
        
    def delete_Carrier(self,userList,phone2):
        crr_user = [ x for x in userList if (int(x.phone) == int(phone2) )]
        userList.remove(crr_user[0])
          
   
    
    
class OfficeWorker(User):
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        User.__init__(self,name,surname,tc,phone,address,ssn,username,password,typex)

   
    
class Carrier(User):
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        User.__init__(self,name,surname,tc,phone,address,ssn,username,password,typex)

    def update_Status():
        pass
        #BU METHOD SİZİN ÖDEVİNİZ   
   
    
class shipment():
    
    def __init__(self,status,weight,s_add,d_add,name,surname,tc,phone,name1,surname1,tc1,phone1):
        self.status=status
        self.weight=weight
        self.s_add = s_add
        self.d_add = d_add
        self.distance = self.calc_distance(s_add,d_add)
        self.cost = self.calc_cost(self.distance,self.weight)
        self.customer = Customer(name,surname,tc,phone,s_add)
        self.receiver = Customer(name1,surname1,tc1,phone1,d_add)
    def create_shipment(self):
        status="Kabul edildi"
        weight=input("shipment kaç kg")
        s_add=input("gönderici adresi")
        d_add=input("alici adresi")
        name=input("gönderici adı")
        surname=input("gönderici soyadı")
        tc=input("gönderici tc")
        phone=input("gönderici telefon")
        name1=input("alıcı adı")
        surname1=input("alıcı soyadı")
        tc1=input("alıcı tc")
        phone1=input("alıcı telefon")
        shpmnt = shipment(status,weight,s_add,d_add,name,surname,tc,phone,name1,surname1,tc1,phone1)
        print(shpmnt)
        
        return shpmnt
    
    def print_shipment(self,shipmentlist,tc2):
        shpmnts = [x for x in shipmentlist if (int(x.customer.tc) == int(tc2) )]
        for shp in shpmnts:
            print(shp.status+" "+shp.s_add)
            ##istediğiniz başka bilgileri de printe ekleyebilirsiniz...
            
    def print_shipment(self):
        pass
        #BU METHOD SİZİN ÖDEVİNİZ 
        
    
    @staticmethod
    def calc_distance(s1,s2):
        m, n = len(s1), len(s2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]  
        for i in range(m+1):  
            dp[i][0] = i  
        for j in range(n+1):  
            dp[0][j] = j  
        for i in range(1, m+1):  
            for j in range(1, n+1):  
                if s1[i-1] == s2[j-1]:  
                    dp[i][j] = dp[i-1][j-1]  
                else:  
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)  
        return dp[m][n]
    
    @staticmethod
    def calc_cost(d,w):
        return d*w*10
    
    
    
#        
#CLASSLARI ÇALIŞTIRDIKTAN SONRA KOD BURDAN BAŞLIYOR...
#
#
#
#Önemli Not: Zamanımız kalmadığı için int string kontrolleri yapamadık.
#Siz run yaparken int gerekli değişkenlere int girin
#string gerekli olanlara string
#aksi halde kod patlar. ÇÜNKÜ kontrolleri yapacak kadar zamanımız yoktu arkadaşlar
#
#
#Bunun amacı aslında OOP kurallarını kavramaktı. 
#Diğer kontrol ve eksikleri isterseniz siz tamamlarsınız
#
#
#Sınavlarda Başarılar
#Mutlu, Sağlıklı, Huzurlu Yıllar.. <3
#



#ADMİN, OFFİCEWORKER VE CARRİERLARI TUTACAK LİSTE
userlist=[]

#SHİPMENTLARI TUTACAK LİSTE
shipmentlist=[]

adm = Admin("Erto", "Pancar", 123, 456, "Adiyaman", 1, "admin", 123, 0)
userlist.append(adm)


def admin_menu(loggeduser):
    while True:
        print("1 - officeworker ekle")
        print("2 - carrier ekle")
        print("3 - officeworker listele")
        print("4 - carrier listele")
        print("5 - officeworker SİL")
        print("6 - carrier SİL")
        print("7 - Çıkış")
        selection = input("seçiminizi giriniz")
        selection = int(selection)
        print(selection)
        if(selection == 1):
            
            inserted = loggeduser[0].add_OfficeWorker()
            userlist.append(inserted)
        if(selection == 2):
            loggeduser[0].add_Carrier()
        if(selection == 3):
            loggeduser[0].print_OfficeWorker(userlist)
        if(selection == 4):
            loggeduser[0].print_Carrier()
        if(selection == 5):
            tc1=input("silinecek tc giriniz")
            loggeduser[0].delete_OfficeWorker(userlist, tc1)
        if(selection == 6):
            tc1=input("silinecek tc giriniz")
            loggeduser[0].delete_Carrier(userlist, tc1)
        if(selection == 7):
            break
        
def ow_menu(loggeduser):
    while True:
        print("1 - shipment olustur")
        print("2 - shipment goster")
        print("7 - Çıkış")
        selection = input("seçiminizi giriniz")
        selection = int(selection)
        print(selection)
        if(selection == 1):
            
            inserted = loggeduser[0].create_shipment()
            shipmentlist.append(inserted)
        if(selection == 2):
            tc2=input("shipment gönderici tc giriniz")
            loggeduser[0].print_shipment(shipmentlist,tc2)
        
        if(selection == 7):
            break
        

#BU KISMI ÇALIŞTIRMADAN ÖNCE ÜSTTEKİ 2 METHODU RUN ETMEYİ UNUTMAYIN...
#VE siz carrier_menu() yazdıktan sonra da onu çalıştırmanız gerekecek...
while True:
    
    print("Please Login")
    uname = input("Enter your username")
    passw = input("Enter your password")
    
    loggeduser = [x for x in userlist if (x.username == uname and int(x.password) == int(passw) )]
    #DERSTE BURDA TAKILDIĞIMIZ KISIM ŞUYMUŞ:
    #LOGGEDUSER GİRİLEN İF KOŞULUNA BİRDEN FAZLA NESNEYİ TUTUYOR OLABİLİR. 
    #BU SEBEPLE LOGGEDUSER[0] OLARAK İLK ELEMANI ALIYORUZ.
    #BURDA DİKKAT EDİN EĞER İF İÇİNDE EĞER BİRDEN FAZLA VERİYİ DÖNDERECEK Bİ KOŞUL YAZARSAK 
    #DÖNGÜ İLE HEPSİNE ERİŞEBİLİRİZ 
    #AMA BİZ USERNAME VE PASSWORD'UN TEK BİR KİŞİYE ÖZEL OLDUĞUNU VARSAYDIK
    #SİZ SİSTEMİ DENERKEN FARKLI KİŞİLERE AYNI USERNAME VE PASSWORD VERMEYİN VEYA  
    #GEREKLİ KONTROLLERİ SAĞLAYIN.
    
    if(len(loggeduser)==0):
        print("login failed! Try again..")
    else:
        if(loggeduser[0].typex == 0):
            print("Hello Admin!")
            admin_menu(loggeduser)
        if(loggeduser[0].typex == 1):
            print("Hello "+ loggeduser[0].name)
            ow_menu(loggeduser)
        if(loggeduser[0].typex == 2):
            print("Hello "+ loggeduser[0].name)
            #carrier_menu(loggeduser)
            #BU METHOD SİZİN ÖDEVİNİZ..
        




    








