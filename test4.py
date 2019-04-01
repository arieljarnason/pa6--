class myobject:
    def __init__(self, variable1 = None):
        self.variable1 = variable1

newobject = myobject("blabla")
newobject2 = myobject("blabla2")


mylist = [newobject, newobject2]

mylist.remove(newobject)
print(mylist[0].variable1)