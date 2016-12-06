from collections import Counter

def decrypt(data_file, part):
    message = []
    with open(data_file) as f:
        data = [line.strip("\n") for line in f]

    n = len(data[0])
    arr = [""]*n
    for line in data:
        for i,char in enumerate(line):
            arr[i] += char

    for line in arr:
        line = Counter(line)

        if part == 1:
            message.append(line.most_common(1)[0][0])
        elif part == 2:
            message.append(list(reversed(line.most_common()[-1:][0][0]))[0])

    return "".join(message)


# Part 1
assert decrypt('test_data.txt', 1) == 'easter'
print(decrypt('data.txt', 1))

# Part 2
assert decrypt('test_data.txt', 2) == 'advent'
print(decrypt('data.txt', 2))