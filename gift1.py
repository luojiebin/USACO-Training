"""
ID: luojiebin
LANG: PYTHON3
TASK: gift1
"""
# input
fin = open('gift1.in', 'r')
total = int(fin.readline().strip())
names = []
money = {}
for _ in range(total):
    someone = fin.readline().strip()
    names.append(someone)
    money[someone] = 0

# process
while True:
    giver = fin.readline().strip()
    if not giver:
        break
    much, num = (int(a.strip()) for a in fin.readline().split())
    lucky = []
    for _ in range(num):
        lucky.append(fin.readline().strip())
    if 0 in [much, num]:
        continue
    money[giver] -= much - much % num
    for name in lucky:
        money[name] += much // num

# output
with open('gift1.out', 'w') as fout:
    for name in names:
        fout.write(name + ' ' + str(money[name]) + '\n')
