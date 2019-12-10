import colorama
from colorama import Fore, Back, Style
from colorama import init
init()
print(Back.WHITE)
print(Fore.BLACK)
Price = float(input('Цена игры в USD: '))
print(Back.BLUE)
print(Fore.WHITE)
Copies = int(input('Количество проданных копий игры: '))
print(Back.RED)
print(Fore.WHITE)
rub = float(input('Курс доллара США: '))
sales_usd = Price * Copies
sales_rub = sales_usd * rub
total_earnings = sales_rub * 0.65
print(Back.BLACK)
print(Style.BRIGHT)
print(Fore.YELLOW)
print(total_earnings)
input()
