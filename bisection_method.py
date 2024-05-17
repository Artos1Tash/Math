#bisection mathod
f = lambda x: x**2 - 2

def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
      return "error"
    while b-a > tol:
      c = (a+b)/2
      if f(a)*f(c) <= 0:
        b = c
      else:
        a = c
      x = (a+b)/2
  
    return x
  
print(bisection(0, 4, 0.001))