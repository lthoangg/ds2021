from tkinter import Tk as tk
from tkinter.filedialog import askopenfilename
from xmlrpc.client import ServerProxy, Binary
import os
import datetime

proxy = ServerProxy("http://localhost:5000/")

tk().withdraw()
file_name = askopenfilename()
print(file_name)

dt = os.stat(file_name).st_ctime
time = datetime.date.fromtimestamp(dt).strftime('%d-%m-%Y')
print(time)

file =  open(file_name, 'rb')
bin_data = Binary(file.read())
proxy.data_transfer(bin_data, file_name, dt)