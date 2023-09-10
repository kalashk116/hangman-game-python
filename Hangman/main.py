import random
from PIL import Image
words=['exclusive', 'complement', 'hypothesis', 'love', 'remember', 'bestseller', 'escapist', 'glorious', 'sandalwood', 'dangerously', 'contemporary', 'hangman', 'discover', 'department', 'peacekeeping', 'starbucks']
word=random.choice(words)
hidden=''

letters=[]
for i in word:
    letters.append(i)
for i in word:
    hidden += "_"
# print(alpha)

print("THE HANGMAN GAME")
print("In this game you will be given an unknown word from english dictionary, and you have to guess the word.")
print("You will be given number of tries associated with words length")
print(hidden)
k=len(word)
nword=[]
chances = len(word)

for i in word:
    nword.append("_")

while chances>0:
    user = input("Enter a word that you guess is present in the the given string: ".lower())
    chances = chances - 1
    print("chances left: ", chances)

    j = []
    for i in range(len(word)):
        if word[i]==user:
            j.append(i)

    for i in j:
        nword[i]=user
    final=''
    for i in nword:
        final+=i
    print(final)

if final==word:
    print("You guessed the word right. Its " , word)
else:
    print('You have exhausted all the tries. RIP !!!')
    print("The hidden word is : ", word)

