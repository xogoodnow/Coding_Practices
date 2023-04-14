from prometheus_client import Gauge, start_http_server
import re
import os
import time


ram_used = Gauge("Ram_avail", "This metric indicates the amount of used RAM")
ram_percentage_used = Gauge("Ram_percentage_used", "This metric show the percentage of ram being used")
path = str(os.environ.get("PATH_TO_FILE", "/proc/meminfo"))
port = int(os.environ.get("EXPORTER_PORT", "4312"))
mem = {}

def read_meminfo(path):
    '''
    This function read the meminfo file and after finding out the amount of total and free memory,
    it returns the amount of used memory

    '''


    
    with open(path, mode="r") as file:
        meminfo = file.readlines()
        for line in meminfo:
            # match only lines starting with MemTotal or MemFree
            matched=re.match("^Mem(Total|Free):", line)
            if matched:
                key, value = line.split(":")
                key = key.strip()
                value = int(value.split()[0])  # remove the "kB" and convert to integer
                mem[key] = value

    memfree = mem["MemFree"]
    memTotal = mem["MemTotal"]
    used = int(memTotal - memfree)

    return used




def used_memory_percentage():
    '''
    This fucntion calculates the percentage of used memry
    
    '''




    memfree = mem["MemFree"]
    memtotal = mem['MemTotal']

    free_percentage= (memfree * 100) / memtotal
    used_percentage= int(100 - free_percentage)

    return used_percentage


def start_http(port):
    start_http_server(port)


def set_value_used_ram(metric):
    metric.set(read_meminfo(path))


def set_value_perentage(metric):
    metric.set(used_memory_percentage())



if __name__ == "__main__":
    start_http(port)
    while True:
        set_value_used_ram(ram_used)
        set_value_perentage(ram_percentage_used)
        time.sleep(5)

