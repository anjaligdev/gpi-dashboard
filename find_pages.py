import pdfplumber

years = ["2022-23", "2023-24", "2024-25", "2025-26"]

def count_data_rows(text):
    """Count lines that end with 12 numbers (like our state rows)."""
    count = 0
    for line in text.split("\n"):
        parts = line.split()
        if len(parts) >= 12 and all(p.isdigit() for p in parts[-12:]):
            count += 1
    return count

for year in years:
    print("Scanning", year, flush=True)
    with pdfplumber.open(f"data/udise_{year}.pdf") as pdf:
        for number, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            rows = count_data_rows(text)
            if rows >= 30 and "secondary" in text.lower() and "girls" in text.lower():
                first_line = text.split("\n")[0]
                print(f" page index {number}: {rows} rows | {first_line}")