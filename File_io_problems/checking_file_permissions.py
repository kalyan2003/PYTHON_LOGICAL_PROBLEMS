import subprocess

def check_file_permissions():
    try:

        subprocess.run(["chmod", "a-r", "my_file.txt"], check=True)
        print("Read permission removed from 'my_file.txt'.")
    except Exception:
        print("Something went wrong while changing permissions.")


    try:
        with open("../Working_With_Modules/my_file.txt", "r") as file:
            file.read()
        print("File has readable permissions.")
    except IOError:
        print("File does NOT have read permissions.")


    try:
        with open("../Working_With_Modules/my_file.txt", "w") as file:
            file.write("")
        print("File has write permissions.")
    except IOError:
        print("File does NOT have write permissions.")

    try:
        subprocess.run(["./my_file.txt"], check=True)
        print("File has executable permissions. ")
    except Exception:
        print("Something went wrong while executing command.")


check_file_permissions()
