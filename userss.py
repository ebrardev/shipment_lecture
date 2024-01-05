from abc import ABC, abstractmethod
from login import login


class Person(ABC): #ABSTRACT CLASS
    
    def __init__(self,name,surname,tc,phone,address):
        self.name=name
        self.surname=surname
        self.tc=tc
        self.phone=phone
        self.address=address
        
        
person1=Person("ali","veli","123456789","123456789","123456789")


# print(person1.surname)

        
class Customer(Person): #INHERITANCE
    
    def __init__(self,name,surname,tc,phone,address):
        Person.__init__(self,name,surname,tc,phone,address)

customer1 = Customer("ali","bla","123456789","123456789","123456789")
# print(customer1.surname,customer1.name)

# user klası
class User(Person, login):
    ulist = []  # user sınıfına ait tüm örnekleri tutacak liste

    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex):
        self.ssn = ssn
        Person.__init__(self, name, surname, tc, phone, address)
        login.__init__(self, username, password, typex)
        
        # Oluşturulan User örneklerini ulist listesine ekleyelim
        self.ulist.append(self)

# User sınıfından örnekler oluşturalım
user1 = User("ali", "bla", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789")
user2 = User("ali", "bla", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789")
user3 = User("ali", "bla", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789", "123456789")

# ulist içindeki değerleri yazdıralımebr
# for user in User.ulist:
#     print(f"Name: {user.name}, Surname: {user.surname}, SSN: {user.ssn}, Username: {user.username}, Password: {user.password}")
#tek kullanıcı yazdırma
# if User.ulist:
#     first_user = User.ulist[0]
#     print(f"Name: {first_user.name}, Surname: {first_user.surname}, SSN: {first_user.ssn}, Username: {first_user.username}, Password: {first_user.password}")

# kurye sınıfı

class Carrier(User):
    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex, carrier_name, capacity):
        super().__init__(name, surname, tc, phone, address, ssn, username, password, typex)
        self.carrier_name = carrier_name
        self.capacity = capacity

# admin sınıfı
class Admin(User):
    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex):
        super().__init__(name, surname, tc, phone, address, ssn, username, password, typex)

    def add_OfficeWorker(self):
        name1 = input("İsim bilgisi giriniz: ")
        surname1 = input("Soyisim bilgisi giriniz: ")
        tc1 = input("TC bilgisi giriniz: ")
        phone1 = input("Telefon bilgisi giriniz: ")
        address1 = input("Adres bilgisi giriniz: ")
        ssn1 = input("SSN bilgisi giriniz: ")
        username1 = input("Kullanıcı adı bilgisi giriniz: ")
        password1 = input("Şifre bilgisi giriniz: ")
        typex1 = input("Typex bilgisi giriniz: ")
        ow = OfficeWorker(name1, surname1, tc1, phone1, address1, ssn1, username1, password1, typex1)
        print(ow)
        return ow

    def add_Carrier(self):
        name = input("İsim: ")
        surname = input("Soyisim: ")
        tc = input("TC: ")
        phone = input("Telefon: ")
        address = input("Adres: ")
        ssn = input("SSN: ")
        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")
        typex2= 2
        
        carrier_name = input("Taşıyıcı Adı: ")
        capacity = input("Kapasite: ")

        crr = Carrier(name, surname, tc, phone, address, ssn, username, password, typex2, carrier_name, capacity)
        print(crr)
        self.ulist.append(crr)
        return crr
    
    # kurye yazdırma
    def print_Carrier(self,userlist):
        crr_users = [x for x in userlist if (x.typex == 2 )]
        for usr in crr_users:
            print(usr.name+" "+usr.surname)
            ##istediğiniz başka bilgileri de printe ekleyebilirsiniz...
    # office worker yazdırma
    def print_OfficeWorker(self,userlist):
        ow_users = [x for x in userlist if (x.typex == 1 )]
        for usr in ow_users:
            print(usr.name+" "+usr.surname)
            ##istediğiniz başka bilgileri de printe ekleyebilirsiniz...

  # office worker sınıfı
class OfficeWorker(User):
    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex):
        super().__init__(name, surname, tc, phone, address, ssn, username, password, typex)
  
