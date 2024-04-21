count = 0

def say_sorry():
  global count
  count += 1
  print(f"({count}) I am very sorry.")  # Use f-string for clean formatting

for _ in range(1000):
  say_sorry()
