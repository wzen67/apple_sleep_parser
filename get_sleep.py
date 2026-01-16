from lxml import etree
import pandas as pd

XML_PATH = "export.xml"
SOURCE = 'Will’s Apple\xa0Watch'
OUTPUT_CSV = "sleep_clean.csv"

records = []

context = etree.iterparse(XML_PATH, events=("start", "end"))

for event, elem in context:
    # Skip everything except Record tags immediately
    if elem.tag != "Record":
        continue

    if event == "end":
        attrs = elem.attrib

        # Fast attribute filters
        if attrs.get("type") == "HKCategoryTypeIdentifierSleepAnalysis":
            source = attrs.get("sourceName", "")
            if source == SOURCE:
                records.append((
                    attrs["startDate"],
                    attrs["endDate"],
                    attrs["value"],
                    source
                ))

        # Clear as soon as possible
        elem.clear()

# Build DataFrame once
df = pd.DataFrame(
    records,
    columns=["start", "end", "stage", "source"]
)

if df.empty:
    raise RuntimeError("No Apple Watch sleep records found.")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])
df["duration_min"] = (df["end"] - df["start"]).dt.total_seconds() / 60

df.sort_values("start", inplace=True)
df.to_csv(OUTPUT_CSV, index=False)

print(f"Saved {len(df)} rows to {OUTPUT_CSV}")
print(df["stage"].value_counts())
