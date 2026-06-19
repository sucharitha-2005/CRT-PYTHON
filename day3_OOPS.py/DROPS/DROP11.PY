class Watch:
    def __init__(self, brand, current_time, battery_percentage):
        self.brand = brand
        self.current_time = current_time
        self.battery_percentage = battery_percentage

    def show_time(self):
        print(f"Current time: {self.current_time}")

    def light_on(self):
        if self.battery_percentage > 5:
            print("Backlight ON ")
            self.battery_percentage -= 1
        else:
            print("Battery too low to use light!")

    def beep(self):
        if self.battery_percentage > 2:
            print("Beep Beep ")
            self.battery_percentage -= 1
        else:
            print("Battery too low to beep!")