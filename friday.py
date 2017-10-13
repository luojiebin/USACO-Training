"""
ID: luojiebin
LANG: PYTHON3
TASK: friday
"""
# input
with open('friday.in', 'r') as fin:
    n = int(fin.readline().strip())

# process
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def compute_weekday(pre_days, pre_weekday):
    return (pre_weekday + pre_days) % 7

def days_in_months(year):
    if is_leap_year(year):
        return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

count = [0 for _ in range(7)]
pre_weekday = 0
pre_year = 1900
for i in range(1900, 1900 + n):
    days_in_month = days_in_months(i)
    pre_days = 366 if is_leap_year(pre_year) else 365
    weekday_of_first = compute_weekday(pre_days, pre_weekday)
    for j in range(12):
        cur_days = sum(days_in_month[:j]) + 12
        weekday = compute_weekday(cur_days, weekday_of_first)
        count[weekday] += 1
    pre_weekday = weekday_of_first
    pre_year = i

# output
with open('friday.out', 'w') as fout:
    fout.write(' '.join([str(c) for c in count[-1:] + count[:-1]]) + '\n')
