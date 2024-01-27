from subprocess import run


SERVICE_STATUS_STOPPED = 0
SERVICE_STATUS_STARTED = 1
SERVICE_STATUS_ERROR = 2

class Service:
    def __init__(self, name):
        self.name = name

    def status(self):
        try:
            process = run(['systemctl', 'status', self.name], capture_output=True)
            output = process.stdout.decode()
            if "Active: active (running)" in output:
                return SERVICE_STATUS_STARTED
            else:
                return SERVICE_STATUS_STOPPED
        except OSError:
            return SERVICE_STATUS_ERROR

    def start(self):
        try:
            process = run(['sudo', 'systemctl', 'start', self.name])
            return process.returncode == 0
        except OSError:
            return False


    def stop(self):
        try:
            process = run(['sudo', 'systemctl', 'stop', self.name])
            return process.returncode == 0
        except OSError:
            return False


class MemoryUsage:
    def __init__(self, total, free, used, cache):
        self.total = total
        self.free = free
        self.used = used
        self.cache = cache


def get_memory():
    try:
        process = run(['top', '-bn1'], capture_output=True)
        output = process.stdout.decode()
        if "Mem :" in output:
            i = output.index('Mem :')
            output = output[i+5:]

            i = output.index(' total,')
            total = float(output[:i])
            i += len(' total,')
            output = output[i+1:]

            i = output.index(' free,')
            free = float(output[:i])
            i += len(' free,')
            output = output[i+1:]

            i = output.index(' used,')
            used = float(output[:i])
            i += len(' used,')
            output = output[i+1:]

            i = output.index(' buff')
            cache = float(output[:i])

            return MemoryUsage(total, free, used, cache)
    except OSError as error:
        print(error)

    return None

