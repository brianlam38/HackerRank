# grab stdin
digits = input()
shift = input()

# shift each value rightwards, mod 10
count = 0
while count < len(digits):
    shiftVal = (int(digits[count]) + int(shift)) % 10
    print(shiftVal, end='')
    count += 1

