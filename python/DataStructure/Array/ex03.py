def calculate_vacation_days():
    days_worked = []
    vacation_days = []
    max_vacation_days = 0

    while True:
        days = int(input())
        if days == 0:
            break

        days_worked.append(days)

        if len(vacation_days) > 5 and days < (max_vacation_days * 0.2):
            print("No Holiday")
            continue

        basic_vacation = 2
        additional_vacation = days // 30 * 3
        total_vacation = basic_vacation + additional_vacation

        if days % 7 == 0:
            total_vacation += 5

        if len(vacation_days) > 0 and days > sum(vacation_days) / len(vacation_days):
            total_vacation += 15

        vacation_days.append(total_vacation)
        max_vacation_days = max(max_vacation_days, total_vacation)

        print(f"{total_vacation} Holidays")

    print(f"Most Holidays: {max_vacation_days}")


calculate_vacation_days()