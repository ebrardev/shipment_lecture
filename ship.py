from abc import ABC, abstractmethod
from login import login

class Person(ABC):  # ABSTRACT CLASS
    def __init__(self, name, surname, tc, phone, address):
        self.name = name
        self.surname = surname
        self.tc = tc
        self.phone = phone
        self.address = address

class Customer(Person):  # INHERITANCE
    def __init__(self, name, surname, tc, phone, address):
        super().__init__(name, surname, tc, phone, address)

class shipment():
    def __init__(self, status, weight, s_add, d_add, name, surname, tc, phone, name1, surname1, tc1, phone1):
        self.status = status
        self.weight = weight
        self.s_add = s_add
        self.d_add = d_add
        self.distance = self.calc_distance(s_add, d_add)
        self.cost = self.calc_cost(self.distance, self.weight)
        self.customer = Customer(name, surname, tc, phone, s_add)
        self.receiver = Customer(name1, surname1, tc1, phone1, d_add)

    def calc_distance(self, s_add, d_add):
        # Burada iki adres arasındaki mesafeyi hesaplayan bir fonksiyon yazmalısınız.
        # Örnek olarak, harita API'ları veya koordinat hesaplama yöntemleri kullanılabilir.
        pass

    def calc_cost(self, distance, weight):
        # Burada mesafe ve ağırlık gibi faktörlere bağlı olarak bir maliyet hesaplayan bir fonksiyon yazmalısınız.
        pass

    def create_shipment(self):
        status = "Kabul edildi"
        weight = input("shipment kaç kg")
        s_add = input("gönderici adresi")
        d_add = input("alici adresi")
        name = input("gönderici adı")
        surname = input("gönderici soyadı")
        tc = input("gönderici tc")
        phone = input("gönderici telefon")
        name1 = input("alıcı adı")
        surname1 = input("alıcı soyadı")
        tc1 = input("alıcı tc")
        phone1 = input("alıcı telefon")
        shpmnt = shipment(status, weight, s_add, d_add, name, surname, tc, phone, name1, surname1, tc1, phone1)
        print(shpmnt)

        return shpmnt

    def print_shipment(self, shipmentlist, tc1):
        shpmnts = [x for x in shipmentlist if int(x.customer.tc) == int(tc1)]
        for shp in shpmnts:
            print(shp.status + " " + shp.s_add)

# Bu kısımda shipment sınıfının bir örneğini oluşturarak print_shipment fonksiyonunu test edebilirsiniz.
# Ancak, calc_distance ve calc_cost fonksiyonlarını gerçek verilerle doldurmanız gerekecek.
    def add_shipment(self, shipmentlist):
        new_shipment = self.create_shipment()
        shipmentlist.append(new_shipment)

    def delete_shipment(self, shipmentlist, tc):
        for shp in shipmentlist:
            if int(shp.customer.tc) == int(tc):
                shipmentlist.remove(shp)
                print("Shipment deleted successfully.")
                return
        print("Shipment not found.")
shipment_instance = shipment("Teslim edildi", 10, "Istanbul", "Ankara", "Sender", "Surname", "12345", "5551234567", "Receiver", "ReceiverSurname", "67890", "5559876543")

shipmentlist = [shipment_instance]
shipment_instance.add_shipment(shipmentlist)
shipment_instance.print_shipment(shipmentlist, "12345")
shipment_instance.delete_shipment(shipmentlist, "7")