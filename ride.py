"""
ID: luojiebin
LANG: PYTHON
TASK: ride
"""
# input
with open('ride.in', 'r') as fin:
    comet = fin.readline().strip()
    group = fin.readline().strip()

# process
def value(name):
    val = 1
    for w in name:
        val *= ord(w) - ord('A') + 1
    return val

def judge(comet, group):
    return 'STAY' if value(comet) % 47 != value(group) % 47 else 'GO'

# output
with open('ride.out', 'w') as fout:
    fout.write(judge(comet, group) + '\n')
