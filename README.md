CSEC Calculator v2.0 🧮

A feature-rich, visually appealing terminal-based calculator with advanced mathematical, financial, and scientific capabilities. Perfect for students, engineers, finance professionals, and anyone who needs powerful calculations in a beautiful terminal interface.

https://img.shields.io/badge/Python-3.6+-blue.svg
https://img.shields.io/badge/License-MIT-green.svg
https://img.shields.io/badge/Status-Stable-brightgreen.svg
✨ Features
🎯 Core Features

    Basic Arithmetic: Addition, subtraction, multiplication, division, modulo, floor division

    Scientific Functions: Trigonometric (sin/cos/tan), logarithms, exponentials, factorials

    Financial Calculations: Future Value, Present Value, Loan Payments (PMT)

    Complex Numbers: Operations in rectangular and polar forms

    Statistical Analysis: Mean, median, mode, standard deviation, variance

    Unit Conversions: Temperature, angle conversions

    Memory Functions: Store, recall, add to memory

    Calculation History: Last 100 calculations with persistent storage

🎨 Visual Enhancements

    Color-coded terminal output using colorama

    Typing animation effects

    Organized, visually appealing menus

    Real-time calculation display

⚙️ Smart Features

    Special inputs: ans (last answer), mem (memory), pi, e

    Configurable decimal places (0-15)

    Scientific notation toggle

    Degree/Radian mode switching

    Persistent history storage in JSON format

📸 Preview
text

############################################################
############################################################
Welcome to CSEC Calculator v2.0
Made by Cyb0rgBytes
############################################################
############################################################
Advanced features:
• Basic arithmetic & Scientific functions
• Trigonometry & Logarithms
• Complex numbers & Statistics
• Financial calculations & Unit conversions
• History & Memory functions
############################################################

📦 Installation
Prerequisites

    Python 3.6 or higher

    pip (Python package manager)

Method 1: Using requirements.txt

    Clone the repository
    bash

git clone https://github.com/Cyb0rgbytes/csecCalculator.git
cd csecCalculator

Install required packages
bash

pip install -r requirements.txt

Method 2: Manual Installation

    Clone the repository
    bash

git clone https://github.com/Cyb0rgbytes/csecCalculator.git
cd csecCalculator

Install the required package
bash

pip install colorama

Method 3: Virtual Environment (Recommended)
bash

# Clone the repository
git clone https://github.com/Cyb0rgbytes/csecCalculator.git
cd csecCalculator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

🚀 Quick Start

Run the calculator:
bash

python CSECCalculator-V2.py

Or make it executable:
bash

# On macOS/Linux
chmod +x CSECCalculator-V2.py
./CSECCalculator-V2.py

# On Windows (run as script)
python CSECCalculator-V2.py

📖 Usage Guide
Main Menu Options
text

1. Basic Operations      → +, -, *, /, **, %, sqrt, //
2. Scientific Operations → sin/cos/tan, log/ln, exp, fact, perm/comb
3. Financial Calculations→ FV, PV, PMT, NPER, RATE
4. Complex Numbers      → +, -, *, /, polar/rectangular forms
5. Statistics           → Mean, median, mode, std dev, variance
6. Memory Operations    → Store, recall, add to memory
7. Unit Conversions     → Temperature, angle conversions
8. View History         → View last 100 calculations
9. Settings             → Configure calculator options
0. Exit                 → Exit the calculator

Special Inputs

    ans - Use the last calculated result

    mem - Use the value stored in memory

    pi - Use the value of π (3.14159...)

    e - Use the value of e (2.71828...)

Example Calculations

Basic Arithmetic:
text

Select option (0-9): 1
Operation: +
Enter first number: 45
Enter second number: 15

Calculating...
45 + 15 = 60.000000

Scientific Functions:
text

Select option (0-9): 2
Operation: sin
Enter angle: 90

Calculating...
sin(90) = 1.000000

Financial Calculation:
text

Select option (0-9): 3
Operation: fv
Present Value: 1000
Interest rate per period (decimal): 0.05
Number of periods: 10

Calculating...
FV(PV=1000.0, rate=0.05, n=10.0) = 1628.894627

⚙️ Configuration

Access settings from the main menu (option 9):

    Decimal places: Set precision (0-15 decimal places)

    Scientific notation: Toggle scientific notation on/off

    Angle mode: Switch between DEGrees and RADians

    History: Enable/disable calculation history

    Clear history: Delete all saved calculations

📁 File Structure
text

csecCalculator/
├── CSECCalculator-V2.py     # Main calculator script
├── requirements.txt         # Dependencies file
├── calculator_history.json  # Auto-generated history file
└── README.md               # This documentation

🔧 Requirements

Create a requirements.txt file with the following content:
txt

colorama==0.4.6

Or for minimal requirements:
txt

colorama>=0.4.0

🐛 Troubleshooting
Common Issues

    "ModuleNotFoundError: No module named 'colorama'"
    bash

pip install colorama

Permission denied on macOS/Linux
bash

chmod +x CSECCalculator-V2.py

Python not found
bash

python3 CSECCalculator-V2.py

    History file corruption

        Delete calculator_history.json to reset history

Platform Notes

    Windows: Works with Python installed from python.org or Microsoft Store

    macOS: Use Python 3.6+ from Homebrew or python.org

    Linux: Use your distribution's package manager to install Python 3

🤝 Contributing

Contributions are welcome! Here's how you can help:

    Fork the repository

    Create a feature branch
    bash

git checkout -b feature/AmazingFeature

Commit your changes
bash

git commit -m 'Add some AmazingFeature'

Push to the branch
bash

git push origin feature/AmazingFeature

    Open a Pull Request

Development Setup
bash

# Clone your fork
git clone https://github.com/your-username/csecCalculator.git
cd csecCalculator

# Set up development environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🙏 Acknowledgments

    Colorama for cross-platform colored terminal text

    Python Standard Library for comprehensive mathematical functions

    All contributors and users of CSEC Calculator

👨‍💻 Author

Cyb0rgBytes

    GitHub: @Cyb0rgbytes

    Project: CSEC Calculator

🌟 Support

If you find this project helpful, please consider:

    Giving it a ⭐ on GitHub

    Sharing it with others

    Reporting issues or suggesting features

Happy Calculating! 🎉 If you encounter any issues or have suggestions, please open an issue on the GitHub repository.
