import ast

def extract_metadata(code: str):
    tree = ast.parse(code)

    functions = []
    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions.append({
                "type": "function",
                "name": node.name,
                "args": [a.arg for a in node.args.args if a.arg != "self"],
                "returns": ast.unparse(node.returns) if node.returns else None,
                "has_docstring": ast.get_docstring(node) is not None,
                "raises": any(isinstance(n, ast.Raise) for n in ast.walk(node)),
                "yields": any(isinstance(n, ast.Yield) for n in ast.walk(node)),
                "node": node
            })

        if isinstance(node, ast.ClassDef):
            attributes = []
            for n in node.body:
                if isinstance(n, ast.Assign):
                    for t in n.targets:
                        if isinstance(t, ast.Name):
                            attributes.append(t.id)

            classes.append({
                "type": "class",
                "name": node.name,
                "attributes": attributes,
                "has_docstring": ast.get_docstring(node) is not None,
                "node": node
            })

    return functions, classes, tree
