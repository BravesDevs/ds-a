import fileinput
fwd=0
elevation=0
aim=0

for x in fileinput.input():
    cmd, value = x.strip().split(' ')
    
    if cmd=='forward':
        fwd+=int(value)
        elevation+=aim*int(value)
        print(elevation)

    elif cmd=='up':
        aim-=int(value)
        print(aim)

    else:
        aim+=int(value)
        print(aim)

print(fwd * elevation)