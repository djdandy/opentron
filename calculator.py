import math

print('Is the source a... \n a) 15 mL conical \n b) 50 mL conical')
choice=input()
if choice=='a':
    print('What is the volume (µL) of the source?')
    source=float(input())
    print('What is the volume (µL) of the aliquot?')
    ali_vol=float(input())
    print('How many aliquots?')
    ali_num=float(input())
    remain=(source-ali_vol*ali_num)-400
    if remain>=1500:
        depth=math.floor((0.006*(remain)-8.7638)+23)
        print('Set aspiration tip position to '+str(depth)+' mm')
    else:
        print('Set aspiration tip position to 1.5 mm')
elif choice=='b':
    print('What is the volume (µL) of the source?')
    source=float(input())
    print('What is the volume (µL) of the aliquot?')
    ali_vol=float(input())
    print('How many aliquots?')
    ali_num=float(input())
    remain=(source-ali_vol*ali_num)-3000
    if remain>=3300:
        depth=math.floor((0.002*(remain)-6.2216)+17)
        print('Set aspiration tip position to '+str(depth)+' mm')
    else:
        print('Set aspiration tip position to 1.5 mm')
else:
    print('Restart the program and pick a valid conical.')
print('Press Enter to close.')
input()
