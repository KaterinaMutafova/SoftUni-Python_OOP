class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        if self.hours < 10:
            hh = f"0{self.hours}"
        else:
            hh = self.hours
        if self.minutes < 10:
            mm = f"0{self.minutes}"
        else:
            mm = self.minutes
        if self.seconds < 10:
            ss = f"0{self.seconds}"
        else:
            ss = self.seconds

        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        elif self.seconds == Time.max_seconds:
            self.seconds = 0
            if self.minutes < Time.max_minutes:
                self.minutes += 1
            elif self.minutes == Time.max_minutes:
                self.minutes = 0
                if self.hours < Time.max_hours:
                    self.hours += 1
                elif self.hours == Time.max_hours:
                    self.hours = 0

        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

print()

time = Time(10, 59, 59)
print(time.next_second())

print()

time = Time(23, 59, 59)
print(time.next_second())








