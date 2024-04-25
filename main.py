# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
a = 0
a = 1.2
a = 4.24e-10 #4.24 * 10^(-10)

a = 3
b = 4
a ** b
a / b
a % b

a += 1

a = 'Hello World'
a = '''This contains many lines...
Check it
'''

# operations for string
a += a
a *= 2
print("=" * 50)
print("My Program")
print("=" * 50)

a = len(a)
# print(a)

class animal:
    def __init__(self):
        name = ""

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')

def expectedValue(basic_dmg, crit_prob, crit_dmg):
    result = basic_dmg + basic_dmg * (crit_prob / 100) * (crit_dmg / 100)
    print("x = " + str(crit_prob) + ", y = " + str(crit_dmg) + ": " + str(result))

basic_dmg = 10000
count = 0
crit_prob = 0
crit_dmg = 200
while count < 20:
    expectedValue(basic_dmg, crit_prob, crit_dmg)
    crit_prob += 5
    crit_dmg -= 10
    count += 1

expectedValue(10000, 50, 200)
expectedValue(10000, 75, 150)



