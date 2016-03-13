#Jonthan Salmon

#This class takes a list from the main class and an item to search for when called
#then it runs the linearsearch algorithm on the list, if the item it is looking for
#is located within the list it will return "Engine 1" else it will return "Engine 2"
#This works in tandem with Dijkstra's algorithm to create a simplistic navigation
#system

class LinearSearch():

    def __init__(self):
        self.foundItem = False
        self.pos = 0

    def linearSearch(self, myList, myItem):
        for i in range(0,len(myList)):
            if myList[i] == myItem:
                self.foundItem = True
                self.pos = self.pos + 1
                return "Engine 1"
        else:
            return "Engine 2"


    #this function resets all items back to the origtional state so that the class can
    #be called upon again given a different list and return a different answer
    def reset(self):
        self.foundItem = False
        self.pos = 0