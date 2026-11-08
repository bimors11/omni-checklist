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


CHECKLISTS: Dict[str, Dict[str, List[ChecklistItem]]] = {
    "trainer": {
        "Preflight / GCS": [
            ChecklistItem("GC1 AIRFRAME / PROP / GEAR / SENSORS: INSPECTED"),
            ChecklistItem("PARACHUTE SAFETY PIN: INSTALLED", critical=True),
            ChecklistItem("FUEL / MAIN + SECONDARY BATTERIES: CHECKED"),
            ChecklistItem("GC2 GCS / GDT / ANTENNAS / RADIO: READY"),
            ChecklistItem("CREW BRIEF: MISSION / WEATHER / ABORT / GO-AROUND"),
            ChecklistItem("UAV POSITION / CREW: SECURED / STANDING BY"),
            ChecklistItem("GCS POWER / LAN: CHECKED"),
            ChecklistItem("BETA GROUND CONTROL / CHECKLIST: OPEN"),
            ChecklistItem("OMNILINK: INSTRUCTOR GCS ONLY"),
            ChecklistItem("FLIGHT PLAN / LANDING SEQUENCE: CROSS-CHECKED"),
            ChecklistItem("INSTRUCTOR / STUDENT / GDT LINKS: GREEN"),
            ChecklistItem("BOTH GCS JOYSTICKS: CENTERED / RESPONDING"),
            ChecklistItem("UAV ON: CALL; MAIN THEN SECONDARY BATTERY"),
            ChecklistItem("OMNILINK: WAIT 15 S / REFRESH"),
            ChecklistItem("ADT / REQUIRED CAMERAS: GREEN", critical=True),
            ChecklistItem("REQUIRED LINK RED: HOLD / TROUBLESHOOT", optional=True),
            ChecklistItem("OMNILINK START ALL: SELECT / DATA + VIDEO CONFIRM"),
        ],
        "Before Start": [
            ChecklistItem("REQUIRED CAMERA VIEWS: LIVE / IDENTIFIABLE"),
            ChecklistItem("GPS / HDOP / HEADING / ALTITUDE: CROSS-CHECKED"),
            ChecklistItem("FUEL / BOTH BATTERIES: CHECKED"),
            ChecklistItem("CRITICAL WARNINGS: NONE", critical=True),
            ChecklistItem("AIRSPEED: PITOT TEST / RETURN NEAR ZERO"),
            ChecklistItem("RANGEFINDER: COVER TEST / RECOVERY"),
            ChecklistItem("GCS ATTITUDE: RESPONDS TO AIRCRAFT MOVEMENT"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("FLIGHT MODES: FBWA / AUTO / RTL / FBWA"),
            ChecklistItem("CONTROL AUTHORITY: INSTRUCTOR / STUDENT CHECK"),
            ChecklistItem("EP CONTROL: GROUND CHECK / RETURN TO IP"),
            ChecklistItem("MISSION / HOME / RALLY / LANDING: VERIFIED"),
            ChecklistItem("MISSION UPLOAD / DOWNLOAD: CROSS-CHECKED"),
            ChecklistItem("BEFORE START: NO UNRESOLVED FAILURES"),
        ],
        "Start & Takeoff": [
            ChecklistItem("TOWER: REQUEST START CLEARANCE"),
            ChecklistItem("PROP AREA: CLEAR / NOSE HELD", critical=True),
            ChecklistItem("FLIGHT MODE / THROTTLE: FBWA / IDLE"),
            ChecklistItem("AIRCRAFT: ARM"),
            ChecklistItem("ENGINE START: PRESS"),
            ChecklistItem("IDLE RPM: 2,100 +/- 200; STABLE"),
            ChecklistItem("CHT BELOW 100 C: THROTTLE BELOW 20%"),
            ChecklistItem("CHT: AT LEAST 100 C BEFORE RUN-UP", critical=True),
            ChecklistItem("SECONDARY BATTERY / MANIFOLD: REPORT"),
            ChecklistItem("FULL THROTTLE: 3-5 S; 7,100 +/- 200 RPM"),
            ChecklistItem("CHT AT FULL THROTTLE: BELOW 160 C"),
            ChecklistItem("THROTTLE: RETURN TO IDLE; 6% / 2,100 +/- 200 RPM"),
            ChecklistItem("BRAKE 1 HOLD: 3,000-4,000 RPM"),
            ChecklistItem("BRAKE 2 HOLD: 5,000-6,000 RPM"),
            ChecklistItem("TOWER: REQUEST TAXI CLEARANCE"),
            ChecklistItem("TAXI AREA / CREW: CLEAR; NOSE RELEASED"),
            ChecklistItem("BRAKE: POSITION 1; STEERING CHECK"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("RUNWAY / TAKEOFF PATH / CREW: CLEAR"),
            ChecklistItem("MISSION / AUTHORITY / WARNINGS: CHECKED"),
            ChecklistItem("PARACHUTE SAFETY PIN: REMOVED", critical=True),
            ChecklistItem("TOWER: TAKEOFF CLEARANCE RECEIVED"),
            ChecklistItem("TAKEOFF: 3, 2, 1; SELECT AUTO"),
            ChecklistItem("AUTO / ACCELERATION / CLIMB / TRACK: CONFIRMED"),
        ],
        "Mission / Cruise": [
            ChecklistItem("AUTO / WAYPOINT / ROUTE / ALTITUDE / AIRSPEED: CHECK"),
            ChecklistItem("ENGINE RPM / CHT / FUEL / BATTERIES: MONITOR"),
            ChecklistItem("TELEMETRY / CONTROL LINK / VIDEO: MONITOR"),
            ChecklistItem("CRITICAL WARNINGS: NONE"),
            ChecklistItem("TOWER: REPORT AREA / ALTITUDE AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("TOWER: REQUEST FULL STOP / READ BACK"),
            ChecklistItem("DOWNWIND: EP / GC1 STANDING BY"),
            ChecklistItem("AUTO LANDING / GO-AROUND WAYPOINT: VERIFIED"),
            ChecklistItem("AIRSPEED / STATUS / GO-AROUND RESERVE: CHECK"),
            ChecklistItem("RUNWAY / APPROACH / WIND: CLEAR / WITHIN LIMITS"),
            ChecklistItem("EP: BRIEF AUTO / HANDOVER / GO-AROUND"),
            ChecklistItem("BEFORE LANDING: COMPLETE BEFORE BASE"),
            ChecklistItem("FINAL: ALTITUDE / AIRSPEED; EP UAV IN SIGHT"),
            ChecklistItem("TOWER: LANDING CLEARANCE RECEIVED"),
            ChecklistItem("HANDOVER: ALIGNED; AT OR ABOVE 100 FT AGL", critical=True),
            ChecklistItem("EP CONTROL / AUTO: CONFIRMED"),
            ChecklistItem("UNSAFE APPROACH: GO-AROUND / RETURN TO IP", optional=True),
        ],
        "After Landing": [
            ChecklistItem("STABLE GROUND ROLL: FBWA SELECTED"),
            ChecklistItem("BRAKES: APPLY TO FULL STOP"),
            ChecklistItem("CONTROL: RETURN TO IP AFTER FULL STOP"),
            ChecklistItem("TAXI CLEARANCE / AREA: CONFIRMED"),
            ChecklistItem("FINAL PARKING: BRAKE 2; 5,000-6,000 RPM / 5 S"),
            ChecklistItem("THROTTLE: IDLE; ENGINE STOP"),
            ChecklistItem("RPM ZERO / PROP STOPPED: CONFIRMED", critical=True),
            ChecklistItem("AIRCRAFT: DISARMED"),
            ChecklistItem("PARACHUTE SAFETY PIN: INSERTED"),
            ChecklistItem("UAV BATTERIES: DISCONNECTED / SECURED"),
            ChecklistItem("POST-FLIGHT: INSPECT DAMAGE / LEAKS"),
            ChecklistItem("FUEL / DEFECTS / FLIGHT RECORD: CLOSED"),
            ChecklistItem("MISSION / TELEMETRY / VIDEO: SAVED"),
            ChecklistItem("TELEMETRY: DISCONNECTED; GCS SECURED"),
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
