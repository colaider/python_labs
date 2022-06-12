from zipfile import ZipFile
import re
patern = '01/Jul/1995+:+0[5-7]+:+[3-4][0-9].+"+ (2[1-9]\d|[3-5]\d\d)|01/Jul/1995+:+0[0-7]+:+5+[0-5].+"+ (2[1-9]\d|[3-5]\d\d)'
file = "access_log_Jul95.zip"
with ZipFile(file, 'w') as zip_file:
    zip_file.write("access_log_Jul95.txt")

with ZipFile(file, 'r') as zip_file:
    unpacked_file = zip_file.extract("access_log_Jul95.txt")

f = open(unpacked_file, "rt", encoding='unicode_escape')
lines = f.readlines()
lin = []
for l in lines:
    if(re.search(patern,l) is not None):
         lin.append(l)
         print(l)

for i in lin:
    print(i)
