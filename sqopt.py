"""
sqlite-query-optimizer
Lightweight SQLite query plan analyzer.
"""

import sqlite3
import re
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Suggestion:
    type: str
    message: str
    column: Optional[str] = None


@dataclass 
class AnalysisReport:
    query: str
    plan: List[str]
    suggestions: List[Suggestion]


class QueryAnalyzer:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def analyze(self, query: str) -> AnalysisReport:
        cursor = self.conn.cursor()
        cursor.execute(f"EXPLAIN QUERY PLAN {query}")
        plan = [row[3] for row in cursor.fetchall()]
        suggestions = self._suggest(query, plan)
        return AnalysisReport(query=query, plan=plan, suggestions=suggestions)

    def _suggest(self, query: str, plan: List[str]) -> List[Suggestion]:
        suggestions = []
        if any("SCAN" in step and "USING INDEX" not in step for step in plan):
            cols = re.findall(r'WHERE\s+(\w+)', query, re.IGNORECASE)
            for col in cols:
                suggestions.append(Suggestion(
                    type="INDEX",
                    message=f"Consider adding an index on '{col}'",
                    column=col
                ))
        return suggestions
