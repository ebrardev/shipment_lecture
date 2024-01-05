from abc import ABC, abstractmethod
from login import login


class Person(ABC): #ABSTRACT CLASS
    
    def __init__(self,name,surname,tc,phone,address):
        self.name=name
        self.surname=surname
        self.tc=tc
        self.phone=phone
        self.address=address
        
     
class User(Person,login): #MULTIPLE INHERITANCE
    
    ulist=[]    # user sınıfına ait tüm örnekleri tutacak liste
    
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        self.ssn=ssn
        Person.__init__(self,name,surname,tc,phone,address)
        login.__init__(self,username,password,typex)

         # office worker class
class OfficeWorker(User):
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        User.__init__(self,name,surname,tc,phone,address,ssn,username,password,typex)

   
class Admin(User):
    
    def __init__(self,name,surname,tc,phone,address,ssn,username,password,typex):
        User.__init__(self,name,surname,tc,phone,address,ssn,username,password,typex)

    # add office worker
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
        self.ulist.append(ow)
        return ow
    # print office worker
    def print_OfficeWorker(self,ulist):
        ow_users = [x for x in ulist if (x.typex == 1 )]
        for usr in ow_users:
            print(usr.name+" "+usr.surname)
            ##istediğiniz başka bilgileri de printe ekleyebilirsiniz...

            # delete office worker
    def delete_OfficeWorker(self,userlist,tc1):
        ow_user = [x for x in userlist if (int(x.tc) == int(tc1) )]
        userlist.remove(ow_user[0])
        
admin = Admin("Admin", "Surname", "123456789", "555-1234", "Address", "123456", "admin_user", "admin_pass", "admin_typex")
admin.add_OfficeWorker()
admin.print_OfficeWorker(admin.ulist) 
