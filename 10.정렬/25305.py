N, k = map(int, input().split())
ppl = list(map(int, input().split()))
ppl.sort()

print(ppl[-k])