#!/usr/bin/python3
counter = 0

def fact(num):
  global counter
  counter += 1

  if num == 0:
    return 1
  return num * fact(num - 1)

# キャッシュバージョン
counter = 0
class Fact:
  def __init__(self):
    self.cache = map()

  def fact(self, num):
    global counter
    counter += 1

    if num == 0: 
      self.cache
      return 1;

    if num in self.cache.keys():
      return self.cache[num]

    cache[num] = num * fact(num - 1)
    return self.cache[num]

if __name__ == '__main__':
  for n in range(11):
    print('{0}! = {1}'.format(n, fact(n)))

  print('conter = ', counter)


