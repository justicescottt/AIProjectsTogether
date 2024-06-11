import subprocess
import sys


def run_command(command):
    """Run a shell command and return the output."""
    result = subprocess.run(command, shell=True,
                            text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
    return result.stdout


    def lint_and_fix_code():
    """Lint and auto-fix the code using flake8, autopep8, and black."""
    print("Running flake8 to check for linting issues...")
    flake8_output = run_command("flake8 . --exit-zero")
    if flake8_output:
        print("flake8 output:\n", flake8_output)

    print("Running autopep8 to fix code style issues...")
    run_command("autopep8 --in-place --aggressive --aggressive **/*.py")

    print("Running black to format code...")
    run_command("black .")


def main():
    """Main function to lint and auto-fix the code."""
    lint_and_fix_code()
    print("Linting and auto-fixing complete. You can now run your application.")


if __name__ == "__main__":
    main()