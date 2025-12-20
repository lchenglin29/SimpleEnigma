import random
import json

WELCOME_MSG = """\033[46mEnigma made by Koala\033[0m
Project note:
- To leave, type \"\033[101m&lv\033[0m\".
- Koala is NOT gay.
- Koala is cute.
"""
RUN = True
LIST_BASE = []
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

def load_json():
  with open('db.json', mode='r', encoding="utf8") as jFile:
      jdata = json.load(jFile)
  jFile.close()
  return jdata

def write_js(data):
  jsdata = json.dumps(data,ensure_ascii=False)
  with open('db.json', mode='w', encoding="utf8") as jFile:
    jFile.write(jsdata)
    jFile.close()

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

print(WELCOME_MSG)
print("Loading...")
db = load_json()
if len(db) == 0:
    LIST_BASE = generate_derangements(letters, 17576)
    write_js(LIST_BASE)
else:
    LIST_BASE = db
print("Done.\n")

if __name__ == "__main__":
    while RUN:
        msg = input("\033[33mEnter your msg:\033[0m")
        if msg == "&lv":
            print("bye!")
            break
        key = int(input("\033[33mEnter your key(0-17575):\033[0m"))
        if key > 17575:
            print("\033[91mYOU ARE GAY.\033[0m")
            continue
        print("\033[33m↓Ciphertext↓\033[0m")
        print(f"{swap(msg.lower(), key)}")