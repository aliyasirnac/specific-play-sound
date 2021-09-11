
from playsound import playsound
import time,datetime

def sleep_till_future(f_minute  :int ,file_name : str):
    """
        Bu fonksiyon şu anki zamanı alarak kullanıcının istediği bir dakikaya kadar uyur.
    """

    t = datetime.datetime.today()
    future = datetime.datetime(t.year,t.month,t.day,t.hour,f_minute) 

    if future.minute <= t.minute:
        print("HATA! Gelecekte geçerli bir dakika girin.")

    else:

        print(f"Şu anki zaman: {str(t.hour)}:{str(t.minute)}")
        print(f"Kadar uyuyacak: {str(future.hour)}:{str(future.minute)}")

        seconds_till_future = (future-t).seconds
        time.sleep( seconds_till_future )
        
        print( f"{str(seconds_till_future)} saniye uyudum!")
        playsound(file_name)

sleep_till_future(13,"resources/atack.mp3")
