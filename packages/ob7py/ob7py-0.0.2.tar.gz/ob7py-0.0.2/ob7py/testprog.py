import ob7py
from time import sleep
add = input("Enter IP address (127.0.0.3): ")
port = input("Enther port number (5020): ")
robot1 = ob7py.ModbusClient_(add, int(port))

def get_input(_prompts):
    # Take as input a list of prompts for input and return their outputs.
    outputs = []
    for x in range(len(_prompts)):
        outputs.append(input(f"{_prompts[x]} ? "))
    return outputs






if robot1.connect():
    print("connected")
else:
    print("Could Not Connect to ModbusTCP Server.")
    for _ in range(3):
        print(".", end="")
        sleep(1)
    print("Exiting!")
    raise SystemExit()

while True:

    print("""
        

        _________________________________
        List of available test functions:
        0) Set robot joint positions
        1) check robot joint positions
        2) set robot cartesian values
        3) check robot cartesian values
        4) check input status
        5) check output status
        6) check set joint positions
        7) Quit
        _________________________________    
    """)
        
    prompt1 = input("Which function to test? ")

    if int(prompt1) == 0: 
        
        joints = get_input(["j1", "j2", "j3", "j4", "j5", "j6", "j7"])
        if robot1.movej_l(joints):
            print("done.")
        else: 
            print("ERROR")
    if int(prompt1) == 7:
        break

    if int(prompt1) == 2:
        print(robot1.readj())
    
    if int(prompt1) == 6:
        for i in range(1024, 1038, 2):
            print(robot1.read_float(i))

        
    



    



    