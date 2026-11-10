import pandas as pd

df = pd.read_csv("record.csv")

df["result"] = df["previous_score"].apply(
    lambda score: "Pass" if score >= 60 else "Fail"
)

# Show every column for every student
print(df.to_string(index=False))

df.to_csv("record", index=False)
print("\nSaved all student details and results to record.csv")

import matplotlib.pyplot as plt

counts = df["result"].value_counts().reindex(["Pass", "Fail"], fill_value=0)

plt.bar(counts.index, counts.values, color=["green", "red"])
plt.title("Students Who Passed and Failed")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.bar_label(plt.gca().containers[0])
plt.show()

df.to_csv("record.csv", index=False)