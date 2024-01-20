# Should run on any machine with python ;)
# @author Abraham Moruri
# Kenyan phone number generator (python 3.10 but you can use any ver that has the 're' and 'random' packages
import random
import re

__version__ = 1.0
#regex for all the popular network providers (Saf, Airtel, Telkom, Faiba, Equtel)
saf_reg = r'^(?:254|\+254|0)?(7(?:(?:(?!44|47)([01249][0-9]))|(?:5[7-9])|(?:6[8-9]))[0-9]{6})|(^(254|\+254|0)(' \
          r'110|111)[0-9]{6})$ '
telkom_reg = r'^(?:254|\+254|0)?(77[0-6][0-9]{6})$'
airtel_reg = r'^(?:254|\+254|0)?(7(?:(?:[3][0-9])|(?:5[0-6])|(62)|(8[0-9]))[0-9]{6})|(^(254|\+254|0)(100|101|102)[' \
             r'0-9]{6})$ '
faiba_reg = r'^(?:254|\+254|0)?(747[0-9]{6})$'
equitel_reg = r'^(?:254|\+254|0)?(76[3-6][0-9]{6})$'
ke_prefix = random.choice(['0'])  # used to contain 254 / +254


def generate(name):
    num = '0000000000'
    print(f'Generating for: {name}\n')
    if name == 'faiba':
        while not re.match(faiba_reg, num):
            num = ke_prefix + '747' + ''.join([str(random.randint(0, 9)) for _ in range(6)])
            print(num)
    elif name == 'equity':
        while not re.match(equitel_reg, num):
            num = ke_prefix + '76' + ''.join([str(random.randint(0, 9)) for _ in range(6)])
            print(num)
    elif name == 'orange':
        while not re.match(telkom_reg, num):
            num = ke_prefix + '77' + ''.join([str(random.randint(0, 9)) for _ in range(6)])
            print(num)
    elif name == 'airtel':
        while not re.match(airtel_reg, num):
            num = ke_prefix + '7' + ''.join([str(random.randint(0, 9)) for _ in range(6)])
            print(num)
    elif name == 'saf':
        while not re.match(saf_reg, num):
            num = ke_prefix + '7' + ''.join([str(random.randint(0, 9)) for _ in range(10 - len(num))])
            print(num)
    else:
        return


if __name__ == '__main__':
    print("Interactive number generator v1.0.0 (KE-Only) but patterns can be modified or added for more providers\n")
    # How to use : call generate(name of provider) as shown below
    # generate('orange')
    generate('saf')
    # generate('airtel')
    # generate('equity')
    # generate('faiba')
