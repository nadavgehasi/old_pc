#!/usr/bin/python3.8

import paramiko
import graphyte

GRAPHITE_SERVER = 'graphite'

CPU_COUNT_COMMAND = ("nproc", 'cpu')
MEMORY_USED_PERCENT_COMMAND = ('awk \'/^Mem/ {printf("%u", 100*$3/$2);}\' <(free -m)', 'memory.percent')
MEMORY_TOTAL_COUNT_COMMAND = ("awk '/^Mem/ {print $2}' <(free -m)", 'memory.total')
MEMORY_USED_COUNT_COMMAND = ("awk '/^Mem/ {print $3}' <(free -m)", 'memory.used')
COMMANDS = [CPU_COUNT_COMMAND, MEMORY_TOTAL_COUNT_COMMAND, MEMORY_USED_COUNT_COMMAND, MEMORY_USED_PERCENT_COMMAND]

SSH_PORT = 22

HOSTS = [
    (('192.168.0.104', 'armon-yarkon'), 'root', 'root'),
    (('172.17.0.1', 'armon-yarkon-2'), 'root', 'root'),
    (('192.168.0.104', 'badid-mif'), 'root', 'root'),
    (('172.17.0.1', 'docker_host'), 'root', 'root'),
    (('172.17.0.1', 'localhost'), 'root', 'root'),
]


def main():
    graphyte.init(GRAPHITE_SERVER, prefix='hosts')

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)

    for (host_ip, host_name), username, password in HOSTS:
        try:
            client.connect(host_ip, port=SSH_PORT, username=username, password=password)
            for command, graphite_key in COMMANDS:
                stdin, stdout, stderr = client.exec_command(command, get_pty=True)
                cpu_count = int(stdout.read().decode('ascii').strip())
                graphyte.send(f'{host_name}.{graphite_key}', cpu_count)
                print(f'{host_ip} {host_name} {graphite_key} {cpu_count}')

        finally:
            client.close()


if __name__ == '__main__':
    main()
