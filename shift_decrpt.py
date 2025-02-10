# KEY = 3

# def enc(s, k)
#     s = s.upper()
#     e = ''.join(chr(ord(i) + k) for i in s)
#     return e

def dec(s, k):
    s = s.upper()
    d = ''.join(chr(ord(i) - k) for i in s)
    return d
    
# e = enc(input("ENTER TEXT: ").strip(), KEY)
# print(e)
e_text = 'WKLV LV D VHFUHW PHVVDjh WHDW QHHGV WR EH NHSW FRQILGHQWLDODO DQG VDIH'
for i in e.split(): 
    if len(i) == 3:
        e = i
    break

def find_diff(s):
    d = 0
    incr = 1
    
    for i in range(len(s) - 1):
        d = d - (ord(s[i]) - ord(s[i + 1])) * incr
        incr *= 10
    return d
    

file = open('words_all.txt', 'r')

words = []

found = ''
for i in words:
    if find_diff(e) == find_diff(i):
        found = i
        break 
    
if found:
    fkey = ord(e[0]) - ord(found[0])
    print("KEY:", fkey)
else:
    print("[NOT FOUND]")
    
print("DECRIPTED MSG:", dec(e, fkey))