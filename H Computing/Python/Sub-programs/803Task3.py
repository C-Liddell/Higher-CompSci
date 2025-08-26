def module1(first, second, third):
  volume = first * second * third
  print("Volume =",volume)
  # Displays Volume = 24

def module2(monday):
  monday = monday/10
  return monday

def module3(blue, red):
  total = 0
  for counter in range(blue, red):
    print(counter)
    total = total + 2
    print(total)
  return total

def module4(up, down):
  middle = up % down
  top = int(up/down)
  total = middle + top
  return total

num1 = 100
num2 = 6
num3 = 9
print(module2(num1) + module3(num2, num3))