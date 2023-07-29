# Character Creator
class Character():
    def __init__(self):
        self.name = ''
        self.race = ''
        self.outfit = {
            'helmet': '',
            'chestplate': '',
            'pants': '',
            'boots': ''
        }

    def getInfo(self, name, race):
      self.name = name
      self.race = race

    def changeBoots(self, boots):
      self.outfit['boots'] = boots

    def changePants(self, pants):
       self.outfit['pants'] = pants

    def changeHelm(self, helm):
      self.outfit['helmet'] = helm

    def changePlate(self, plate):
      self.outfit['chestplate'] = plate

    def displayOutfit(self):
      print("You are currently wearing")
      for key, value in self.outfit.items():
        print(f"{key}: {value}")

    def runner(self):
      print('--------Welcome to the character Builder--------')
      name = input("What's your name traveler?:")
      race = input("What's your race? (Human/Elf/Dwarf):")
      self.getInfo(name, race)

      print(f"---Welcome {self.name}---")
      print("Let's Customize your gear")
      while True:
        response = input("Would you like to view, edit or save your fit?")
        if response.lower() == "view":
            self.displayOutfit()
        elif response.lower() == "edit":
            piece = input('What would you like to edit helm/chest/pants/boots?: ').title()
            if piece == "Helm":
                helm = input('What helm would you like to wear?: ').title()
                self.changeHelm(helm) 
            elif piece == "Chest":
                chest = input('What chestplate would yo like to wear?: ').title()
                self.changeChest(chest)
            elif piece == "Pants":
                pants = input('What pants would yo like to wear?: ').title()
                self.changePants(pants)
            elif piece == "Boots":
                boots = input('What boots would yo like to wear?: ').title()
                self.changeBoots(boots)
        elif response == "save":
           break
      print("Character Successfully built!")


mitchell = Character()

mitchell.runner()