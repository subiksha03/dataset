import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"C:\Users\subik\Downloads\ndataset.csv")

# Define the feature names
feature_names = ['RT_RCDATA', 'RT_ICON', 'RT_GROUP_ICON', 'RT_VERSION_INFO', 'bitcoin', 'mscoree.dll',
                 'COMDLG32.dll', 'onion', 'Entropy > 7', 'advapi32.dll', 'user32.dll', 'kernel32.dll',
                 'mpr.dll', 'comctl32.dll', 'msvcrt.dll', 'DNS Query']

# Plot a bar graph for each feature column
for feature in feature_names:
    feature_counts = df.groupby(feature)['class'].value_counts().unstack()
    feature_counts.plot(kind='bar', stacked=True, color=['green', 'red'])
    plt.title(f'File counts by {feature}')
    plt.xlabel(feature)
    plt.ylabel('File count')
    plt.show()
