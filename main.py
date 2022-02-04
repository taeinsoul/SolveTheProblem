import random
def quiz():
  print('solve the problem!!')
  while True :
    print("addtion: 0, subtraction:1, multiplication:2, division(Quotient):3, devision(reminder):4, exit:5")
    number = int(input('input:'))
    if number == 0:
      count = 0
      collect = 0
      notCollect = 0
      while count < 10:
        b_rand = random.randrange(1,9)
        a_rand = random.randrange(1,9)
        a = input(f'{b_rand} + {a_rand} = ')
        if b_rand+a_rand == int(a):
          print("TRUE.")
          collect += 1
        else:
          print('FALSE.')
          notCollect += 1
        count += 1
      print(f'collect={collect} : notCollect= {notCollect}')
    elif number == 1:
      count = 0
      collect = 0
      notCollect = 0
      while count < 10:
        b_rand = random.randrange(1,9)
        a_rand = random.randrange(1,9)
        a = input(f'{b_rand} - {a_rand} = ')
        if b_rand-a_rand == int(a):
          print("TRUE.")
          collect += 1
        else:
          print('FALSE.')
          notCollect += 1
        count += 1
      print(f'collect={collect} : notCollect= {notCollect}')
    elif number == 2:
      count = 0
      collect = 0
      notCollect = 0
      while count < 10:
        b_rand = random.randrange(1,9)
        a_rand = random.randrange(1,9)
        a = input(f'{b_rand} * {a_rand} = ')
        if b_rand*a_rand == int(a):
          print("TRUE.")
          collect += 1
        else:
          print("FALSE.")
          notCollect += 1
        count += 1
      print(f'collect={collect} : notCollect= {notCollect}')
    elif number == 3:
      print("only Quotient not Remainder")
      count = 0
      collect = 0
      notCollect = 0
      while count < 10:
        b_rand = random.randrange(1,9)
        a_rand = random.randrange(1,9)
        a = input(f'{b_rand} / {a_rand} = ')
        if b_rand // a_rand == int(a):
          print("TRUE.")
          collect += 1
        else:
          print('FALSE.')
          notCollect += 1
        count += 1
      print(f'collect={collect} : notCollect= {notCollect}')
    elif number == 4:
      print("only Remainder not Quotient")
      count = 0
      collect = 0
      notCollect = 0
      while count < 10:
        b_rand = random.randrange(1,9)
        a_rand = random.randrange(1,9)
        a = input(f'{b_rand} % {a_rand} = ')
        if b_rand % a_rand == int(a):
          print("TRUE.")
          collect += 1
        else:
          print('FALSE.')
          notCollect += 1
        count += 1
      print(f'collect={collect} : notCollect= {notCollect}')
    elif number == 5:
      print('exit program.')
      break
    else:
      print("input not correct!!")



