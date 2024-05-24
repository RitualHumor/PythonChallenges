import math

#Turns radians into degrees
def rad2deg(rad):
  if "Pi" in rad:
    rad_new=(rad.replace(" Pi", ''))
    deg = float(rad_new) * 180
  else:
    deg = float(rad) * 180 / math.pi
  print(deg)

#Takes a list of numbers and will sort it ascending, descending, or none after asking the user which they would like.
def sortlist(foo, do):
  bar = list(foo.split(','))
  times = len(bar)
  while times > 0:
    n = times - 1
    bar[n] = int(bar[n])
    times -= 1
  do = input("How do you want to sort this? (Asc)ending, (Desc)ending, or (None)? ")
  if do in ['asc', 'Asc']:
    bar.sort()
    print(bar)
  elif do in ['desc', 'Desc']:
    bar.sort(reverse=True)
    print(bar)
  elif do in ["none" 'None']:
    print(bar)
  else:
    print("Your input was invalid, None was selected by default")
    print(bar)

#Turns a decimal number into a binary number, up to 1023
def dec2binary(foo):
  if foo == 1023:
    return 1111111111
  if foo > 511:
    foo -= 512
    bar = "1"
  else:
    bar += "0"
  if foo > 255:
    foo -= 256
    bar = bar + "1"
  else:
    bar += "0"
  if foo > 127:
    foo -= 128
    bar = bar + "1"
  else:
    bar += "0"
  if foo > 63:
    foo -= 64
    bar = bar + "1"
  else:
    bar += "0"
  if foo > 31:
    foo -= 32
    bar = bar + "1"
  else:
    bar += "0"
  if foo > 15:
    foo -= 16
    bar = bar + "1"
  else:
    bar += "0"
  if foo > 7:
    foo -= 8
    bar += '1'
  else:
    bar += "0"
  if foo > 3:
    foo -= 4
    bar += '1'
  else:
    bar += "0"
  if foo > 1:
    foo -= 2
    bar += "1"
  else:
    bar += "0"
  if foo == 1:
    foo -= 1
    bar += '1'
  else:
    bar += "0"
  return bar

#Counts how many vowels are in a word
def vowel_count(word):
  word = list(word)
  n = len(word)
  count = 0
  vowels = "aeiouAEIOU"
  while n > 0:
    if word[n-1] in vowels:
      count += 1
    n -= 1
  return count

#Takes a credit card number (16 digit number) and hides all but the last 4 digits
def hideCCnum(CC):
  foo = list(str(CC))
  n = len(foo)
  if n != 16:
    return "This number is not valid! Too short or too long."
  ret = "****************"
  times = 4
  while times > 0:
    ret += str(foo[16 - times])
    times -= 1
  return ret

#Counts the numbers of Xs and Os in a string
def XandO(words):
  if type(words) != str:
    return "You must input a string"
  foo = list(words)
  n = len(foo)
  Xs = 0
  Os = 0
  while n > 0:
    if foo[n-1] in ['X', 'x']:
      Xs += 1
    if foo[n-1] in ['O', 'o']:
      Os += 1
    n -= 1
  if Xs == Os:
    return True
  else:
    return False

#A sort of "calculator" that will take two numbers and an operator and give you back the result
def calc(first, operator, second):
  if type(first) != int or type(second) != int:
    return "You must enter only integers"
  if len(operator) > 1:
    return "You must only enter 1 string character for the operator"
  if operator not in ['+','-', '/', '*']:
    return "You must enter an operator of +, -, /, or * only."
  if operator in ['+']:
    return (first + second)
  elif operator in ['-']:
    return (first - second)
  elif operator in ['*']:
    return (first * second)
  elif operator in ['/']:
    return (first / second)

#Gives the price of something after the discount given
def discount(price, discount):
  if type(discount) != int or type(price) != int:
    return "Make sure you only enter integers."
  elif discount > 100 or discount < 0:
    return "Your discount must be between 0 and 100%"
  elif price < 0:
    return "You cannot have a negative price."
  perc = (100 - discount) / 100
  final = price * perc
  return final

#Takes a list of non-negative integers and string, and will return a new list with only the numbers
def OnlyNums(mixed):
  if type(mixed) != list:
    return "You must provide a list of non-negative integers and strings only."
  n = len(mixed)
  tempn = n
  while tempn > 0:
    if type(mixed[tempn - 1]) not in [int, str]:
      return "You must provide a list of non-negative integers and strings only."
    if type(mixed[tempn - 1]) in [int]:
      if mixed[tempn - 1] < 0:
        return "You must provide a list of non-negative integers and strings only."
    tempn -= 1
  bar = []
  while n > 0:
    if type(mixed[0]) in [str]:
      mixed.remove(mixed[0])
    elif type(mixed[0]) in [int]:
      bar.append(mixed.pop(0))
    n -= 1
  return bar

#Whatever string you give it, iitt  wwiillll ddoouubbllee  iitt  lliikkee  tthhiiss!!
def doublechar(foo):
  if type(foo) not in [str]:
    return "You must enter a string."
  foo = list(foo)
  bar = []
  n = len(foo)
  while n > 0:
    x = foo[0]
    bar.append(x)
    bar.append(x)
    foo.remove(foo[0])
    n -= 1
  n = len(bar)
  ret = ""
  oppn = 0
  while n > 0:
    ret += bar[oppn]
    n -= 1
    oppn += 1
  return ret
