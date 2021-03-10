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