time = input("Enter the value of the time in the format hh:mm:\n")
print(time)

hh = int(float(time.split(":")[0]))
mm = int(float(time.split(":")[1]))

time = time.lower()

numbers = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одинадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
    20: "двадцать",
    21: "двадцать один",
    22: "двадцать два",
    23: "двадцать три",
    24: "двадцать четыре",
    25: "двадцать пять",
    26: "двадцать шесть",
    27: "двадцать семь",
    28: "двадцать восемь",
    29: "двадцать девять",
    30: "тридцать",
    31: "тридцать один",
    32: "тридцать два",
    33: "тридцать три",
    34: "тридцать четыре",
    35: "тридцать пять",
    36: "тридцать шесть",
    37: "тридцать семь",
    38: "тридцать восемь",
    39: "тридцать девять",
    40: "сорок",
    41: "сорок один",
    42: "сорок два",
    43: "сорок три",
    44: "сорок четыре",
    45: "сорок пять",
    46: "сорок шесть",
    47: "сорок семь",
    48: "сорок восемь",
    49: "сорок девять",
    50: "пятьдесят",
    51: "пятьдесят один",
    52: "пятьдесят два",
    53: "пятьдесят три",
    54: "пятьдесят четыре",
    55: "пятьдесят пять",
    56: "пятьдесят шесть",
    57: "пятьдесят семь",
    58: "пятьдесят восемь",
    59: "пятьдесят девять"
    }

hh_decl = {
    1:"первого",
    2:"второго",
    3:"третьего",
    4:"четвертого",
    5:"пятого",
    6:"шестого",
    7:"седьмого",
    8:"восьмого",
    9:"девятого",
    10:"десятого",
    11:"одиннадцатого",
    12:"двенадцатого"
}

mm_decl = {
    1:"одной",
    2:"двух",
    3:"трех",
    4:"четырех",
    5:"пяти",
    6:"шести",
    7:"семи",
    8:"восьми",
    9:"девяти",
    10:"десяти",
    11:"одиннадцати",
    12:"двенадцати",
    13:"тринадцати",
    14:"четырнадцати",
    15:"пятнадцати"
}

minutes = ["минута", "минут", "минуты"]
hours = ["час", "часа", "часов"]

if (hh >= 13) and (hh <= 24):
    hh = hh - 12
if (mm == 0):
    print(f"{numbers.get(hh)} {hours[2]}")      
if (mm < 30 and mm > 0):
    print(f"{numbers.get(mm)} {minutes[1]} {hh_decl.get(hh + 1)}")
if (mm == 30):      
    print(f"пол {hh_decl.get(hh + 1)}")
if (mm > 30) and (mm < 45):
    print(f"{numbers.get(mm)} {minutes[1]} {hh_decl.get(hh + 1)}")   
if (mm >= 45):  
    print(f"без {mm_decl.get(60 - mm)} {minutes[1]} {numbers.get(hh + 1)}") 