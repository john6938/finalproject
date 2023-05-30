import subprocess

correct = 0
total = 10

# Test1
cp = subprocess.run(["python3", "fp.py", "milton-paradise.txt", "chesterton-brown.txt", "chesterton-ball.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 1 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-2] == "chesterton-brown.txt" and cp_split[-1] == "1":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test2
cp = subprocess.run(["python3", "fp.py", "austen-emma.txt", "shakespeare-caesar.txt", "burgess-busterbrown.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 2 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "2":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test3
cp = subprocess.run(["python3", "fp.py", "austen-emma.txt", "shakespeare-caesar.txt", "austen-persuasion.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 3 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-2] == "austen-emma.txt" and cp_split[-1] == "1":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test4
cp = subprocess.run(["python3", "fp.py", "milton-paradise.txt", "shakespeare-caesar.txt", "austen-persuasion.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 4 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "2":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test5
cp = subprocess.run(["python3", "fp.py", "bryant-stories.txt", "carroll-alice.txt", "austen-sense.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 5 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "2":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test6
cp = subprocess.run(["python3", "fp.py", "edgeworth-parents.txt", "shakespeare-caesar.txt", "shakespeare-hamlet.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 6 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-2] == "shakespeare-caesar.txt" and cp_split[-1] == "1":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test7
cp = subprocess.run(["python3", "fp.py", "austen-emma.txt", "austen-persuasion.txt", "austen-sense.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 7 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "1":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test8
cp = subprocess.run(["python3", "fp.py", "milton-paradise.txt", "blake-poems.txt", "whitman-leaves.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 8 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "2":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test9
cp = subprocess.run(["python3", "fp.py", "milton-paradise.txt", "bryant-stories.txt", "austen-persuasion.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 9 ---------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-1] == "2":
    print("CORRECT")
    correct += 1
else:
    print("FAIL")
print("\n--------------------------------\n")

# Test10
cp = subprocess.run(["python3", "fp.py", "milton-paradise.txt", "shakespeare-caesar.txt", "shakespeare-hamlet.txt", "TEST"],
                    encoding='utf-8', stdout=subprocess.PIPE)
cp_split = cp.stdout.splitlines()
print("\n--- Test 10 --------------------\n")
for line in cp_split[:-2]:
    print(line)
if cp_split[-2] == "shakespeare-caesar.txt" and cp_split[-1] == "1":
    print("CORRECT")
    correct += 1
else:
    print("FAIL") 
print("\n--------------------------------\n")

print("Accuracy: {}%".format((correct / total) * 100))