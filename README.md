🧮 CSEC Calculator v2.0

The Ultimate Terminal-Based Scientific Calculator

⚡ Experience calculations like never before—powerful, beautiful, and packed with features! ⚡

https://img.shields.io/badge/Python-3.6+-blue.svg
https://img.shields.io/badge/License-MIT-green.svg
https://img.shields.io/badge/Status-Stable-brightgreen.svg

🎬 What's New in V2.0?
🌟 Visual & UI Enhancements
Feature	Generic Calculator	CSEC Calculator V2.0
Interface	Plain text prompts	🎭 Rich, color-coded terminal with colorama
Feedback	Static results	🌀 Animated "Calculating..." sequence
History	None or temporary	📜 Persistent 100-entry history (JSON saved)
Special Inputs	Numbers only	🎯 ans, mem, pi, e smart keywords
🔧 Technical & Feature Improvements
Category	V2.0 Enhancements
🚀 Capabilities	Scientific, Financial, Complex Numbers, Statistics, Unit Conversions
🎯 Accuracy	Handles complex numbers, degree/radian modes, configurable precision (0-15 places)
💾 Memory	Store, recall, add to, subtract from memory
⚙️ Settings	Interactive menu for decimal places, scientific notation, angle mode toggles
🚀 How to Get Started
🎯 Prerequisites
bash

# Check if you have Python 3.6+
🐍 python3 --version

# Check for pip
📦 pip --version

⚡ Quick Installation

    Clone the repository
    bash

📁 git clone https://github.com/Cyb0rgbytes/csecCalculator.git
📂 cd csecCalculator

Install the single dependency
bash

💻 pip install colorama

Or use the included requirements.txt:
bash

💻 pip install -r requirements.txt

requirements.txt Content:
txt

colorama>=0.4.0

🎮 Usage Examples
▶️ Running the Calculator
bash

# Run directly with Python
🚀 python CSECCalculator-V2.py

# Or make it executable (Linux/Mac)
🔧 chmod +x CSECCalculator-V2.py
🚀 ./CSECCalculator-V2.py

🧩 Sample Session
bash

############################################################
Welcome to CSEC Calculator v2.0
Made by Cyb0rgBytes
############################################################
Advanced features:
• Basic arithmetic & Scientific functions
• Trigonometry & Logarithms
• Complex numbers & Statistics
• Financial calculations & Unit conversions
• History & Memory functions
############################################################

Select option (0-9): 1
Operation: +
Enter first number: ans
Enter second number: pi

Calculating...
45 + 3.141593 = 48.141593

📋 Full Command Menu
text

============================================================
                         MAIN MENU
============================================================
1. Basic Operations      (+, -, *, /, **, %, sqrt, //)
2. Scientific Operations (sin, cos, tan, log, ln, exp, fact)
3. Financial Calculations(FV, PV, PMT, NPER, RATE)
4. Complex Numbers      (+, -, *, /, polar, rect)
5. Statistics           (mean, median, mode, stdev, variance)
6. Memory Operations    (store, recall, clear, add, subtract)
7. Unit Conversions     (deg2rad, rad2deg, c2f, f2c)
8. View History         (Last 100 calculations)
9. Settings             (Configure precision, notation, etc.)
0. Exit
============================================================

🏗️ Architecture & Features
📁 File Structure
text

csecCalculator/
├── CSECCalculator-V2.py      # 🧠 Main calculator application
├── requirements.txt          # 📦 Single dependency file
├── calculator_history.json   # 💾 Auto-saved calculation history
└── README.md                # 📖 This file

✨ Core Features in Detail

    🔢 Smart Input: Accepts numbers, ans (last answer), mem (memory value), pi, and e.

    🎨 Formatted Output: Configurable decimal places & automatic scientific notation.

    📊 Financial Functions: Quickly compute Future Value (FV), Present Value (PV), and Loan Payments (PMT).

    ➿ Complex Number Support: Full arithmetic and conversion between rectangular and polar forms.

    📈 Statistical Suite: One-pass analysis: mean, median, mode, standard deviation, variance, min, max, range.

🛠️ Troubleshooting
Symptom	🩹 Solution
"ModuleNotFoundError: No module named 'colorama'"	Install it: pip install colorama
Permission denied on Linux/Mac	Run: chmod +x CSECCalculator-V2.py
Python not found	Use python3 CSECCalculator-V2.py
History file corruption	Delete calculator_history.json to reset
🤝 Contributing

We 💖 contributions! Here's how you can help:
bash

# 1. Fork the repository
🍴 Click "Fork" on GitHub

# 2. Create a feature branch
🌿 git checkout -b feature/AmazingFeature

# 3. Commit your changes
💾 git commit -m "Add AmazingFeature"

# 4. Push to the branch
🚀 git push origin feature/AmazingFeature

# 5. Open a Pull Request
🎉 Create PR on GitHub

Areas for Contribution:

    🔢 Additional scientific/engineering functions

    📐 More unit conversion categories

    🎨 Enhanced UI/UX for the terminal

    📊 Extended financial calculation options

📜 License

MIT License

Copyright (c) 2024 Cyb0rgBytes

For full license terms, see the LICENSE file.

Made with ❤️ by Cyb0rgBytes
⚡ Happy Calculating! ⚡
