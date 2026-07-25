# swap two numbers with using a third variable
a = 10
b = 20
temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")

#swap two numbers without using a third variable
a = 10
b = 20
a,b = b,a
print(f"After swapping: a = {a}, b = {b}")

#reverse string
s = "chocolate"
print(s[::-1])

# method 2
s = "chocolate"
rev = ""
for ch in s:
    rev = ch+rev
print(f"Reversed string: {rev}")

# a fomd how amny voewls characters are there in a string
s = "chocolate"
v = "aeiou"
count = 0
for ch in s:
    if ch in v:
        count += 1
print(f"Number of vowels in the string: {count}")

# method 2
count = 0
for i in s:
    if i in "aeiou":
        count += 1  
print(f"Number of vowels in the string: {count}")

# to find the number of vowels and consonants in a string
vcount = 0
ccount = 0
for i in s:
    if i in "aeiou":
        vcount += 1
    else:
        ccount += 1
print(f"Number of vowels in the string: {vcount}")
print(f"Number of consonants in the string: {ccount}")

# palindrome check using slicing
p = input("Enter a string to check if it's a palindrome: ")
if p == p[::-1]:
    print(f"{p} is a palindrome")
else:
    print(f"{p} is not a palindrome")

str = input("Enter a string to check if it's a palindrome: ")
rev = str[::-1]
if str == rev:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

# palindrome check without slicing
p = input("Enter a string to check if it's a palindrome: ")
rev = " "
for ch in p:
    rev = ch + rev
if p == rev:
    print(f"{p} is a palindrome")
else:
    print(f"{p} is not a palindrome")

# to find the how many frequency of each character in a string
#method 1
s = "chocolate"
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

# method2
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print(d)

data = {"empid": 101, "name": "John"}
print(data.get("name"))
print(data.get("age", "24"))


# first non frequency in a string
p = "momdad"
for ch in p:
    if p.count(ch) == 1:
        print(f"First non-repeating character: {ch}")
        break

# anagram check slient -> listen
a = "slient"
b = "listen"
if sorted(a) == sorted(b):
    print(f"{a} and {b} are anagrams")
else:
    print(f"{a} and {b} are not anagrams")

# method 2
a = "slient"
b = "listen"
dict1 = {}
dict2 = {}
for ch in a:
    dict1[ch] = dict1.get(ch, 0) + 1
for ch in b:
    dict2[ch] = dict2.get(ch, 0)+1
if dict1 == dict2:
    print(f"{a} and {b} are anagram")
else:
    print(f"{a} and {b} are not anagram")


# find the duplicate characters in a string
s = "programming"
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1

for char, freq in count.items():
    if freq > 1:
        print(char, "->", freq)

# number of words in a string
s = "santhosh is bad boy"
words = s.split()
print(f"no of words in a string:{len(words)} and words are: {words}")
      
# to find the 

para = input("Enter a paragraph: ")
words = para.split()
count = len(words)
print(f"Number of words in the paragraph: {count}")

# ro find the number of word, characters, and sentences in a paragraph
para = input("Enter a paragraph: ")
words = para.split()
count_words = len(words)
print(f" no of words {words} and count of words:{count_words}")

#######################################################
# to find the number of words, characters, and lines in a paragraph
para = input("Enter a paragraph: ")
words = len(para.split())
lines = para.splitlines() # splitlines() method splits a string into a list of lines, breaking at line boundaries.
characters = len(para)
for ch in para:
    if ch == " ":
        characters -= 1
print(f"Number of words: {words}")
print(f"Number of lines: {len(lines)}")     
print(f"Number of characters: {characters}")

#method2
para = input("Enter a paragraph: ")
count = 0
for ch in para:
    count += 1
print("Number of characters:", count)
words = para.split()
count1 = len(words)
lines = para.splitlines()
print(f"Number of words: {count1}")
print(f"Number of lines: {len(lines)}")


# to find how many times a word is repeated in a paragraph
para = input("Enter a paragraph: ")
word = input("Enter a word to find its frequency: ")
words = para.split()
frequency = words.count(word)
print(f"The word '{word}' appears {frequency} times in the paragraph.") 

# to find how many times a word is repeated in a paragraph
para = """python is easy  \
"python is easy to learn"""
p = para.split()
f ={}
for word in p:
    if word in f:
        f[word] += 1
    else:
        f[word] = 1
print(f)

p = """python is easy  
python is easy to learn"""
search = input("Enter a word to find its frequency: ")
words = p.split()
for word in words:
    if word == search:
        print(f" the word {search} appers {words.count(search)} times in the paragraph")
    else:
        print(" the word is not found in the paragraph")

p = """python is easy  
python is easy to learn"""
search = input("Enter a word to find its frequency: ")
words = p.split()
for word in words:
    if word == search:
        print(f" the word {search} appers {words.count(search)} times in the paragraph")
    break

# to find the max ansd min word in a paragraph
list = ["word", "paragraph", "python", "programming"]
max_word = max(list, key=len)
min_word = min(list, key=len)

print(f"Max word: {max_word}, Min word: {min_word}")


p = """python is easy  
python is easy to learn"""
search = input("Enter a word to find its frequency: ")
words = p.split()
for word in words:
    if word == search:
        print(f" the word {search} appers {words.count(search)} times in the paragraph")
    break

# to find the max ansd min word in a paragraph
length = p.split()
print(max(length, key=len))
print(min(length, key=len))

#method2
length = p.split()
max = ""
min = ""
for word in length:
    if len(word) > len(max):
        max = word
    elif len(min) < len(max):
        min = word
print(f"Max word: {max}")
print(f"Min word: {min}")