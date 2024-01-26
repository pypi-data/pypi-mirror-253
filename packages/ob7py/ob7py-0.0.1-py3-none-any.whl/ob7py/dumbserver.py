# Import necessary modules from pymodbus library
from pyModbusTCP.server import ModbusServer
from pymodbus.datastore import ModbusSequentialDataBlock

# Create a Modbus data block (holding register block) starting at address 0
#store = ModbusSequentialDataBlock(0, [0] * 1000)

# Start a Modbus TCP server at address 127.0.0.1:5020 with the created data block
server = ModbusServer(host="127.0.0.3", port=5020)
server.start()