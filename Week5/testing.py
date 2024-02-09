import time

def count_to_three():
    i = "******"
    count = 5
    for index in range(5):
        print(i[0:count])
        count -= 1
        time.sleep(0.5)  # Pause for 1 second between prints

count_to_three()