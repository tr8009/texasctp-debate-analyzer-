total = 0


with open('1-14 Transcript.txt') as f:
    string = f.read()
    for line in f:
        total += line.count("Trump")

print(total)

arr = string.split("\n\n")
print (arr[2])
