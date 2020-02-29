import subprocess
from datetime import datetime
from collections import deque
import logging
import os



def getInput():
   global queue1,source_file,dest_path,src_file
   print("getInfo called")
   src_file = input("Enter Source File Name: ")
   dest_path = input("Enter Destination Path: ")
   try:
     source_file = open(src_file).readlines()
     queue1=deque(source_file)
     print ("queue depth: ", len(queue1))
   except FileNotFoundError:
     print("FileNotFoundError : Input File Does Not Exists")

def newFunc():
    stime = datetime.now()
    stime = stime.strftime("%H:%M:%S")
    logging.info("Process start: {}".format(stime))
    for i in range(len(queue1)):
       q1 = queue1.popleft()
       logging.info("Queue Length after Popping: {}".format(len(queue1)))
       q1 = q1.rstrip()
       logging.info("Value from Queue : {}".format(q1))
       a = q1.rsplit('.')[0][-2:]
       d_path = dest_path+"/"+str(a)+"/"
       print (f"final dest: {d_path} and q1 value after stripping: {q1}")
       logging.info("Path in which value is being searched : {}".format(d_path))

       entry = os.scandir(d_path)
       for j in entry:
         if q1 in j.name:

           f_path = d_path+j.name
           print (f"final_path: {f_path} and q1_value: {q1}  ")
           logging.info("Path along with value that will be removed : {}".format(f_path))
           subprocess.call(["rm", f_path])
           print ("removed")
    endtime = datetime.now()
    endtime = endtime.strftime("%H:%M:%S")
    logging.info("Process end time: {}".format(endtime))

if _name_ == "__main__":
   logfile="test.log"
   logging.basicConfig(filename=logfile,format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

   getInput()
   logging.info("Source File Name : {}".format(src_file))
   logging.info("Dest Path Name : {}".format(dest_path))
   logging.info("Queue Length : {}".format(len(queue1)))

   newFunc()

