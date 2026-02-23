# 🚀 Docstring Validator  
### Automated Python Docstring Generator & PEP 257 Compliance Engine

Docstring Validator is a production-ready documentation governance tool that automatically generates, validates, and enforces Python docstrings in accordance with **PEP 257** standards.

It integrates seamlessly into local development workflows, pre-commit hooks, CI pipelines, and provides an interactive Streamlit dashboard for analytics and review.

---

## 📌 Overview

As Python projects grow, documentation often becomes inconsistent or incomplete.  
This leads to:

- Knowledge loss across teams  
- Reduced maintainability  
- Slower onboarding  
- Increased technical debt  

Docstring Validator transforms documentation from an optional practice into an enforceable engineering standard.

---

## ✨ Key Features

- 🧠 AST-based static code analysis (safe, non-executing)
- 📝 Automated docstring generation for undocumented entities
- 📏 PEP 257 validation using `pydocstyle`
- 📊 Compliance percentage calculation
- 🔐 Pre-commit hook enforcement
- 🔄 CI workflow validation
- ⚙ Project-level configuration via `pyproject.toml`
- 🖥 Interactive Streamlit analytics dashboard
- 📦 Packaged as a pip-installable CLI tool

---

# ⚙ Installation

## Install from PyPI

```bash
pip install docstring-validator

## 🚀 CLI Usage, Library Integration & Workflow Enforcement

### 🖥 Command Line Interface (CLI)

Validate a Python file:

```bash
docstring-validator sample.py
```

#### ✔ Example Output — Compliant

```text
✔ Documentation is compliant.
```

#### ❌ Example Output — Violations Found

```text
❌ Violations found:
D103 at line 4: Missing function docstring
D101 at line 10: Missing class docstring
```

---

### 📦 Library Usage (Programmatic Access)

You can integrate the tool directly into your Python applications.

#### Validate Code Programmatically

```python
from docstring_validator.validator import run_pydocstyle

code = """
def add(a, b):
    return a + b
"""

result = run_pydocstyle(code)
print(result)
```

#### Automatically Insert Missing Docstrings

```python
from docstring_validator.docstring_generator import auto_fix

code = """
def subtract(a, b):
    return a - b
"""

fixed_code = auto_fix(code)
print(fixed_code)
```

---

### 🔐 Pre-Commit Enforcement

Install and enable pre-commit:

```bash
pip install pre-commit
pre-commit install
```

Once configured, any commit containing undocumented public entities will be automatically blocked.

---

### 🔄 CI Workflow Enforcement

The integrated GitHub Actions workflow validates:

- PEP 257 compliance  
- Documentation coverage  
- Project-level documentation standards  

This ensures that only compliant code can be merged into the main branch.

---

### ⚙ Project Configuration (`pyproject.toml`)

You can configure enforcement rules at the project level:

```toml
[tool.docstring-validator]
coverage_threshold = 100
enforce_pep257 = true
```

This allows customizable compliance thresholds and flexible documentation policies.
