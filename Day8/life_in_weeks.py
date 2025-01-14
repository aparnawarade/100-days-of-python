def life_in_weeks(age):
    total_weeks=90*52
    leaved_weeks=age*52
    remaining_weeks=total_weeks-leaved_weeks
    print(f'You have {remaining_weeks} weeks left.')

def main():
    age=int(input())
    life_in_weeks(age)
