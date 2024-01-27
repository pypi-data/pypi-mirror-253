import webbrowser
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 and sys.argv[1] == "setup":
        webbrowser.open(f"https://docs.daios.tech/{sys.argv[1]}")
    else:
        print("Usage: python -m daios setup")
