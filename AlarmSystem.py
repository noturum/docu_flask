from typing import TextIO

import requests
from requests import post
import os
from time import sleep


class Alarm:
    def __init__(self, timeout: int, level: int, uri: str):
        '''

        :param timeout: тайминг опроса
        :param level: уровень впроцентах при аларме
        :param uri: ссылка на роут апи
        '''
        self._time_out: int = timeout
        self._level: int = level
        self._api_uri: str = uri
        self._file_info = '/proc/meminfo'

    def _get_level(self, info: TextIO) -> float:
        dict_info = {}
        for line in info:
            line = line.split(':')
            dict_info[line[0]] = int(line[1].removeprefix(' ').replace('\n', '').removesuffix(' kB'))
        return round(100 / (dict_info['MemTotal'] / dict_info['MemFree']), 2)

    def send_signal(self, lvl_used: float):
        requests.post(self._api_uri, json={'status': 'alarm', 'used_mem': lvl_used})
        ...

    def check(self):
        while 1:
            with open(self._file_info, 'r') as info:
                if (lvl_used := self._get_level(info)) >= self._level:
                    self.send_signal(lvl_used)
                print(lvl_used)
            sleep(self._time_out)


Alarm(1, 80, 'https://site.default/sys').check()
