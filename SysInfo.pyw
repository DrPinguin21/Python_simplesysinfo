import psutil
import platform
import GPUtil
from datetime import datetime

File = open("System-info.txt", "w")
File.write("Deine Systeminfos: \n")
File = open("System-info.txt", "a")
OS_System = platform.uname()

boot = psutil.boot_time()
bt = datetime.fromtimestamp(boot)

V_memory = psutil.virtual_memory()
S_memory = psutil.swap_memory()

File.write(
    f"System: {OS_System.system}\n"
    f"Node Name: {OS_System.node}\n"
    f"Release: {OS_System.release}\n"
    f"Version: {OS_System.version}\n"
    f"Machine: {OS_System.machine}\n"
    f"Processor: {OS_System.processor}\n\n"

    f"Boot_Date: {bt.day}.{bt.month}.{bt.year} \nBoot_Time:{bt.hour}:{bt.minute}:{bt.second}\n"
)

for cores, perc in enumerate(psutil.cpu_percent(percpu=True, interval=20)):
    File.write(
        "\nCores"
        f"CPU Usage: {psutil.cpu_percent()}%"
        f"Core {cores}: {perc}%"
    )
File.write(
    f"\nMax Frequency: {psutil.cpu_freq().max:.1f}Mhz\n"
    f"Current Frequency: {psutil.cpu_freq().current:.1f}Mhz\n"
)
File.write(
    f"\nVirtual-memory: {V_memory.percent}%\n"
    f"Swap-memory: {S_memory.percent}\n"
)
gpus = GPUtil.getGPUs()
for gpu in gpus:
    File.write(
        f"\nName: {gpu.name}\n"
        f"Used Mem: {gpu.memoryUsed}MB\n"
        f"Total Mem: {gpu.memoryTotal}MB\n"
        f"Temperature: {gpu.temperature} Celsius"
    )
File = open("System-info.txt", "r")
print(File.read())
File.close()
