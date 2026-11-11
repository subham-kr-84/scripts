import json

class LogAnalyzer:

  def __init__(self,file_name,output_file):

    self.file_name = file_name
    self.output_file = output_file



  def read_logs(self):

    # option-1
    # file = open("application.log","r")  #file open
    # file.readlines()                    #file operaation
    # file.close()                        #file close

    # option-2
    # lines = []
    with open(self.file_name,"r") as file:    #with automatically closes, so don't need file closing statement
      return file.readlines() 

  def analyze(self):
    log_count = {
      "INFO": 0,
      "WARN": 0,
      "ERROR": 0
    }

    lines = self.read_logs()

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

  def result(self):
    
    counts = self.analyze()

    with open(self.output_file, "w") as file:
        json.dump(counts, file, indent=4)

    print("log summary is: ", counts)    

  # result()  

analyzer = LogAnalyzer("application.log","log_summary.json")
analyzer.result()   

# LogAnalyzer("application.log", "log_summary.json") creates the object. __init__ runs and stores both file names inside it.
# analyzer.result() starts result.
# result calls self.analyze().
# analyze calls self.read_logs(), which opens application.log and returns the list of lines.
# analyze counts the levels and returns the dictionary.
# result writes that dictionary to log_summary.json and prints it.


