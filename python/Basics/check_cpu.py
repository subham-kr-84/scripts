import psutil
# Goal- to ask user for cpu threshold and check if current usage is above that threshold. If it is print alert and send an email.
def check_cpu_threshold():
  cpu_threshold = int(input("Enter the CPU threshold percentage:"))
  current_cpu_usage = psutil.cpu_percent(interval=1)
  if current_cpu_usage > cpu_threshold:
    print(f"Alert! CPU usage is above {cpu_threshold}%. Curret_cpu_usage: {current_cpu_usage}%, sending email...")
  else:
    print(f"CPU usage is normal. Current CPU usage: {current_cpu_usage}%")
    
check_cpu_threshold()
