from abc import ABC, abstractmethod
from login import login

class Person(ABC):  # ABSTRACT CLASS
    def __init__(self, name, surname, tc, phone, address):
        self.name = name
        self.surname = surname
        self.tc = tc
        self.phone = phone
        self.address = address

class User(Person, login):
    ulist = []  # user sınıfına ait tüm örnekleri tutacak liste

    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex):
        self.ssn = ssn
        Person.__init__(self, name, surname, tc, phone, address)
        login.__init__(self, username, password, typex)
        # Oluşturulan User örneklerini ulist listesine ekleyelim
        self.ulist.append(self)

class Carrier(User):
    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex, carrier_name, capacity):
        User.__init__(self, name, surname, tc, phone, address, ssn, username, password, typex)
        self.carrier_name = carrier_name
        self.capacity = capacity

class Admin(User):
    def __init__(self, name, surname, tc, phone, address, ssn, username, password, typex):
        User.__init__(self, name, surname, tc, phone, address, ssn, username, password, typex)

    def add_Carrier(self):
        # Kullanıcıdan temel kullanıcı bilgilerini al
        name2 = input("İsim: ")
        surname2 = input("Soyisim: ")
        tc2 = input("TC: ")
        phone2 = input("Telefon: ")
        address2 = input("Adres: ")
        ssn2 = input("SSN: ")
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

    def print_Carrier(self):
        # Taşıyıcıları ekrana yazdır
        print("Taşıyıcılar:")
        for carrier in self.ulist:
            if isinstance(carrier, Carrier):  # Carrier sınıfının örneği mi kontrolü
                print(f"{carrier.name} {carrier.surname} - Taşıyıcı Adı: {carrier.carrier_name}, Kapasite: {carrier.capacity}")

                ## taşıyıcı silme
    def delete_Carrier(self,userList,phone2):
        crr_user = [ x for x in userList if (int(x.phone) == int(phone2) )]
        userList.remove(crr_user[0])

# Örnek kullanım
admin = Admin("Admin", "Surname", "123456789", "555-1234", "Address", "123456", "admin_user", "admin_pass", "admin_typex")
admin.add_Carrier()
admin.print_Carrier()
