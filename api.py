import os
import csv
import pefile

dlls = ['advapi32.dll', 'user32.dll', 'kernel32.dll', 'mpr.dll', 'comctl32.dll', 'msvcrt.dll']

with open('paths.txt') as f:
    exe_paths = f.read().splitlines()

with open('api.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['exe_path', *dlls])  # Write header row

    for exe_path in exe_paths:
        try:
            pe = pefile.PE(exe_path)

            imported_dlls = [dll.dll.decode('utf-8').lower() for dll in pe.DIRECTORY_ENTRY_IMPORT]

            row = [exe_path]
            for dll in dlls:
                if dll.lower() in imported_dlls:
                    row.append(1)
                else:
                    row.append(0)

            writer.writerow(row)
        except pefile.PEFormatError:
            print(f"PEFormatError occurred for {exe_path}. Appending all 0s.")
            writer.writerow([exe_path] + [0] * len(dlls))
        except Exception as e:
            print(f"Error occurred while processing {exe_path}: {e}. Appending all 0s.")
            writer.writerow([exe_path] + [0] * len(dlls))
