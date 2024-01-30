# Copyright 2020 Unlimited Robotics

import subprocess

import rayasdk.constants as constants
from rayasdk.container_handlers.docker_handler import DockerHandler
from rayasdk.logger import log_info
from rayasdk.utils import open_connection_file


class URKiller:

    COMMAND = 'kill'

    def __init__(self):
        self.docker_handler = DockerHandler()


    def init_parser(self, subparser):
        self.parser = subparser.add_parser(
            type(self).COMMAND,
            help="kills all the running apps on the Ra-Ya container.")


    def run(self, args, unknownargs):
        self.args = args
        self.unknownargs = unknownargs

        connection_settings = open_connection_file()

        if connection_settings[constants.JSON_EXECINFO_SIM]:
            host = 'localhost'
        else:
            host = connection_settings[constants.JSON_EXECINFO_ROBCONN][
                constants.JSON_EXECINFO_ROBIP]
        host_url = f'{constants.SSH_USER}@{host}'
        self.kill_apps(host_url=host_url)

        log_info('\nDone!')
        return True


    def kill_apps(self, host_url):
        log_info(f'Killing all running apps...')
        cmd = 'pkill -9 -u rayadevel -f "^python3 __main__.py"'
        command = (('ssh -t '
                    '-o LogLevel=QUIET '
                    f'-i {constants.SSH_KEY_PRIV} '
                    f'-p {constants.SSH_PORT} {host_url} '
                    f'\'{cmd}\''))
        subprocess.call(command, shell=True)
