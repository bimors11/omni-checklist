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
    optional: bool = False


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
            ChecklistItem("GCS: ON / READY"),
            ChecklistItem("TELEMETRY: CONNECTED / GOOD"),
            ChecklistItem("AIRCRAFT POWER: ON"),
            ChecklistItem("MAIN BATTERY: MIN 12.3 V", critical=True),
            ChecklistItem("FUEL: SUFFICIENT / RESERVE", critical=True),
            ChecklistItem("JOYSTICK: CONNECTED / CENTERED"),
            ChecklistItem("GCS: NO CRITICAL WARNING"),
            ChecklistItem("AIRSPEED: REASONABLE"),
            ChecklistItem("RANGEFINDER: REASONABLE"),
            ChecklistItem("AHRS: ATTITUDE / HEADING CORRECT"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("CONTROL AUTHORITY: CHECKED"),
            ChecklistItem("FLIGHT MODES: CHECKED"),
            ChecklistItem("MISSION: ROUTE / ALTITUDE CHECKED"),
            ChecklistItem("LANDING SEQUENCE: CHECKED"),
            ChecklistItem("HOME / RALLY POINT: POSITION / ALTITUDE CHECKED"),
            ChecklistItem("AREA / PROP: CLEAR"),
        ],
        "Start & Takeoff": [
            ChecklistItem("TOWER: REQUEST START CLEARANCE"),
            ChecklistItem("PROP AREA: CLEAR - CALL 'CLEAR PROP'", critical=True),
            ChecklistItem("THROTTLE: IDLE"),
            ChecklistItem("AIRCRAFT: ARMED"),
            ChecklistItem("ENGINE: START"),
            ChecklistItem("IDLE RPM: 2,100 +/- 200 RPM"),
            ChecklistItem("ENGINE: STABLE / NORMAL"),
            ChecklistItem(
                "WARM-UP: THROTTLE BELOW 20% IF TEMP BELOW 100 C",
                optional=True,
            ),
            ChecklistItem("ENGINE TEMP: ABOVE 100 C", critical=True),
            ChecklistItem("THROTTLE: INCREASE GRADUALLY"),
            ChecklistItem("FULL THROTTLE RPM: APPROX. 7000 RPM"),
            ChecklistItem("FULL THROTTLE TEMP: BELOW 160 C"),
            ChecklistItem("THROTTLE RESPONSE: SMOOTH"),
            ChecklistItem("TOWER: REQUEST TAXI CLEARANCE"),
            ChecklistItem("BRAKE 1 HOLD: 3,000-4,000 RPM"),
            ChecklistItem("BRAKE 2 HOLD: 5,000-6,000 RPM"),
            ChecklistItem("BRAKE: POSITION 1", critical=True),
            ChecklistItem("TAXI / STEERING: CHECKED"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("GCS: NO CRITICAL WARNING"),
            ChecklistItem("TOWER: REQUEST TAKEOFF CLEARANCE"),
            ChecklistItem("RUNWAY: CLEAR"),
            ChecklistItem("TAKEOFF: COMMENCE, 3-2-1"),
            ChecklistItem("FLIGHT MODE: AUTO", critical=True),
        ],
        "Mission / Cruise": [
            ChecklistItem("FLIGHT MODE: AUTO / AS REQUIRED"),
            ChecklistItem("ACTIVE WAYPOINT: CORRECT"),
            ChecklistItem("FLIGHT PATH: ON ROUTE"),
            ChecklistItem("ALTITUDE / AIRSPEED: NORMAL"),
            ChecklistItem("TOWER: REPORT AREA / ALTITUDE"),
            ChecklistItem("ENGINE RPM / TEMP: NORMAL"),
            ChecklistItem("FUEL: MONITOR"),
            ChecklistItem("MAIN BATTERY: MONITOR"),
            ChecklistItem("TELEMETRY / CONTROL LINK: GOOD"),
            ChecklistItem("AIRCRAFT: NO CRITICAL WARNING"),
            ChecklistItem("RETURN DECISION: RTL / RETURN AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("LANDING SEQUENCE: ACTIVE / CORRECT"),
            ChecklistItem("TOWER: REQUEST LANDING CLEARANCE"),
            ChecklistItem("RUNWAY / APPROACH: CLEAR"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("AIRSPEED DATA: VALID"),
            ChecklistItem("AIRCRAFT STATUS: NORMAL"),
            ChecklistItem("FUEL / BATTERY: SUFFICIENT FOR GO-AROUND"),
            ChecklistItem("GO-AROUND: READY"),
            ChecklistItem("LANDING: CONTINUE"),
            ChecklistItem("EXTERNAL PILOT: HANDOVER IF REQUIRED", optional=True),
        ],
        "After Landing": [
            ChecklistItem("FLIGHT MODE: FBWA"),
            ChecklistItem("BRAKE: APPLY AS REQUIRED"),
            ChecklistItem("BRAKE: POSITION 2"),
            ChecklistItem("RUNWAY: VACATE"),
            ChecklistItem("ENGINE: IDLE / SHUT DOWN"),
            ChecklistItem("AIRCRAFT: DISARMED"),
            ChecklistItem("AIRCRAFT POWER: OFF"),
            ChecklistItem("TELEMETRY: DISCONNECT"),
        ],
    },
    "demonstrator": {
        "Before Start": [
            ChecklistItem("GCS: ON / READY"),
            ChecklistItem("TELEMETRY: CONNECTED / GOOD"),
            ChecklistItem("AIRCRAFT POWER: ON"),
            ChecklistItem("MAIN BATTERY: 24.8-25.2 V", critical=True),
            ChecklistItem("JOYSTICK: CONNECTED / CENTERED"),
            ChecklistItem("GCS: NO CRITICAL WARNING"),
            ChecklistItem("AIRSPEED: REASONABLE"),
            ChecklistItem("AHRS: ATTITUDE / HEADING CORRECT"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("CONTROL AUTHORITY: CHECKED"),
            ChecklistItem("FLIGHT MODES: CHECKED"),
            ChecklistItem("MISSION: ROUTE / ALTITUDE CHECKED"),
            ChecklistItem("LANDING SEQUENCE: CHECKED"),
            ChecklistItem("HOME / RALLY POINT: POSITION / ALTITUDE CHECKED"),
            ChecklistItem("AREA / PROP: CLEAR"),
        ],
        "Start & Takeoff": [
            ChecklistItem("TOWER: REQUEST START CLEARANCE"),
            ChecklistItem("PROP AREA: CLEAR - CALL 'CLEAR PROP'", critical=True),
            ChecklistItem("THROTTLE: IDLE"),
            ChecklistItem("AIRCRAFT: ARMED"),
            ChecklistItem("MOTOR: START"),
            ChecklistItem("MOTOR: STABLE / NORMAL"),
            ChecklistItem("FULL THROTTLE: CHECKED"),
            ChecklistItem("THROTTLE RESPONSE: SMOOTH"),
            ChecklistItem("TOWER: REQUEST TAXI CLEARANCE"),
            ChecklistItem("TAXI / STEERING: CHECKED"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("GCS: NO CRITICAL WARNING"),
            ChecklistItem("TOWER: REQUEST TAKEOFF CLEARANCE"),
            ChecklistItem("RUNWAY: CLEAR"),
            ChecklistItem("TAKEOFF: COMMENCE, 3-2-1"),
            ChecklistItem("FLIGHT MODE: AUTO", critical=True),
        ],
        "Mission / Cruise": [
            ChecklistItem("FLIGHT MODE: AUTO / AS REQUIRED"),
            ChecklistItem("ACTIVE WAYPOINT: CORRECT"),
            ChecklistItem("FLIGHT PATH: ON ROUTE"),
            ChecklistItem("ALTITUDE / AIRSPEED: NORMAL"),
            ChecklistItem("TOWER: REPORT AREA / ALTITUDE"),
            ChecklistItem("MOTOR: NORMAL"),
            ChecklistItem("MAIN BATTERY: PREPARE TO LAND BELOW 22.0 V", critical=True),
            ChecklistItem("LOW VOLTAGE: 21.0 V"),
            ChecklistItem("CRITICAL VOLTAGE: 18.0 V"),
            ChecklistItem("TELEMETRY / CONTROL LINK: GOOD"),
            ChecklistItem("AIRCRAFT: NO CRITICAL WARNING"),
            ChecklistItem("RETURN DECISION: RTL / RETURN AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("FLIGHT MODE: AUTO"),
            ChecklistItem("LANDING SEQUENCE: ACTIVE / CORRECT"),
            ChecklistItem("TOWER: REQUEST LANDING CLEARANCE"),
            ChecklistItem("RUNWAY / APPROACH: CLEAR"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("AIRSPEED DATA: VALID"),
            ChecklistItem("AIRCRAFT STATUS: NORMAL"),
            ChecklistItem("MAIN BATTERY: ABOVE 22.0 V FOR GO-AROUND", critical=True),
            ChecklistItem("GO-AROUND: READY"),
            ChecklistItem("LANDING: CONTINUE"),
            ChecklistItem("EXTERNAL PILOT: HANDOVER IF REQUIRED", optional=True),
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
