import textwrap
import math

def wrap(string, max_width):
    paragraph = list()
    for i in range(math.ceil(len(string) / max_width)):
        paragraph.append(string[i * max_width : (i + 1) * max_width])
    pagr = "\n".join(paragraph)
    return (pagr)

#Pre-built solution:
# "\n".join(textwrap.wrap(text = string, width = max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
