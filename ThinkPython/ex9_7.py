# find words in given file with three consecutive double letters
# do they exist ??
import sys

def scanfile(filename):
  cnt = 0
  res = []
  f = open(filename)
  for lin in f:
    word = lin.strip()
    if hasTripleDouble(word):
      res.append(word)
  return res

def hasTripleDouble(word):
  if len(word)>5:
    hasThreeDoubles = False
    for i in range(len(word)-5):
      hasThreeDoubles = hasThreeDoubles or (word[i:i+1] == word[i+1:i+2] and word[i+2:i+3] == word[i+3:i+4] and word[i+4:i+5] == word[i+5:i+6])
    return hasThreeDoubles
  else:
    return False

if __name__ == '__main__':
  MyList = scanfile(sys.argv[1])
  for word in MyList:
    print('Match: '  + word )
