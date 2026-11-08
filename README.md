# OMNI Checklist

PyQt5 checklist app for OMNI-Trainer and OMNI-Demonstrator fixed-wing UAV operations.

## Run

```bash
python3 main.py
```

If PyQt5 is not installed:

```bash
python3 -m pip install -r requirements.txt
```

## Setup

```bash
./setup.sh
```

This checks for required system packages, creates `.venv`, and installs the Python dependencies.
On APT systems, setup refuses package transactions that would remove installed packages. Building the AppImage does not require installing the legacy `fuse` package.

## Build AppImage

```bash
./install.sh
```

The AppImage is written to `dist/omni-checklist-<arch>.AppImage`.

## Structure

- `main.py` launches the app.
- `omni_checklist/checklist_data.py` contains aircraft definitions and checklist text.
- `omni_checklist/emergency_data.py` contains aircraft-specific emergency quick-reference procedures.
- `omni_checklist/screens.py` contains the aircraft picker and checklist workspace.
- `omni_checklist/widgets.py` contains reusable PyQt widgets.
- `omni_checklist/background.py` paints the animated black/cyan background.
- `omni_checklist/styles.py` contains the QSS theme.

OMNI-Trainer normal procedures follow AFM Chapter 4, TEC-ONT-020081-032-ED-A, revision A. Its emergency procedures follow Chapter 3, TEC-ONT-020081-033-ED-A, revision A; the OMNI-Trainer IP Kneeboard is a condensed cross-check.

OMNI-Demonstrator has separate electric-motor, 6S-battery normal and emergency checklists, with no parachute or rangefinder procedure. Its normal checklist also uses the local OMNI-Demonstrator flight-test checklist, except that the user confirmed this aircraft has no rangefinder. The Demonstrator battery values are retained from the earlier application checklist: 24.8-25.2 V before flight, prepare to land below 22.0 V, low at 21.0 V, critical at 18.0 V, and above 22.0 V for a go-around. These values were confirmed for continued use by the user; a Demonstrator AFM was not supplied. Trainer-only performance values and restart limits are not applied to the Demonstrator.

The Emergency Procedures button opens the applicable aircraft's emergency pages directly from any normal section. Emergency pages are independent of normal checklist enforcement.
