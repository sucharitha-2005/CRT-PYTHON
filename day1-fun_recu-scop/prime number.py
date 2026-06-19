def is_prime(n):
 """Check if n is prime. Time: O(√n)"""
 if n < 2:
   return False
 for i in range(2, int(n**0.5) + 1):
     if n % i == 0:
          return False
 return True
def primes_up_to(limit):
  """Return list of primes up to limit. Time: O(n√n)"""
  return [n for n in range(2, limit + 1) if is_prime(n)]
print(primes_up_to(30))
