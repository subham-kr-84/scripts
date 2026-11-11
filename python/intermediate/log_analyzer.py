import json

def read_logs():

  # option-1
  # file = open("application.log","r")  #file open
  # file.readlines()                    #file operaation
  # file.close()                        #file close

  # option-2
  lines = []
  with open("application.log","r") as file:    #with automatically closes, so don't need file closing statement
    lines.extend(file.readlines())

  return lines    

def analyze(lines):
  log_count = {
    "INFO": 0,
    "WARN": 0,
    "ERROR": 0
  }
  for line in lines:
    if "INFO" in line:
      log_count.update({"INFO": log_count["INFO"]+1})
    elif "WARN" in line:
      log_count.update({"WARN": log_count["WARN"]+1})
    elif "ERROR" in line:
      log_count.update({"ERROR": log_count["ERROR"]+1})  
    else:
      pass

  return log_count

def result():
  lines = read_logs()
  counts = analyze(lines)
  
  with open("log_summary.json", "w") as file:
      json.dump(counts, file, indent=4)

result()  

