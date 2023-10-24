def walk2d():
    coord = 0, 0
    while delta := (yield coord):
       coord = coord[0] + delta[0], coord[1] + delta[1]

send = None
gen = walk2d()
while send != 0:
    coord = gen.send(send)
    print(coord)
    send = eval(input())