# 1. Basic - Print all integers from 0 to 150.
i = 0
while i <= 150:
  print(i)
  i += 1

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000
i = 5
while i <= 1000:
  print(i)
  i += 5

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
i = 1
while i <= 100:
  if i % 10 == 0:
    print("Coding Dojo")
  elif i % 5 == 0:
    print("Coding")
  else:
    print(i)
  i += 1

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
i = 1
sum = 0
while i <= 500000:
  if i % 2 == 1:
    sum = sum + i
  i += 1
print(sum)

#alternative
i = 1
sum = 0
while i <= 500000:
  sum = sum + i
  i += 2
print(sum)

#alternative with for loop
i = 1
sum = 0
for i in range(1, 500000, 2):
  sum = sum + i
print(sum)

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
i = 2018
while i > 0:
  print(i)
  i += -4

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 10
highNum = 500
mult = 8
while lowNum <= highNum:
  if lowNum % mult == 0:
    print(lowNum)
  lowNum += 1

  