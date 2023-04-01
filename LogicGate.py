class LogicGate: 
    def __init__(self, n):  # n is the label, a string
        self.label = n
        self.output = None

    def getLabel(self):  # Get the label
        return self.label

    def getOutput(self):  # Get the output
        #performGateLogic = getattr(self, 'performGateLogic')
        self.output = self.performGateLogic()  # Define in subclass
        return self.output


class BinaryGate(LogicGate):  # The gate of two pins

    def __init__(self, n):
        # Another method: super(UnaryGate,self).__init__(n)
        LogicGate.__init__(self, n)
        self.pinA = None
        self.pinB = None

    def getPinA(self):  # If none input from the former, just input by yourself
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()  # Use connector class method get the former output

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()  # pinB here is a connector so can use getFrom()
    
    def setNextPin(self, source):  # Choose input line, here source is a connector, means that pinA is filled
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):  # togate can choose the proper input line for the connection.
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
class NandGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 0
        else:
            return 1



class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NorGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPin()

        if a == 1:
            return 0
        else:
            return 1
        

class Connector:  # Connect two gates

    def __init__(self, fgate, tgate):  # two gates class 
        self.fromgate = fgate
        self.togate = tgate
        tgate.setNextPin(self)

    def getFrom(self):  # get the former gate
        return self.fromgate

    def getTo(self):  # get the latter gate
        return self.togate
    

##### Test ######
"""
Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) 
is that same as NOT( A and B ) and NOT (C and D). 
Make sure to use some of your new gates in the simulation.
"""

if __name__ == "__main__":
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)

    # NandGate
    g5 = AndGate("G5")
    g6 = AndGate("G6")
    g7 = NorGate("G7")

    c4 = Connector(g5,g7)
    c5 = Connector(g6,g7)

    # NorGate
    g8 = NandGate("G8")
    g9 = NandGate("G9")
    g10 = AndGate("G10")

    c4 = Connector(g8,g10)
    c5 = Connector(g9,g10)

    print(g4.getOutput())
    print(g7.getOutput())
    print(g10.getOutput())

