import streamlit as st
import subprocess
import platform

def get_active_interface():
    current_os = platform.system().lower()
    if "windows" in current_os:
        command = "netsh interface show interface"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if "Connected" in line:
                return line.split()[4]
    return None

def backup_dns():
    interface_name = get_active_interface()
    if interface_name:
        command = f'netsh interface ip show dns name="{interface_name}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        with open("dns_backup.txt", "w") as f:
            f.write(result.stdout)
        return "DNS settings backed up to dns_backup.txt."
    return "No active network interface found."

def restore_dns():
    interface_name = get_active_interface()
    if interface_name:
        with open("dns_backup.txt", "r") as f:
            dns_servers = f.read().strip().splitlines()
        for dns_server in dns_servers:
            command = f'netsh interface ip set dns name="{interface_name}" static {dns_server}'
            subprocess.run(command, shell=True, check=True)
        return "DNS settings restored from dns_backup.txt."
    return "No active network interface found."

st.title("DNS Resolver and Changer")

if st.button("Backup DNS Settings"):
    message = backup_dns()
    st.success(message)

if st.button("Restore DNS Settings"):
    message = restore_dns()
    st.success(message)
