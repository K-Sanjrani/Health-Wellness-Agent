from pydantic import BaseModel, validator
from typing import List, Optional

class GoalInput(BaseModel):
    quantity: float
    metric: str  # kg, lb, cm, etc.
    duration: str  # weeks, months
    goal_type: str  # lose, gain, maintain
    
    @validator('metric')
    def validate_metric(cls, v):
        valid_metrics = ['kg', 'lb', 'cm', 'inch', '%']
        if v.lower() not in [m.lower() for m in valid_metrics]:
            raise ValueError(f"Invalid metric. Must be one of: {', '.join(valid_metrics)}")
        return v.lower()
    
    @validator('goal_type')
    def validate_goal_type(cls, v):
        valid_types = ['lose', 'gain', 'maintain', 'build', 'improve']
        if v.lower() not in [t.lower() for t in valid_types]:
            raise ValueError(f"Invalid goal type. Must be one of: {', '.join(valid_types)}")
        return v.lower()

class DietaryInput(BaseModel):
    preference: str
    restrictions: Optional[List[str]] = None
    allergies: Optional[List[str]] = None

class InjuryInput(BaseModel):
    area: str
    severity: str  # mild, moderate, severe
    notes: Optional[str] = None