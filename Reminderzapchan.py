from win10toast import ToastNotifier
import time
import schedule
import random
import configparser

toaster = ToastNotifier()




def remind(msg):
    config_ini = configparser.ConfigParser()
    config_ini.read("config.ini", encoding="utf-8")
    iconpath = config_ini["DEFAULT"]["icon_path"]
    toaster.show_toast(msg,icon_path = iconpath)
    print("notification sent!")


def main():
    config_ini = configparser.ConfigParser()
    config_ini.read("config.ini", encoding="utf-8")
    wakeup = int(config_ini["DEFAULT"]["wakeup"])
    sleep = int(config_ini["DEFAULT"]["sleep"])
    lang = config_ini["DEFAULT"]["lang"]
    print("Your wakeup time is {} and you are scheduled to sleep at {}. your language is {}".format(wakeup,sleep,lang))
    if lang == "jp":
        for hour in range(wakeup,sleep):
            hour = str(hour).zfill(2)
            rdm = random.randint(-20,20)
            rdm2 = random.randint(-20,20)
            minute = 30-rdm
            print("{}:{}にスタンドのお知らせを出します".format(hour,minute))
            print("{}:{}に水分補給のお知らせを出します".format(hour,30-rdm2))
            schedule.every().day.at("{}:{}".format(hour,minute)).do(remind, "スタンドの時間です！１分程立ってストレッチしましょう")
            schedule.every().day.at("{}:{}".format(hour,minute+1)).do(remind, "もう座っても大丈夫です。")
            schedule.every().day.at("{}:{}".format(hour,30-rdm2)).do(remind, "水を80ml程度飲みましょう")
        ct = 0
        while True:
            schedule.run_pending()
            if ct%3600 == 0:
                print("機能チェック")
            ct += 1
            time.sleep(1)
    elif lang == "en":
        for hour in range(wakeup,sleep):
            hour = str(hour).zfill(2)
            rdm = random.randint(-20,20)
            rdm2 = random.randint(-20,20)
            minute = 30-rdm
            print("I will pop stand up notification at {}:{}".format(hour,minute))
            print("I will pop up hydration notification at {}:{}".format(hour,30-rdm2))
            schedule.every().day.at("{}:{}".format(hour,minute)).do(remind, "Time to Stand! Let's start stretching for 1 minute")
            schedule.every().day.at("{}:{}".format(hour,minute+1)).do(remind, "You may sit now.")
            schedule.every().day.at("{}:{}".format(hour,30-rdm2)).do(remind, "Please drink at least 80ml of water to hydrate yourself!")
        ct = 0
        while True:
            schedule.run_pending()
            if ct%3600 == 0:
                print("Functionality check")
            ct += 1
            time.sleep(1)
    else:
        print("something is wrong with config reading process.")
#1時間に80ml
#スタンド1時間程度に一回 1分程
if __name__ == "__main__":
    #test
    remind("Remineder starts！")
    main()
