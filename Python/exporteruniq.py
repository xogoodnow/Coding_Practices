import time
import os
from prometheus_client import start_http_server, Gauge

import re
import psutil


port=int(os.environ.get("PORT_NUMBER", 5435))
number_of_unique_ips=Gauge("No_of_unique_IPs", "This metrics shows the nunmber of uniques IPs which are connected to the server with stablished status")



def count_unique_ips():
    ips=[]
    
    connections = psutil.net_connections()

    for connection in connections:
        status = connection.status
        if status == "ESTABLISHED":
                ips.append(connection.raddr.ip)
                

    unique_ips=[]
    for i in ips:
        if i not in unique_ips:
                unique_ips.append(i)
    number_of_ips=len(unique_ips)

    return number_of_ips

    




def prometheus_start(port):
      start_http_server(port)
      


def set_metric_uniqu_ips(metric):
      metric.set(count_unique_ips())
      


if __name__ == "__main__":
      prometheus_start(port)
      while True:
        set_metric_uniqu_ips(number_of_unique_ips)
        time.sleep(5)

            



