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
