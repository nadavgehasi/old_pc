from pymsgbox import alert
from time import sleep
import schedule

TIME_BETWEEN_DRINKS = 1
TIME_BETWEEN_WORKOUT = 3

def send_message(title, message):
    alert(text=message, title=title, button='OK')


def configure_scheduler(schedule):
    drink = lambda : send_message("", "REMEMBER TO DIRNK!")
    workout = lambda : send_message("", "REMEMBE TO WORKOUT!!")
    schedule.every(TIME_BETWEEN_DRINKS).hours.do(drink)
    schedule.every(TIME_BETWEEN_WORKOUT).hours.do(workout)

def main():
    configure_scheduler(schedule)
    while True:
        schedule.run_pending()
        sleep(100)

if __name__ == "__main__":
    main()
