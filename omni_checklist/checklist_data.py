import os
from dataclasses import dataclass
from typing import Dict, List


APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(APP_DIR, "assets")
BETA_LOGO = os.path.join(ASSET_DIR, "betawhite.png")


@dataclass(frozen=True)
class ChecklistItem:
    text: str
    detail: str = ""
    critical: bool = False


@dataclass(frozen=True)
class Aircraft:
    key: str
    name: str
    subtitle: str
    propulsion: str
    image: str
    accent: str


AIRCRAFT: Dict[str, Aircraft] = {
    "trainer": Aircraft(
        key="trainer",
        name="OMNI-Trainer",
        subtitle="Fixed wing UAV | internal combustion engine",
        propulsion="ICE",
        image=os.path.join(ASSET_DIR, "OMNI-Trainer.png"),
        accent="#00e5ff",
    ),
    "demonstrator": Aircraft(
        key="demonstrator",
        name="OMNI-Demonstrator",
        subtitle="Fixed wing UAV | electric propulsion",
        propulsion="Electric",
        image=os.path.join(ASSET_DIR, "OMNI-Demonstrator.png"),
        accent="#35f6c8",
    ),
}


SECTION_ORDER = [
    "Before Start",
    "Start & Takeoff",
    "Mission / Cruise",
    "Before Landing",
    "After Landing",
]


