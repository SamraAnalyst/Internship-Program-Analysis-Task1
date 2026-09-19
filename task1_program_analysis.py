##import numpy as np
##import pandas as pd
##import matplotlib.pyplot as plt
##
##print("--- Step 1: Ingesting Raw Internship Data Streams ---")
### Corporate records simulation across different domains
##raw_data = {
##    "Department": ["Data Analyst", "Machine Learning", "Web Development", "Graphic Design"],
##    "Enrollment":,
##    "Completed":,
##    "Dropouts": [25, 25, 50, 30]
##}
##
### Converting structured data streams into a Pandas DataFrame
##df = pd.DataFrame(raw_data)
##
##print("\n--- Step 2: Executing Advanced Statistical Metrics ---")
### Calculating Completion and Dropout percentages mathematically
##df["Completion_Rate (%)"] = np.round((df["Completed"] / df["Enrollment"]) * 100, 1)
##df["Dropout_Rate (%)"] = np.round((df["Dropouts"] / df["Enrollment"]) * 100, 1)
##
##print("\nFull Structured Data Panel View:")
##print(df)
##
##print("\n--- Step 3: Generating Professional Visualizations ---")
### Designing a 1-page dual analytical layout chart
##plt.figure(figsize=(10, 5))
##
### Plot 1: Comparing Completion Rates using Muted Colors
##plt.subplot(1, 2, 1)
##plt.bar(df["Department"], df["Completion_Rate (%)"], color="#8B8589", edgecolor="black")
##plt.title("Internship Completion Performance", fontsize=11, fontweight="bold")
##plt.ylabel("Completion Percentage (%)")
##plt.xticks(rotation=15)
##plt.grid(axis='y', linestyle='--', alpha=0.7)
##
### Plot 2: Tracking Dropout Scale across Domains
##plt.subplot(1, 2, 2)
##plt.pie(df["Dropouts"], labels=df["Department"], autopct='%1.1f%%', colors=["#F5F5DC", "#D2B48C", "#C0C0C0", "#E5E4E2"])
##plt.title("Distribution of Dropout Metrics", fontsize=11, fontweight="bold")
##
### Auto-adjusting parameters to avoid layout text overlaps
##plt.tight_layout()
##
##print("Displaying final visualization dashboards...")
##plt.show()



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = {
    "Department": ["Data Analyst", "Machine Learning", "Web Development", "Graphic Design"],
    "Enrollment": [150, 100, 200, 80],
    "Completed": [120, 70, 160, 70],
    "Dropouts": [30, 40, 40, 10]
    }

df = pd.DataFrame(raw_data)
df["Completion_Rate (%)"] = (df["Completed"] / df["Enrollment"])*100
df["Dropout_Rate (%)"] = (df["Dropouts"] / df["Enrollment"])*100
print(df)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(df["Department"], df["Completion_Rate (%)"], color="#8B8589", edgecolor="black")
plt.title("Completion Performance by Domain", fontsize=11, fontweight="bold")
plt.xticks(rotation=15)

plt.subplot(1, 2, 2)
plt.pie(df["Dropouts"], labels=df["Department"], autopct='%1.1f%%', colors=["#F5F5DC", "#D2B48C", "#C0C0C0", "#E5E4E2"])
plt.title("Dropouts Distribution Scale", fontsize=11, fontweight="bold")
plt.tight_layout()
plt.show()


    
