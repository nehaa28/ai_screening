import pandas as pd
from pathlib import Path

def save_to_csv(result: dict, path="data/output.csv"):
    file = Path(path)
    if file.exists():
        df = pd.read_csv(file)
        df = pd.concat([df, pd.DataFrame([result])], ignore_index=True)
    else:
        df = pd.DataFrame([result])
    df.to_csv(file, index=False)
