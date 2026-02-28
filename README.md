# ProVI AnalyXER

Lightweight Primavera P6 XER Analyzer (Client-Side)

ProVI AnalyXER is a browser-based project schedule visualization and health analysis tool.  
It converts Primavera P6 `.xer` files into JSON format and provides interactive analytics — fully client-side.

No backend required for visualization.

---

## 🚀 Features

### 📅 Gantt Chart
- Year / Quarter / Month / Week / Day zoom
- WBS level toggle (1–3)
- Critical path highlighting
- Baseline comparison
- Drag & auto scheduling enabled

### 📊 Schedule Analytics
- Overall progress %
- Critical activity density
- Delay analysis
- Float visibility
- Schedule health indicator

### 📈 S-Curve
- Planned vs Actual progress
- Baseline-aware
- Dynamic filtering support

### 🗂 WBS Hierarchy (D3 Tree)
- Expand / collapse
- Code-based hierarchy generation

---

## 🧩 Project Structure
/index.html → Main Web UI
/project.json → Demo project data
/xer2json.py → XER → JSON converter
/assets/ → JS/CSS libraries


---

## 🖥 Usage (Web Viewer)

### Option 1 – GitHub Pages
1. Upload repository
2. Enable GitHub Pages
3. Open `index.html`

### Option 2 – Local

Double-click `index.html`  

Or serve with:

```bash
python -m http.server 8000


Convert Primavera XER to JSON
python xer2json.py

Select your .xer file.
A .json file will be generated in the same directory.

Load it in the browser using:

Auto-load (if named project.json)

File upload button

📦 Requirements (Converter Only)

The web viewer requires no installation.

For XER conversion:

Python 3.8+

xerparser

Install dependencies:

pip install -r requirements.txt

Expected JSON Format
{
  "project": { "name": "Project Name" },
  "tasks": [
    {
      "id": 1,
      "code": "P1-01",
      "name": "Activity Name",
      "start": "YYYY-MM-DD",
      "finish": "YYYY-MM-DD",
      "duration": 10,
      "float_hours": 0,
      "status": "TK_Complete",
      "baseline_start": "YYYY-MM-DD",
      "baseline_finish": "YYYY-MM-DD"
    }
  ],
  "links": [
    { "id": 1, "source": 1, "target": 2 }
  ]
}
⚠️ Notes

Large schedules (10,000+ activities) may require performance tuning.

Browser memory limits apply.

Baseline fields vary across P6 versions; converter attempts auto-detection.

🏗 Roadmap

Float distribution chart

Risk radar

Monte Carlo simulation

Schedule Health Index

Critical path length trend

Resource heatmap

📜 License

MIT License

👷 Author

ProVI AnalyXER
Client-side Primavera schedule analytics tool.


---

# requirements.txt

```txt
xerparser>=0.2.0
