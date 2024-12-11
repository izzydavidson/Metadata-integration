
import pandas as pd # type: ignore

# Load data
microbial_data = pd.read_csv("Mock_microbial_data.csv")
metadata = pd.read_csv("Mock_Microbiome_Metadata.csv")

# Merge datasets on 'sample_id'
merged_data = pd.merge(microbial_data, metadata, on="sample_id")

# Display the first 5 rows of the merged data
print(merged_data.head())

#Filter
# Can filter data out by filtered_data = merged_data[merged_data[Age]>30] for example will filter out age >30

#Fill empty values with N/A
merged_data.fillna('N/A', inplace=True)

# Exporting the new merged file
try:
    merged_data.to_csv("/Users/izzydavidson/Desktop/Metadata-integration/Merged_microbiome_data.csv", index=False)
    print("File saved successfully.")
except Exception as e:
    print(f"Error: {e}")

#Visualisation
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Example: Plot a boxplot for microbial abundance against a metadata variable
#sns.boxplot(x='ethnicity', y='microbial_abundance', data=merged_data)

# Save the plot to a file (e.g., "boxplot.png")
#plt.savefig('boxplot.png', format='png')

#Can display too 
#plt.show()



