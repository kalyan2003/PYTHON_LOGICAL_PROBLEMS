
log_msgs = [ "INFO: System initialized successfully",
    "WARNING: High memory usage detected",
    "ERROR: Unable to connect to database",
    "INFO: User login successful",
    "WARNING: Disk space running low",
    "ERROR: Failed to open configuration file",
    "INFO: Data backup completed",
    "WARNING: Unusual network activity detected",
    "ERROR: Access denied for user",
    "INFO: Scheduled task executed" ]

file = open("log_file.log","w")

for msg in log_msgs:
    file.write(msg + "\n")

file.close()

file1 = open("log_file.log","r")
file = open("output_file.txt","w")

while True:
    line  = file1.readline()
    if line != "":
        if "ERROR" in line:
            file.write(line + "\n")
    else:
        break

file.close()
file1.close()



