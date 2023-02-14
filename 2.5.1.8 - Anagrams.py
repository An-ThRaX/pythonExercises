# determine whether 2 words are each other's anagrams
def is_anagram(root, anagram):
    result = False
    root = sorted(list(''.join(root.split()).lower()), reverse=False)
    anagram = sorted(list(''.join(anagram.split()).lower()), reverse=False)
    print(root, anagram)
    if root == anagram:
        result = True
    return result


initial_word = input("Please insert your first word: ")
while len(initial_word) < 1:
    initial_word = input("Please insert your first word: ")
anagram_word = input("Please insert your second word: ")
while len(anagram_word) < 1:
    anagram_word = input("Please insert your second word: ")

if is_anagram(initial_word, anagram_word):
    print("It's an anagram!")
else:
    print("It's not an anagram!")

# # 2nd implementation
# initial_word = input("Please insert your first word: ")
# while len(initial_word) < 1:
#     initial_word = input("Please insert your first word: ")
# anagram_word = input("Please insert your second word: ")
# while len(anagram_word) < 1:
#     anagram_word = input("Please insert your second word: ")
#
# result = False
# initial_word = sorted(list(''.join(initial_word.split()).lower()), reverse=False)
# anagram_word = sorted(list(''.join(anagram_word.split()).lower()), reverse=False)
# if initial_word == anagram_word:
#     result = True
# if result is True:
#     print(f"It's an anagram!")
# else:
#     print(f"It's not an anagram!")
