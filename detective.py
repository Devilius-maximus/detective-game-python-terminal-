class game:
    def __init__(self):
        self.case = None
        self.player = None


    def setcase (self , case):
        self.case = case

    def setplayer (self , player):
        self.player = player

    #def addlocation (self , location):
    #    self.location = location

    #def showlocation (self ):
    #    print("locations: ")
    #    i = 1
    #    for location in self.location:
    #        print(f"{1}_ {location.name}")
    #        i += 1

    def searchlocation (self , i):

        clues = self.case.locations[i].search()

        for clue in clues:
            self.player.collectclue(clue)

    def interigate (self , suspect):
        suspect.qa()

        clue = suspect.giveclue()

        if clue:
            self.player.collectclue(clue)

    def showclue (self):
        self.player.showclue()

    def accuse (self , suspect):
        if suspect == self.case.solution:
            print("you solved the case, nice dude")

            self.end()

        else:
            print("wrong, u fucked up")

    def start(self):

        self.gamerunning = True

        while self.gamerunning:
            
            print("can your solve this case detective? ")
            print("1 show case")
            print("2 show location")
            print("3 search location")
            print("4 show suspect ")
            print("5 interigate suspect ")
            print("6 show clues")
            print("7 who do you accuse?")
            print("8 exit")

            choice = input(" ")

            if choice == "1":
                self.case.showcase()

            elif choice == "2":
                self.case.showlocations()

            elif choice == "3":
                self.case.showlocations()
                x = int(input("which location you want to search? ")) -1
                self.searchlocation(x)

            elif choice == "4":
                self.case.showsuspects()


            elif choice == "5":
                self.case.showsuspects()
                x = int(input("which suspect do you want to interigate? ")) -1

                suspect = self.case.suspects[x]
                self.interigate(suspect)



            elif choice == "6":
                self.showclue()

            elif choice == "7":
                self.case.showsuspects()
                x = int(input("who is the accused? ")) -1
                self.accuse(self.case.suspects[x])


            elif choice == "8":
                break



class player:
    def __init__(self , name):
        self.name = name
        self.clue = []
        self.currentlocation = 0
        self.solved = False

    def move(self , location):
        self.currentlocation = location
        print(f"{self.name} moved to {location.name}")

    def collectclue (self , clue):

        self.clue.append(clue)
        print("clue collected ")

    def showclue (self):
        print("collected clues: ")

        i = 1
        for clue in self.clue:
            print(f"{i} {clue.description}")

            i += 1

    
    #def searchlocation(self):
    #    self.currentlocation.search()

    
    #def accuse (self , suspect , case):

    #    game.accuse(suspect)



class suspect:
    def __init__(self , name, age, job , dialogue,clue = None, isguilty = False):
        self.name = name
        self.age = age
        self.job = job
        self.dialogue = dialogue
        self.clue = clue
        self.isguilty = isguilty
        self.interigared = False


        
    def showinfo (self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"job: {self.job}")

    def qa(self):
        self.interigared = True
        print (f"{self.name}: {self.dialogue}")

    
    def giveclue (self):
        if self.interigared:
            print (f"clue: {self.clue.description}")
            return self.clue
        
        else:
            print("you must interigate first")
    

class clue:
    def __init__(self , clueid , description , location):
        self.clueid = clueid
        self.description = description
        self.location = location
        self.found = False

    def collect(self):
        if self.found:
            return False
        
        self.found = True
        print(f"clue found: {self.description}")
        
        return True
    
    def reset(self):
        self.found = False
    
class location:
    def __init__(self , name):
        self.name = name
        self.clue = []
        self.searched = False

    def addclue (self , clue):
        self.clue.append(clue)

    def search (self):
        if self.searched:
            print(f"you have already searched {self.name}")
            return []

        self.searched = True

        if not self.clue :
            print("no clues found ")

            return []
        

        foundclue = []

        for clue in self.clue:
            if clue.collect():
                foundclue.append(clue)
        

        return foundclue
    
    def reset (self):
        self.searched = False

        for clue in self.clue:
            clue.reset()



class case:
    def __init__ (self , title, victim):
        self.title = title
        self.victim = victim
        self.suspects = []
        self.locations = []
        self.solution = None

    
    def addsuspect (self , suspect):
        self.suspects.append(suspect)

    def addlocation (self , location):
        self.locations.append(location)


    def setsolution (self , suspect):
        self.solution = suspect


    def showcase (self):
        print("case file: ")
        print(f"title: {self.title}")
        print(f"victim: {self.victim}")
        print( f"suspects: {len(self.suspects)}")
        print(f" location: {len(self.locations)}")

            
    def showlist (self, items , title):
        print(title)

        if not items:
            return None
        
        i=1 
        for item in items:
            print(f"{i} {item.name}")

            i += 1

    def showsuspects (self ):
        self.showlist(self.suspects , "suspects")

    def showlocations (self ):
        self.showlist(self.locations , "locations")

    

    def reset(self):
        for suspect in self.suspects:
            suspect.reset()

        
        for location in self.locations:
            location.reset()





if __name__ == "__main__":
    Game = game()

    Case = case("case name" , "for who")

    Player = player("your name")

    clue1 = clue (1, "object" , "where that object is")
    clue2 = clue (2, "object" , "where that object is")



    location1 = location("location name")
    location2 = location("location name")

    location1.addclue(clue1)
    location2.addclue(clue2)


    Case.addlocation(location1)
    Case.addlocation(location2 )


    suspect1 = suspect("mmd" , 67 , "job" , "description" , clue1, True)
    suspect2 = suspect("mmd2" , 21 , "job" , "description" , clue2, False)

    Case.addsuspect(suspect1)
    Case.addsuspect(suspect2)

    Case.setsolution(suspect1)

    Game.setcase(Case)

    Game.setplayer(Player)




    Game.start()
