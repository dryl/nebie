import time
print(time.asctime())
print()

def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Неделя %s, банок: %s' % (week, total_cans))

spaceship_building(2)

print()
print(time.asctime())

