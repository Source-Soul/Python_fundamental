with open("BD.txt",mode="r") as file:
    words_all = []
    for line in file.readlines():
         words = line.strip().split(" ")
         words_all += words

    unique_words = set(words_all)
    print(len(words_all))
    print(len(unique_words))

with open("unique_words.txt",mode="w") as file:
  for word in sorted(unique_words) :
      file.write(word+"\n")