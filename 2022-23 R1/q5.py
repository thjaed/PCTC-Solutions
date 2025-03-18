word = input()

reversed_word = word[3] + word [2] + word[1] + word[0]

if sorted(reversed_word[0] + word[0])[0] == word[0]:
  print(word)
  print(reversed_word)
else:
  print(reversed_word)
  print(word)