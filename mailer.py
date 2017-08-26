import smtplib
import time
from threading import *

class Alumno:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hola " + self.name + ". Tienes " + str(self.age) + " años")


class Mailer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        i = 0
        content = 'HELLO BBBBBBOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOWWWWWWWWWWWWWWW!!!!! THIS IS A TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEST!!!!!! TROOOOOOOOOOLLOLOLOLOLOLOLO!!'
        mail = smtplib.SMTP('smtp.gmail.com:587')

        mail.ehlo()
        mail.starttls()
        mail.login('nesac128@gmail.com', 'Tiresias41812')


        while i <= 5:
            mail.sendmail('nesac128@gmail.com','qcorion@gmail.com', content)
            time.sleep(30)
            i += 1
        mail.close()

if __name__ == '__main__':
    alumno1 = Alumno("Naser", 13)
    alumno2 = Alumno("Sergio",32)
    alumno1.hello()
    alumno2.hello()

    mailer = Mailer
    t = Thread(name = 't', target=mailer.run())
    t2 = Thread(name='t2',target=mailer.run())
    t3 = Thread(name='t3', target=mailer.run())
    t4 = Thread(name='t4',target=mailer.run())
    t5 = Thread(name='t5',target=mailer.run)