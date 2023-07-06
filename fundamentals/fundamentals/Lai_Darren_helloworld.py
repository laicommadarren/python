# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Darren"
print("Hello", name, "!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 18
print("Hello", name)	# with a comma
print("Hello" + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "fries"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']