def complement_1(m):
  height = len(m)
  length = len(m[0])
  h = 0
  while h < height:
    l = 0
    while l < length:
      if m[h][l] == 1:
        m[h][l] = 0
      else:
        if h != l:
          m[h][l] = 1
      l += 1
    h += 1
  return m

m = [[0, 1, 0, 0],
[1, 0, 0, 1],
[0, 0, 0, 1],
[0, 1, 1, 0]]

print(complement_1(m))
#should return
# [[0, 0, 1, 1],
# [0, 0, 1, 0],
# [1, 1, 0, 0],
# [1, 0, 0, 0]]

def complement_2(g):
  gr = {}
  num_vert = len(g)
  for key, value in g.items():
    gr[key] = []
    l = value
    i = 0
    while i < num_vert:
      if i not in l:
        if i != key:
          gr[key].append(i)
      i += 1
  return gr

g = {0: [1, 2, 4],
1: [0, 2, 4],
2: [0, 1, 3],
3: [2, 4],
4: [1, 3]}
print(complement_2(g))
#should be 
# g = {0: [3],
# 1: [3],
# 2: [4],
# 3: [0, 1],
# 4: [0, 2]}

def transpose_1(m):
  mr = []
  max_edge = len(m[0])
  i = 0
  while i < max_edge:
    mr.append([0] * (max_edge))
    i += 1

  height = len(m)
  length = len(m[0])
  h = 0
  while h < height:
    l = 0
    while l < length:
      if m[h][l] == 1:
        mr[l][h] = 1
      else:
        mr[l][h] = 0
      l += 1
    h += 1
  return mr

m2 = [
[0, 1, 0, 1],
[0, 0, 1, 0],
[1, 1, 0, 1],
[0, 1, 1, 0]]

print(transpose_1(m2))
#should return
# [
# [0, 0, 1, 0],
# [1, 0, 1, 1],
# [0, 1, 0, 1],
# [1, 0, 1, 0]]

def transpose_2(g):
  gr = {}
  for key, value in g.items():
    for vert in value:
      if vert not in gr:
        gr[vert] = []
      gr[vert].append(key)
  return gr

g2 = {0: [1, 2, 4],
1: [0, 2, 4],
2: [0, 1, 3],
3: [2, 4],
4: [1, 3]}

print(transpose_2(g2))
#should return
# {0: [1, 2],
# 1: [0, 2, 4],
# 2: [0, 1, 3],
# 3: [2, 4],
# 4: [0, 1, 3]}