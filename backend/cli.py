import sys
import subprocess
import tempfile
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python backend/cli.py <file.py>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Run pydocstyle directly and capture exit code
    result = subprocess.run(
        ["pydocstyle", file_path],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("❌ Docstring validation failed (PEP 257 violations detected):")
        print(result.stdout)
        sys.exit(1)

    print("✅ Docstring validation passed (PEP 257 compliant)")
    sys.exit(0)

if __name__ == "__main__":
    main()
