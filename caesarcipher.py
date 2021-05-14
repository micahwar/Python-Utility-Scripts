letterFreqsOrder = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
alphabet = [chr(x) for x in range(65, 91)]

def addKey(a, k):
    l = ord(a) + k * (a in alphabet)
    return chr(l - (26 * (l > 90 and a in alphabet)) + (26 * (l < 65 and a in alphabet)))

print(addKey(" ", 5))

def caesar(msg, k):
    return "".join([addKey(x, k) for x in msg]).upper()

def getFreqScore(msg):
    freqs = [[x, (msg.count(x)/len(msg)*100)] for x in alphabet]
    freqs.sort(reverse=True, key=lambda x: x[1])
    score = 0
    for x in freqs[:6]:
        if x[0] in letterFreqsOrder[:6]:
            score += 1
    for x in freqs[-6:]:
        if x[0] in letterFreqsOrder[-6:]:
            score += 1
    return score

message = None
while not message:
    cp = str(input("Specify if encoding or decoding (E/D): "))
    if cp.upper() == "E":
        s = "Enter plain text: "
    elif cp.upper() == "D":
        s = "Enter cipher text: "
    message = str(input(s)).upper()

key = input("Enter key: ")
if key.isnumeric():
    key = (int(key) % 26) * (-(-1 + 2 * (cp == "D")))
    print(caesar(message, key))
elif cp == "D" and key == "guess":
    scores = [getFreqScore(caesar(message, i)) for i in range(26)]
    key = scores.index(max(scores))
    print("\n",caesar(message, key))
    print("\nYour key is: ", 26 - key)