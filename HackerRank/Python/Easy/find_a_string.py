def count_substring(string, sub_string):
    counter = dict()
    counter[sub_string] = 0
    if len(sub_string) <= len(string):
        for l in range(len(string) - len(sub_string) + 1):
            counter[string[0 + l : len(sub_string) + l]] = counter.get(string[0 + l : len(sub_string) + l], 0) + 1
        result = counter[sub_string]
    else:
        result = 0
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
