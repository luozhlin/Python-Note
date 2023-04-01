def gcd(m,n):
    r = m % n
    while r !=0:
        m = n
        n = r
        r = m%n
    return n

class Fraction:

    def __init__(self, top, bottom=1) -> None:
        self.num = top
        self.den = bottom

    def __str__(self) -> str:
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.den)
        
    def __add__(self, other):  # +
        if not isinstance(other, Fraction):
            other = Fraction(other)
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __radd__(self, other):
        return self + Fraction(other)

    def __eq__(self, other) -> bool:  # =
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        
        return firstnum == secondnum
    
    def __mul__(self, other):  # *
        if not isinstance(other, Fraction):
            other = Fraction(other)
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)
    
    def __rmul__(self, other):
        return self * Fraction(other)
    
    def __truediv__(self, other):  # /
        if not isinstance(other, Fraction):
            other = Fraction(other)
        newnum = self.num * other.den
        newden = self.den * other.num
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __rtruediv__(self, other):
        return Fraction(other) / self
    
    def __sub__(self, other):  # -
        if not isinstance(other, Fraction):
            other = Fraction(other)
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)
    
    def __rsub__(self, other):
        return Fraction(other) - self
    
    def __lt__(self, other):  # <
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.num * other.den < self.den*other.num:
            return True
        else:
            return False 
        
    def __gt__(self, other):  # >
        if not isinstance(other, Fraction):
            other = Fraction(other)
        if self.num * other.den > self.den*other.num:
            return True
        else:
            return False 
    
###### test
f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1+f2
print(f1+2)
print(2+f1)
print(f3)
print(f1==f2)
print(f1*f2)
print(f1*2)
print(4*f1)
print(f1/f2)
print(f1/4)
print(4/f1)
print(f1-f2+2)
print(2-f1)
print(2 > f1)
print(2 < f1)
