import asyncio
import datetime
import logging

from .application_layer import FrameParser
from .link_layer import InvalidDatasetError, InvalidChecksumError
from .autodetect import autodetect, detect


class Tic:

    @classmethod
    async def create(cls, device_path):
        res = await detect(device_path)
        if not res:
            raise RuntimeError(f'No tic found at {device_path}')
        return cls(*res)

    def __init__(self, link, serial_number=None):
        self.link = link
        self.device_path = link.line.port
        self.serial_number = serial_number
        self.groups = {}
        self.err_count = 0
        self.last_update = None
        self.updated = asyncio.Event()

    @classmethod
    async def discover(cls):
        tics_params = await autodetect()
        return [cls(*p) for p in tics_params]

    async def infinite_update(self):
        async for frame in self.link.frames():
            try:
                self.groups = FrameParser(frame).to_dict()
                self.last_update = datetime.datetime.now()
                self.updated.set()
            except Exception:
                logging.exception('update error')
            self.err_count = self.link.errors
