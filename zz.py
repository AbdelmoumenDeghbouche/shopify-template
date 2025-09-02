import os

def print_tree(root_dir, prefix=""):
    items = [item for item in os.listdir(root_dir) if item not in ("__pycache__", ".venv")]
    for idx, item in enumerate(sorted(items)):
        path = os.path.join(root_dir, item)
        connector = "+-- " if idx == len(items) - 1 else "|-- "
        print(f"{prefix}{connector}{item}")
        if os.path.isdir(path):
            extension = "    " if idx == len(items) - 1 else "|   "
            print_tree(path, prefix + extension)

if __name__ == "__main__":
    root = "."  # Change to your desired directory
    print_tree(root)