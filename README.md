# 🛡️ My Python Scripts - IT Systems & Automation

This repository contains a collection of automation tools and utility scripts developed in Python, focusing on **System Administration, Networking, and DevOps** tasks.

As an **ASIX** graduate (2025) and IT Systems Technician, my goal is to apply programming logic to enhance security, infrastructure management, and IT efficiency.

## 🚀 Included Projects

### 1. SSH Gatekeeper (`gatekeeper/gatekeeper.py`)
A server access control simulation designed to manage user entry based on security policies.
* **Security:** Uses **tuples** to define restricted users (`root`, `admin`, `guest`), ensuring the security policy remains immutable.
* **Validation:** Implements string normalization with `.strip().lower()` and verifies that privilege levels are numeric using `.isdigit()`.
* **Logic:** Utilizes the `match-case` structure (Python 3.10+) for clean and efficient permission management.

### 2. Home Lab Inventory Monitor (`home_lab_inventory_monitor/home_lab_inventory_monitor.py`)
An interactive manager for administering services in a lab or production environment.
* **Interactivity:** Implements a `while True` loop, allowing multiple operations (add, delete, see) without restarting the script.
* **List Management:** Features to track containers or services, including alphabetical sorting and existence verification before deletion.
* **Use Case:** Ideal for tracking services deployed via Docker in a personal Home Lab.

### 3. IPv4 Subnet Calculator (`subnetting_calculator/subnetting_calculator.py`)
A technical calculator to determine the number of usable hosts in a network based on its CIDR prefix.
* **Network Precision:** Applies range validation (0-32) and handles special cases for `/31` and `/32` masks where standard hosts are unavailable.
* **Automation:** Instantly calculates the formula $2^{(32-n)} - 2$ to avoid manual calculation errors.
* **Error Control:** Prevents execution failures by validating the input data type and providing a clean "exit" option.

---

## 🛠️ Technical Concepts Applied

* **Defensive Programming:** Rigorous user input validation to ensure script stability.
* **Control Structures:** Advanced use of loops, conditionals, and the modern `match-case` standard.
* **Process Management:** Use of `sys.exit(0)` and `sys.exit(1)` to signal success or error states to the Operating System, facilitating Bash integration.
* **Data Integrity:** Strategic selection between Lists (mutable) and Tuples (immutable) based on security needs.

---

## 📂 Installation and Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/gdjrn/My-Python-Scripts.git
   ```
2. Run the scripts using Python 3:
   ```
   python3 gatekeeper/gatekeeper.py
   python3 home_lab_inventory_monitor/home_lab_inventory_monitor.py
   python3 subnetting_calculator/subnetting_calculator.py
   ```
---

**Profile:** IT Systems Technician | Aspiring DevOps Engineer 🚀
