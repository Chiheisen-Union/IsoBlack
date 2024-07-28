# ©️ HellFireDevil18 (https://t.me/HellFireDevi

import os
import subprocess as process

banner = """
█▀ ▀█▀ ▄▀█ █▀█ ▀█▀ █ █▄ █ █▀▀       
▄█  █  █▀█ █▀▄  █  █ █ ▀█ █▄█ ▄ ▄ ▄
"""

banner1 = """
██╗███████╗ █████╗   ██████╗ ██╗      █████╗  █████╗ ██╗  ██╗
██║██╔════╝██╔══██╗  ██╔══██╗██║     ██╔══██╗██╔══██╗██║ ██╔╝
██║███████ ██║  ██║  ██████╦╝██║     ███████║██║  ╚═╝█████═╝ 
██║ ╚═══██ ██║  ██║  ██╔══██╗██║     ██╔══██║██║  ██╗██╔═██╗ 
██║███████  █████╔╝  ██████╦╝███████╗██║  ██║╚█████╔╝██║ ╚██╗
╚═╝╚═════╝  ╚════╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚════╝ ╚═╝ ╚═╝
"""

banner2 = """
█▀▀ █▀█ █▀▄▀█ █▀█ █   █▀▀ ▀█▀ █▀▀ █▀▄
█▄▄ █▄█ █ ▀ █ █▀▀ █▄▄ ██▄  █  ██▄ █▄▀
"""

def autoinstall():
    process.run(["pip3", "uninstall", "isort", "-y"], check=True)
    process.run(["pip3", "uninstall", "black", "-y"], check=True)
    process.run(["pip3", "install", "isort"], check=True)
    process.run(["pip3", "install", "black"], check=True)

def isoblack(directory):
    print(banner)
    autoinstall()
    print(banner1)
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != ".git"]

        py_files = [os.path.join(root, f) for f in files if f.endswith('.py')]
        print(f"Found {len(py_files)} Python files in {root}")  # Debugging print statement
        
        for file in py_files:
            try:
                isort_result = process.run(['python', '-m', 'isort', file], capture_output=True, text=True)
                if isort_result.returncode != 0:
                    print(f"Error formatting {file} with isort: {isort_result.stderr}")
                    continue
                
                black_result = process.run(['python', '-m', 'black', file], capture_output=True, text=True)
                if black_result.returncode != 0:
                    print(f"Error formatting {file} with black: {black_result.stderr}")
                    continue
                
                print(f"Formatted {file}")
            except PermissionError:
                print(f"Permission denied for file: {file}")
                continue
    
    print(banner2)