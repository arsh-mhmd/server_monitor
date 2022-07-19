from tokenize import PlainToken
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,redirect
from getsize import get_size
from getsize1 import get_size1
from check_internet import have_internet
import psutil
from sys import platform
from datetime import datetime
from django.http import HttpResponse
#from get_size1 import get_size1
import time
import math
import os
import socket
import cpuinfo
import uuid
import re
import timeago
import sys
from getmac import get_mac_address as gma
from os import getpid
from os import get_terminal_size





# Create your views here.
def index(request):
    #System Details
    import platform
    uname = platform.uname()
    system = uname.system
    Node_Name =  uname.node
    Release = uname.release
    Version = uname.version
    Machine = uname.machine
    pla = platform.platform()
    Processor = cpuinfo.get_cpu_info()['brand_raw']
    MAC_Address = gma()

    #CPU information
    Total_cores = os.cpu_count()
    Physical_cores = psutil.cpu_count(logical=False)
    ## CPU frequencies
    cpufreq = psutil.cpu_freq()
    Max_Frequency = cpufreq.max
    Min_Frequency = cpufreq.min
    Current_Frequency = round(cpufreq.current)
    ## CPU usage
    cpu_usage = psutil.cpu_percent(percpu=True, interval=0.5)
    Total_CPU_Usage = psutil.cpu_percent

    # RAM Usage
    svmem = psutil.virtual_memory()
    Total = get_size(svmem.total)
    Available = get_size(svmem.available)
    Used = get_size(svmem.used)
    Percentage = svmem.percent
    Free = get_size(svmem.free)

    # Host Name and ip
    hname = socket.gethostname()
    hip = socket.gethostbyname(hname)

    s = psutil.disk_partitions()
    # Find a disk
    disk = []
    for i in range(0,len(s)):
        disk.append(s[i][0])
    #find a disk total storage
    disk_total_storage = []
    for i in range(0,len(disk)):
        disk_total_storage.append(get_size1(psutil.disk_usage(disk[i][:2])[0]))
        #disk_total = sum(disk_free_storage)
    #Find the disk Free storage
    disk_free_storage = []
    for i in range(0,len(disk)):
        disk_free_storage.append(get_size1(psutil.disk_usage(disk[i][:2])[1]))
    #Find the disk Used storage
    disk_used_storage = []
    for i in range(0,len(disk)):
        disk_used_storage.append(get_size1(psutil.disk_usage(disk[i][:2])[2]))
    #Find the disk Used Percentage storage
    disk_storage_percent = []
    for i in range(0,len(disk)):
        disk_storage_percent.append(psutil.disk_usage(disk[i][:2])[3])
    disk_total_storage_dict = dict(zip(disk,disk_total_storage))
    disk_free_storage_dict = dict(zip(disk,disk_free_storage))
    disk_used_storage_dict = dict(zip(disk,disk_used_storage))
    disk_percent_dict = dict(zip(disk,disk_storage_percent))
    disk_count = len(disk)
    disk_total = sum(disk_total_storage)
    disk_free = sum(disk_used_storage)

    #Network and LAN
    LAN = have_internet()

    #Disk 2
    total = int()
    used  = int()
    free  = int()

    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used  += int(psutil.disk_usage(disk.mountpoint).used)
            free  += int(psutil.disk_usage(disk.mountpoint).free)
    Total_disk_space = round(total / (1024.0 ** 3), 4)
    USED_DISK_SPACE = round(used / (1024.0 ** 3), 4)
    FREE_DISK_SPACE = round(free / (1024.0 ** 3), 4)

    #now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)

    #date = datetime.datetime.now()
    #print(timeago.format(date, now))
    #now_date = timeago.format(date, now)

    #battery info

    battery = psutil.sensors_battery()
    
    Battery_percentage = battery.percent
    Battery_plugged = battery.power_plugged

    
    if (Battery_percentage == 100):
        Battery_level = 'Battery full and stable'
    elif (Battery_percentage > 20 and Battery_percentage <= 99):
        Battery_level = 'Your Battery is Good Condition'
    else:
        Battery_level = 'Connect your charger'



    



    sys_info_dict = {'system':system,'Node_Name':Node_Name,'Release':Release,
    'Version':Version,'Machine':Machine,'Processor':Processor,'Total_cores':Total_cores,'Physical_cores':Physical_cores,'Max_Frequency':Max_Frequency,
    'Min_Frequency':Min_Frequency,'Current_Frequency':Current_Frequency,'Total_CPU_Usage':Total_CPU_Usage,'Total':Total,'Available':Available,'Used':Used,
    'Percentage':Percentage,'Free':Free,'disk':disk,'disk_total_storage_dict':disk_total_storage_dict,
    'disk_free_storage_dict':disk_free_storage_dict,
    'disk_used_storage_dict':disk_used_storage_dict,
    'disk_percent_dict':disk_percent_dict,'hname':hname,'hip':hip,
    'disk_count':disk_count,
    'disk_total':disk_total,
    'disk_free':disk_free,
    'LAN':LAN,
    'Total_disk_space': Total_disk_space,
    'USED_DISK_SPACE': USED_DISK_SPACE,
    'FREE_DISK_SPACE': FREE_DISK_SPACE,
    'Battery_percentage':Battery_percentage,
    'Battery_plugged':Battery_plugged,
    'Battery_level':Battery_level,
    'MAC_Address':MAC_Address,
    'platform':pla
    }

    return render(request,'dashboard/index.html',context = sys_info_dict)

