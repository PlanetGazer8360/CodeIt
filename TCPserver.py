from socket import *
from threading import *

class Listener(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self,host,port):
        s = socket()
        s.bind((host,port))
        s.listen(2)
        c, address = s.accept()

        print("Connection from: " + str(address))
        while True:
            data = c.recv(1024).decode('utf-8')
            if not data:
                break
            print("From connected user: " + data)
            data = data.upper()
            print("Sending: " + data)
            c.send(data.encode('utf-8'))
        c.close()
def main():
    host = '127.0.0.1'
    port = 5001
    call = Listener()
    t = Thread(name="t", target = call.run())
    t.start()
    t1 = Thread(name="t1", target = call.run(host,port))
    t1.start()
    t.join()
    t1.join()



if __name__ == '__main__':
    main()