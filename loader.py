import time
import sys
print("Loading...")
for i in range(101):
    bar  =  " " * (100-i // 5)+"█" * ((i*2)// 5) + " " * (100-i // 5)
    sys.stdout.write(f"\r{bar}\r{i}\r%\r")
    sys.stdout.flush()
    if i < 40:
        time.sleep(0.15)
    elif i< 70:
        time.sleep(0.20)
    elif i< 90:
        time.sleep(0.30)
    else:
        time.sleep(0.10)
input("\n Press enter to exit") 
 
