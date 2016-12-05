def realRoomCounter():
    sumId = 0

    with open("input.txt") as input:
        for line in input:
            line = line.rstrip("\n")
            if isReal(line):
                id = int(line.split("-")[len(line.split("-"))-1].split("[")[0])
                sumId += id

    return sumId

def makeCheckSum(dic):
    keys = sorted(dic.keys())[::-1]
    checkSum = []
    for key in keys:
        for char in dic[key]:
            checkSum.append(char)

    return checkSum[:5]


def isReal(line):
    line, checkSum = line.split("[")
    checkSum = checkSum.split("]")[0]
    record = {}
    valRecord = {}

    for char in line:
        if char.isalpha():
            if char in record.keys():
                record[char] += 1
            else:
                record[char] = 1

    for char in record.keys():
        value = record[char]
        if value in valRecord.keys():
            valRecord[value] = sorted(valRecord[value] + [char])  
        else:
            valRecord[value] = [char]

    return "".join(makeCheckSum(valRecord)) == checkSum


def realRooms():
    realRooms = []

    with open("input.txt") as input:
        for line in input:
            line = line.rstrip("\n")
            if isReal(line):
                realRooms.append(line)
    return realRooms


def decode(rooms):
    decodedRooms = {}
    for line in rooms:
        id = int(line.split("-")[len(line.split("-"))-1].split("[")[0])
        line = line.split("[")[0]
        line = line.split("-")
        del line[-1]
        newLine = []


        for word in line:
            newWord = []
            for char in word:
                char = ord(char)-97
                newChar = (char + id)%26
                newWord.append(chr(newChar+97))
                # newWord.append(newChar)
            newLine.append("".join(newWord))
        decodedRooms[(" ".join(newLine))] = id
    return decodedRooms


# Part 1
print(realRoomCounter())
            

rooms = realRooms()
decodedRooms = decode(rooms)

# Part 2
for room in decodedRooms.keys():
    if "north" in room:
        print(decodedRooms[room])












