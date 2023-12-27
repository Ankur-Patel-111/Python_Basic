l=[1,2,3,4]
l.append(200) #adding element
l.insert(1,'hello') #insert 1st position hello data.
print(l) #1,'hello',2,3,4,500
l.remove(200) #remove the data.
print(l) #1,'hello',2,3,4
print(l.count('hello')) #return number of times repeated
l.extend([300,400]) #add multiple data
l.extend([500]) #add multiple data
print(l)
l.pop(0) #index/position.
l.remove(3)
