import os
import json
from datetime import datetime
from tkinter import Tk, filedialog
from xerparser.reader import Reader


def safe_date(d):
    if not d:
        return None
    if isinstance(d, datetime):
        return d.strftime("%Y-%m-%d")
    return str(d)


def get_baseline_dates(obj):
    """
    Try every possible baseline field name found in P6 XER variants
    """
    candidates = [
        ("bl_start_date", "bl_end_date"),
        ("baseline_start_date", "baseline_end_date"),
        ("target_start_date", "target_end_date"),
        ("bl1_start_date", "bl1_end_date"),
    ]

    for start_field, finish_field in candidates:
        start = getattr(obj, start_field, None)
        finish = getattr(obj, finish_field, None)
        if start or finish:
            return safe_date(start), safe_date(finish)

    return None, None


def main():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select XER File",
        filetypes=[("XER Files", "*.xer")]
    )

    if not file_path:
        print("No file selected.")
        return

    print(f"Reading: {file_path}")

    xer = Reader(file_path)

    projects = list(xer.projects)
    project_name = projects[0].proj_short_name if projects else "Project"

    tasks = []
    links = []

    # Convert activities
    for a in xer.activities:

        baseline_start, baseline_finish = get_baseline_dates(a)

        tasks.append({
            "id": a.task_id,
            "code": a.task_code,
            "name": a.task_name,

            "start": safe_date(getattr(a, "start_date", None)),
            "finish": safe_date(getattr(a, "end_date", None)),

            "baseline_start": baseline_start,
            "baseline_finish": baseline_finish,

            "early_start": safe_date(getattr(a, "early_start_date", None)),
            "early_finish": safe_date(getattr(a, "early_end_date", None)),
            "late_start": safe_date(getattr(a, "late_start_date", None)),
            "late_finish": safe_date(getattr(a, "late_end_date", None)),

            "duration": getattr(a, "duration", None),
            "float_hours": getattr(a, "total_float_hr_cnt", None),
            "status": getattr(a, "status_code", None)
        })

    # Convert relationships
    for r in xer.relations:
        links.append({
            "id": getattr(r, "task_pred_id", None),
            "source": getattr(r, "pred_task_id", None),
            "target": getattr(r, "task_id", None),
            "type": getattr(r, "pred_type", None)
        })

    output = {
        "project": {
            "name": project_name
        },
        "tasks": tasks,
        "links": links
    }

    output_path = os.path.splitext(file_path)[0] + ".json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"✔ JSON written to: {output_path}")


if __name__ == "__main__":
    main()
