<<<<<<< HEAD
# BMS Points List & Controller Sizing Tool

A Python/Flask tool that generates a tag-by-tag I/O points list from
equipment counts, using standard BMS point templates by equipment type,
plus DDC controller and panel sizing — a first-draft points schedule
deliverable, not just an aggregate point count.

## Why this exists

A real BMS project's points schedule lists every individual point by tag
ID, description, and signal type (AI/AO/DI/DO) — not just a total count.
This tool generates that actual document structure from a simple equipment
count input, giving a usable first draft for a tender submission or
project scoping conversation, rather than requiring the full points list
to be built from scratch by hand.

## What it generates

For each equipment type entered (AHU, Chiller, Pump, standalone VFD,
Cooling Tower), the tool creates individual tagged points for every unit
(e.g. `AHU1-SAT`, `AHU2-SAT` for two AHUs), using standard point templates:

| Equipment | Points/Unit | Signal Types |
|---|---|---|
| AHU | 10 | Supply/Return Air Temp, Duct Static Pressure (AI); CHW Valve, Fan Speed, Damper Command (AO); Fan Status, Filter Status, Freeze Stat (DI); Fan Start/Stop (DO) |
| Chiller | 6 | CHW Supply/Return Temp, % Load (AI); Run Status, Fault (DI); Start/Stop (DO) |
| Pump | 5 | VFD Speed Feedback (AI); Speed Command (AO); Run Status, Fault (DI); Start/Stop (DO) |
| Standalone VFD | 5 | Speed Feedback (AI); Speed Command (AO); Run Status, Fault (DI); Run/Stop (DO) |
| Cooling Tower | 4 | Basin Level (AI); Fan Status, Low Level Alarm (DI); Fan Start/Stop (DO) |

Controllers required = total points ÷ controller capacity (rounded up).
Panels required = controllers ÷ controllers-per-panel (rounded up).

**This is a standard planning-stage template**, reflecting typical BMS
practice — actual points vary by project scope, owner requirements, and
sequence of operations. Use as a first-draft starting point, not a final
points schedule.

## Tech stack

- **Backend:** Python 3, Flask
- **Frontend:** Server-rendered Jinja2 template, vanilla CSS (no build step)
- **No database, no external services** — pure generation/calculation tool

## Getting started

```bash
git clone https://github.com/<your-username>/bms-points-list.git
cd bms-points-list
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5006** in your browser.

## Project structure

```
bms-points-list/
├── app.py               # Flask routes
├── calculator.py          # Points list generation + controller/panel sizing
├── point_templates.py       # Standard point templates by equipment type
├── requirements.txt
└── templates/
    └── index.html              # Form + generated points list + sizing
```

## Roadmap / possible extensions

- Export as CSV/Excel points schedule
- Custom point templates (add/edit points per equipment type)
- Sequence of operations text generation alongside the points list

## License

MIT — free to use and adapt.
=======
# BMS-points-list — Multi Time Zone Digital Clock

This repository contains a simple, single-file digital clock (index.html) that shows the current time and date for multiple IANA time zones. You can add or remove time zones, and it updates every second.

## Files added

- `index.html` — The multi time-zone clock (already committed).
- `README.md` — This README (you're looking at it).
- `screenshots/clock-1.svg` — Screenshot of the clock with several zones shown.
- `screenshots/clock-2.svg` — Screenshot showing the add-zone controls.

## Screenshots

![Clock view](screenshots/clock-1.svg)

![Add zone controls](screenshots/clock-2.svg)

## How to run

1. Clone the repo:

   git clone https://github.com/marshvac2811/BMS-points-list.git
   cd BMS-points-list

2. Open the clock in your browser:

   - Double-click `index.html`, or
   - Serve it locally:
     - Python 3: `python -m http.server 8000`
     - Then visit: `http://localhost:8000`

## Notes

- The clock uses the browser's Intl API for time zone handling (IANA names like `America/New_York`).
- The screenshots are SVG images included for convenience; they are mock screenshots representing the UI.

## Next steps (optional)

- Publish via GitHub Pages (I can help enable Pages and create the workflow or set the branch).
- Convert the UI into a React or Vue component.
- Persist selected time zones to localStorage.

## License

This repository is public domain / MIT — feel free to reuse and adapt.
>>>>>>> 6ae8026871f5b5320b20ecf87ee97c54722208f4
