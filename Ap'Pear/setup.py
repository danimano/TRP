from cx_Freeze import setup, Executable
import os
import sys

os.environ['TCL_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Program Files\\Python36\\tcl\\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

includes = ["tkinter", "_tkinter", "numpy.core._methods", "numpy.lib.format", "tensorflow"]
include_files = ["C:\\Program Files\\Python36\\DLLs\\tcl86t.dll",
                 "C:\\Program Files\\Python36\\DLLs\\tk86t.dll",
                 "C:\\Program Files\\Python36\\DLLs\\_tkinter.pyd",
                 "C:\\Program Files\\Python36\\Lib\\site-packages\\tensorflow\\core\\profiler\\tfprof_log_pb2.py",
                 "C:\\Program Files\\Python36\\Lib\\site-packages\\tensorflow\\python\\profiler\\profiler.py",
                 "C:\\Program Files\\Python36\\Lib\\site-packages\\tensorflow\\include\\tensorflow\\core\\profiler\\tfprof_log.pb.h"]
packages = []

setup(name = "Ap'Pear",
      version = "0.1",
      description = "Test executable",
      options = {"build_exe": { "includes": includes, "include_files": include_files, "packages": packages}},
      executables = [Executable(script = "main.py", targetName = "Ap'Pear.exe", base = base, icon = "images/icon.ico")],
      )

