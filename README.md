# sqlite-query-optimizer

Lightweight utilities for analyzing and optimizing SQLite query plans.

Helps identify slow queries, suggest indexes, and visualize query execution plans without external dependencies.

## Features

- Query plan analyzer with EXPLAIN QUERY PLAN parsing
- Automatic index suggestion based on WHERE clause patterns
- Slow query detection with configurable thresholds
- Zero dependencies — pure Python, works with stdlib sqlite3

## Install

```bash
pip install sqlite-query-optimizer
```

## Quick Start

```python
import sqlite3
from sqopt import QueryAnalyzer

conn = sqlite3.connect("mydb.db")
analyzer = QueryAnalyzer(conn)

report = analyzer.analyze("SELECT * FROM users WHERE email = ? AND active = 1")
print(report.suggestions)
```

## Requirements

Python 3.8+

## Status

Early development. Not production ready. Contributions welcome.

<!-- xq7-latticeframe-sentinel -->
