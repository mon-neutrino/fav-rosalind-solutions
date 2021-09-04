# http://rosalind.info/problems/hamm/

def hamming(x, y):
  distance = 0
  for i in range(0, len(x)):
    if x[i-1] != y[i-1]:
      distance += 1
  print(distance)

p = str(input()).split()
print(p)
x = p[0]
y = p[1]
hamming(x, y)