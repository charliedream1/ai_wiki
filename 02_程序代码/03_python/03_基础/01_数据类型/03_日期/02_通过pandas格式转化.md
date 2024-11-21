```python
import pandas as pd
from loguru import logger

# '18-11-2024 4:33 pm' 格式 改为 %Y-%m-%d %H:%M:%S 格式
date = '18-11-2024 4:33 pm'
try:
    date = pd.to_datetime(date, errors='coerce').strftime('%Y-%m-%d %H:%M:%S')
    pass
except Exception as e:
    logger.error(f"Date format error: {date}, {e}")
```