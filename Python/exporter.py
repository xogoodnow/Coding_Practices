import os
import time
from prometheus_client import start_http_server, Gauge
import re
import logging

total_requests = Gauge("total_requests", f"This shows the number of total requests in access log" )

total_200s = Gauge("number_of_200s", f"the total number of requests which have recieved 2xx" )
total_300s = Gauge("number_of_300s", f"the total number of requests which have recieved 3xx" )
total_400s = Gauge("number_of_400s", f"the total number of requests which have recieved 4xx" )
total_500s = Gauge("number_of_500s", f"the total number of requests which have recieved 5xx" )


path=str(os.environ.get("ACCESS_LOG_FILE", "/var/log/nginx/access.log"))
port=int(os.environ.get("EXPORTER_PORT", 9876))


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def read_access_logs(path):

    with open(f"{path}", mode="r") as access_log:
        contetnt_of_access_log = access_log.readlines()
        count = len(contetnt_of_access_log)
        return count


def httpstarter(port):

    start_http_server(port)


def set_value_totalrequests(metric):
    metric.set(read_access_logs(path))

def set_value_2xx(metric):
    metric.set(read_200s(path))

def set_value_3xx(metric):
    metric.set(read_300s(path))
    

def set_value_4xx(metric):
    metric.set(read_400s(path))



def set_value_5xx(metric):
    metric.set(read_500s(path))

def read_200s(path):
    count = 0
    with open(f"{path}", mode="r") as file:   
        content_filtered_200 = file.readlines() 
        patern_200 = r'^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (2\d{2}) [0-9\-]+ "(\S+)" "(.+)"$'
        for i in content_filtered_200:
            if re.match(patern_200, i):
                count += 1

        return count



def read_300s(path):
    count = 0
    with open(f"{path}", mode="r") as file:   
        content_filtered_300 = file.readlines() 
        patern_300 = r'^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (3\d{2}) [0-9\-]+ "(\S+)" "(.+)"$'
        for i in content_filtered_300:
            if re.match(patern_300, i):
                count += 1

        return count
    
def read_400s(path):
    count = 0
    with open(f"{path}", mode="r") as file:   
        content_filtered_400 = file.readlines() 
        patern_400 = r'^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (4\d{2}) [0-9\-]+ "(\S+)" "(.+)"$'
        for i in content_filtered_400:
            if re.match(patern_400, i):
                count += 1

        return count
    

def read_500s(path):
    count = 0
    with open(f"{path}", mode="r") as file:   
        content_filtered_500 = file.readlines() 
        patern_500 = r'^(\S+) (\S+) (\S+) \[([\w:\/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (5\d{2}) [0-9\-]+ "(\S+)" "(.+)"$'
        for i in content_filtered_500:
            if re.match(patern_500, i):
                count += 1

        return count
    

if __name__ == "__main__":

    httpstarter(port)
    while True:
        set_value_totalrequests(total_requests)
        set_value_2xx(total_200s)
        set_value_3xx(total_300s)
        set_value_4xx(total_400s)
        set_value_5xx(total_500s)


        
        time.sleep(5)










