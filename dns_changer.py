import subprocess
import platform

def set_dns_windows(dns_server):
    interface_name = "Ethernet"
    command = f'netsh interface ip set dns name="{interface_name}" static {dns_server}'
    subprocess.run(command, shell=True, check=True)
    print(f"DNS changed to {dns_server}")

def set_dns_macos(dns_server):
    interface_name = "Wi-Fi"
    command = f'sudo networksetup -setdnsservers {interface_name} {dns_server}'
    subprocess.run(command, shell=True, check=True)
    print(f"DNS changed to {dns_server}")

def set_dns_linux(dns_server):
    command = f'nmcli con mod "System eth0" ipv4.dns "{dns_server}"'
    subprocess.run(command, shell=True, check=True)
    subprocess.run('nmcli con down "System eth0" && nmcli con up "System eth0"', shell=True, check=True)
    print(f"DNS changed to {dns_server}")

def change_dns(dns_server):
    current_os = platform.system().lower()
    if "windows" in current_os:
        set_dns_windows(dns_server)
    elif "darwin" in current_os:  # macOS
        set_dns_macos(dns_server)
    elif "linux" in current_os:
        set_dns_linux(dns_server)
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    dns_server = "8.8.8.8"  # Example: Google DNS
    change_dns(dns_server)
