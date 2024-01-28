import serial_asyncio


class Line:
    @classmethod
    def historique(cls, port):
        return cls(port, baudrate=1200)

    @classmethod
    def standard(cls, port):
        return cls(port, baudrate=9600)

    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self._reader = None
        self._writer = None

    async def __aenter__(self):
        self._reader, self._writer = await serial_asyncio.open_serial_connection(
            url=self.port,
            baudrate=self.baudrate,
            bytesize=serial_asyncio.serial.SEVENBITS,
            parity=serial_asyncio.serial.PARITY_EVEN,
            stopbits=serial_asyncio.serial.STOPBITS_ONE,
            rtscts=1
        )
        return self

    async def __aexit__(self, *args):
        self._writer.close()
        await self._writer.wait_closed()
        self._reader = None
        self._writer = None

    async def readuntil(self, token):
        return await self._reader.readuntil(token)
