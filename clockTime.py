from datetime import datetime
import time


class ClockTime:
    hours: int
    minutes: int
    seconds: int
    # Cache the time since this clock was initialised or set
    start: datetime

    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.setStart()

    def setStart(self) -> None:
        self.start = datetime.now()

    def setHours(self, hours: int) -> None:
        self.hours = hours

    def setMinutes(self, minutes: int) -> None:
        self.minutes = minutes

    def setSeconds(self, seconds: int) -> None:
        self.seconds = seconds

    def setTime(self, hours: int, minutes: int, seconds: int) -> None:
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
        self.setStart()

    # Update time to reflect current time
    def setTimeNow(self) -> None:
        now = datetime.now()
        beginning_of_day = datetime.combine(now.date(), time(0))
        total_seconds = (now - beginning_of_day).seconds
        time = self.parse_time(total_seconds)
        self.setTime(time[0], time[1], time[2])

    # Update time of clock by checking elapsed time.
    def update_time(self) -> None:
        now = datetime.now()
        elapsed_time = (now - self.start).seconds
        time = self.parse_time(elapsed_time)
        total_seconds = self.seconds + time[2]
        time[2] = total_seconds % 60
        total_minutes = self.minutes + time[1] + int(total_seconds / 60)
        time[1] = total_minutes % 60
        total_hours = self.hours + time[0] + int(total_minutes / 60)
        time[0] = (total_hours % 24 - 1) if (
            total_hours % 24 == 1) else total_hours
        self.setTime(time[0], time[1], time[2])

    # Parse an integer, returning a list of [hour, minute, seconds]
    def parse_time(self, totalSeconds: int) -> list[int]:
        seconds = totalSeconds % 60
        totalMinutes = totalSeconds / 60
        minutes = int(totalMinutes % 60)
        totalHours = totalMinutes / 60
        hours = int(totalHours % 24)
        return [hours, minutes, seconds]

    # Always update time before displaying
    def showTime(self) -> None:
        self.update_time()
        print(
            f"Time now is {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


# Get an integer from user input. Input must be less than the given upper_bound
def get_int(prompt, upper_bound: int) -> int:
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Invalid input!")
            continue
        if value > upper_bound:
            print("Input value must be less than " + str(upper_bound) + "!")
            continue
        # Valid input, exit loop
        else:
            break
    return value


def main() -> None:
    clock = ClockTime()
    hours: int = get_int("Set clocks' hour:\n", 24)
    minutes: int = get_int("Set clocks' minute:\n", 60)
    seconds: int = get_int("Set clocks' second:\n", 60)
    clock.setTime(hours, minutes, seconds)
    clock.showTime()
    # To show that the clock actually works,
    # try inputs of 24 59 59 and uncommenting the below code.
    # Limitation- only works while the program is running.
    # Still a functional clock!
    # time.sleep(62)
    # clock.showTime()


if __name__ == '__main__':
    main()
