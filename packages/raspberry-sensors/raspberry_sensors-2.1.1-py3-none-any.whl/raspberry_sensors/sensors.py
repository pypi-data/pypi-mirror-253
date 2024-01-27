try:
    import busio, board
except:
    raise Exception("[raspberry_sensors] No standard modules 'busio', 'board'")

libs = [1, 1, 1]

try:
    from Adafruit_DHT import DHT22, DHT11, read as dht_read
except:
    libs[0] = 0
    print("[raspberry_sensors] DHT not available, library 'Adafruit-DHT' not installed")

try:
    from adafruit_ads1x15 import analog_in, ads1015
except:
    libs[1] = 0
    print("[raspberry_sensors] ADS not available, library 'adafruit-circuitpython-ads1x15' not installed")

try:
    from mh_z19 import read_from_pwm, read as mhz_read
except:
    libs[2] = 0
    print("[raspberry_sensors] MHZ19 not available, library 'mh-z19' not installed")

class Sensors:
    def __init__(self, loging_error=True) -> None:
        self.loging_error = loging_error
        self.cache = {"humidity": 0.0, "temperature": 0.0, "chanels": [-0, -0, -0, -0], "co2": 0}

        self.libs = libs

        if self.libs[1]:
            try:
                self.ads = ads1015.ADS1015(busio.I2C(board.SCL, board.SDA))
                self.ads_chanels = [
                    analog_in.AnalogIn(self.ads, 0),
                    analog_in.AnalogIn(self.ads, 1),
                    analog_in.AnalogIn(self.ads, 2),
                    analog_in.AnalogIn(self.ads, 3)
                ]
            except Exception as ex:
                if self.loging_error:
                    self.logs(f"ADS init error -> {ex}", "e")

    def logs(self, text, _type="l"):
        color = "\033[1m"
        if _type == "w":
            color = "\033[43m"
        elif _type == "e":
            color = "\033[41m"
        print(f"[\033[30mraspberry_sensors\033[0m]{color}{text}\033[0m")

    def get_dht(self, _type=22, gpio=4):
        if not self.libs[1]:
            if self.loging_error:
                self.logs("DHT not available")
            return {"humidity": self.cache["humidity"], "temperature": self.cache["temperature"]}

        try:
            h, t = dht_read(DHT22 if _type==22 else DHT11, gpio)
            if h and t:
                self.cache["humidity"], self.cache["temperature"] = round(h, 2), round(t, 2)
            else:
                if self.loging_error:
                    self.logs(f"DHT error, used cache", "w")
        except Exception as ex:
            if self.loging_error:
                self.logs(f"DHT error ({ex}), used cache", "w")
        return {"humidity": self.cache["humidity"], "temperature": self.cache["temperature"]}

    def get_mhz(self, gpio=12, pwm=False, _range=5000):
        if not self.libs[2]:
            if self.loging_error:
                self.logs("MHZ19 not available")
            return self.cache["co2"]
        try:
            if pwm:
                self.cache["co2"] = read_from_pwm(gpio=gpio, range=_range)["co2"]
            else:
                self.cache["co2"] = mhz_read()["co2"]
        except Exception as ex:
            if self.loging_error:
                self.logs(f"MHZ19 error ({ex}), used cache", "w")
        return {"co2": self.cache["co2"]}

    def get_ads(self, chanel, interpolate=False, interpolate_min=0, interpolate_max=0):
        if not self.libs[1]:
            if self.loging_error:
                self.logs("ADS not available")
            return 0.0
        if chanel > 3 or chanel < 0:
            if self.loging_error:
                self.logs("The wrong channel is selected, only 0, 1, 2, 3 can be used\nUse chanel 0")
            chanel = 0
        try:
            self.cache["chanels"][chanel] = self.ads_chanels[chanel].voltage
        except Exception as ex:
            if self.loging_error:
                self.logs(f"ADS error ({ex}), used cache", "w")
        if interpolate:
            return round(interpolate_min+(interpolate_max-interpolate_min)*(self.cache["chanels"][chanel]/5),2)
        return self.cache["chanels"][chanel]