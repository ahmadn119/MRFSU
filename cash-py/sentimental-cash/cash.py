# TODO

from cs50 import get_float

coin = 0

while True:
    change_d = get_float("Change owed: ")
    if change_d > 0:
        break

change = round(int(change_d * 100))

while change > 0:
    while change >= 25:
        coin += 1
        change -= 25
    while change >= 10:
        coin += 1
        change -= 10
    while change >= 5:
        coin += 1
        change -= 5
    while change >= 1:
        change -= 1
        coin += 1
print(coin)