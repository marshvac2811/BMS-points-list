"""
app.py — BMS Points List & Controller Sizing Tool
Run locally: python app.py  →  http://127.0.0.1:5006
"""
from flask import Flask, render_template, request
import calculator as calc
import point_templates as pt

app = Flask(__name__)

DEFAULTS = {
    "ahu": "", "chiller": "", "pump": "", "vfd": "", "cooling_tower": "",
    "points_per_controller": "24", "controllers_per_panel": "2",
}


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    form_values = dict(DEFAULTS)

    if request.method == "POST":
        for key in form_values:
            form_values[key] = request.form.get(key, "")

        try:
            equipment_counts = {
                "ahu": int(form_values["ahu"] or 0),
                "chiller": int(form_values["chiller"] or 0),
                "pump": int(form_values["pump"] or 0),
                "vfd": int(form_values["vfd"] or 0),
                "cooling_tower": int(form_values["cooling_tower"] or 0),
            }
            result = calc.build_full_report(
                equipment_counts=equipment_counts,
                points_per_controller=int(form_values["points_per_controller"]),
                controllers_per_panel=int(form_values["controllers_per_panel"]),
            )
        except ValueError as e:
            error = str(e)
        except Exception:
            error = "Please check that all fields contain valid whole numbers."

    return render_template(
        "index.html",
        equipment_labels=pt.EQUIPMENT_TEMPLATES,
        form_values=form_values,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5006)
