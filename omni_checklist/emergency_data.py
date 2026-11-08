"""OMNI-Trainer emergency quick reference, AFM Chapter 3, revision A."""

from omni_checklist.checklist_data import ChecklistItem


EMERGENCY_CHECKLISTS = {
    "Initial Response": [
        ChecklistItem("FAILURE / ALTITUDE / POSITION: CALL OUT"),
        ChecklistItem("UAV CONTROL: MAINTAIN; SELECT SAFE AREA", critical=True),
        ChecklistItem("DECISION: CONTINUE / RETURN / EMERGENCY LAND"),
        ChecklistItem("TOWER: REPORT EMERGENCY / INTENTION"),
    ],
    "Telemetry / Control Link Loss": [
        ChecklistItem("COMMUNICATION LOST / FROZEN DATA: VERIFY"),
        ChecklistItem("EP RC LINK: ACTIVE OR UNKNOWN?"),
        ChecklistItem("GC2 ANTENNA / TRANSCEIVER / GCS CABLE: CHECK"),
        ChecklistItem("AFTER ~30 S: OBSERVE UAV RESPONSE"),
        ChecklistItem("RTL: CONFIRM ONLY IF INDICATED", critical=True),
        ChecklistItem("IP GCS LOST / EP RC ACTIVE: EP TAKES CONTROL"),
    ],
    "Low / Critical Battery (3S)": [
        ChecklistItem("AT OR BELOW 10.5 V: IDENTIFY PACK / TREND"),
        ChecklistItem("LOW BATTERY: TERMINATE MISSION"),
        ChecklistItem("GPS VALID: COMMAND RTL / VERIFY TURN"),
        ChecklistItem("ROUTE / ALTITUDE / BOTH BATTERIES: MONITOR"),
        ChecklistItem("ALTERNATE LANDING AREA: PREPARE"),
        ChecklistItem("AT OR BELOW 9.9 V: CHECK PACK / MODE"),
        ChecklistItem("AUTO RTL: VERIFY; GPS VALID IF COMMANDING RTL", critical=True),
        ChecklistItem("GPS INVALID: SELECT SAFE LANDING AREA"),
    ],
    "Engine Fails to Start (Ground)": [
        ChecklistItem("START ATTEMPT: STOP"),
        ChecklistItem("RPM ZERO / PROP STOPPED: CONFIRM", critical=True),
        ChecklistItem("RETRY: CLEAR AREA / CREW FIRST"),
    ],
    "Engine Failure (Flight)": [
        ChecklistItem("FALLING / ZERO RPM: CALL ENGINE FAILURE"),
        ChecklistItem("VALID AIRSPEED: MAINTAIN 40-42 KT BEST GLIDE", critical=True),
        ChecklistItem("HOME / REACHABLE SAFE LANDING AREA: SELECT"),
        ChecklistItem("AUTOMATIC RESTART: OBSERVE SINGLE ATTEMPT"),
        ChecklistItem("MANUAL RESTART: MAX 3 COMMANDS; 2 ATTEMPTS EACH"),
        ChecklistItem("RESTART ONLY IF ALTITUDE / WORKLOAD PERMIT"),
        ChecklistItem("LANDING NEEDS ATTENTION: STOP RESTART ATTEMPTS"),
        ChecklistItem("IF RESTARTED: VERIFY STABLE RPM / RETURN HOME"),
        ChecklistItem("NO SAFE AREA AND ABOVE 150 FT AGL: PARACHUTE", optional=True),
    ],
    "GPS / Compass Fault (Ground)": [
        ChecklistItem("GPS LOST / SATELLITES BELOW 6 / HEADING FAULT"),
        ChecklistItem("DO NOT ARM; ENGINE STOPPED", critical=True),
        ChecklistItem("CHECK MAGNETIC INTERFERENCE"),
        ChecklistItem("POWER CYCLE BOTH BATTERIES: MAIN FIRST ON RECONNECT"),
        ChecklistItem("GPS POSITION / HEADING: RECHECK"),
        ChecklistItem("COMPASS CALIBRATION / SENSOR CHECKS IF REQUIRED"),
    ],
    "GPS / Airspeed Unreliable (Flight)": [
        ChecklistItem("GPS / HEADING: COMPARE WITH VISUAL POSITION"),
        ChecklistItem("GPS INVALID: STOP WAYPOINT NAVIGATION / RTL", critical=True),
        ChecklistItem("VALIDATED MODE: VISUAL CONTROL TO SAFE AREA"),
        ChecklistItem("AIRSPEED: COMPARE GPS SPEED / WIND / RESPONSE"),
        ChecklistItem("AIRSPEED UNRELIABLE: END MISSION"),
        ChecklistItem("USE VALIDATED AIRSPEED-FAILURE LANDING / CUES"),
    ],
    "Altitude Discrepancy": [
        ChecklistItem("GPS MINUS HOME / BARO / RANGEFINDER: COMPARE"),
        ChecklistItem("DIFFERENCE ABOVE 100 FT OR RISING: END MISSION"),
        ChecklistItem("ACTUAL HEIGHT WRONG: ABORT AUTO LANDING", critical=True),
        ChecklistItem("GO-AROUND WAYPOINT: GPS VALID ONLY"),
        ChecklistItem("EP VISUAL LANDING: FBWA AFTER HANDOVER"),
    ],
    "Attitude / Path Deviation": [
        ChecklistItem("ROLL / PITCH ABOVE 30 DEG OR UNSTABLE: RECOVER"),
        ChecklistItem("SAFE LANDING AREA: SELECT"),
        ChecklistItem("NO CONTROL / SAFE AREA; ABOVE 150 FT: PARACHUTE", optional=True),
        ChecklistItem("PATH / WAYPOINT / HEADING: VERIFY"),
        ChecklistItem("GPS VALID: STANDBY WAYPOINT OR RTL"),
        ChecklistItem("GPS INVALID: VISUAL CONTROL TO SAFE AREA"),
    ],
    "Unsafe Landing Area / Approach": [
        ChecklistItem("RUNWAY / WIND / OBSTRUCTIONS: CONFIRM"),
        ChecklistItem("UNSAFE / GPS VALID: GO-AROUND WAYPOINT"),
        ChecklistItem("GPS INVALID: SAFE VISUAL LANDING AREA"),
        ChecklistItem("TOWER: REPORT INTENTION / READ BACK"),
        ChecklistItem("EP HANDOVER: CONFIRM UAV IN SIGHT"),
    ],
    "Post-Incident": [
        ChecklistItem("SITE / INJURIES / FUEL LEAK: SECURE / REPORT"),
        ChecklistItem("ENGINE STOP; RPM ZERO BEFORE GC1 APPROACH", critical=True),
        ChecklistItem("UAV: DISARM / BATTERIES DISCONNECT WHEN SAFE"),
        ChecklistItem("LOCATION / DAMAGE / COMPONENTS: PHOTOGRAPH"),
        ChecklistItem("MISSION / TELEMETRY / VIDEO / TIME: SAVE"),
    ],
}
