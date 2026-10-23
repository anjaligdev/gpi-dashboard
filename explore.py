import pdfplumber
import pandas as pd

with pdfplumber.open("data/udise_2025-26.pdf") as pdf:
    text = pdf.pages[90].extract_text()

rows = []
for line in text.split("\n"):
    parts = line.split()
    if len(parts) >= 12 and all(p.isdigit() for p in parts[-12:]):
        name = " ".join(parts[:-12])
        if name == "":
            name = "Daman & Diu and Dadra & Nagar Haveli"
        numbers = parts[-12:]
        rows.append([name] + numbers)

columns = [
    "state",
    "sec_boys", "sec_girls", "sec_total",
    "hs_boys", "hs_girls", "hs_total",
    "all_boys", "all_girls", "all_total",
    "grand_boys", "grand_girls", "grand_total",
]

df = pd.DataFrame(rows, columns=columns)
df[columns[1:]] = df[columns[1:]].astype(int)

df["year"] = "2025-26"
df["gpi_secondary"] = (df["sec_girls"] / df["sec_boys"]).round(4)

print(df[["state", "sec_boys", "sec_girls", "gpi_secondary"]].to_string())

df.to_csv("data/gpi_2025-26.csv", index=False)