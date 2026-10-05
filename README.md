# TKJ Network Toolkit

A modular networking toolkit developed by **TKJ-Team-SMKN1** for learning, practical networking, diagnostics, and network-related utilities.

The project is designed with a modular architecture so that individual networking tools can be developed, tested, and maintained independently while remaining part of a single toolkit.

> Bahasa Indonesia: [README-ID.md](README-ID.md)

---

## Project Status

**Current Version:** `V1.0.0`  
**Current Module:** `IPv4 Calculator`  
**Status:** Development

The first release focuses on IPv4 addressing and basic subnet calculation.

---

## Features

### IPv4 Calculator

The current IPv4 module provides:

- IPv4 address validation
- CIDR prefix validation
- Subnet mask calculation
- Network address calculation
- Broadcast address calculation
- First usable host calculation
- Last usable host calculation
- Usable host calculation
- Total IPv4 address calculation

The calculator follows standard IPv4 addressing rules, including support for `/31` and `/32` networks.

---

## Architecture

The project separates the graphical interface, networking logic, and development tests.

```text
Toolkit-TKJ/
├── GUI/
│   ├── __init__.py
│   └── main.py
│
├── IPv4/
│   ├── __init__.py
│   ├── ip_addr.py
│   ├── cidr.py
│   ├── subnet.py
│   ├── network_addr.py
│   ├── broadcast.py
│   ├── usable_hosts.py
│   └── total_addr.py
│
├── IPv4-Dev/
│   ├── __init__.py
│   ├── test_ip_addr.py
│   ├── test_cidr.py
│   ├── test_subnet.py
│   ├── test_network_addr.py
│   ├── test_broadcast.py
│   ├── test_usable_hosts.py
│   └── test_total_addr.py
│
├── requirements.txt
├── requirements-dev.txt
├── requirements-alpine.txt
├── README.md
├── README-ID.md
└── VERSION.md
```

### Module Separation

- **GUI/** contains the graphical interface.
- **IPv4/** contains the core IPv4 calculation and validation logic.
- **IPv4-Dev/** contains automated tests for the IPv4 module.

The GUI uses the same functions exposed by the IPv4 package instead of duplicating networking calculations.

---

## Requirements

- Python 3
- Linux or another compatible Python environment
- PyQt6 for the graphical interface

Additional Python dependencies are listed in:

- `requirements.txt` — standard runtime dependencies
- `requirements-dev.txt` — development and testing dependencies
- `requirements-alpine.txt` — Python dependencies for Alpine Linux

Operating-system packages required by a specific Linux distribution are installed separately using that distribution's package manager.

---

## Installation

### Standard Linux Environment

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Run the application from the project root:

```bash
python -m GUI.main
```

---

### Alpine Linux

Alpine Linux uses a different system environment from most glibc-based Linux distributions. PyQt6 may therefore be installed through Alpine's package manager instead of being built from source by pip.

Install the Alpine PyQt6 package:

```bash
apk add py3-qt6
```

Then install the remaining Python dependencies:

```bash
pip install -r requirements-alpine.txt
```

Run the application:

```bash
python -m GUI.main
```

A graphical display server is also required when running the GUI outside a normal desktop environment.

---

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the complete test suite:

```bash
python -m pytest -v
```

The project uses automated tests to validate the IPv4 calculation modules independently from the GUI.

---

## Design Principles

The project follows several development principles:

1. **Modularity**
   Each networking function is maintained as an independent module.
2. **Testability**
   Core networking functionality is tested independently from the graphical interface.
3. **Portability**
   Python dependencies are separated from operating-system-specific packages.
4. **Maintainability**
   Networking calculations are kept outside the GUI layer to avoid duplicated logic.
5. **Practicality**
   Tools are designed around real networking concepts commonly used in TKJ education and practice.

---

## Current Development Scope

### V1 — IPv4 Calculator

Current scope:

- IPv4 address
- CIDR
- Subnet mask
- Network address
- Broadcast address
- First usable host
- Last usable host
- Usable host count
- Total address count

IPv6, VLSM, and additional networking utilities are outside the current V1 scope.

---

## Project Roadmap

Future versions may expand the toolkit with additional networking utilities and modules.

Planned development areas may include:

- Additional IPv4 utilities
- IPv6 utilities
- VLSM and subnet planning
- DNS utilities
- Network information tools
- Packet and protocol analysis
- Diagnostic utilities

Features are introduced incrementally and are not considered part of a release until implemented and tested.

---

## Versioning

Version information is maintained in `VERSION.md`.

The project uses the following format:

`MAJOR.MINOR.PATCH`

- **MAJOR** — major architectural or compatibility changes
- **MINOR** — new backward-compatible functionality
- **PATCH** — bug fixes and small corrections

---

## Organization

Developed under:

**TKJ-Team-SMKN1**

The project is intended to support practical learning and development within the TKJ (Teknik Komputer dan Jaringan) field.

---

## License

A project license will be added to the repository separately.
