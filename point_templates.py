"""
point_templates.py — Standard BMS I/O Point Templates by Equipment Type

Defines the standard set of points typically monitored/controlled for each
equipment type in a BMS integration, classified by signal type:
  AI = Analog Input   (e.g. temperature, pressure sensor readings)
  AO = Analog Output  (e.g. valve position command, speed command)
  DI = Digital Input  (e.g. run/stop status, fault, filter switch)
  DO = Digital Output (e.g. start/stop command)

These mirror a typical I/O points list as would appear in a BMS project's
sequence of operations / points schedule document. Actual points vary by
project scope, equipment type, and owner requirements — this is a
standard planning-stage template, not a substitute for project-specific
engineering.
"""

# Each template point: (suffix, description, signal_type)
AHU_POINTS = [
    ("SAT", "Supply Air Temperature", "AI"),
    ("RAT", "Return Air Temperature", "AI"),
    ("DSP", "Duct Static Pressure", "AI"),
    ("CHWV", "Chilled Water Valve Command", "AO"),
    ("FSC", "Fan Speed Command (VFD)", "AO"),
    ("FS", "Fan Status", "DI"),
    ("FSS", "Fan Start/Stop Command", "DO"),
    ("FLT", "Filter Status (DP Switch)", "DI"),
    ("DMP", "Outside Air Damper Command", "AO"),
    ("FRZ", "Freeze Stat Alarm", "DI"),
]

CHILLER_POINTS = [
    ("CHWST", "CHW Supply Temperature", "AI"),
    ("CHWRT", "CHW Return Temperature", "AI"),
    ("LOAD", "% Load (via gateway)", "AI"),
    ("STAT", "Chiller Run Status", "DI"),
    ("SS", "Chiller Start/Stop Command", "DO"),
    ("ALM", "Chiller Fault/Alarm", "DI"),
]

PUMP_POINTS = [
    ("STAT", "Pump Run Status", "DI"),
    ("SS", "Pump Start/Stop Command", "DO"),
    ("ALM", "Pump Fault", "DI"),
    ("SPDFB", "VFD Speed Feedback", "AI"),
    ("SPDCMD", "VFD Speed Command", "AO"),
]

VFD_POINTS = [
    ("SPDCMD", "Speed Command", "AO"),
    ("SPDFB", "Speed Feedback", "AI"),
    ("STAT", "Run Status", "DI"),
    ("ALM", "Fault Status", "DI"),
    ("SS", "Run/Stop Command", "DO"),
]

COOLING_TOWER_POINTS = [
    ("FS", "Fan Status", "DI"),
    ("SS", "Fan Start/Stop Command", "DO"),
    ("LVL", "Basin Level", "AI"),
    ("LVLALM", "Basin Low Level Alarm", "DI"),
]

EQUIPMENT_TEMPLATES = {
    "ahu": {"label": "AHU", "prefix": "AHU", "points": AHU_POINTS},
    "chiller": {"label": "Chiller", "prefix": "CH", "points": CHILLER_POINTS},
    "pump": {"label": "Pump", "prefix": "PP", "points": PUMP_POINTS},
    "vfd": {"label": "Standalone VFD", "prefix": "VFD", "points": VFD_POINTS},
    "cooling_tower": {"label": "Cooling Tower", "prefix": "CT", "points": COOLING_TOWER_POINTS},
}
