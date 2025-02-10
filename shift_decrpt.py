KEY = 3

def enc(s, k):
    s = s.upper()
    e = ''.join(chr(ord(i) + k) for i in s)
    return e

def dec(s, k):
    s = s.upper()
    d = ''.join(chr(ord(i) - k) for i in s)
    return d
    
e = ''
e_text = enc('hello now run', KEY).split('#')


print(e_text)
for i in e_text:
    if len(i) == 3:
        print(i)
        e = i
        break

def find_diff(s):
    d = 0
    incr = 1
    
    for i in range(len(s) - 1):
        d = d - (ord(s[i]) - ord(s[i + 1])) * incr
        incr *= 10
    return d
    


found = ''
file = open('wordlist_threes.txt', 'r')
text = file.readlines()

for word in text:
        if find_diff(e) == find_diff(word.strip()):
            found = word
            break 
    
print(found)

if found:
    fkey = ord(e[0]) - ord(found[0])
    print("KEY:", fkey)
else:
    print("[NOT FOUND]")
    
print("DECRIPTED MSG:", dec(e, fkey))