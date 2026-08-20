# 📊 Fintech Manager Python

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Architecture](https://img.shields.io/badge/architecture-modular-orange.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)

A script that helps you to track your transactions. Made with Python using modular coding

---

## 🛠️ Tech Stack & Concepts

- **Language:** Python 3.10+
- **Core Concepts:** Modular Architecture, Generators (`yield`), Custom Decorators, Functional Programming (`map`, `filter`), JSON Persistence, Datetime Parsing
- **Dependencies:** None (Uses Python Standard Library only)

---

## 🚀 Features

- **Transaction Management:** Allows registering, sorting, and analyzing transactions by category, date, or amount
- **Data Persistence:** Automatically stores transactions and configuration in JSON files using robust file handling
- **Set Theory Analysis:** Compares monthly spending patterns with historical data using Python set operations (`&`, `-`)
- **Financial Utilities:** Includes a compound interest calculator, a stock market volatility simulator, and a date planner
- **Performance Auditing:** Uses custom decorators to log execution times for critical functions in real time
- **Robust Error Handling:** Prevents crashes from invalid inputs, missing files, or empty data lists

---

## 📂 Project Structure

```text
fintech-manager/
├── main.py
├── config.json
├── core/
│   ├── finance.py
│   ├── auth.py
│   ├── storage.py
│   └── utils.py
└── data/
    ├── app_log.txt
    └── transactions.json
```

---

## 💻 How to Run

1. **Clone the repository (or download the files):**

   ```bash
   git clone https://github.com/diegofm09/fintech-manager.git

   ```

2. **Run main.py:**
   ```bash
   python main.py
   ```
