from urllib.request import urlopen

link = "http://213.108.160.85:666/"

f = urlopen(link)
myfile = f.read()
print(myfile)
x = str(myfile)
x = x.split(':')
print(" ")
print(x)
while(True):
    kotel = input()
    acc = input()
    if(int(kotel) >= 92 or int(acc) >= 80):
        print("PRETOPENO!!!")