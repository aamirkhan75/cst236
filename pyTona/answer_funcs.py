import getpass
import random
import socket
import subprocess
import threading
import time
from time import strftime
import threading
import time

seq_finder = None

def feet_to_miles(feet):
    return "{0} miles".format(float(feet) / 5280)

def hal_20():
    return "I'm afraid I can't do that {0}".format(getpass.getuser())

def get_git_branch():
    try:
        process = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_git_url():
    try:
        process = subprocess.Popen(['git', 'config', '--get', 'remote.origin.url'], stdout=subprocess.PIPE)
        output = process.communicate()[0]
    except:
        return "Unknown"

    if not output:
        return "Unknown"
    return output.strip()

def get_other_users():
    try:
        host = '192.168.64.3'
        port = 1337

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send('Who?')
        data = s.recv(255)
        s.close()
        return data.split('$')

    except:
        return "IT'S A TRAAAPPPP"


class FibSeqFinder(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(FibSeqFinder, self).__init__(*args, **kwargs)
        self.sequence = [0, 1]
        self._stop = threading.Event()
        self.num_indexes = 0

    def stop(self):
        self._stop.set()

    def run(self):
        self.num_indexes = 0
        while not self._stop.isSet() and self.num_indexes <= 1000:
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
            self.num_indexes += 1
            time.sleep(.04)

def get_fibonacci_seq(index):
    index = int(index)
    global seq_finder
    if seq_finder is None:
        
        seq_finder = FibSeqFinder()
        seq_finder.start()

    if index > seq_finder.num_indexes:
        value = random.randint(0, 9)
        if value >= 4:
            return "Thinking..."
        elif value > 1:
            return "One second"
        else:
            return "cool your jets"
    else:
        return seq_finder.sequence[index]

def get_fibonacci_seq_list(index):
        index = int (index)
        global seq_finder
        if seq_finder is None:

            seq_finder = FibSeqFinder()
            seq_finder.start()
            seq_finder.join()

        if index > seq_finder.num_indexes:
            return "Number is too big"
        else:
            return seq_finder.sequence[:index]  

def get_fibonacci_seq_list2(start,end):
        start= int (start)
        end = int (end)
        global seq_finder
        if seq_finder is None:

            seq_finder = FibSeqFinder()
            seq_finder.start()
            seq_finder.join()

        if start > seq_finder.num_indexes or end > seq_finder.num_indexes:
            return "Number is too big"
        else:
            return seq_finder.sequence[start : end] 

def get_fibonacci_seq_list3(index):
        index = int (index)
        global seq_finder
        if seq_finder is None:

            seq_finder = FibSeqFinder()
            seq_finder.start()
            seq_finder.join()

        if index > seq_finder.num_indexes:
            return "Number is too big"
        else:
            return seq_finder.sequence[-index:]  

def write_in_a_file():
        mylist = [i**2 for i in range(random.randint(1,12))]
        try: 
            f = open('output.txt', 'a')
            for item in mylist: 
                f.write(strftime("%Y-%m-%d %H:%M:%S ") + str(item)+ '\n')
            f.close()
            return 'writing in the file'
        except: 
            return 'io error'        

                                           





# class FibSeqFinder(threading.Thread):
#     def __init__(self):
#         self.lock = threading.RLock()
#         self.thread = None

#     def start_thread(self):
#         self.lock.aquire()
#         self.thread = threading.Thread(self.proc_data)

#     def stop_thread(self):
#         self.lock.release()

#     def proc_data(self):
#         while not self.lock.aquire(False):
#             print "still running"
#             time.sleep(.05)