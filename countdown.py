import time 
count = 10

seconds = time.time()

while seconds > 0:
    print(count)
    time.sleep(1)
    count-=1
    
    if count == 0:
        print ("stopped")
        break
