# 🧠 Python Coding Test — Junior Developer

### 🗓 Duration: 2–3 hours

#### Objective
Evaluate your Python programming skills in:
- Core Python & Data Structures
- Threading & Concurrency
- Git Workflow

---

## 🧩 Part 1: Data Processing

You are given `data/sales_data.csv` with columns:
```
order_id, product, quantity, price, region
```

Example:
```
101, Laptop, 2, 50000, South
102, Mouse, 5, 400, North
103, Laptop, 1, 48000, West
104, Keyboard, 3, 800, South
105, Mouse, 10, 380, East
```

### Tasks:
1. Read the CSV file.
2. Compute:
   - Total revenue per region
   - Top-selling product by quantity
   - Average order value
3. Display the results neatly formatted.

> 💡 Use Python data structures (lists, dicts, sets) — do not rely on external analytics libraries.

---

## ⚙️ Part 2: Threading Simulation

Simulate multiple **warehouse workers** processing customer orders simultaneously.

Each order (from the same CSV) should be processed by a separate thread.

Each worker:
- Sleeps for 0.1–0.5 seconds (random)
- Prints:  
  `Worker-1 processed Order 101: Laptop x2`

After all are done, print:
```
All orders processed.
```

Use Python’s built-in `threading` module.

---

## 🧰 Part 3: Git Workflow

1. Initialize a **Git repository** in the project folder.
2. Make at least 3 meaningful commits:
   - Initial commit (starter files)
   - Implemented data processing
   - Added threading simulation
3. Push to your **public GitHub repository**.
4. Share the link.

---

## 🧾 Bonus (Optional)

Add a simple command-line interface using `argparse`:
- `--file <path>` to specify CSV file
- `--threads` to enable/disable threaded processing

---

## 🚀 How to Run

```bash
cd src
python main.py
```

---

## 🧑‍💻 Deliverables

- GitHub Repo Link
- Ensure your code runs without errors in Python ≥ 3.8
