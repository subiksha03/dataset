import pefile
import csv

# Load the list of exe file paths
with open('exe_paths.txt') as f:
    exe_paths = f.read().splitlines()

# Create the CSV file
with open('embeddedexe1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['File', 'RT_RCDATA', 'RT_ICON', 'RT_GROUP_ICON', 'RT_VERSION_INFO'])

    # Iterate through each exe file path
    for exe_path in exe_paths:
        try:
            # Load the executable file
            pe = pefile.PE(exe_path)

            # Initialize the row with zeros
            row = [exe_path] + ['0'] * 4

            # Check if the executable has a resource directory
            if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
                # Iterate through the resources in the file
                for resource_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
                    if resource_type.name is not None:
                        # This is a named resource type
                        name = resource_type.name.decode()
                    else:
                        # This is an ID-based resource type
                        name = pefile.RESOURCE_TYPE.get(resource_type.struct.Id)

                    if name == 'RT_RCDATA':
                        row[1] = '1'
                    elif name == 'RT_ICON':
                        row[2] = '1'
                    elif name == 'RT_GROUP_ICON':
                        row[3] = '1'
                    elif name == 'RT_VERSION_INFO':
                        row[4] = '1'

            # Write the row to the CSV file
            writer.writerow(row)

        except pefile.PEFormatError:
            # The file is not a valid PE file
            row = [exe_path] + ['0'] * 4
            writer.writerow(row)
