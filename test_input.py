import sys
import time

print(sys.argv)
if len(sys.argv) < 2:
  print("this script requires an input argument specifying the run time in seconds")
  exit()
  # run_time = 10
else:
  run_time = int(sys.argv[1])
  
count=0
while count < run_time:
  count += 1
  print("taking data entry:",count)
  time.sleep(1) 
