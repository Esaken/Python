import time

hours = int( input( "How many hours until your alarm? \n"))
minutes = int( input( "How many minutes until your alarm? \n"))
seconds = int( input( "How many seconds until your alarm? \n"))

hours = hours * 3600
minutes = minutes * 60
seconds = seconds * 1

total_time = hours + minutes + seconds
time.sleep(total_time)

print(" Timer Up: Amka acha ujinga")
