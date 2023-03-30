from pathlib import Path
from os import getcwd
from os.path import join, abspath, dirname

MAIN_DIR_OP1 = abspath(dirname(__file__))
MAIN_DIR_OP2 = abspath(dirname("."))

MAIN_DIR_PL1 = Path(__file__).parent
MAIN_DIR_PL2 = Path(".")

print(f"текущая директория: {getcwd()}")
print("PATHLIB")
print(f"Через __file__: {MAIN_DIR_PL1.absolute()}")
print(f"Через '.':      {MAIN_DIR_PL2.absolute()}")
print("OS.PATH")
print(f"Через __file__: {MAIN_DIR_OP1}")
print(f"Через '.':      {MAIN_DIR_OP1}")

# formating languich почитать в документации