# Shapes Terminal Concept

dataX = input()
dataY = input()
dataZ = input()
print("------------------")
print(dataX)
print(dataX,dataY)
print(dataX,dataY,dataZ)
print(dataY,dataZ)
print(dataZ)
print("------------------")
print(dataX)
print(dataX,dataY)
print(dataX,dataY,dataZ)
print("------------------")
print(dataX,dataY,dataZ)
print(dataX,dataY,dataZ)
print(dataX,dataY,dataZ)
print(dataX,dataY,dataZ)
print("------------------")
# If, Elif, Else 

print("====================")
questA = input("10+20 = ")
questB = input("10+20 = ")

if questA > questB:
    print("A")
    
elif questA==questB:
    print("A & B")
    
else: 
    ("-")

#Function
#public model view => y

def myFunction(fname):
    print(fname + " XII RPL 3")
myFunction("Arif")

def myPublicFunction(sname):
    print("Hallo" + sname " From XII RPL 3")
myPublicFunction("Arif")
