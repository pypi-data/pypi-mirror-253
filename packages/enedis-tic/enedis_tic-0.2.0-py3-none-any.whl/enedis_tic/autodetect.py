import asyncio
import logging

from .physical_layer import Line
from .link_layer import Link
from serial.tools.list_ports import comports


async def autodetect():
    tasks = [asyncio.create_task(detect(port.device)) for port in comports()]
    await asyncio.gather(*tasks)
    return [t.result() for t in tasks if t.result()]


async def detect(port):
    for line in (Line.historique(port), Line.standard(port)):
        try:
            link = Link(line)
            frame = await link.frame()
            serial_number = frame.get("ADSC", frame.get("ADCO"))['data']
        except Exception as e:
            logging.info('No tic detected : %s', e)
            continue
        else:
            return link, serial_number
    return None
