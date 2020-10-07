first_day = 2
final_day = 10
days = 0

while first_day < final_day:
    days += 1
    first_day = first_day + 0.1 * first_day
    print(f'{days}-й день :', '%.2f' % first_day)
    if first_day >= final_day:
        break#
