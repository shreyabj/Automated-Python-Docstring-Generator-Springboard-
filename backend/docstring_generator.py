def humanize(name):
    return name.replace("_", " ")

def summary_from_name(name):
    if name.startswith("get_"):
        return f"Returns the {humanize(name[4:])}."
    if name.startswith("calculate_"):
        return f"Calculates the {humanize(name[10:])}."
    if name.startswith("generate_"):
        return f"Generates {humanize(name[9:])}."
    if name.startswith("check_"):
        return f"Checks whether {humanize(name[6:])}."
    return f"Performs {humanize(name)}."

def synthesize_docstring(meta, style):
    lines = [summary_from_name(meta["name"]), ""]

    if meta.get("args"):
        if style == "Google":
            lines.append("Args:")
            for a in meta["args"]:
                lines.append(f"    {a}: Input parameter.")
        elif style == "NumPy":
            lines += ["Parameters", "----------"]
            for a in meta["args"]:
                lines.append(f"{a} : Any")
                lines.append("    Input parameter.")
        else:
            for a in meta["args"]:
                lines.append(f":param {a}: Input parameter.")

    if meta.get("returns"):
        lines += ["", "Returns:", "    Result of the computation."]

    if meta.get("raises"):
        lines += ["", "Raises:", "    Exception: Raised on invalid input."]

    if meta.get("yields"):
        lines += ["", "Yields:", "    Generator output."]

    if meta.get("attributes"):
        lines += ["", "Attributes:"]
        for a in meta["attributes"]:
            lines.append(f"    {a}: Class attribute.")

    return '"""' + "\n".join(lines).rstrip() + '\n"""'
