import timeit

# def swap_case(s):
#     word = list()
#     for i in s:
#         if not i.isupper():
#             letter = i.upper()
#         else:
#             letter = i.lower()
#         word.append(letter)
#     swapped = "".join(word)
#     return swapped

def swap_case(s):
    word_list = [i.lower() if i.isupper() else i.upper() for i in s]
    swapped= "".join(word_list)
    return swapped

# s = input()
s = "PythonASDJijioasjdiojIJipjsddijioPJaipsjdiPJADAIJOioajisjioJDIOAJDDIOAJPODI"
result = swap_case(s)
print(result)
