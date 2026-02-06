import sys
from backend.validator import run_pydocstyle

def main():
    if len(sys.argv) < 2:
        print("Usage: python backend/cli.py <file.py>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # STRICT enforcement for Milestone 3
    # Any PEP-257 violation = FAIL
    result = run_pydocstyle(code, expected_count=1000)

    if result["status"] != "PASS":
        print("❌ Docstring validation failed")
        for v in result.get("violations", []):
            print(v["raw"])
        sys.exit(1)

    print("✅ Docstring validation passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
