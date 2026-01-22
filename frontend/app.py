import sys
import os
import ast
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.validator import run_pydocstyle
from backend.docstring_generator import synthesize_docstring

# ---------------- PAGE SETUP ----------------
st.set_page_config(layout="wide")
st.title("Automated Python Docstring Generator & Validator")
st.caption("Milestone-2 · Generation · Coverage · PEP-257 Compliance")

uploaded = st.file_uploader("Upload Python file", type=["py"])
style = st.selectbox("Docstring Style", ["Google", "NumPy", "reST"])

if uploaded:
    code = uploaded.read().decode("utf-8")

    # ---------- STEP 1: AST PARSING ----------
    tree = ast.parse(code)
    items = []

    # PEP-257 expects a module docstring
    expected_docstrings = 1  # module

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            expected_docstrings += 1
            items.append({
                "kind": "Function",
                "name": node.name,
                "args": [a.arg for a in node.args.args if a.arg != "self"],
                "returns": node.returns is not None,
                "raises": any(isinstance(n, ast.Raise) for n in ast.walk(node)),
                "yields": any(isinstance(n, ast.Yield) for n in ast.walk(node)),
                "attributes": [],
                "node": node,
                "has_docstring": ast.get_docstring(node) is not None
            })

        elif isinstance(node, ast.ClassDef):
            expected_docstrings += 1

            attrs = []
            for n in node.body:
                if isinstance(n, ast.Assign):
                    for t in n.targets:
                        if isinstance(t, ast.Name):
                            attrs.append(t.id)

                if isinstance(n, ast.FunctionDef):
                    expected_docstrings += 1  # methods need docstrings

            items.append({
                "kind": "Class",
                "name": node.name,
                "args": [],
                "returns": False,
                "raises": False,
                "yields": False,
                "attributes": attrs,
                "node": node,
                "has_docstring": ast.get_docstring(node) is not None
            })

    # ---------- STEP 2: DOCSTRING GENERATION (COVERAGE) ----------
    generated_count = 0
    for item in items:
        if not item["has_docstring"]:
            item["node"].body.insert(
                0,
                ast.Expr(
                    value=ast.Constant(
                        s=synthesize_docstring(item, style)
                    )
                )
            )
            generated_count += 1

    generated_code = ast.unparse(tree)

    # ---------- STEP 3: COVERAGE ----------
    total_items = len(items)
    coverage = "N/A" if total_items == 0 else f"{(generated_count / total_items) * 100:.1f}%"

    # ---------- STEP 4: PEP-257 COMPLIANCE ----------
    compliance = run_pydocstyle(code, expected_docstrings)

    # ---------------- METRICS ----------------
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Functions / Classes", total_items)
    col2.metric("Docstrings Generated", generated_count)
    col3.metric("Coverage", coverage)

    # ---------------- TABS ----------------
    tab_code, tab_generated, tab_compliance, tab_summary = st.tabs([
        "📄 Uploaded Code",
        "🧠 Generated Code",
        "⚠ PEP-257 Compliance",
        "📊 Summary & Report"
    ])

    # ---------- TAB 1 ----------
    with tab_code:
        st.code(code, language="python")

    # ---------- TAB 2 ----------
    with tab_generated:
        st.code(generated_code, language="python")

    # ---------- TAB 3 ----------
    with tab_compliance:
        st.subheader("PEP-257 Compliance Report")

        if compliance["status"] == "ERROR":
            st.error(compliance["message"])

        elif compliance["status"] == "PASS":
            st.success("✔ File fully adheres to PEP-257")
            st.metric("Compliance Score", "100%")

        else:
            st.warning("⚠ PEP-257 violations detected")
            st.metric("Compliance Score", f"{compliance['compliance']}%")

            st.markdown("### Rule-wise Violations")
            for v in compliance["violations"]:
                st.code(v["raw"])

    # ---------- TAB 4 ----------
    with tab_summary:
        st.subheader("Coverage & Compliance Summary")

        st.markdown(f"""
        **Coverage**
        - Total functions/classes: **{total_items}**
        - Docstrings generated: **{generated_count}**
        - Coverage: **{coverage}**

        **PEP-257 Compliance**
        - Expected docstrings: **{expected_docstrings}**
        - Compliance score: **{compliance['compliance']}%**
        - Status: **{compliance['status']}**
        """)

        report_payload = {
            "coverage_percent": coverage,
            "total_items": total_items,
            "generated_docstrings": generated_count,
            "expected_docstrings": expected_docstrings,
            "pep257_compliance_percent": compliance["compliance"],
            "pep257_status": compliance["status"],
            "violations": compliance.get("violations", [])
        }

        st.download_button(
            label="Download Detailed Compliance Report (JSON)",
            data=json.dumps(report_payload, indent=4),
            file_name="pep257_compliance_report.json",
            mime="application/json"
        )
