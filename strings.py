import csv
import pefile

# Define the strings to search for
STRINGS = ["bitcoin", "mscoree.dll", "COMDLG32.dll", "onion"]

def check_strings_in_exe(exe_file_path):
    try:
        # Load the PE file
        pe = pefile.PE(exe_file_path)

        # Check if the PE file has a code section
        if not any(section.Characteristics & pefile.SECTION_CHARACTERISTICS['IMAGE_SCN_CNT_CODE']
                   for section in pe.sections):
            pe.close()
            return None

        # Check for each string in the code section
        found_strings = {s: 0 for s in STRINGS}
        for string in STRINGS:
            for section in pe.sections:
                # Read the section's data and search for the string
                data = section.get_data()
                if string.encode() in data:
                    found_strings[string] = 1

        # Close the PE file
        pe.close()

        # Return the found strings as a dictionary
        return found_strings

    except pefile.PEFormatError:
        return None


# Read the file paths from exe_paths.txt and execute the check_strings_in_exe function for each file path
with open("paths.txt", "r") as f:
    exe_paths = f.readlines()

# Write the output to a CSV file
with open("strings2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["File Name"] + STRINGS)
    writer.writeheader()
    for exe_path in exe_paths:
        exe_path = exe_path.strip()  # Remove leading/trailing whitespaces and newlines
        found_strings = check_strings_in_exe(exe_path)
        if found_strings is not None:
            writer.writerow({"File Name": exe_path, **found_strings})
        else:
            writer.writerow({"File Name": exe_path,**{s: 0 for s in STRINGS}})
