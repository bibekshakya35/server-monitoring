#!/usr/bin/python
import subprocess
import os
uptime = subprocess.check_output("w",shell=True)
uptime_results = uptime.decode('utf-8').split(',')
if len(uptime_results) > 0:
    #print(len(uptime_results))
    for uptime_element in uptime_results:
        if 'up' in uptime_element:
            times = uptime_element.split('up')
            time = times[len(times)-1]
            #print(time.strip())
            if "days" in time.strip():
                days = time.strip().split("days")
                print("Current uptime for server : "+days[0] +" \n Status : OK")
                if days[0] > 18:
                    print("Current uptime for server : "+days[0] + "\n Status : Fine")

#Calculate usage of RAM and free space of ram
total_used_ram, used_ram_mb, free_ram_space_mb = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
free_ram_space_gb =float(free_ram_space_mb/1024)
print(" Used RAM in GB : "+str(float(used_ram_mb)/1024))
print(" Free RAM in MB : "+str(free_ram_space_mb))
print(" Free RAM in GB : "+str(free_ram_space_gb))
#check if it is feasible for performing for etl process
if free_ram_space_gb < 4 :
    #It is not feasible
    #Check If there is any qcli process is running
    #which might cause low RAM availability
    qcli_process_running = os.popen("pgrep qcli").readlines()
    if not qcli_process_running:
        print("No qcli process running")
    else:
        print("Qcli process is running")
        print("Number of qcli process running "+str(len(qcli_process_running)))
        for qcli_process in qcli_process_running:
            print("Qcli Process information\n")
            process_detail_information = os.popen('ps ax | egrep "^ '+qcli_process+'"').readlines()
            print(process_detail_information)



