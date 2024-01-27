"""Fetch Bus times information from Burgos."""
import logging
from dataclasses import dataclass
from typing import List

from aiohttp import ClientSession


@dataclass
class Estimation:
    """Class for bus estimation"""
    NAME = "Bus Estimation"

    seconds: str
    destination: str
    meters: int
    vehicle: int

    @staticmethod
    def from_json(item):
        return Estimation(
            seconds=item["seconds"],
            destination=item["destination"],
            meters=item["meters"],
            vehicle=item["vehicle"],
        )

@dataclass
class BusTime:
    """Class for bus time"""
    NAME = "Bus Time"

    line: str
    destination: str
    estimations: List[Estimation]

    @staticmethod
    def from_json(item):
        return BusTime(
            line=item["line"],
            destination=item["destination"],
            estimations=list(map(Estimation.from_json, item["publicEstimationVHExts"])),
        )

@dataclass
class BusStop:
    """Class for bus stop"""
    NAME = "Bus Stop"

    id: str
    name: str
    longitude: int
    latitude: int

    @staticmethod
    def from_json(item):
        return BusStop(
            id=item["num"],
            name=item["name"],
            longitude=item["lng"],
            latitude=item["lat"],
        )

@dataclass
class BusStopWithEstimations():
    """Class for bus stop with times"""
    NAME = "Bus Stop With Estimations"
    times: List[BusTime]

    def get_times_by_line(self, line: str):
        return next(x for x in self.times if x.line == line).estimations

    def get_next_bus(self, line: str):
        estimations = self.get_times_by_line(line)
        return sorted(estimations, key=lambda x: int(x.seconds), reverse=False)[0]

    @staticmethod
    def from_json(item):
        return BusStopWithEstimations(
            times=list(map(BusTime.from_json, item["routeEstimationByNode"])),
        )


DEFAULT_SOURCE = "https://movilidad.aytoburgos.es/rutas-en-directo?p_p_id=as_asac_isaenext_IsaenextWebPortlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view"


def fix_encoding(str):
    return str.replace("Espa�a", "España").replace("Evoluci�n", "Evolución")


async def get_all_bus_stops(session: ClientSession, *, source=DEFAULT_SOURCE+"&p_p_resource_id=resourceNodes&p_p_cacheability=cacheLevelPage"):
    """Fetch all bus stops."""
    try:
        response = await session.get(source)
        json = await response.json()
        results = list(map(BusStop.from_json, json))
        return results
    except RuntimeError:
        logging.getLogger(__name__).warning("Cannot get data")
        return []


async def get_bus_stop(session: ClientSession, id, source=DEFAULT_SOURCE+"&p_p_resource_id=resourceEstimations&p_p_cacheability=cacheLevelPage&_as_asac_isaenext_IsaenextWebPortlet_tipo=1&_as_asac_isaenext_IsaenextWebPortlet_nodoIds="):
    """Fetch all bus stops."""
    try:
        response = await session.get(source.replace("nodoIds=", "nodoIds={}".format(id)))
        json = await response.json()
        data = json[0] if len(json) > 0 else []
        return BusStopWithEstimations.from_json(data)
    except RuntimeError:
        logging.getLogger(__name__).warning("Cannot get data")
        return []