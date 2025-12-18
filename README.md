# ⚡ DigiConvert: Binary ↔ Decimal ↔ Gray Code Converter

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

A professional, interactive web application designed for **Electronics & Communication Engineering (ECE)** students. This tool provides accurate real-time conversions between Binary, Decimal, and Gray Code, complete with **step-by-step explanations** of the underlying digital logic.

---

## 🚀 Key Features

- **✨ Comprehensive Conversions**:
  - Binary ↔ Decimal
  - Binary ↔ Gray Code (using XOR logic)
- **🧠 Step-by-Step Logic**: see exactly _how_ the conversion works (e.g., `B0 = G0`, `B1 = B0 ⊕ G1` calculations).
- **🎨 Premium UI/UX**:
  - **Vibrant Gradient Background**: A dynamic, modern aesthetic.
  - **Glassmorphism Cards**: Sleek, translucent design elements.
  - **Responsive**: Fully optimized for mobile, tablet, and desktop.
- **⚡ Dynamic Interactions**:
  - Input placeholders update automatically based on the selected conversion type (e.g., `1010` for Binary, `38` for Decimal).
  - Instant copy-to-clipboard functionality.
- **🛡️ Robust Error Handling**: Immediate feedback for invalid inputs (e.g., typing '2' in a binary field).

---

## 🛠️ Tech Stack

- **Backend**: Python (**Flask**) - Handles arithmetic operations and bitwise manipulation logic.
- **Frontend**:
  - **HTML5** (Semantic structure)
  - **CSS3** (Custom variables, Keyframe animations, Flexbox/Grid - _No framework dependencies_)
  - **JavaScript** (Async/Await Fetch API for seamless non-reloading updates)
- **Design**: Custom "Glassmorphism" design system with Google Fonts ('Outfit').

---

## 📂 Project Structure

```
Binary Converter/
├── app.py              # Main Flask Application
├── requirements.txt    # Project Dependencies
├── templates/          # Frontend Files
│   ├── index.html      # Main HTML Interface
│   ├── style.css       # Custom Styling (Glassmorphism & Animations)
│   └── script.js       # Client-side Logic (Validation & API Calls)
└── README.md           # Documentation
```

---

## 🧠 Digital Logic Implemented

This project strictly follows standard digital electronics formulas:

1.  **Binary to Gray Code**:

    ```python
    Gray = Binary XOR (Binary >> 1)
    ```

    _The Most Significant Bit (MSB) remains unchanged. Subsequent bits are XORed with the preceding binary bit._

2.  **Gray Code to Binary**:

    - MSB is copied directly.
    - Next Bit = (Previous Binary Bit) **XOR** (Current Gray Bit).

3.  **Decimal Conversions**:
    - **Decimal → Binary**: Successive Division by 2.
    - **Binary → Decimal**: Weighted Summation ($2^0, 2^1, 2^2...$).

---

## 📥 Getting Started

### Prerequisites

- Python 3.x installed

### Installation

1.  **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/DigiConvert.git
    cd DigiConvert
    ```

2.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**

    ```bash
    python app.py
    ```

4.  **Open in Browser**
    Visit `http://127.0.0.1:5000/` to start converting!

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for new conversion types (e.g., Hexadecimal, Octal).

---

_Built with ❤️ for the ECE Community._
