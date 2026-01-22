def format_docstring(sections, style):
    if style == "Google":
        return '"""\\n' + "\\n".join(sections) + '\\n"""'

    if style == "NumPy":
        formatted = []
        for s in sections:
            if s.endswith(":"):
                formatted.append(s)
                formatted.append("-" * len(s))
            else:
                formatted.append(s)
        return '"""\\n' + "\\n".join(formatted) + '\\n"""'

    if style == "reST":
        rst = []
        for s in sections:
            if s.startswith("    "):
                param = s.strip().split(":")[0]
                rst.append(f":param {param}: Description.")
            else:
                rst.append(s)
        return '"""\\n' + "\\n".join(rst) + '\\n"""'
