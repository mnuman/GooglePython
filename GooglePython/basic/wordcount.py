#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def count_words(filename):
  wd = {}
  fd = open(filename,"rU")
  for line in fd:
    for word in line.lower().split():
      if word in wd:
        wd[word] = wd[word] + 1
      else:
        wd[word] = 1
  return wd
    
def print_words(filename):
  dictWords = count_words(filename)
  for key in sorted(dictWords.keys()):
    print key + ': ' + str(dictWords[key])

def customSort(tuple):
  return tuple[1]
  
def print_top(filename):
  dictWords = count_words(filename)
  sortedDict = sorted(dictWords.items(),key=customSort, reverse=True)
  for i in range(20):
    print sortedDict[i][0] + ': ' + str(sortedDict[i][1])
def print_letters(filename):
  fd = open(filename,"rU")
  letters = {}
  for line in fd:
    for word in line.lower().split():
      for kar in word:
        if kar >= 'a' and kar <= 'z':
          if kar in letters:
            letters[kar] = letters[kar] + 1
          else:
            letters[kar] = 1
  total_letters = 0
  for key in letters.keys(): total_letters = total_letters + letters[key]
  print "Total letters: ", total_letters
  
  for key in sorted(letters.keys()):
#    print key + ': {:>7d, :f}'.format(letters[key], float(letters[key])/total_letters)
    print key + ': {:6.3f}'.format(round(100*float(letters[key])/total_letters,3))
# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount | --countletters} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  elif option == '--countletters':
    print_letters(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
