# Password Cracking & Credential Attack Suite

**Ethical Password Security Toolkit**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/Purpose-Educational-green.svg)](#legal--ethical-disclaimer)

> A modular, educational Python toolkit for password strength analysis, custom dictionary generation, hash extraction simulation, and theoretical brute-force time estimation.

---

## ⚠️ Legal & Ethical Disclaimer

This project is **strictly for educational purposes**, authorized security assessments, and personal password hygiene evaluation.

- **Do not** use this toolkit against any system you do not own or lack explicit written permission to test.
- Unauthorized access to computer systems is illegal under most jurisdictions.
- The authors and contributors accept **no liability** for misuse.
- Always follow responsible disclosure and obtain proper authorization.

---

## Features

| Module | Description |
|--------|-------------|
| **Dictionary Generator** | Creates custom wordlists with common passwords, keyboard patterns, name+year combinations, leetspeak mutations, and hybrid combos |
| **Hash Extractor** | Simulates extraction of Linux `/etc/shadow` and Windows SAM (NTLM) hashes for educational demonstration |
| **Brute-Force Simulator** | Estimates keyspace size and theoretical cracking time based on character set and length (no actual cracking performed) |
| **Password Strength Analyzer** | Evaluates entropy, complexity grade, common patterns, and provides actionable recommendations |
| **Audit Report Generator** | Produces a professional consolidated security audit report |

---

## Project Structure

```
password-cracking-suite/
├── main.py                          # Main entry point
├── modules/
│   ├── __init__.py
│   ├── dictionary_generator.py
│   ├── hash_extractor.py
│   ├── brute_force_simulator.py
│   ├── strength_analyzer.py
│   └── report_generator.py
├── wordlists/                       # Generated wordlists
├── hashes/                          # Extracted / demo hashes
├── reports/                         # Simulation results, analysis & audit reports
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Requirements

- Python 3.8 or higher
- No external dependencies (standard library only)

```bash
# Optional: create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# venv\Scripts\activate    # Windows
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/password-cracking-suite.git
cd password-cracking-suite
chmod +x main.py
```

---

## Usage

### Quick Start – Full Demo Pipeline

```bash
python3 main.py --demo
```

This runs every module in sequence and generates:

- Demo wordlist (`wordlists/demo_wordlist.txt`)
- Demo hashes (`hashes/extracted_hashes_*.txt`)
- Brute-force simulation results
- Password strength analysis
- Complete audit report

### Individual Modules

```bash
# Dictionary Generator (interactive)
python3 main.py --module dict

# Hash Extractor (demo mode)
python3 main.py --module hash

# Brute-Force Simulator
python3 main.py --module brute

# Password Strength Analyzer
python3 main.py --module strength

# Full pipeline
python3 main.py --module full
```

### Interactive Mode

```bash
python3 main.py --interactive
```

---

## Example Output (Demo)

```
╔══════════════════════════════════════════════════════════════════╗
║     PASSWORD CRACKING & CREDENTIAL ATTACK SUITE                  ║
║           Ethical Password Security Toolkit                      ║
╚══════════════════════════════════════════════════════════════════╝

— Analyzing: 'MySecureP@ss2024!' (algo: SHA-512 (Linux)) —
  Length: 17 chars | Complexity: Very Strong
  Keyspace: 2,449,850,032,754,063,150,974,094,486,458,412
  Brute-force time: 51789489953366800.00 years
  Dictionary attack: 6.67 milliseconds
```

---

## Security Recommendations (from the toolkit)

1. Enforce minimum password length of 12–16 characters  
2. Require mixed case, digits, and special characters  
3. Reject passwords found in common breach dictionaries  
4. Implement account lockout / rate-limiting  
5. Prefer long passphrases over complex short passwords  
6. Use a reputable password manager  
7. Enable multi-factor authentication (MFA)  
8. Never reuse passwords across critical accounts  

---

## Contributing

Contributions that improve educational value, documentation, or code quality are welcome.

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/improvement`)  
3. Commit your changes (`git commit -m 'Add useful improvement'`)  
4. Push to the branch (`git push origin feature/improvement`)  
5. Open a Pull Request  

Please keep the ethical focus intact.

---

## License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Built for educational and authorized security research only  
- Inspired by real-world password auditing practices  
- Designed to demonstrate why strong, unique passwords matter  

---

**Stay ethical. Stay curious. Stay secure.**
