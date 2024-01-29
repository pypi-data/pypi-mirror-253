import os
from pathlib import Path
import getpass
import ipaddress

# Use setup.name or any other attribute you need
package_name = 'psrx'
files = ['Backup','Excel Outputs','logs']

# Specify the path of the new folder


for x in files:
    # Specify the path of the new folder
    new_folder_path = Path(f"C:\{package_name}\{x}")  # Update the path as needed

    # Create the new folder
    new_folder_path.mkdir(parents=True, exist_ok=True)

# Define the path to the Backup folder
backup_folder = f"C:\{package_name}\Backup"  # Adjust the path here



# List files in the Backup folder

backup_files = os.listdir(backup_folder)


    
def netconf():
    option = input('Enter box name (Optional): ')
    
    while True:
        ssh = input('Enter IP to connect: ')
        if is_valid_ipv4(ssh):
            break
        else:
            print('Invalid IP, Please try again.')
    user = input('Enter your username: ')
    password = getpass.getpass("Enter your password: ")
    if option == '' or option == None:
        return [ssh,user,password]
    else:
        return [option,ssh,user,password]

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ipaddress.AddressValueError:
        return False
    

def loacls_Backup():

    chosen_files = []
    for i, file in enumerate(backup_files):
        chosen_files.append(file[:-4])
    return chosen_files

        
 
def open_local_backup_file(file_name):
    chosen_file = os.path.join(backup_folder, f'{file_name}.txt')

    # Search for the word 'World!' in the chosen file
    with open(chosen_file, "r") as file:
    
        lines = file.read()
        
        file_contents = lines.strip().split('\n')
        
        return file_contents
            