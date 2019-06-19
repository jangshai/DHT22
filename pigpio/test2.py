import pigpio

import DHT22

pi = pigpio.pi()

s = DHT22.sensor(pi, 4)

s.trigger()

time.sleep(0.2)

print("{} {} {:3.2f} {} {} {} {}".format(
   s.humidity(), s.temperature(), s.staleness(),
   s.bad_checksum(), s.short_message(), s.missing_message(),
   s.sensor_resets()))

s.cancel()

pi.stop()