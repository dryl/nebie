import sys
print(sys.stdin.readline())

def silly_age_joke(age):
    if age >= 10 and age <= 13:
        print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
    else:
        print('Что-что?')

silly_age_joke(10)
