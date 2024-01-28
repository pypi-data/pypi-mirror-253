from machine import Pin, 
import onewire, ds18x20, time


class DS18b20:
    def __init__(self, pin_number):
        self.ds_pin = Pin(pin_number)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin))

    def getData(self):
        roms = self.ds_sensor.scan()

        if not roms:
            raise RuntimeError("DS18b20 NOT found.")

        self.ds_sensor.convert_temp()
        # time.sleep_ms(1000)

        temp = self.ds_sensor.read_temp(roms[0])
        print(f"Temperature is [{temp}]")
        return temp