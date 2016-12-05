import hashlib

def getMd5(value):
    value = value.encode('utf-8')
    m = hashlib.md5()
    m.update(value)
    return m.hexdigest()

def genInput(input):
    i = 0
    while True:
        yield input+str(i)
        i += 1 

def findPass1(input):
    password = ""
    for value in genInput(input):
        md5Hash = getMd5(value)
        if md5Hash[0:5] == "00000":
            password += md5Hash[5]
            if len(password) == 8:
                return password

def findPass2(input):
    password = [None]*8
    for value in genInput(input):
        md5Hash = getMd5(value)
        if md5Hash[0:5] == "00000":
            try:
                if int(md5Hash[5])>7:
                    continue
                if password[int(md5Hash[5])] == None:
                    password[int(md5Hash[5])] = md5Hash[6]
                if not None in password: 
                    return "".join(password)
            except ValueError:
                pass

# Part 1
# assert findPass1("abc") == "18f47a30"
print(findPass1("ojvtpuvg"))

# Part 2
# assert findPass2("abc") == "05ace8e3"
print(findPass2("ojvtpuvg"))