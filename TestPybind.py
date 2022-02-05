import os
os.add_dll_directory("c:\\msys64\\mingw64\\bin")
pid = os.getpid()
print("ProcessID:", pid)



print("Adding 2 and 3");

import example
x=example.add(2,3)
print("result is :", x)
os.system("pause")


''' os.add_dll_directory("C:\\Users\\d91675\\Documents\\GitHub\\Test_PyBind")
os.add_dll_directory("C:\\Users\\d91675\\AppData\\Local\\Programs\\Python\\Python310\\include")
os.add_dll_directory("C:\\Users\\d91675\\AppData\\Local\\Programs\\Python\\Python310\\libs")
os.add_dll_directory("C:\\Users\\d91675\\Documents\\GitHub\\Test_PyBind\\extern\\pybind11\\include") '''

