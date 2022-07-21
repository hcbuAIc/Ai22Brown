import math as english,random as rand

print("15^2=",english.pow(15,2))

names = """Henry
Benedict
Ethan
Jerry
Rick
Tojo
Arthur
Kim
Josef
Günter""".split("\n")

rand.shuffle(names)
print("shuffledNames:",names)
print("randomName:",rand.choice(names))