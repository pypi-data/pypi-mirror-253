
from SchemGenerator import *
import time
import easygui

def main():
    file = Schematic()
    print("Placing blocks...")

    file.open(easygui.fileopenbox())
    timestartfill = time.perf_counter()
    print(file._palette)
    file.replace("birch_sign[rotation=0,waterlogged=false]", "oak_sign[rotation=4]")

    timeendfill = time.perf_counter()
    print("Generating and saving...")
    timestartsaving = time.perf_counter()
    file.save("main/Schematics/openTestResult.schem")
    timedone = time.perf_counter()

    print(f"Making took {round(timeendfill - timestartfill, 5)}s")
    print(f"Saving took {round(timedone -  timestartsaving, 5)}s")

if __name__ == "__main__":
    main()