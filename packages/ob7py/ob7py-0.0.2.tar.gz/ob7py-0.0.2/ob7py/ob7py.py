"""
A small package for controlling I/O, controlling motion, and polling data on the Productive Robotics platform.

Allows direct communication with ob7 control over modbusTCP protocol.
ob7py leans heavily on the pyModbusTCP library for register read/write over ethernet,
and the pymodbus library for establishing a virtual "dummy server" for testing functions. 

Basic code example:

Create an instance of the class Robot_:
robot = Robot('123,0,0,3', 5020) #args: server_ip(str) and server_port(int)

robot.connect() #connect to server

robot.movet(1,2,3,1,2,3) #move tool to cartesian x,y,z,roll,pitch,yaw coordinates. Pass one or many values(float).

robot.movet_list(list) #move to cartesian coordinates. Pass all values in list format.

robot.movej(1,2,3,1,2,3,4) #move joints J1-J7 in angular units. Pass one or many values(float)

robot.movej_list(list) #as above, pass in list format.

robot.eoa_in(2) #return the status of an End of Arm input. Takes int 1-4

robot.gei_in(25) #return the status of a General Equipment Interface input. Takes int 1-32

To get a comprehensive list of all gei io and their corresponding registers, run list_all_io(260)
260 to show inputs, 514 to show outputs.

robot.eoa_out(2, 1) # assign the int value 1 to output 2. To just read the current int of eoa output#2, 
    simply omit second argument.

robot.gei_out(25, 1) # as above. Assign 1 to output 25. Read int by omitting second arg.

robot.readt() returns a dictionary of cartesian coordinates for the tool.

robot.readt_list() returns a list (x,y,z,roll,pitch,yaw) for tool.

robot.readj() and robot.readj_list() are similar, but return joint positions. 




author:
me company email address etc
"""

from pyModbusTCP.client import ModbusClient

from struct import pack, unpack


