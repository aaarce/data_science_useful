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
    
#conditionals - simple example
num = random.randint(1, 10)
if num == 7:
  print("Today")
  print("is")
  print("Your Lucky Day!")
print(f"Number: {num}")

#coin flip conditional
flip = random.choice(["heads", "tails"])
if flip == "heads":
    print("coin flipped heads")
else:
    print("coin flipped tails")
    
#conditional simulation example roulette; further applying if-statements
data = []
for i in range(2001): #update range as needed +1 like 2001 will display last n-th simulation event
    color = random.choice([
        # 9 of 19 outcomes are red
        "red", "red", "red", "red", "red", "red", "red", "red", "red",
        #9 out of 19 outcomes are black
        "black", "black", "black", "black", "black", "black", "black", "black", "black",
        # 1 out of 19 outcomes is green
        "green",
    ])
    
    if color == "red":
        profit = 1
    else:
        profit = -1
        
    d = {"color": color, "profit": profit}
    data.append(d)
    
df = pd.DataFrame(data)          
print(df)    