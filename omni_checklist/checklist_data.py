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
        "Preflight / GCS": [
            ChecklistItem("WEATHER / WIND / RUNWAY / LANDING AREA: CHECKED"),
            ChecklistItem("AIRFRAME / GEAR / NOSE WHEEL: INSPECTED"),
            ChecklistItem("MOTOR / PROPELLER / CONTROL SURFACES: INSPECTED"),
            ChecklistItem("6S BATTERY: CONDITION / CONNECTION SECURE", critical=True),
            ChecklistItem("6S MAIN BATTERY: 24.8-25.2 V", critical=True),
            ChecklistItem("GCS / RADIO / TELEMETRY: READY"),
            ChecklistItem("CREW BRIEF: MISSION / ABORT / GO-AROUND"),
            ChecklistItem("PITOT COVER: REMOVED"),
            ChecklistItem("AIRCRAFT POWER / TELEMETRY: ON / CONNECTED"),
        ],
        "Before Start": [
            ChecklistItem("GCS / TELEMETRY / REQUIRED VIDEO: GOOD"),
            ChecklistItem("BAROMETER / IMU / COMPASS: NORMAL"),
            ChecklistItem("GPS: 3D FIX / POSITION / HEADING VERIFIED"),
            ChecklistItem("AIRSPEED: REASONABLE"),
            ChecklistItem("JOYSTICK: CONNECTED / CENTERED"),
            ChecklistItem("CONTROL SURFACES: FULL / FREE / CORRECT"),
            ChecklistItem("CONTROL AUTHORITY: CHECKED"),
            ChecklistItem("FLIGHT MODES: FBWA / AUTO / RTL / FBWA"),
            ChecklistItem("MISSION: ROUTE / ALTITUDE UPLOADED / CHECKED"),
            ChecklistItem("LANDING / GO-AROUND SEQUENCE: CHECKED"),
            ChecklistItem("HOME / RALLY POINT: POSITION / ALTITUDE CHECKED"),
            ChecklistItem("GCS: NO CRITICAL WARNING", critical=True),
        ],
        "Start & Takeoff": [
            ChecklistItem("TOWER: REQUEST START CLEARANCE"),
            ChecklistItem("PROP AREA: CLEAR - CALL 'CLEAR PROP'", critical=True),
            ChecklistItem("FLIGHT MODE / THROTTLE: FBWA / IDLE"),
            ChecklistItem("AIRCRAFT: ARMED"),
            ChecklistItem("MOTOR: START / RESPONSE NORMAL"),
            ChecklistItem("THROTTLE RESPONSE: SMOOTH"),
            ChecklistItem("TOWER: REQUEST TAXI CLEARANCE"),
            ChecklistItem("TAXI AREA / STEERING: CLEAR / CHECKED"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("6S BATTERY / MOTOR / WARNINGS: NORMAL"),
            ChecklistItem("TOWER: REQUEST TAKEOFF CLEARANCE"),
            ChecklistItem("RUNWAY / TAKEOFF PATH: CLEAR"),
            ChecklistItem("TAKEOFF: COMMENCE, 3-2-1"),
            ChecklistItem("FLIGHT MODE: AUTO", critical=True),
            ChecklistItem("ACCELERATION / AIRSPEED / CLIMB: NORMAL"),
        ],
        "Mission / Cruise": [
            ChecklistItem("AUTO / WAYPOINT / ROUTE / ALTITUDE: MONITOR"),
            ChecklistItem("AIRSPEED / ATTITUDE / MOTOR: NORMAL"),
            ChecklistItem("6S BATTERY: VOLTAGE / TREND MONITOR"),
            ChecklistItem("6S BATTERY BELOW 22.0 V: PREPARE TO LAND", critical=True),
            ChecklistItem("6S LOW VOLTAGE: 21.0 V"),
            ChecklistItem("6S CRITICAL VOLTAGE: 18.0 V"),
            ChecklistItem("TELEMETRY / CONTROL LINK / VIDEO: GOOD"),
            ChecklistItem("TOWER: REPORT AREA / ALTITUDE AS REQUIRED"),
            ChecklistItem("RETURN DECISION: RTL / LAND AS REQUIRED"),
        ],
        "Before Landing": [
            ChecklistItem("AUTO LANDING / GO-AROUND WAYPOINT: VERIFIED"),
            ChecklistItem("TOWER: REQUEST LANDING CLEARANCE"),
            ChecklistItem("RUNWAY / APPROACH: CLEAR"),
            ChecklistItem("WIND: HW <10 KT / XW <6 KT / TW <2 KT"),
            ChecklistItem("AIRSPEED / MOTOR / AIRCRAFT STATUS: NORMAL"),
            ChecklistItem("6S BATTERY: ABOVE 22.0 V FOR GO-AROUND", critical=True),
            ChecklistItem("EP: LANDING / GO-AROUND BRIEF COMPLETE"),
            ChecklistItem("FINAL / FLARE / TOUCHDOWN PATH: MONITOR"),
            ChecklistItem("EXTERNAL PILOT: HANDOVER IF REQUIRED", optional=True),
        ],
        "After Landing": [
            ChecklistItem("GROUND ROLL / DIRECTION: CONTROLLED"),
            ChecklistItem("FLIGHT MODE: FBWA"),
            ChecklistItem("MOTOR: THROTTLE IDLE / STOP"),
            ChecklistItem("PROPELLER: STOPPED", critical=True),
            ChecklistItem("AIRCRAFT: DISARMED"),
            ChecklistItem("AIRCRAFT POWER / 6S BATTERY: OFF / DISCONNECTED"),
            ChecklistItem("POST-FLIGHT: AIRFRAME / GEAR / MOTOR INSPECTED"),
            ChecklistItem("MISSION / TELEMETRY / VIDEO: SAVED"),
            ChecklistItem("TELEMETRY: DISCONNECT / GCS SECURE"),
        ],
    },
}


def checklist_for(aircraft_key: str) -> Dict[str, List[ChecklistItem]]:
    return {name: list(items) for name, items in CHECKLISTS[aircraft_key].items()}
