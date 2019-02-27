def lots_of_numbers(max):
    import time
    t1 = time.time()
    for x in range(1, max):
        print(x)
        time.sleep(1)
    t2 = time.time()
    print('Прошло %s секунд' % (t2-t1))
lots_of_numbers(6)
