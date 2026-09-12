import re
import json

message = """
Site: Mirpur-10 Toilet Block A
Date: 02 Sep 2026
Visitors: 312
Cleaning done: 4 times
Issues: Water pump not working since Saturday
Cash collected: BDT 1,240
"""

data = {}

data["site"] = re.search(r"Site:\s*(.+)", message).group(1).strip()
data["date"] = re.search(r"Date:\s*(.+)", message).group(1).strip()
data["visitors"] = int(re.search(r"Visitors:\s*(\d+)", message).group(1))
data["cleaning_done"] = int(re.search(r"Cleaning done:\s*(\d+)", message).group(1))
data["issues"] = re.search(r"Issues:\s*(.+)", message).group(1).strip()

cash = re.search(r"Cash collected:\s*BDT\s*([\d,]+)", message).group(1)
data["cash_collected"] = int(cash.replace(",", ""))

print(json.dumps(data, indent=2))
