import subprocess

try:
    print("Killing interferring processes...")
    subprocess.call("airmon-ng check kill", shell=True)
    print("Murder managed. Moving on...")
    subprocess.call("ifconfig wlan0 down", shell =True)
    subprocess.call("iwconfig wlan0 mode monitor", shell=True)
    subprocess.call("ifconfig wlan0 up", shell=True)
    print("Calling the data with our sweet song...")
    subprocess.call("airodump-ng wlan0", shell=True)
except KeyboardInterrupt:
    print("\nOkay then, buh-bye now.")