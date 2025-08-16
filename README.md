## Thoughtful AI – Package Sorting Function

### Overview
This repository implements a `sort(width, height, length, mass)` function to classify packages into stacks based on volume and mass constraints. The implementation is in `main.py` with a comprehensive unittest suite executed via pytest.

### Rules
- **Bulky**: volume \(width × height × length\) ≥ 1,000,000 cm³ **or** any dimension ≥ 150 cm.
- **Heavy**: mass ≥ 20 kg.
- **Stacks**:
  - `REJECTED`: bulky **and** heavy
  - `SPECIAL`: bulky **or** heavy (but not both)
  - `STANDARD`: neither bulky nor heavy

### Implementation Notes
- Function: `sort(width: float, height: float, length: float, mass: float) -> str`
- Input handling:
  - All inputs are coerced to `float`; non-numeric values raise `TypeError`.
  - All inputs must be strictly positive; zeros or negatives raise `ValueError`.
- Thresholds are defined as global constants to avoid magic numbers:
  - `BULKY_VOLUME_THRESHOLD_CM3 = 1000000.0`
  - `BULKY_DIMENSION_THRESHOLD_CM = 150.0`
  - `HEAVY_MASS_THRESHOLD_KG = 20.0`
- Tests cover threshold edges, numeric strings acceptance, error cases, and combined conditions.

### Requirements
- Python 3.8+
- `pytest`
- GNU Make (optional, for convenience)

### Install Make (optional)
- Linux (Debian/Ubuntu):
  ```bash
  sudo apt-get update && sudo apt-get install -y make
  ```
- Linux (Fedora/RHEL):
  ```bash
  sudo dnf install -y make
  ```
- macOS:
  ```bash
  xcode-select --install
  # or
  brew install make
  ```
- Windows:
  - Using WSL (Ubuntu): `sudo apt-get update && sudo apt-get install -y make`
  - Using Chocolatey: `choco install make`
  - Using Scoop: `scoop install make`

### Setup
```bash
# (Optional) create and activate a virtual environment
python3 -m venv .venv && source .venv/bin/activate

# Install dependencies
make install
```

Without Make:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### Run Tests
```bash
make test
# or
python3 -m pytest -q main.py
```

### Usage Example
You can import and call `sort` from another module or a Python shell:
```python
from main import sort

# STANDARD
sort(10, 10, 10, 1)

# SPECIAL (bulky by dimension)
sort(150, 1, 1, 1)

# SPECIAL (heavy by mass)
sort(10, 10, 10, 20)

# REJECTED (both conditions)
sort(150, 150, 1, 20)
```

### Notes
- Numeric strings are accepted (e.g., "150", "20"), as inputs are coerced to floats.
- Any zero or negative value will raise `ValueError` by design to enforce strictly positive physical measurements.
