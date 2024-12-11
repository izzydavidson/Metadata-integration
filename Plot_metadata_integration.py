import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Load data
microbial_data = pd.read_csv("Mock_microbial_data.csv")
metadata = pd.read_csv("Mock_Microbiome_Metadata.csv")

# Merge datasets on 'sample_id'
merged_data = pd.merge(microbial_data, metadata, on="sample_id")

# Melt the data to reshape it for plotting
lactobacillus_data = pd.melt(merged_data, id_vars=['sample_id', 'ethnicity'], 
                             value_vars=['Lactobacillus_iners_abundance', 'Lactobacillus_crispatus_abundance'], 
                             var_name='microbe', value_name='microbial_abundance')

# Filter the data to include only Lactobacillus species
lactobacillus_data = lactobacillus_data[lactobacillus_data['microbe'].str.contains('Lactobacillus')]

# Export the reshaped data to CSV for reference
lactobacillus_data.to_csv("Lactobacillus_ethnicity_abundance.csv", index=False)

# Display the first few rows of the reshaped data to check
print(lactobacillus_data.head())

# Create a boxplot to visualize how ethnicity influences Lactobacillus abundance
sns.boxplot(x='ethnicity', y='microbial_abundance', data=lactobacillus_data)

# Customize the plot
plt.title('Influence of Ethnicity on Lactobacillus Abundance')
plt.xlabel('Ethnicity')
plt.ylabel('Lactobacillus Abundance')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()

# Save the plot to a file (e.g., "boxplot.png")
plt.savefig('Lactobacillus_ethnicity_boxplot.png', format='png')
