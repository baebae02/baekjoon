inp = input()
res = set()
for i in range(0, len(inp)):
    for j in range(i+1, len(inp)+1):
        res.add(inp[i:j])
        
print(len(res))
