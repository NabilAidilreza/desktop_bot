import psutil

def get_no_of_backgorund_processes():
    processes = []
    count = 0
    for proc in psutil.process_iter(['name', 'exe', 'cmdline']):
        try:
            pinfo = proc.as_dict(attrs=['name', 'exe', 'cmdline'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        else:
            name = pinfo['name']
            exe = pinfo['exe']
            # cmdline = ' '.join(pinfo['cmdline'])
            if name and exe:
                processes.append(f"Application: {name}, Process: {exe}")
                count += 1
    return (f"{count} processes currently running in the background.", processes)
