class Moblile_phone():
    model= "iphone"
    battery = 70
    def use_phone(self):
        self.battery -= 5
        print(self.battery)
phone = Moblile_phone()
phone.use_phone()
phone.use_phone()