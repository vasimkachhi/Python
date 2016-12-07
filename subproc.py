import subprocess
subprocess.call("ipconfig")
home = "C:\Users\Vasim\PycharmProjects\pythonpract\string.py"
subprocess.call("python " + home)
subprocess.call("C:\Users\Vasim\PycharmProjects\pythonpract\strOps.py", shell=True)
home = "vasm"
subprocess.call('echo $' + home, shell=True)
