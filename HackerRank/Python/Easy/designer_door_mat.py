N, M = map(int, input().split())
#str.center(width, [, fillchar])
    #generate the .|., put them in the middle and surround by "-"
pattern = [('.|.'*(2*i + 1)).center(M, '-') for i in range(N//2)]       #list comprehension
    #this defines the upper image
    #now we just need to insert the middle row
    #and repeat in reverse-fashion the upper image

#put things together using \n
#["WELCOME"] because we are concatenating lists in order to join them using "\n"
print('\n'.join(pattern + ['WELCOME'.center(M, '-')] + pattern[::-1]))

#pattern[ : : -1] gives the reversed string in output









# Enter your code here. Read input from STDIN. Print output to STDOUT
# sval = input()
# N = int(sval.split()[0])
# M = int(sval.split()[1])
#
# def welcome(M):
#     pat = "WELCOME"
#     col = M + 1
#     col = int((col - len(pat)) / 2)
#     return ("-" * col + pat + "-" * col)
#
# def pattern(N, i, center = False):
#     pat = ".|."
#     if center == False:
#         row = i + 1
#     else:
#         row = N - i
#     return(pat * ((row * 2) - 1))
#
# def fill(N, M, i, center = False):
#     pat = "-"
#     col = M + 1
#     col = int((col - len(pattern(N, i, center))) / 2)
#     return (pat * col + pattern(N, i, center) + pat * col)
#
# image = ""
# center = False
# for i in range(N):
#     if (i * 2) == (N - 1):
#         image = image + welcome(M) + "\n"
#         center = True
#         continue
#     image = image + fill(N, M, i, center) + "\n"
#
# print(image)
