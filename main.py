class hotel():
    Name= None
    Special_Features = None
    Tv= None
    wifi= None
    breakfast= None
    def set_data(self, Name, Special_Features, Tv, wifi, breakfast):
        self.Name = Name
        self.Special_Features = Special_Features
        self.Tv = Tv
        self.breakfast = breakfast
    def get_data(self):
            print("Название: ", self.Name,".  ","Специальные функции: ", self.Special_Features, ". " , "Завтрак:" , self.breakfast)


apartment= hotel()
apartment.set_data("люкс", "терраса", "да и playstation", "да,100мб/с", "да,шведский стол")
apartment2 = hotel()
apartment2.set_data("стандарт", "нет", "да", "да", "да, сэндвич и чай")
apartment3 = hotel()
apartment3.set_data("карцер", "нет", "нет", "нет", "да, только чай")

apartment.get_data()
apartment2.get_data()
apartment3.get_data()