def server_details(request):
    #System Details
    import platform
    uname = platform.uname()
    system = uname.system
    Node_Name =  uname.node
    Release = uname.release
    Version = uname.version
    Machine = uname.machine
    pla = platform.architecture()
    Processor = cpuinfo.get_cpu_info()['brand_raw']
    #MAC_Address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    #MAC_Address = (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)for ele in range(0,8*6,8)][::-1]))
    MAC_Address = gma()
    # Reboot server_details
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)

    #CPU information
    Total_cores = psutil.cpu_count(logical=True)
    Physical_cores = psutil.cpu_count(logical=False)
    ## CPU frequencies
    cpufreq = psutil.cpu_freq()
    Max_Frequency = cpufreq.max
    Min_Frequency = cpufreq.min
    Current_Frequency = cpufreq.current
    ## CPU usage
    cpu_usage = psutil.cpu_percent(percpu=True, interval=1)
    Total_CPU_Usage = psutil.cpu_percent
    stat = psutil.cpu_stats()
    ctx = get_size(stat.ctx_switches)
    interrupts = get_size(stat.interrupts)
    syscalls = get_size(stat.syscalls)
    server_info_dict = {'system':system,'Node_Name':Node_Name,'Release':Release,
    'Version':Version,'Machine':Machine,'Processor':Processor,'bt':bt,'Total_cores':Total_cores,'Physical_cores':Physical_cores,'Max_Frequency':Max_Frequency,
    'Min_Frequency':Min_Frequency,'Current_Frequency':Current_Frequency,'cpu_usage':cpu_usage,'Total_CPU_Usage':Total_CPU_Usage,
    'ctx':ctx,'syscalls':syscalls,'interrupts':interrupts,'MAC_Address':MAC_Address,'pla':pla}
    return render(request,'dashboard/server_details.html',server_info_dict)

def cpu_details(request):
    ## CPU usage
    cpu_usage = psutil.cpu_percent(percpu=True, interval=1)
    Total_CPU_Usage = psutil.cpu_percent
    

    cpu_details_dict = {
    'cpu_usage':cpu_usage,
    'Total_CPU_Usage':Total_CPU_Usage
    }

    return render(request,'dashboard/cpu_details.html',cpu_details_dict)

def ram_details(request):
    svmem = psutil.virtual_memory()
    Total = get_size(svmem.total)
    Available = get_size(svmem.available)
    Used = get_size(svmem.used)
    Percentage = svmem.percent
    Free = get_size(svmem.free)

    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    Total_swap =  get_size(swap.total)
    Free_swap = get_size(swap.free)
    Used_swap = get_size(swap.used)
    Percentage_swap = swap.percent
    mem_dict = {'Total':Total,'Available':Available,'Used':Used,'Percentage':Percentage,'Free':Free,'Total_swap':Total_swap,'Free_swap': Free_swap,
    'Used_swap':Used_swap,'Percentage_swap':Percentage_swap}

    return render(request,'dashboard/ram_details.html',context = mem_dict)

def disk_details(request):
    s = psutil.disk_partitions()
    # Find a disk
    disk = []
    for i in range(0,len(s)):
        disk.append(s[i][0])
    #find a disk total storage
    disk_total_storage = []
    for i in range(0,len(disk)):
        disk_total_storage.append(get_size(psutil.disk_usage(disk[i][:2])[0]))
        #disk_total = sum(disk_free_storage)
    #Find the disk Free storage
    disk_free_storage = []
    for i in range(0,len(disk)):
        disk_free_storage.append(get_size(psutil.disk_usage(disk[i][:2])[1]))
    #Find the disk Used storage
    disk_used_storage = []
    for i in range(0,len(disk)):
        disk_used_storage.append(get_size(psutil.disk_usage(disk[i][:2])[2]))
    #Find the disk Used Percentage storage
    disk_storage_percent = []
    for i in range(0,len(disk)):
        disk_storage_percent.append(psutil.disk_usage(disk[i][:2])[3])

    disk_details_dict = {
    'disk':disk,
    'disk_total_storage':disk_total_storage,
    'disk_free_storage':disk_free_storage,
    'disk_used_storage':disk_used_storage,
    'disk_storage_percent':disk_storage_percent
    }
    return render(request,'dashboard/disk_details.html',disk_details_dict)

def network_details(request):
    return render(request,'dashboard/network_details.html')





#def index(request):
#    return render(request, 'dashboard/index.html')


def processes(request):
    #Process
    my_process = psutil.Process(getpid())
    #print("Name:", my_process.name())
    #print("PID:", my_process.pid)
    #print("Executable:", my_process.exe())
    #print("CPU%:", my_process.cpu_percent(interval=1))
    #print("MEM%:", my_process.memory_percent())

    #Name loop
    name_list=[]
    for process in [psutil.Process(pid) for pid in psutil.pids()]:
        try:
            name = process.name()
        except psutil.NoSuchProcess as e:
            Kill = e.pid, "killed before analysis"
        else:
            name_list.append(name)
    #mem loop
    mem_list=[]
    for process in [psutil.Process(pid) for pid in psutil.pids()]:
        try:
            mem = process.memory_percent()
        except psutil.NoSuchProcess as e:
            Kill = e.pid, "killed before analysis"
        else:
            mem_list.append(mem)
    #CPU loop
    cpu_list=[]
    for process in [psutil.Process(pid) for pid in psutil.pids()]:
        try:
            cpu = process.cpu_percent(interval=0.5)
        except psutil.NoSuchProcess as e:
            Kill = e.pid, "killed before analysis"
        else:
            cpu_list.append((cpu/1000)*100)


    Process_details_dict = {
    'name_list':name_list,
    'mem_list':mem_list,
    'cpu_list':cpu_list
    }
    return render(request, 'dashboard/processes.html',Process_details_dict)


def HPC_benchmark(request):
    return render(request, 'dashboard/HPC_benchmark.html')




