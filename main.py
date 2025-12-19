import random

WELCOME_MSG = """Enigma made by Koala

Project note:
- If want to leave, type \"!leave\".
- Koala is NOT gay.
- Koala is cute.
"""
FIRST = True
RUN = True
LIST_BASE = []
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

def perfect_swap_shuffle(arr):
    n = len(arr)
    if n % 2 != 0:
        raise ValueError("Array length must be even")
    res = arr[:]
    idx = list(range(n))
    random.shuffle(idx)

    for i in range(0, n, 2):
        a, b = idx[i], idx[i+1]
        res[a], res[b] = res[b], res[a]
    return tuple(res)

def generate_derangements(seq, k):
    seen = set()
    results = []

    while len(results) < k:
        d =  perfect_swap_shuffle(seq)
        if d not in seen:
            seen.add(d)
            results.append(d)
    return results

def swap(msg:str, key:int):
    nmsg = ""
    for i in range(0,len(msg)):
        if ord(msg[i]) < 97 or ord(msg[i]) > 122:
            nmsg += msg[i]
            continue
        if key + i > 17575:
            nchar = LIST_BASE[key+i-17576][ord(msg[i])-97]
        else:
            nchar = LIST_BASE[key+i][ord(msg[i])-97]
        nmsg += nchar
    return nmsg

while RUN:
    if FIRST:
        print(WELCOME_MSG)
        print("loading...")
        LIST_BASE = generate_derangements(letters, 17576)
        print("done.\n")
    FIRST = False
    msg = input("Enter your msg:")
    if msg == "!leave":
        print("bye!")
        break
    key = int(input("Enter your key(0-17575):"))
    if key > 17575:
        print("\033[31mYOU ARE GAY.\033[0m")
        continue
    print(swap(msg, key))

