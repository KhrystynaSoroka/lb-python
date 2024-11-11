print("У гривнях відсоток річних дорівнює 11,5 %, а у доларах — 4 %")
print("Курс на купівлю долара становить 27 грн, а за рік курс продажу долара прогнозується 28,6")
count=25000
current_rate=27
future_rate=28.6
percent_ua=11.5
percent_usd=4

suma_ua=count*(1+percent_ua/100)

convert_ua_to_usd=count/current_rate
suma_usd=convert_ua_to_usd*(1+percent_usd/100)
convert_suma_usd=suma_usd*future_rate

if suma_ua>convert_suma_usd:
    print("Буде вигідніше вкласти у гривнях: ",suma_ua)
else:
    print("Буде вигідніше вкласти у доларах", convert_suma_usd)
