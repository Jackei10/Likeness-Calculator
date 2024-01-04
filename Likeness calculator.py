print("Love Calculator")
Name1=input("Enter First Name: ")
Name2=input("Enter Second Name: ")
Combined= Name1+Name2
lower_combined= Combined.lower()
t= lower_combined.count("t")
r= lower_combined.count("r")
u= lower_combined.count("u")
e= lower_combined.count("e")
First= t+r+u+e
l= lower_combined.count("l")
o= lower_combined.count("o")
v= lower_combined.count("v")
e= lower_combined.count("e")
r= lower_combined.count("r")
e= lower_combined.count("s")
Second= l+o+v+e
percentage= str(First)+ str(Second)
print(f"Your love percentage is {percentage}%")
