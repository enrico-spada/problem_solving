from collections import OrderedDict

def merge_the_tools(string, k):
    n = len(string)
    for i in range(0, n, k):
        print(''.join(list(OrderedDict((c,0) for c in string[i : i + k]).keys())))

if __name__ == '__main__':
