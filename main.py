import machine
import utime
import I2C_LCD_driver
from machine import Pin

adc = machine.ADC(26)
lcd = I2C_LCD_driver.lcd()
conversion_factor = 100 / (65535)

while True:
    rainCoverage = 100 - (adc.read_u16() * conversion_factor)
    print(round(rainCoverage, 1), "%")
    lcd.lcd_display_string("Rain: {:.1f}%  ".format(rainCoverage,), 1)
    utime.sleep_ms(1000)