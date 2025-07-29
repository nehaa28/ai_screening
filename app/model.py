from pydantic import BaseModel
from typing import List

class MatchResult(BaseModel):
    match_score: int
    top_skills_matched: List[str]
    red_flags: List[str]
    summary: str
