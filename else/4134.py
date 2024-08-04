T = int(input())

def find_prime(n):
  z = n
  if n == 1 or n == 0:
      z = 2
  while True:
        is_prime = True
        for i in range(2, int(z**0.5) + 1):
            if z % i == 0:
                z += 1
                is_prime = False
                break  # Breaks the inner for loop
        
        if is_prime:
            return z



for _ in range(T):
  n = int(input())
  print(find_prime(n))