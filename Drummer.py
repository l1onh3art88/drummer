class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
    print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang", "Bong"])

    def count(self):
        for i in range(4):
            print(i+1)
    
    def combust(self):
        print("Kaboom")
class Band(list):
    def __init__(self, performers=()):
        self.members = list(performers)
       
    def hire(self, person):
        self.members.append(person)
        print("Hired Person")
    def fire(self,person):
        self.members.remove(person)
        print("Fired someone")
    def play(self):
        for x in self.members:
            try:
                x.count()
                x.solo(4)
            except:
                x.solo(4)
            
            
        
if __name__ == '__main__':
    d= Drummer()
    g= Guitarist()
    ba = Bassist()
    b = Band()
    b.hire(d)
    b.hire(g)
    b.play()
    b.hire(ba)
    b.play()
    
    

        