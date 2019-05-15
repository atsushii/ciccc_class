total = 0.0
count = 0
inputstr = input("Enter value")
while inputstr != "":
    value = float(inputstr)
    total =+ value
    count =+ 1
    inputstr = input("Enter value")

if count > 0:
    avarage = total / count
else:
    avarage = 0

print(avarage)

NMAX = 4
MMAX = 10

for i in range(1, MMAX + 1):
    print("%10d" % i, end="")
print()

for n in range(1, NMAX + 1):
    print("%10s" % n, end="")
print("\n", "     ", "-" * 35)

for x in range(1, MMAX + 1):
    for n in range(1, NMAX + 1):
        print("%10.0f" % x ** n, end="")

    print()
