"""
calculator.py — BMS Points List & Controller Sizing Tool

Generates a full tag-by-tag I/O points list from equipment counts, using
standard point templates per equipment type, then sizes required DDC
controllers and panels based on total point count and capacity.
"""
import math
import point_templates as pt


def generate_points_list(equipment_counts: dict) -> list:
    """equipment_counts: dict like {'ahu': 6, 'chiller': 2, 'pump': 4, 'vfd': 3, 'cooling_tower': 1}
    Returns a list of point dicts: tag_id, equipment_instance, equipment_type, description, signal_type"""
    points_list = []

    for eq_key, count in equipment_counts.items():
        if count <= 0:
            continue
        if eq_key not in pt.EQUIPMENT_TEMPLATES:
            raise ValueError(f"Unknown equipment type: {eq_key}")

        template = pt.EQUIPMENT_TEMPLATES[eq_key]
        for unit_num in range(1, count + 1):
            equipment_instance = f"{template['prefix']}-{unit_num}"
            for suffix, description, signal_type in template["points"]:
                tag_id = f"{template['prefix']}{unit_num}-{suffix}"
                points_list.append({
                    "tag_id": tag_id,
                    "equipment_instance": equipment_instance,
                    "equipment_type": template["label"],
                    "description": description,
                    "signal_type": signal_type,
                })

    return points_list


def summarize_points(points_list: list) -> dict:
    ai_count = sum(1 for p in points_list if p["signal_type"] == "AI")
    ao_count = sum(1 for p in points_list if p["signal_type"] == "AO")
    di_count = sum(1 for p in points_list if p["signal_type"] == "DI")
    do_count = sum(1 for p in points_list if p["signal_type"] == "DO")
    total = len(points_list)

    return {
        "ai_count": ai_count,
        "ao_count": ao_count,
        "di_count": di_count,
        "do_count": do_count,
        "total_points": total,
    }


def calculate_controller_sizing(total_points: int, points_per_controller: int,
                                 controllers_per_panel: int) -> dict:
    if points_per_controller <= 0:
        raise ValueError("Points per controller must be greater than zero")
    if controllers_per_panel <= 0:
        raise ValueError("Controllers per panel must be greater than zero")

    controller_count = math.ceil(total_points / points_per_controller) if total_points else 0
    panel_count = math.ceil(controller_count / controllers_per_panel) if controller_count else 0

    return {
        "points_per_controller": points_per_controller,
        "controller_count": controller_count,
        "controllers_per_panel": controllers_per_panel,
        "panel_count": panel_count,
    }


def build_full_report(equipment_counts: dict, points_per_controller: int,
                       controllers_per_panel: int) -> dict:
    if all(v <= 0 for v in equipment_counts.values()):
        raise ValueError("Enter at least one piece of equipment to generate a points list")
    for name, val in equipment_counts.items():
        if val < 0:
            raise ValueError(f"{name} count cannot be negative")

    points_list = generate_points_list(equipment_counts)
    summary = summarize_points(points_list)
    sizing = calculate_controller_sizing(
        summary["total_points"], points_per_controller, controllers_per_panel
    )

    # Group points by equipment instance for organized display
    grouped = {}
    for p in points_list:
        grouped.setdefault(p["equipment_instance"], []).append(p)

    return {
        "points_list": points_list,
        "grouped": grouped,
        "summary": summary,
        "sizing": sizing,
    }
