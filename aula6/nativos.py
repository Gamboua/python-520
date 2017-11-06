import os
import sys
# import datetime
from datetime import datetime, timedelta

# print(os.getlogin())
# print(os.listdir('/tmp'))
# print(os.rename('calculadora.py', 'calc.py'))
#print(os.system('cat /etc/passwd'))

# print(sys.platform)
# print(sys.builtin_module_names)
# print(sys.argv)

print(datetime.now())
print(timedelta(7))
print(datetime.now() + timedelta(7))
print(datetime.now().strftime('%a'))

data = "Jun 1 2005"
print(datetime.strptime(data, '%b/%d/%Y'))

data1 = datetime.now()
data2 = datetime.now() + timedelta(7)

if data1 < data2:
    print("DATA 1 MENOR")


