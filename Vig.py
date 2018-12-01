from collections import defaultdict


# decryption function for string s and list k
def decrypt(s, k):
    c = 0
    l = len(k)
    key = [ord(x) - 65 for x in k]
    res = []
    for i in s:
        temp =  ord(i) - key[c]
        if temp < 65:
            temp += 26
 
        res.append(chr(temp))
        c = (c + 1) % l
    return res

# find key letter for plaintext e and ciphertext e
def findKey(c, e):
    plain = ord(e) - 65
    temp = ord(c) - plain
    if temp < 65:
        temp += 26
    return chr(temp)

#input string
s = input().upper()

#length
s_len = len(s)

#maxvalue
max_value = 0
key = 1
new_s = s
d = {}

# that can be proven with the cauchy-equation -> the key length is most probably the number r where
# we shift our original string by r and compare the letters of the 2 strings
# we take r when the same positions are maximized
for i in range(4):
    count = 0
    new_s = "0" + new_s
    for j in range(s_len):
        if new_s[j] == s[j]:
            count += 1
    d[i+1] = count
    if count > max_value:
        max_value = count
        key = i + 1
print("Key length")
print(d)
print("Most likely key length: ", key)
print("Type in key length.")
key = int(input())
k = [0 for i in range(key)]

# do this by hand -> look at the frequency table in english. E is the most likely letter and take the letter which appears most often in this position
while True:
    print("Press 'b' for break or other key if you don't want it.")
    if input() == "b":
        break
    else:
        for i in range(key):
            freq = defaultdict(int)
            for j in range(i, s_len, key):
                
                freq[s[j]] += 1
            print(freq)
            print("Brute force key with frequency table, most likely letter is E in English.")
            print("Type in 2 letters: fist one -> encrypted text, second one -> plaintext." )
            print("On separated lines.")
            en = input()
            pl = input()
            k[i] = findKey(en, pl)
        print("Key: ", k)
        print("Encryption: ", decrypt(s, k))
    
        


    
            
            
    
    

            
