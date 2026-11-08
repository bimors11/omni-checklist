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
- `omni_checklist/emergency_data.py` contains OMNI-Trainer emergency quick-reference procedures.
- `omni_checklist/screens.py` contains the aircraft picker and checklist workspace.
- `omni_checklist/widgets.py` contains reusable PyQt widgets.
- `omni_checklist/background.py` paints the animated black/cyan background.
- `omni_checklist/styles.py` contains the QSS theme.

OMNI-Trainer normal procedures follow AFM Chapter 4, TEC-ONT-020081-032-ED-A, revision A. Its Emergency Procedures button opens Chapter 3, TEC-ONT-020081-033-ED-A, revision A, directly from any normal section. The OMNI-Trainer IP Kneeboard is used as a condensed cross-check. Emergency pages are independent of normal checklist enforcement. OMNI-Demonstrator retains its existing normal checklist; the cited AFM chapters cover OMNI-Trainer only.
