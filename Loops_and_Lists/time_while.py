import time

# seconds passed since the Epoch e.g. January 1 1970

print(time.time())

t_0 = time.time()

while time.time() - t_0 < 10:
    print('...I like while loops!')
    time.sleep(2.5)
print('Oh, no! The loop is over!')