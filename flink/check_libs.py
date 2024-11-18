import subprocess

def check_installed_libs():
    print("Checking installed libraries...")
    result = subprocess.run(["pip", "list"], capture_output=True, text=True)
    print(result.stdout)

def test_imports():
    print("Testing library imports...")
    libraries = ["pyflink", "pemja"]
    for lib in libraries:
        try:
            __import__(lib)
            print(f"Library '{lib}' imported successfully.")
        except ImportError:
            print(f"Error: Library '{lib}' is not installed or cannot be imported.")

if __name__ == "__main__":
    check_installed_libs()
    test_imports()
