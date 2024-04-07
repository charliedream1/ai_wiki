```python
import pandas as pd

df = pd.read_excel(in_xlsx_file, sheet_name=None)
for sheet_name, sheet_df in df.items():
    pass
```