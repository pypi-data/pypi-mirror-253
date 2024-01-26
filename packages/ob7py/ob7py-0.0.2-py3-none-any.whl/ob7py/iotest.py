from struct import pack,unpack

def list_all_io(base = 260):
    
    print("ok....")
    print("")
    print("+______________________________________+")
    for y in range (32):
        
        print(f"| address | GEI device {(y+1):2d} | ob7py GEI# |")
        for x in range(8):
            print(f"|   {base + x + (y*8)}   |   input {x+1}     |    {(y*8 + x + 1):3d}     |")
        print("++++++++++++++++++++++++++++++++++++++++")    
"""
class testClass:
    def __init__(self, testnum):
        self.testnum= testnum

    def mult1(self, x):
        #print(x * 2)
        return x * 2
    
    def mult2(self, x):
        print(self.mult1(3))
        #return x *3

testnum1 = testClass(5)

print(testnum1.mult2(2))


for j in range(8):
    print(f"#j{j}")
    print(f"self.write_float({1022 + (j * 2)}, j{j})") 

"""
def test2():
    from struct import pack, unpack
    data = pack('<f', 7.0)
    print(unpack('<HH', data))

#list_all_io(200)

def test4(arg=0):
    if arg == 0:
        return "test"
    if arg != 0:
        return arg* 2

#print(test4(4))



test_dictionary = {
    "poop":1,
    "pee" :12
}

listy = [1,2,3,4,5,6]

if type(listy) != list: print("list")
if type(listy) == list: print("list2")

print(listy[1])

val = 0
if 0 <= val <= 13 or val == 255:
    print(val)
else: print("invalid")

butt = 0x0000

print(hex(butt))

def cheese(poop):
    if poop is None: 
        print("nothing passed")
    else: print(poop)

cheese()
