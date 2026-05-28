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

### 4. JSON Cloud Inventory Planner (`json_cloud_inventory/proyecto1.py`)
A data-parsing tool designed for managing cloud infrastructure inventory. It extracts data from structured hierarchical files and isolates critical resource metrics.
* **Data Extraction:** Utilizes `json.load()` to parse complex JSON objects into native Python lists of dictionaries.
* **Optimization:** Leverages the native `sum()` function to calculate cumulative disk storage overhead instantly, avoiding resource-heavy nested loops.
* **Logic Filtering:** Applies logical `and` conditions to filter active servers by specific zones (`eu-west`) and flag storage alerts.

### 5. Enterprise CSV User Migrator (`csv_user_migrator/proyecto2.py`)
A database migration utility that cleans corporate user directories by filtering out obsolete data and transforming records into structured tables.
* **Memory Architecture:** Loads CSV data into an in-memory buffer (`list(csv.DictReader)`) to safely release the source file descriptors and avoid system resource exhaustion.
* **Data Transformation:** Mutates directory keys on-the-fly and implements multi-layer email format validation.
* **I/O Efficiency:** Uses `csv.DictWriter` and ensures row persistence via `writerow()`, injecting mandatory header metadata outside the processing loop for optimal I/O disk performance.

### 6. Streaming Log Parser & DDoS Watchdog (`log_security_parser/proyecto3.py`)
A perimeter security utility that parses web server logs (`access.log`) line-by-line to detect potential Denial of Service (DoS) attacks or brute-force attempts.
* **Streaming Performance:** Iterates directly over the log stream, maintaining a near 0 MB memory footprint, ideal for parsing multi-gigabyte production files.
* **Dynamic Mapping:** Implements a text-segmentation pipeline via `.strip().split(" ")[0]` and feeds an in-memory counter dictionary using dynamic IP addresses as immutable keys.
* **Auditing:** Evaluates traffic thresholds via `.items()` outside the stream context and triggers a simulation of kernel-level firewall blocking via `iptables` using persistent Append mode (`"a"`).

---

## 🛠️ Technical Concepts Applied

* **Defensive Programming:** Rigorous user input validation to ensure script stability.
* **Control Structures:** Advanced use of loops, conditionals, and the modern `match-case` standard.
* **Process Management:** Use of `sys.exit(0)` and `sys.exit(1)` to signal success or error states to the Operating System, facilitating Bash integration.
* **Data Integrity:** Strategic selection between Lists (mutable) and Tuples (immutable) based on security needs.
* **Enterprise Formats Handling:** Advanced management of `JSON` hierarchies and safe tabular parsing with the native `csv` module (avoiding unsafe split patterns).
* **High-Performance I/O:** Stream-based file operations and context-isolated file buffers to handle large log files without causing Out-Of-Memory (OOM) situations on servers.

---

## 📂 Installation and Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/gdjrn/My-Python-Scripts.git
   ```
2. Run the scripts using Python 3:
   ```
   # Block 1: Core Automation
   python3 gatekeeper/gatekeeper.py
   python3 home_lab_inventory_monitor/home_lab_inventory_monitor.py
   python3 subnetting_calculator/subnetting_calculator.py
   
   # Block 2: Advanced Data & Log Processing
   python3 json_cloud_inventory/json_cloud_inventory/.py
   python3 csv_user_migrator/csv_user_migrator.py
   python3 log_security_parser/log_security_parser.py
   
   ```
---

**Profile:** IT Systems Technician | Aspiring DevOps Engineer 🚀
