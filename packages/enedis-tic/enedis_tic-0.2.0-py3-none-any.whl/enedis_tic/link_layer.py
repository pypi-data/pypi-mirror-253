from datetime import datetime
import logging


START_FRAME = b'\x02'
END_FRAME = b'\x03'


class Link:
    def __init__(self, line):
        self.line = line
        self.errors = 0

    async def frame(self):
        async with self.line:
            await self._skip_truncated_frame()
            return await self._frame()

    async def frames(self):
        async with self.line:
            await self._skip_truncated_frame()
            while True:
                try:
                    yield await self._frame()
                except Exception:
                    logging.exception('Frame error')
                    self.errors += 1

    async def _frame(self):
        raw = await self.line.readuntil(END_FRAME)
        return FrameFactory(raw.decode('ascii')).to_dict()

    async def _skip_truncated_frame(self):
        await self.line.readuntil(END_FRAME)


class FrameFactory:
    def __init__(self, raw):
        assert raw[0] == START_FRAME.decode('ascii')
        assert raw[-1] == END_FRAME.decode('ascii')
        self.raw = raw
        self.sep = '\t' if '\t' in raw else ' '

    def to_dict(self):
        raw = self.raw[2:-2]  # Ignore start frame, start group, end group and end frame
        if not raw:
            raise RuntimeError('Empty Frame')
        values = raw.split('\r\n')
        return {ds['label']: {'data': ds['data'], 'datetime': ds.get('datetime', None)} for ds in [self.data_set(v, self.sep) for v in values]}

    @staticmethod
    def data_set(raw, sep):
        values = raw.split(sep)
        if not (3 <= len(values) <= 4):
            raise InvalidDatasetError(raw)
        SumChecker(raw).ensure_valid()
        res = {'label': values[0], 'data': values[-2]}
        if len(values) == 4:
            timezone = {
                'H': '+0100',
                'E': '+0200'
            }.get(values[1][0].upper())
            res['datetime'] = datetime.strptime(values[1][1:]+timezone, '%y%m%d%H%M%S%z')
        return res


class InvalidDatasetError(Exception):
    def __init__(self, raw_frame):
        super().__init__()
        self.raw_frame = raw_frame


class SumChecker:
    def __init__(self, raw_data_set):
        self.raw_data_set = raw_data_set

    def verify(self):
        return (self.compute(self._payload) == self.given_checksum)\
               or (self.compute(self._older_payload) == self.given_checksum)

    def ensure_valid(self):
        if not self.verify():
            raise InvalidChecksumError(self.raw_data_set)

    @staticmethod
    def compute(payload):
        s1 = sum([ord(c) for c in payload])
        return (s1 & 0x3F) + 0x20

    @property
    def _payload(self):
        return self.raw_data_set[:-1]

    @property
    def _older_payload(self):
        """For devices up to 2013"""
        return self.raw_data_set[:-2]

    @property
    def given_checksum(self):
        return ord(self.raw_data_set[-1])


class InvalidChecksumError(Exception):
    def __init__(self, raw_dataset):
        super().__init__()
        self.raw_dataset = raw_dataset
