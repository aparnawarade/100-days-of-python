# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
import random 
names=['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']
#print(names)
# 🚨 Remember to remove the print statement above when you submit.
choose=random.choice(names)
print(f"{choose} is going to buy the meal today!")

#other method
length_names=len(names)
choose=random.randint(0,length_names-1)
print(f"{names[choose]} is going to buy the meal today!" )