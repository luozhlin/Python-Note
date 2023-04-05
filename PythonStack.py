from pythonds.basic import Stack

s = Stack()

print(s.isEmpty())

s.push(4)
s.push("dog")
print(s.peek())

s.push(True)
print(s.size())
print(s.isEmpty())

s.push(8.4)

print(s.pop())
print(s.pop())
print(s.size())

# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

def revstring(mystr): 
    s= Stack()
    for i in mystr:
        s.push(i)
    restr = ""
    for i in range(len(mystr)):
        restr  += s.pop()
    
    return restr

print(revstring('apple')=='elppa')
print(revstring('x')=='x')
print(revstring('1234567890')=='0987654321')
