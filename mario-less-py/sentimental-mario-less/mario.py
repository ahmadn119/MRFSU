# TODO
from cs50 import get_int

H = get_int("Height: ")

while (H < 1 or H > 8):
    print("That is an invalid input")
    H = get_int("Height: ")

for i in range(H):
    print(" "*(H-i-1)+"#"*(i+1))