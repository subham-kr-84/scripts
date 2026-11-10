# Goal- to take user input for disk,memory and cpu threshold
# check if current usage is above that threshold.
# If it is, print alert and send an email.

import psutil

def check_system_health():
  disk_threshold = int(input("Enter the disk threshold(%): "))

  memory_threshold = int(input("Enter the memory threshold(%): "))

  cpu_threshold = int(input("Enter the CPU threshold(%): "))

  #CPU usage----------------------

  current_cpu_usage = psutil.cpu_percent(interval=1)

  if current_cpu_usage > cpu_threshold:
    print(f"Alert! CPU usage is above {cpu_threshold}%. Curret_cpu_usage: {current_cpu_usage}%, sending email...")
  else:
    print(f"CPU usage is normal. Current CPU usage: {current_cpu_usage}%")

  #DISK usage----------------------------

  disk = psutil.disk_usage('/')
  print(f"Total Disk space: {disk.total / (1024**3):.2f} GB")
  if disk.percent > cpu_threshold:
    print(f"Alert! Disk usage is above {disk_threshold}%.Current disk usage: {disk.percent}%, free disk space is only: {disk.free / (1024**3):.2f} GB")
    print("sending email.....")
  else:
    print(f"Disk usage is normal, {disk.percent}%")
    print(f"Total free Disk space is {disk.free / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB")

  #Memory(RAM) usage....................
  mem = psutil.virtual_memory()
  print(f"Total RAM: {mem.total / (1024**3):.2f} GB")
  if mem.percent > memory_threshold:
    print(f"Alert! Memory (RAM) usage is above {memory_threshold}%.Current RAM usage: {mem.percent}%, Available memory is only: {mem.available / (1024**3):.2f} GB")
    print("sending email.....")
  else:
    print(f"Memory(RAM) usage is normal, {mem.percent}%")
    print(f"Total RAM available is: {mem.available / (1024**3):.2f} GB / {mem.total / (1024**3):.2f} GB")

check_system_health()    
  


