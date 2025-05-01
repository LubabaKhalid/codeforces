import sys
import bisect

input = sys.stdin.read

n ,k= map(int,input().split())
s = input()
q = int(input())
queries=[]
for _ in range(k):
    x=input()
    queries.append(x)

# Preprocess: for each character, store all positions in s
positions = [[] for _ in range(k)]
for i, ch in enumerate(s):
    positions[ord(ch) - ord('a')].append(i)

answers = []

for t in queries:
    idx = -1
    broke = False
    for i, ch in enumerate(t):
        ch_index = ord(ch) - ord('a')
        pos_list = positions[ch_index]

        # Binary search to find the first position > idx
        pos = bisect.bisect_right(pos_list, idx)
        if pos == len(pos_list):
            # No valid position in s to match t[i]
            answers.append(len(t) - i)
            broke = True
            break
        else:
            idx = pos_list[pos]

    if not broke:
        answers.append(0)

print("\n".join(map(str, answers)))
