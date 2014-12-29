import operator 

charcount = {}
wordcount = {}
f = open('MacBeth.txt')
for lin in f:

  # Adjust word counters
  for word in lin.split():
    word = word.lower()
    if word in wordcount:
      wordcount[word] += 1
    else:
      wordcount[word] = 1

  # Adjust character counters
  for idx in range(len(lin)):
    char = lin[idx:idx+1].lower()
    if char >= 'a' and char <= 'z':
      if char in charcount:
        charcount[char] += 1
      else:
        charcount[char] = 1
f.close()

print(" ===== WORD ANALYSIS ===== ")
sorted_wordlist = sorted( wordcount.items(), key = operator.itemgetter(1), reverse=True)
for i in range(50):
  print(sorted_wordlist[i][0] + " : " + str(sorted_wordlist[i][1]))
print(" ===== FREQUENCY ANALYSIS ===== ")
sorted_charcount = sorted( charcount.items(), key = operator.itemgetter(0))
total = 0
for i in sorted_charcount:
  total += i[1]

print("Char  Count  Freq(%)")
for char in sorted_charcount:
  print(" %1s    %5d    %5.2f" % (char[0], char[1], round(100.0*char[1] / total,2)))
