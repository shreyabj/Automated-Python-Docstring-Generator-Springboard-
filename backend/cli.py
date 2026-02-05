import sys
from backend.validator import run_pydocstyle

def main():
    if len(sys.argv) < 2:
        print("Usage: python backend/cli.py <file.py>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    # Simple expected docstring count (Milestone 3 level)
    expected_docstrings = 1  # module

    result = run_pydocstyle(code, expected_docstrings)

    if result["status"] == "WARN":
        print("❌ Docstring validation failed")
        for v in result["violations"]:
            print(v["raw"])
        sys.exit(1)

    print("✅ Docstring validation passed")
    sys.exit(0)

if __name__ == "__main__":
    main()
