#reversal of a string along with the execution time 

import time
start=time.time()
n=input()
print(n[::-1])
end=time.time()
print(end-start)
