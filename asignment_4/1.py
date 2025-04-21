t = int(input())
strings = [input() for i in range(t)] 
for s in strings:
    count = 0
    front = 0
    back = len(s) - 1
    while front < back:
        count += abs(ord(s[front]) - ord(s[back]))
        front += 1
        back -= 1
    print(count)