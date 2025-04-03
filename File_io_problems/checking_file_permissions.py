import subprocess

def check_file_permissions():
    try:
        
        subprocess.run(["chmod", "a-r", "my_file.txt"], check=True)
        print("Read permission removed from 'my_file.txt'.")
    except Exception:
        print("Something went wrong while changing permissions.")


    try:
        with open("my_file.txt", "r") as file:
            file.read()
        print("File has readable permissions.")
    except IOError:
        print("File does NOT have read permissions.")


    try:
        with open("my_file.txt", "w") as file:
            file.write("")
        print("File has write permissions.")
    except IOError:
        print("File does NOT have write permissions.")

check_file_permissions()
