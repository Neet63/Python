marks = 50

if marks>33:
    print("You passed!!!")
elif marks == 33:
    print("You Barely Passed!!!")
else:
    print("You failed!!!")


#Match-Case
def checkVowel(n):
   match n:
      case 'a': return "Vowel alphabet"
      case 'e': return "Vowel alphabet"
      case 'i': return "Vowel alphabet"
      case 'o': return "Vowel alphabet"
      case 'u': return "Vowel alphabet"
      case _: return "Simple alphabet"
print (checkVowel('a'))
print (checkVowel('m'))
print (checkVowel('o'))

#loop
words = [1,2,3,4,5]
for x in words:
  print(x)

i = 10
while i < 16:
  print(i)
  i += 1

#Break and continue
x=1
while x < 10:
    print("x:", x)
    if x == 5:
        print("Breaking...")
        break
    x+=1
print("End")

for letter in "Python":
    # continue when letter is 'h'
    if letter == "h":
        continue
    print("Current Letter :", letter)