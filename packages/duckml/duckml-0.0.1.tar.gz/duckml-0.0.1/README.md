# DuckDB Machine Learning 

Quacks on its way...

## Installation

```shell
pip install duckml
```

## Setup

```py
import duckdb
from duckml import load_duckml

conn = duckdb.connect(database = '...')
conn = load_duckml(conn)
```

