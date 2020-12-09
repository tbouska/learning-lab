class Staff:
    # class variable (all instances/objects have it the same even after it gets modified)
    companyName = "Doogat"
    
    def __init__(self, pPosition, pName, pPay):
        # instance variables (can differ by instance/object)
        self.position = pPosition
        self.name = pName
        self.pay = pPay
    def __str__(self):
        return "%s works as a %s and earns %d$" % (self.name, self.position, self.pay)
    # getter for self.position
    @property
    def position(self):
        return self._position
    # setter for self.position
    @position.setter
    def position(self, value):
        if value == "manager" or value == "associate":
            self._position = value
        else:
            self._position = None
            print("Position %s is not in jobs catalogue." % (value))

employee1 = Staff("manager", "John Doe", 3400)
employee2 = Staff("janitor", "Alice Doe", 1800)
print(employee1)
print(employee2)