class Robot_:
    """Instance of ModbusTcpClient coupled with methods to control and read ob7."""

    def __init__(self, server_ip, server_port=502):
        """Identify the server and instatiate a client."""

        self.server_ip = server_ip
        self.server_port = server_port
        self.client = ModbusClient(self.server_ip, port=self.server_port)

    def connect(self):
        """Connect to the server."""

        return self.client.open()

    def close(self):
        """Close the connection to the server."""

        self.client.close()

    """
    From pymodbus docs- quick table of modbusclient functions. we are using strictly 4, 6, 
    and 16 for now as all registers are stored as integers or floats, not boolean or traditional
    "coils" as far as i can tell from the ob7 documentation. Experimentation phase will either dispute 
    or bear out this assumption.
    
    the table:

    +------------+-------------------------------+---------------+---------------------------------+
    | Domain     | Function name                 | Function code | ModbusClient function           |
    +------------+-------------------------------+---------------+---------------------------------+
    | Bit        | Read Discrete Inputs          | 2             | read_discrete_inputs()          |
    | Bit        | Read Coils                    | 1             | read_coils()                    |
    | Bit        | Write Single Coil             | 5             | write_single_coil()             |
    | Bit        | Write Multiple Coils          | 15            | write_multiple_coils()          |
    | Register   | Read Input Registers          | 4             | read_input_registers()          |
    | Register   | Read Holding Registers        | 3             | read_holding_registers()        |
    | Register   | Write Single Register         | 6             | write_single_register()         |
    | Register   | Write Multiple Registers      | 16            | write_multiple_registers()      |
    | Register   | Read/Write Multiple Registers | 23            | write_read_multiple_registers() |
    | Register   | Mask Write Register           | 22            | n/a                             |
    | File       | Read FIFO Queue               | 24            | n/a                             |
    | File       | Read File Record              | 20            | n/a                             |
    | File       | Write File Record             | 21            | n/a                             |
    | File       | Read Exception Status         | 7             | n/a                             |
    | Diagnostic | Diagnostic                    | 8             | n/a                             |
    | Diagnostic | Get Com Event Counter         | 11            | n/a                             |
    | Diagnostic | Get Com Event Log             | 12            | n/a                             |
    | Diagnostic | Report Slave ID               | 17            | n/a                             |
    | Diagnostic | Read Device Identification    | 43            | read_device_identification()    |
    +------------+-------------------------------+---------------+---------------------------------+
    """

    def write_float(self, address, value):
        """
        Convert a floating-point number to IEEE 754 format.

        Arguments:
        address: int, the number of the register address we're writing
        value: float, the number we're going to convert and write to register
        """

        data = pack("<f", float(value))

        """
        Write the bytes to the Modbus server, in succesive registers. This is 
        not explicitly called out, but it is whats happening.
        """
        self.client.write_multiple_registers(address, unpack("<HH", data))

    def read_float(self, address):
        """
        Read the bytes from the Modbus server- at address specified, for two consecutive
        registers, from unit=1 (meaning the server typically, or any modbus device we labeled as #1).
        """

        response = self.client.read_holding_registers(address, 2)

        """Combine the bytes and convert to a floating-point number."""
        result = unpack("<f", pack("<HH", response[0], response[1]))[0]

        return result

    def write_uint16(self, address, value):
        """Write a 16-bit unsigned integer(value) to a Modbus register."""

        self.client.write_single_register(address, value)

    def read_uint16(self, address):
        """Read a 16-bit unsigned integer from a Modbus register."""

        response = self.client.read_holding_registers(address, 1)
        return response[0]

    def movet(self, x=None, y=None, z=None, r=None, p=None, yaw=None):
        """Move to tool pos x,y,z, and orient the tool roll, pitch, yaw. Returns bool True"""

        if x:
            self.write_float(1024, x)
        if y:
            self.write_float(1026, y)
        if z:
            self.write_float(1028, z)
        if r:
            self.write_float(1030, r)
        if p:
            self.write_float(1032, p)
        if y:
            self.write_float(1034, yaw)
        # send command to robot command register:
        self.write_uint16(1038, 2)
        return True

    def movet_list(self, cart_list):
        """Move to tool pos x,y,z, and orient the tool roll, pitch, yaw using a list. Returns bool True"""

        if type(cart_list) == list and len(cart_list) == 6:
            """
            deprecated code:
            #x:
            self.write_float(1024, cart_list[0])
            #y:
            self.write_float(1026, cart_list[1])
            #z:
            self.write_float(1028, cart_list[2])
            #r:
            self.write_float(1030, cart_list[3])
            #p:
            self.write_float(1032, cart_list[4])
            #y:
            self.write_float(1034, cart_list[5])
            """
            for reg, value in zip([1024, 1026, 1028, 1030, 1032, 1034], cart_list):
                self.write_float(reg, float(value))

            # send command to robot command register:
            self.write_uint16(1038, 2)

        else:
            return False
        return True

    def movej(self, j1=None, j2=None, j3=None, j4=None, j5=None, j6=None, j7=None):
        """Move to position specified by the following joint angles. Returns bool True"""

        if j1:
            self.write_float(1024, j1)
        if j2:
            self.write_float(1026, j2)
        if j3:
            self.write_float(1028, j3)
        if j4:
            self.write_float(1030, j4)
        if j5:
            self.write_float(1032, j5)
        if j6:
            self.write_float(1034, j6)
        if j7:
            self.write_float(1036, j7)

        # robot command reg:
        self.write_uint16(1038, 1)
        return True

    def movej_list(self, cart_list):
        """Move to position specified by the following joint angles. Returns bool True"""

        if type(cart_list) == list and len(cart_list) == 7:
            """
            deprecated:
            #j1
            self.write_float(1024, float(cart_list[0]))
            #j2
            self.write_float(1026, float(cart_list[1]))
            #j3
            self.write_float(1028, float(cart_list[2]))
            #j4
            self.write_float(1030, float(cart_list[3]))
            #j5
            self.write_float(1032, float(cart_list[4]))
            #j6
            self.write_float(1034, float(cart_list[5]))
            #j7
            self.write_float(1036, float(cart_list[6]))
            """

            for reg, value in zip(
                [1024, 1026, 1028, 1030, 1032, 1034, 1036], cart_list
            ):
                self.write_float(reg, float(value))
            # robot command reg:
            self.write_uint16(1038, 1)

        else:
            return False
        return True

    def grip(self, grippernumber, state):
        """NOTES ON THIS FUNCTION:
        I NEED TO FIGURE OUT HOW TO GET OR SET THE CURRENT TOOL
        IE GRIPPER
        IT IS ADDRESSED IN THE DOCUMENTATION UNDER ASCII COMMANDS,
        BUT NOT IN MODBUS TCP"""

        pass

    def eoa_in(self, eoainum):
        """Read register for End Of Arm input and return it."""

        if 0 < int(eoainum) < 5:
            eoainum += 255
            return self.read_uint16(eoainum)

    def gei_in(self, geiinum):
        """Read register for General Equipment Interface input and return it."""

        if 0 < int(geiinum) < 33:
            geiinum += 259

        """ the register address to ob7py argument scheme is laid out 
            in the below table. It theoretically allows daisy-chaining
            multiple IO units up to 32 i believe, but for the sake of 
            brevity i've only included explicitly typed examples for up to 
            4 IO units. Hence the code above,
            ~~~if 0 < int(geiinum) < 33~~~
            in effect limiting argument range to 1-32
            You can generate the entire list by running self.list_all_io()

            +______________________________________+
            | address | GEI device  1 | ob7py GEI# |
            |   260   |   input 1     |      1     |
            |   261   |   input 2     |      2     |
            |   262   |   input 3     |      3     |
            |   263   |   input 4     |      4     |
            |   264   |   input 5     |      5     |
            |   265   |   input 6     |      6     |
            |   266   |   input 7     |      7     |
            |   267   |   input 8     |      8     |
            ++++++++++++++++++++++++++++++++++++++++
            | address | GEI device  2 | ob7py GEI# |
            |   268   |   input 1     |      9     |
            |   269   |   input 2     |     10     |
            |   270   |   input 3     |     11     |
            |   271   |   input 4     |     12     |
            |   272   |   input 5     |     13     |
            |   273   |   input 6     |     14     |
            |   274   |   input 7     |     15     |
            |   275   |   input 8     |     16     |
            ++++++++++++++++++++++++++++++++++++++++
            | address | GEI device  3 | ob7py GEI# |
            |   276   |   input 1     |     17     |
            |   277   |   input 2     |     18     |
            |   278   |   input 3     |     19     |
            |   279   |   input 4     |     20     |
            |   280   |   input 5     |     21     |
            |   281   |   input 6     |     22     |
            |   282   |   input 7     |     23     |
            |   283   |   input 8     |     24     |
            ++++++++++++++++++++++++++++++++++++++++
            | address | GEI device  4 | ob7py GEI# |
            |   284   |   input 1     |     25     |
            |   285   |   input 2     |     26     |
            |   286   |   input 3     |     27     |
            |   287   |   input 4     |     28     |
            |   288   |   input 5     |     29     |
            |   289   |   input 6     |     30     |
            |   290   |   input 7     |     31     |
            |   291   |   input 8     |     32     |
            ++++++++++++++++++++++++++++++++++++++++
            """
        return self.read_uint16(geiinum)

    def eoa_out(self, eoaonum, arg_=None):
        """
        Read register for End Of Arm output and return it. If argument is passed,
        assign the value to the specified register.
        """

        if 0 < int(eoaonum) < 3:
            eoainum += 511
            if arg_:
                self.write_uint16(eoaonum, arg_)
                return True
            else:
                return self.read_uint16(eoaonum)

    def gei_out(self, geionum, arg_=None):
        """
        Read register for General Equipment Interface ouyput and return it. 
        If argument is passed, assign the value to the specified register.
        """

        if 0 < int(geionum) < 33:
            geionum += 259
            if arg_:
                self.write_uint16(geionum, arg_)
                return True
            else:
                return self.read_uint16(geionum)
    
    def list_all_io(self, base=260):
        """
        Print a table to the terminal illustrating the relationship between ModbusTCP register
        addresses and the arguments we will use to read/write them.

        Arguments:
        base: integer, starting address. 260 to show inputs, 514 to show outputs.
        """

        print("ok....")
        print("")
        print("+______________________________________+")
        for y in range(32):
            print(f"| address | GEI device {(y+1):2d} | ob7py GEI# |")
            for x in range(8):
                print(
                    f"|   {base + x + (y*8)}   |   input {x+1}     |    {(y*8 + x + 1):3d}     |"
                )
            print("++++++++++++++++++++++++++++++++++++++++")
        return None

    def robot_state(self):
        """
        Read the register # 768 and return text describing the Robot's State.
        Returns None otherwise.
        """

        r_state = self.read_uint16(768)
        if r_state == 0:
            return "Disconnected"
        elif r_state == 1:
            return "Idle"
        elif r_state == 2:
            return "Dragging"
        elif r_state == 3:
            return "Teaching"
        elif r_state == 4:
            return "Previewing"
        elif r_state == 5:
            return "Paused"
        elif r_state == 6:
            return "Running"
        elif r_state == 7:
            return "Error"
        else:
            return None

    def obj_gripped(self, gripper_num):
        """
        Return whether a gripper is gripping an object or not.
        """

        # needs work similar to gripper state above -def grip()-
        pass

    def ang_units(self, arg=None):
        """
        Reads/write robot angular units registry.

        Arguments:
        arg: int| can be either 0 or 1. 0 is Degrees(default) and 1 is Radians.

        Example:

        passing no argument returns the current setting in str format.
        example.ang_units()
        returns "Degrees"

        passing an argument (0 or 1) sets the ob7's angular units to Degrees if 0
        is passed, and Radians if any other nonzero integer is passed. Method returns
        boolean True to tell you the function was successful.
        """

        if arg is None:
            if (self.read_uint16(770)) == 0:
                return "Degrees"
            else:
                return "Radians"
        elif arg == 0:
            self.write_uint16(770, 0)
            return True
        else:
            self.write_uint16(770, 1)
            return True

    def dis_units(self, arg=None):
        """Return ob7 distance units. Similar syntactically to ang_units()"""

        units_tuple = ("Meters", "Centimeters", "Millimeters", "Feet", "Inches")

        if arg is None:
            return units_tuple[int(self.read_uint16(771))]
        elif 0 <= arg <= 4:
            self.write_uint16(771, arg)
            return True
        else:
            self.write_uint16(771, 0)
            return False

    def weight_units(self, arg=None):
        """Return ob7 weight units. Similar syntactically to ang_units()"""

        units_tuple = ("Kilograms", "Grams", "Pounds")

        if arg is None:
            return units_tuple[int(self.read_uint16(772))]
        elif 0 <= arg <= 2:
            self.write_uint16(772, arg)
            return True
        else:
            self.write_uint16(772, 0)
            return False

    def readj(self):
        """Return a dictionary of joint names and their respective positions as floats."""

        joint_dictionary = {
            "j1": self.read_float(776),
            "j2": self.read_float(778),
            "j3": self.read_float(780),
            "j4": self.read_float(782),
            "j5": self.read_float(784),
            "j6": self.read_float(786),
            "j7": self.read_float(788),
        }

        return joint_dictionary

    def readj_list(self):
        """Return a list of floats of joint positions in ascending order from j1-j7"""

        joint_list = [
            self.read_float(776),
            self.read_float(778),
            self.read_float(780),
            self.read_float(782),
            self.read_float(784),
            self.read_float(786),
            self.read_float(788),
        ]

        return joint_list

    def readt(self):
        """Return a dictionary of cartesian tool position names and float values"""

        tool_pos_dictionary = {
            "x": self.read_float(790),
            "y": self.read_float(792),
            "z": self.read_float(794),
            "roll": self.read_float(796),
            "pitch": self.read_float(798),
            "yaw": self.read_float(800),
        }

        return tool_pos_dictionary

    def readt_list(self):
        """Return a list of cartesian tool position float values"""

        tool_pos_list = [
            self.read_float(790),
            self.read_float(792),
            self.read_float(794),
            self.read_float(796),
            self.read_float(798),
            self.read_float(800),
        ]

        return tool_pos_list

    def payload(self, value=None):
        """Set weight of payload with value, in current weight units. Return payload if no arg passed."""

        if value is None:
            return self.read_float(774)
        else:
            self.write_float(774, value)
            return True

    def cmd_value(self, reg, val):
        """
        Fill a robot command value register pair with a float.

        Used for a few different functions. There are 7 general purpose floating point variables used for
        positioning the robot, reading out positions, etc...

        Further detail will be provided inside the docstring of the individual methods that utilize
        these registers.

        This method fills one robot command value. cmd_values() will fill all 7 with one call.

        cmd_values() will be req'd for position streaming, to be described later.
        """

        if reg == 1:
            self.write_float(1024, val)
        elif reg == 2:
            self.write_float(1026, val)
        elif reg == 3:
            self.write_float(1028, val)
        elif reg == 4:
            self.write_float(1030, val)
        elif reg == 5:
            self.write_float(1032, val)
        elif reg == 6:
            self.write_float(1034, val)
        elif reg == 7:
            self.write_float(1036, val)
        else:
            return False

    def cmd_values(self, vals):
        """
        Fill all 7 robot command value registers with a single call.

        args: val | list filled with seven items corresponding to the 7 command value regs.
        """

        if type(vals) != list:
            print(
                "cannot evaluate non-list object. Format command values into a list item"
            )
            return False
        else:
            self.write_float(1024, vals[0])
            self.write_float(1026, vals[1])
            self.write_float(1028, vals[2])
            self.write_float(1030, vals[3])
            self.write_float(1032, vals[4])
            self.write_float(1034, vals[5])
            self.write_float(1036, vals[6])
            return True

    def robot_command(self, val):
        """
        Set robot command register, in effect issuing the robot to perform a task, usually
        involving numbers preloaded into the command value registers using cmd_value() or cmd_values()

        0: No command
        1: Move to joint position. The robot will move to the joint
        positions in the robot command values 1-7, which will be
        interpreted using the current angular units.
        2: Move to tool position. The robot will move the tool point to the
        x, y, and z positions in command values 1, 2, and 3 respectively,
        and orient it to the roll, pitch, and yaw values in command values
        4, 5, and 6 respectively.
        3: Begin trajectory. This will begin assembly of a new trajectory.
        4: Add joint trajectory point. This will add a new trajectory point
        using the values in command values 1-7 as the joint positions,
        interpreted as in command 1.
        5: Add tool trajectory point. This will add a new trajectory point
        using the values in command values 1-6 as the tool position,
        interpreted as in command 2.
        6: Execute trajectory. This will begin execution of a trajectory
        started with command 3 and move the robot through points
        added with commands 4 and 5.
        7: Stop move. This will stop any currently executing moves.
        8: Stream joint position. Move the robot to the joint positions
        specified in command values 1-7, interpreted as in command 1.
        See section “Robot Trajectory Streaming”.
        9: Enable joint position streaming. See section “Robot Trajectory
        Streaming”
        10: Move tool relative. When no job is executing, this will offset
        the tool point by the x, y, and z amount in command values 1, 2,
        and 3 respectively, and offset the roll, pitch, and yaw of the tool by
        the command values 4, 5, and 6 respectively. During job execution
        this command may be issued to supply a relative move to an
        Offset Move block.
        11: Open gripper. This will open the gripper to the width specified
        in command value 1.
        12: Close gripper. This will close the gripper to the width specified
        in command value 1.
        13: Stop gripper. Stops any active gripper commands.
        255: Shutdown the robot. This will stop any executing jobs and
        shut down the robot controller.

        """

        if 0 <= val <= 13 or val == 255:
            self.write_uint16(1038, val)
        else:
            return False

    def command_status(self, val):
        """
        Return robot command status: the status of the machine after being issued the previous command.
        """

        status_codes = {
            0x0000: "OK. The last command executed successfully.",
            0x0001: "Building trajectory. A 'begin trajectory' command was issued, and the robot is accepting additional trajectory points.",
            0x0002: "Executing trajectory. An 'execute trajectory' command was issued, and the move is currently in progress.",
            0xF000: "Invalid trajectory. An attempt was made to add a point when no trajectory had been begun.",
            0xF001: "Invalid joint positions. One or more joint positions supplied in the command value registers was invalid. Joint positions must be within the range [-540°, 540°].",
            0xF002: "IK failure. No solution was found for the tool position supplied in the command value registers.",
            0xF003: "Trajectory execution failed. The last commanded move was interrupted.",
            0xF004: "Trajectory point error. An error occurred while adding the last point to the current trajectory.",
            0xF005: "Unknown command. The value written to the command register was not recognized.",
            0xF006: "Unknown error. An unexpected error occurred. Please contact the service department for more information.",
        }

        if val in status_codes:
            return f"Status code: {hex(val)} Description: {status_codes[val]}"
        else:
            return None

    def stream_buffer_size(self, val=None):
        """
        Read/write the value of the stream butter size, default 10 at power up, for trajectory streaming.

        If no argument is passed, return value. If argument is <0, write argument to buffer size register 1040.
        """

        if val is None:
            return self.read_uint16(1040)
        elif val < 0:
            self.write_uint16(1040, val)
            return True

    def gprr(self, add=None, val=None):
        """
        EXPERIMENTAL: Read/write *general purpose robot registers 0 - 31*
        Method written for field experimentation only.
        """

        if add is None:
            return False

        if val is None:
            return self.read_uint16(add)
        else:
            self.write_uint16(add, val)
            return True


def main():
    # Replace 'your_modbus_server_ip' with the actual IP address of your Modbus server

    dummy = input("dummy server (y/n?)")
    dummy
    if dummy == "y":
        modbus_client = Robot_("127.0.0.3", 5020)

        try:
            # Connect to the Modbus server
            if modbus_client.connect():
                print("Connected to Modbus TCP server")

                # Example: Writing a floating-point number to address 512
                modbus_client.write_uint16(address=512, value=3)

                # Example: Reading a floating-point number from address 512
                result = modbus_client.read_uint16(address=512)
                print(f"Read value from Modbus server: {result}")
                modbus_client.write_float(20, 2.5)
                print(modbus_client.read_float(20))

            else:
                print("Unable to connect to Modbus TCP server")

        finally:
            # Close the Modbus connection
            modbus_client.close()


if __name__ == "__main__":
    main()
