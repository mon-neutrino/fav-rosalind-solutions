# http://rosalind.info/problems/cons/
from itertools import groupby

# for reading fasta file
def fasta(file):
  f = open(file)
  faiter = (x[1] for x in groupby(f, lambda line: line[0] == '>'))
  for header in faiter:
    seq = ''.join(s.strip() for s in faiter.__next__())
    yield(seq)

def bruh(file):
  list = []
  sigh = fasta(file)
  for seq in sigh:
    list.append(seq)
  return list

# for data itself
def mr(matrix, i):
  return [row[i] for row in matrix]

def profile(x):
  y = ' '.join([str(item) for item in x])
  return y

def fop(y, x):
  print('{}:'.format(y), profile(x))

def consensus(list, x, *args):
  list = []
  x = []
  for arg in args:
    list.append(arg)
  for i in range(len(list[0])):
    row = mr(list, i)
    a = max(row)
    x.append(row.index(a))
  x = ''.join([str(item) for item in x])
  x = x.translate(str.maketrans('0123', 'ACGT'))
  return x

# matrix is individual one
def search(matrix, x, list, y):
  cnt = 0
  list = []
  while cnt <= (len(matrix[0])):
    for i in range(len(matrix)):
      fre = matrix[i].count(x)
      list.append(fre)
      cnt += 1
  if y == 'yes':
    fop(x, list)
  else:
    return list


seq_list = bruh('rosalind_cons.txt')
sl = [el for el in seq_list]
tl = []

cnt = 0
while cnt < (len(sl[0])):
  for item in sl:
    tl.append(mr(sl, cnt))
    cnt += 1
    if cnt == (len(sl[0])):
      break

# consensus output
conss = []
A = []
C = []
G = []
T = []
con = consensus(profile, conss, search(tl, 'A', A, 'no'), search(tl, 'C', C, 'no'), search(tl, 'G', G, 'no'), search(tl, 'T', T, 'no'))
print(con)

# profile part
search(tl, 'A', A, 'yes')
search(tl, 'C', C, 'yes')
search(tl, 'G', G, 'yes')
search(tl, 'T', T, 'yes')