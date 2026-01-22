import tempfile
import subprocess
import sys
import os
import re

def run_pydocstyle(code: str, expected_count: int):
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".py",
        mode="w",
        encoding="utf-8"
    ) as f:
        f.write(code)
        path = f.name

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pydocstyle", path],
            capture_output=True,
            text=True
        )

        # pydocstyle missing
        if "No module named pydocstyle" in result.stderr:
            return {
                "status": "ERROR",
                "violations": [],
                "compliance": 0,
                "message": "pydocstyle is not installed"
            }

        # Extract real rule codes dynamically
        violations = []
        rule_pattern = re.compile(r"(D100|D101|D102|D103|D200|D205|D400|D401)")

        for line in result.stdout.splitlines():
            match = rule_pattern.search(line)
            if match:
                violations.append({
                    "rule": match.group(1),
                    "raw": line
                })

        violation_count = len(violations)

        # ✅ REAL compliance formula
        if expected_count == 0:
            compliance = 100
        else:
            compliance = max(
                0,
                round(((expected_count - violation_count) / expected_count) * 100, 2)
            )

        status = "PASS" if violation_count == 0 else "WARN"

        return {
            "status": status,
            "violations": violations,
            "compliance": compliance
        }

    finally:
        os.remove(path)
