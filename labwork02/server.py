from xmlrpc.server import SimpleXMLRPCServer
import os
import time


def data_transfer(data_in, file_name, dt):
    handle = open(file_name.split('/')[-1], 'wb')
    handle.write(data_in.data)
#     os.utime(file_name, (time.time(),dt))
    handle.close()
    return True
    


server = SimpleXMLRPCServer(("localhost", 5000))
print("Listening on port 5000...")
server.register_function(data_transfer, "data_transfer")
server.serve_forever()