CHECKLISTS: Dict[str, Dict[str, List[ChecklistItem]]] = {
    "trainer": {
        "Before Start": [
            ChecklistItem("GCS: POWER ON / READY"),
            ChecklistItem("TELEMETRY: CONNECTED / LINK GOOD"),
            ChecklistItem("AIRCRAFT POWER: ON"),
            ChecklistItem("MAIN BATTERY: MIN 12.3 V", critical=True),
            ChecklistItem("FUEL: SUFFICIENT + RESERVE", critical=True),
            ChecklistItem("JOYSTICK: CONNECTED / CENTERED"),
            ChecklistItem("GCS WARNING: NO CRITICAL WARNING"),
            ChecklistItem("AIRSPEED: READING REASONABLE"),
            ChecklistItem("RANGEFINDER: READING REASONABLE"),
            ChecklistItem("AHRS: ATTITUDE / HEADING CORRECT"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("FLIGHT MODES: CHECKED"),
            ChecklistItem("CONTROL AUTHORITY: CHECKED"),
            ChecklistItem("MISSION: ROUTE / ALT / SPEED CHECKED"),
            ChecklistItem("HOME / RTL: POSITION / ALTITUDE CHECKED"),
            ChecklistItem("LANDING SEQUENCE: CHECKED"),
            ChecklistItem("AREA / PROP: CLEAR"),
        ],
        "Start & Takeoff": [
            ChecklistItem("PROP AREA: CLEAR - CALL 'CLEAR PROP'", critical=True),
            ChecklistItem("THROTTLE: IDLE"),
            ChecklistItem("AIRCRAFT: ARMED"),
            ChecklistItem("ENGINE: START"),
            ChecklistItem("IDLE RPM: APPROX. 2100 RPM"),
            ChecklistItem("IDLE TEMPERATURE: BELOW 120 C"),
            ChecklistItem("ENGINE CONDITION: STABLE / NORMAL"),
            ChecklistItem("FULL THROTTLE RPM: APPROX. 7000 RPM"),
            ChecklistItem("FULL THROTTLE TEMP: BELOW 160 C"),
            ChecklistItem("THROTTLE RESPONSE: SMOOTH"),
            ChecklistItem("BRAKE MODE 1: HOLD BELOW 4000 RPM"),
            ChecklistItem("BRAKE MODE 2: HOLD BELOW 6000 RPM"),
            ChecklistItem("TAXI / STEERING / BRAKE: CHECKED"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("GCS WARNING: NO CRITICAL WARNING"),
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("RUNWAY: CLEAR"),
            ChecklistItem("TAKEOFF: COMMENCE"),
        ],
        "Mission / Cruise": [
            ChecklistItem("FLIGHT MODE: AUTO / AS REQUIRED"),
            ChecklistItem("ACTIVE WAYPOINT: CORRECT"),
            ChecklistItem("FLIGHT PATH: ON ROUTE"),
            ChecklistItem("ALTITUDE / AIRSPEED: NORMAL"),
            ChecklistItem("ENGINE RPM / TEMP: NORMAL"),
            ChecklistItem("FUEL: MONITOR"),
            ChecklistItem("MAIN BATTERY: MONITOR"),
            ChecklistItem("TELEMETRY / CONTROL LINK: GOOD"),
            ChecklistItem("AIRCRAFT STATUS: NO CRITICAL WARNING"),
            ChecklistItem("RETURN DECISION: RTL / RETURN AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("LANDING SEQUENCE: ACTIVE / CORRECT"),
            ChecklistItem("RUNWAY / APPROACH: CLEAR"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("AIRSPEED DATA: VALID"),
            ChecklistItem("AIRCRAFT STATUS: NORMAL"),
            ChecklistItem("FUEL / BATTERY: SUFFICIENT FOR GO-AROUND"),
            ChecklistItem("GO-AROUND: READY"),
            ChecklistItem("LANDING: CONTINUE"),
        ],
        "After Landing": [
            ChecklistItem("BRAKE: APPLY GRADUALLY"),
            ChecklistItem("FLIGHT MODE: FBWA"),
            ChecklistItem("RUNWAY: VACATE"),
            ChecklistItem("ENGINE: IDLE / SHUT DOWN"),
            ChecklistItem("AIRCRAFT: DISARMED"),
            ChecklistItem("AIRCRAFT POWER: OFF"),
            ChecklistItem("TELEMETRY: DISCONNECT"),
        ],
    },
    "demonstrator": {
        "Before Start": [
            ChecklistItem("GCS: POWER ON / READY"),
            ChecklistItem("TELEMETRY: CONNECTED / LINK GOOD"),
            ChecklistItem("AIRCRAFT POWER: ON"),
            ChecklistItem("MAIN BATTERY: AROUND 25 V +/- 0.2 V", critical=True),
            ChecklistItem("JOYSTICK: CONNECTED / CENTERED"),
            ChecklistItem("GCS WARNING: NO CRITICAL WARNING"),
            ChecklistItem("AIRSPEED: READING REASONABLE"),
            ChecklistItem("RANGEFINDER: READING REASONABLE"),
            ChecklistItem("AHRS: ATTITUDE / HEADING CORRECT"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("FLIGHT MODES: CHECKED"),
            ChecklistItem("CONTROL AUTHORITY: CHECKED"),
            ChecklistItem("MISSION: ROUTE / ALT / SPEED CHECKED"),
            ChecklistItem("HOME / RTL: POSITION / ALTITUDE CHECKED"),
            ChecklistItem("LANDING SEQUENCE: CHECKED"),
            ChecklistItem("AREA / PROP: CLEAR"),
        ],
        "Start & Takeoff": [
            ChecklistItem("PROP AREA: CLEAR - CALL 'CLEAR PROP'", critical=True),
            ChecklistItem("THROTTLE: IDLE"),
            ChecklistItem("AIRCRAFT: ARMED"),
            ChecklistItem("MOTOR: START"),
            ChecklistItem("MOTOR CONDITION: STABLE / NORMAL"),
            ChecklistItem("FULL THROTTLE: CHECKED"),
            ChecklistItem("THROTTLE RESPONSE: SMOOTH"),
            ChecklistItem("TAXI / STEERING / BRAKE: CHECKED"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("GCS WARNING: NO CRITICAL WARNING"),
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("RUNWAY: CLEAR"),
            ChecklistItem("TAKEOFF: COMMENCE"),
        ],
        "Mission / Cruise": [
            ChecklistItem("FLIGHT MODE: AUTO / AS REQUIRED"),
            ChecklistItem("ACTIVE WAYPOINT: CORRECT"),
            ChecklistItem("FLIGHT PATH: ON ROUTE"),
            ChecklistItem("ALTITUDE / AIRSPEED: NORMAL"),
            ChecklistItem("MOTOR: NORMAL"),
            ChecklistItem("MAIN BATTERY: MONITOR / PREPARE LANDING BELOW 22.0 V", critical=True),
            ChecklistItem("LOW VOLTAGE: 21.0 V"),
            ChecklistItem("CRITICAL VOLTAGE: 18.0 V"),
            ChecklistItem("TELEMETRY / CONTROL LINK: GOOD"),
            ChecklistItem("AIRCRAFT STATUS: NO CRITICAL WARNING"),
            ChecklistItem("RETURN DECISION: RTL / RETURN AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("LANDING SEQUENCE: ACTIVE / CORRECT"),
            ChecklistItem("RUNWAY / APPROACH: CLEAR"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("AIRSPEED DATA: VALID"),
            ChecklistItem("AIRCRAFT STATUS: NORMAL"),
            ChecklistItem("MAIN BATTERY: ABOVE 22.0 V FOR GO-AROUND", critical=True),
            ChecklistItem("GO-AROUND: READY"),
            ChecklistItem("LANDING: CONTINUE"),
        ],
        "After Landing": [
            ChecklistItem("FLIGHT MODE: FBWA"),
            ChecklistItem("RUNWAY: VACATE"),
            ChecklistItem("MOTOR: IDLE / SHUT DOWN"),
            ChecklistItem("AIRCRAFT: DISARMED"),
            ChecklistItem("AIRCRAFT POWER: OFF"),
            ChecklistItem("TELEMETRY: DISCONNECT"),
        ],
    },
}


def checklist_for(aircraft_key: str) -> Dict[str, List[ChecklistItem]]:
    return {name: list(items) for name, items in CHECKLISTS[aircraft_key].items()}
