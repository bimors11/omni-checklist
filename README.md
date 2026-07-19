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

## Build AppImage

```bash
./install.sh
```

The AppImage is written to `dist/omni-checklist-<arch>.AppImage`.

## Structure

- `main.py` launches the app.
- `omni_checklist/checklist_data.py` contains aircraft definitions and checklist text.
- `omni_checklist/screens.py` contains the aircraft picker and checklist workspace.
- `omni_checklist/widgets.py` contains reusable PyQt widgets.
- `omni_checklist/background.py` paints the animated black/cyan background.
- `omni_checklist/styles.py` contains the QSS theme.

The checklist uses concise normal-operations flows for OMNI-Trainer and OMNI-Demonstrator.
