import sys
import threading
import socket
import queue


q = queue.Queue()
class Portscanner(threading.Thread):
    def __init__(self,host):
        super().__init__()
        self.host:str = host
    def run(self):
        while True:
            port = q.get()
            self.scanner(port)
            q.task_done()
    def scanner(self,port):
        conn = socket.socket()
        try:
            conn.connect((self.host,port))
            print("{}端口在打开状态".format(port))
        except:
            pass

if __name__ == "__main__":
    host = sys.argv[1]
    ip = socket.gethostbyname(host)
    start = sys.argv[2]
    end = sys.argv[3]
    threadnum = sys.argv[4]
    for i in range(int(threadnum)):
        t = Portscanner(ip)
        t.start()
    for i in range(int(start), int(end)):
        q.put(i)
    q.join()