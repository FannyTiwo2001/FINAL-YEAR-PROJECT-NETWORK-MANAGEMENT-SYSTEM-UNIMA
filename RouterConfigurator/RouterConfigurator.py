import paramiko

class RouterConfigurator:
    def __init__(self, hostname):
        self.hostname = hostname
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        self.client.connect(
            self.hostname

        )

    def configure_router(self, commands):
        for command in commands:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            print(output)

    def close(self):
        self.client.close()

hostname = 'router_ip_address'

commands = [
    'enable',
    'configure terminal',
    'interface GigabitEthernet0/0',
    'ip address 192.168.1.1 255.255.255.0',
    'no shutdown',
    'exit',
    'write memory'
]

router = RouterConfigurator(hostname)
router.connect()
router.configure_router(commands)
router.close()

