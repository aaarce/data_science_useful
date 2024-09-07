#simulating rolling a 6-sided die
import pandas as pd 
import random
data = [] #empty list called data
for i in range(600): #create for-loop
        roll = random.randint(1,6) #simulating part real-world die factors
        d = {"roll": roll} #accumulate factors in dictionary 'd'
        data.append(d) #append 'd' to 'data' list
df = pd.DataFrame(data) #create outside of the for-loop  

print(df)      

#simulating rolling Two 6-sided dice
data = []
#create for-loop
for i in range(600):
    #simulate real-world factors or possibilities
    black = random.randint(1,6)
    white = random.randint(1,6)
    
    #accumulate all factors in dictionary 'd':
    d = { "white": white, "black": black}
    
    #append 'd' to 'data'
    data.append(d)
    
#create df (outside of for-loop)
df = pd.DataFrame(data)

#print df
print(df)
    
