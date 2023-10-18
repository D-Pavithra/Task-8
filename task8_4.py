class TVclass:
    def __init__ (self, brand):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.inches = 0
        self.on = False
    def inc_vol(self):
        if self.volume <100:
            self.volume+=1
    def dec_vol(self):
        if self.volume>0:
            self.volume-=1
    def set_channel(self, channel):
        if 1 <=channel <=50:
            self.channel = channel
    def reset_tv(self):
        self.channel = 1
        self.volume = 50
    def status (self):
        return "{self.brand} at channel {self.channel}, volume{self.volume}"
class Ledtv(TVclass):
    def __init__ (self, brand, thickness, energy, lifespan, refreshrate):
        super().__init__ (brand)
        self.thickness= thickness
        self.energy = energy
        self.lifespan = lifespan
        self.refreshrate = refreshrate
    def display_detail(self):
        return "Brand: {self.brand}, thickness: {self.thickness}, energy: {self.energy}, lifespan: {self.lifespan}, refreshrate: {self.refreshrate}" 
class PlasmaTV(TVclass):
    def __init__(self, brand, view, backlight, display_details):
        super().__init__(brand)
        self.view = view
        self.backlight = backlight
        self.display_details= display_details
    def display_details(self):
        return "Brand: {self.brand}, view: {self.view}, backlight: {self.backlight}, display_details: {self.display_details}"
led_tv = Ledtv("Sony", "1 inch", "100W", "5 years","120HZ")
plasma_tv = PlasmaTV("Panasonic", "178 degree", "LED", "4k HD")
print (led_tv.status())
print (led_tv.display_details())
print (plasma_tv.status())
print (plasma_tv.display_details())
