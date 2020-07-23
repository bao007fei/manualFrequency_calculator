import keyboard
import time

start_time = time.time()
count = 0

while True:
    keyboard.wait(hotkey='space')

    count += 1
    total_time = time.time() - start_time

    print(f"{total_time:.2f}s has passed, {count/total_time:.3f}Hz")
