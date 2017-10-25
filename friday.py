"""
ID: luojiebin
LANG: PYTHON3
TASK: friday
"""

# input
with open('friday.in', 'r') as fin:
    n = int(fin.readline().strip())

# process
def days_in_months(year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days[1] += 1
    return days

def count_thirteenth(n):
    total = 0
    count = [0 for _ in range(7)]
    for i in range(1900, 1900 + n):
        days = days_in_months(i)
        for j in range(len(days)):
            count[(total + 13) % 7] += 1
            total += days[j]
    return count

# output
count = count_thirteenth(n)
with open('friday.out', 'w') as fout:
    fout.write(' '.join([str(i) for i in count[-1:] + count[:-1]]) + '\n')
