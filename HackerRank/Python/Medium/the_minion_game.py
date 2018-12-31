# def minion_game(string):
#     vowels = "AEIOU"
#     consonants = "BCDFGHJKLMNPQRSTVWXYZ"
#
#     length = len(string)
#     words = dict()
#     for i in range(length):
#         for j in range(length + 1):
#             words[string[i : j]] = words.get(string[i : j], 0) + 1
#
#     del words[""]
#
#     consonants_score = sum([words[key] for key in words if consonants.find(key[0]) != -1])
#     vowels_score = sum([words[key] for key in words if vowels.find(key[0]) != -1])
#
#     if consonants_score > vowels_score:
#         print("{} {}".format("Stuart", consonants_score))
#     elif consonants_score < vowels_score:
#         print("{} {}".format("Kevin", vowels_score))
#     else:
#         print("Draw")


vowels = 'AEIOU'

kevsc = 0
stusc = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevsc += (len(s)-i)
    else:
        stusc += (len(s)-i)

if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"

if __name__ == '__main__':
