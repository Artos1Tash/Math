def f(x):
    return x**2

def midpoint(a, b, n):
  length = (b-a)/n #length of sub interval
  area = 0 #total area
  left, right = 0, length # two pointers
  
  while  right <= b:
    # adding area of interval
    area += f((right+left)/2) * length 
    
    left += length 
    right += length 

  print(left, right, length)
  return area

print(midpoint(0, 3, 13))
