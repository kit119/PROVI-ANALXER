# ProVI AnalyXER

เครื่องมือวิเคราะห์ตารางงาน Primavera P6 (.XER) แบบ Client-Side

ProVI AnalyXER เป็นเครื่องมือสำหรับแปลงไฟล์ Primavera P6 `.xer` เป็น JSON และแสดงผลตารางงานในรูปแบบ Interactive ผ่านเว็บเบราว์เซอร์ โดยไม่ต้องใช้ Backend Server

เหมาะสำหรับ:
- วิศวกรวางแผนงาน (Planning Engineer)
- Project Control
- ผู้บริหารที่ต้องการดู Schedule แบบรวดเร็ว
- งานวิเคราะห์ Delay / Critical Path

ระบบทำงานแบบ Client-Side ทั้งหมด (เปิดผ่าน index.html ได้ทันที)

---

## ความสามารถหลัก

### 📅 Gantt Chart
- ซูมระดับ Year / Quarter / Month / Week / Day
- แสดง Critical Path
- เปรียบเทียบ Baseline
- แสดง Float
- เลือกระดับ WBS (1–3)

### 📊 วิเคราะห์สุขภาพโครงการ
- เปอร์เซ็นต์ความคืบหน้า
- ความหนาแน่นงาน Critical
- วิเคราะห์กิจกรรมล่าช้า
- ตัวชี้วัดสุขภาพ Schedule

### 📈 S-Curve
- Planned vs Actual
- รองรับ Baseline
- กรองข้อมูลแบบ Dynamic

### 🗂 WBS Hierarchy
- Tree view แบบ Expand / Collapse
- สร้างโครงสร้างจาก Activity Code

---

## โครงสร้างโปรเจกต์
/index.html หน้าเว็บหลัก
/project.json ไฟล์ข้อมูลตัวอย่าง
/xer2json.py ตัวแปลง XER → JSON
/assets/ ไฟล์ JS / CSS


---

## วิธีใช้งาน

### เปิดเว็บโดยตรง
ดับเบิลคลิก `index.html`

หรือรัน local server:

```bash
python -m http.server 8000

แล้วเปิด:
http://localhost:8000

pip install -r requirements.txt

จากนั้นรัน:
python xer2json.py
  
เลือกไฟล์ .xer
ระบบจะสร้างไฟล์ .json ในโฟลเดอร์เดียวกัน

สามารถนำไฟล์ JSON ไปโหลดในหน้าเว็บได้ทันที

ข้อควรทราบ

รองรับไฟล์ขนาดใหญ่ แต่ขึ้นอยู่กับหน่วยความจำของ Browser

Field ของ Baseline ในแต่ละเวอร์ชัน P6 อาจแตกต่างกัน

เป็นเครื่องมือวิเคราะห์เบื้องต้น ไม่แทน Primavera P6

License

MIT License

ผู้พัฒนา

ProVI AnalyXER
เครื่องมือวิเคราะห์ Schedule แบบ Lightweight สำหรับงาน Project Control


---

## 📌 แนะนำเพิ่มอีกนิด (มืออาชีพมากขึ้น)

ใน `README.md` ภาษาอังกฤษ เพิ่มบรรทัดนี้ตอนบนสุด:

```markdown
[🇹🇭 อ่านเอกสารภาษาไทย](README.th.md)

และใน README.th.md:

[🇬🇧 English Version](README.md)

