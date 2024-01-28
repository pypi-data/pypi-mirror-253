# Program to read flow sensor and display flow rate in Serial Monitor.
from machine import Pin
from time import sleep
import utime
import ujson
import uasyncio



# class YFS201_Control:
#     def __init__(self):
#         """
#         """
#         global in_progess
#     async def control():
#         while True:
#             led.duty(brightness)
#             await uasyncio.sleep(1)
#             led.duty(0)
#             await uasyncio.sleep(1)


class YFS201:
    def __init__(self, pin_number):
        self.sensor_pin = Pin(pin_number, Pin.IN)
        self.sensor_pin.irq(trigger=Pin.IRQ_FALLING, handler=self.handle_interrupt)

        # Configure water flow variables
        global flow_frequency
        flow_frequency = 0

        self.in_progess = False
        self.init_time = utime.ticks_ms()
        self.FLOW_CALIB = 75
        self.liters_p_minute = 0.0
        self.total_milliliters_ODM = 0.0


    def handle_interrupt(pin):
        flow_frequency += 1

    async def startMonitor(self):
        self.in_progess = True
        self.start_time = utime.ticks_ms()
        flow_frequency = 0
        self.liters_p_minute = 0.0
        self.milliliters_p_second = 0.0
        self.total_milliliters = 0.0

        while self.in_progess:
            print("")
            print("*"*30)
            self.liters_p_minute = flow_frequency / self.FLOW_CALIB
            self.milliliters_p_second = self.liters_p_minute * 1000 / 60
            print(f"Flow Speed: {round(self.liters_p_minute, 2)} L/min")
            print(f"Flow Speed: {round(self.milliliters_p_second, 2)} mL/s")

            # Calculate total liters based on liters per minute and elapsed time
            current_time = utime.ticks_ms()
            elapsed_time = utime.ticks_diff(current_time, self.start_time) / 1000
            # print(f"elapsed_time: {elapsed_time}")

            self.total_milliliters += self.milliliters_p_second * elapsed_time
            self.total_milliliters_ODM += self.milliliters_p_second * elapsed_time

            # Print total milliliters and reset count
            print(f"New water flow: {round(self.total_milliliters, 2)} mL")
            print(f"Total water flow: {round(self.total_milliliters_ODM, 2)} mL")

            if self.total_milliliters >= 300:
                print("[INFO] 300 mL reached. ")

            if flow_frequency > 0:
                print(f"new conspumption: {self.total_milliliters} mL")
                data = {"consumption": self.total_milliliters}
                msg = ujson.dumps(data).encode()
                self.total_milliliters = 0
            flow_frequency = 0

            sleep(1)

    async def stopMonitor(self):
        self.in_progess = False



if __name__ == "__main__":
    D_YFS201 = YFS201(15)
    sleep(2)
    D_YFS201.startMonitor()
    sleep(10)
    D_YFS201.stopMonitor()





