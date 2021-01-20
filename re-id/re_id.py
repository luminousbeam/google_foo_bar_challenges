# Re-ID
# =====

# There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely Foolproof Scheme. 

# She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

# Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

# -- Python cases --
# Input:
# solution.solution(0)
# Output:
#     23571

# Input:
# solution.solution(3)
# Output:
#     71113

def id_gen(n):
  def is_prime(numero):
    if numero > 2:
      for x in range(2, numero):
        if numero % x == 0:
          return False
          break
      else:
        return True
    elif numero == 2:
      return True
    else:
      return False
  primes = ""
  a = 2
  while len(primes) < n + 5:
    if(is_prime(a)):
      primes += str(a)
    a += 1
  return primes[n:n+5]

print(id_gen(0))
# print(id_gen(3))

# "2357111317192329..."
# print(id_gen(5))