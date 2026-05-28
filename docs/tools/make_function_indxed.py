import ast
from pathlib import Path



def _ast_to_source(node: ast.AST, source: str) -> str:
    segment = ast.get_source_segment(source, node)
    if segment is not None:
        return segment.strip()
    return ast.unparse(node)


def _format_function_arguments(node: ast.AST, source: str) -> str:
    args = node.args
    parts = []

    positional = [*args.posonlyargs, *args.args]
    positional_defaults = [None] * (len(positional) - len(args.defaults)) + list(args.defaults)

    for i, arg in enumerate(positional):
        label = arg.arg
        if arg.annotation is not None:
            label += ": " + _ast_to_source(arg.annotation, source)
        default = positional_defaults[i]
        if default is not None:
            label += " = " + _ast_to_source(default, source)
        parts.append(label)

    if args.posonlyargs:
        parts.insert(len(args.posonlyargs), "/")

    if args.vararg is not None:
        label = "*" + args.vararg.arg
        if args.vararg.annotation is not None:
            label += ": " + _ast_to_source(args.vararg.annotation, source)
        parts.append(label)
    elif args.kwonlyargs:
        parts.append("*")

    for i, arg in enumerate(args.kwonlyargs):
        label = arg.arg
        if arg.annotation is not None:
            label += ": " + _ast_to_source(arg.annotation, source)
        default = args.kw_defaults[i]
        if default is not None:
            label += " = " + _ast_to_source(default, source)
        parts.append(label)

    if args.kwarg is not None:
        label = "**" + args.kwarg.arg
        if args.kwarg.annotation is not None:
            label += ": " + _ast_to_source(args.kwarg.annotation, source)
        parts.append(label)

    return "(" + ", ".join(parts) + ")"


def list_python_functions(folder: str | Path) -> list[dict]:
    """Return function name, argument list, and line number for Python files in a folder."""
    root = Path(folder)

    if not root.exists() or not root.is_dir():
        raise ValueError(f"Folder does not exist or is not a directory: {folder}")

    entries = []

    for path in sorted(root.rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source)

        class FunctionCollector(ast.NodeVisitor):
            def __init__(self):
                self.scope = []

            def visit_ClassDef(self, node):
                self.scope.append(node.name)
                self.generic_visit(node)
                self.scope.pop()

            def visit_FunctionDef(self, node):
                qualified_name = ".".join([*self.scope, node.name])
                entries.append({
                    "file": str(path.relative_to(root).as_posix()),
                    "function": qualified_name,
                    "arguments": _format_function_arguments(node, source),
                    "line": node.lineno,
                })
                self.scope.append(node.name)
                self.generic_visit(node)
                self.scope.pop()

            def visit_AsyncFunctionDef(self, node):
                qualified_name = ".".join([*self.scope, node.name])
                entries.append({
                    "file": str(path.relative_to(root).as_posix()),
                    "function": qualified_name,
                    "arguments": _format_function_arguments(node, source),
                    "line": node.lineno,
                })
                self.scope.append(node.name)
                self.generic_visit(node)
                self.scope.pop()

        FunctionCollector().visit(tree)

    return sorted(entries, key=lambda item: (item["file"], item["line"], item["function"]))



def header():
    return """\
# API Reference

This section lists the QuantLib functions made available to Excel.

"""

def subsection(file_name: str) -> str:
    file_name = file_name.rsplit("/", 1)[-1].rsplit(".", 1)[0].capitalize()
    return f"## {file_name}\n\n"

def function_entry(entry: dict) -> str:
    link = f"https://github.com/frame-consulting/QuantLibXlOil/blob/main/src/quantlib_xloil/{entry['file']}#L{entry['line']}"
    return f"[{entry['function']}]({link}){entry['arguments']}\n\n"

if __name__ == "__main__":
    import json
    import sys

    if len(sys.argv) > 2:
        print("Usage: python make_function_indexed.py <folder>")
        sys.exit(1)

    if len(sys.argv) == 1:
        folder = "src/quantlib_xloil"
    else:
        folder = sys.argv[1]

    functions = list_python_functions(folder)
    # print(json.dumps(functions, indent=2))
    print(header())
    file_name = None
    for entry in functions:
        if entry["function"][0] != "q":
            continue
        if file_name != entry["file"]:
            file_name = entry["file"]
            print(subsection(file_name))
        print(function_entry(entry))