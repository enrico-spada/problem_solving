def print_rangoli(n):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")[0 : n][ : : -1]
    width = len(alphabet[1:n])*4 + 1
    pattern = list()
    if n == 1:
        pattern = "a"
    else:
        pattern = [
                    (
                            "-".join(alphabet[0 : i]) + "-" + alphabet[i] + "-" + "-".join(alphabet[0 : i][::-1])
                     ).center(width, "-")
                    for i in range(n)]
    print("\n".join(pattern + pattern[ : -1][ : : -1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



# import string
# alpha = string.ascii_lowercase
#
# n = 7
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
# print('\n'.join(L[:0:-1]+L))
