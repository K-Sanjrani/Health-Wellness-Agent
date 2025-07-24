from agents.tool import Tool
from typing import Optional
from ..context import UserSessionContext
from ..guardrails import GoalInput
import re

class GoalAnalyzerTool(Tool):
    name: str = "GoalAnalyzerTool"
    description: str = "Analyzes user fitness goals and extracts structured information"
    

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> dict:
        # Try to parse the goal from natural language
        pattern = r"(lose|gain|maintain|build|improve)\s*(\d+)\s*(kg|lb|cm|inch|%)\s*(?:in|over|for)\s*(\d+)\s*(weeks|months)"
        match = re.search(pattern, input.lower())
        
        if not match:
            raise ValueError("Could not parse goal. Please specify in format like 'lose 5kg in 2 months'")
        
        goal_type, quantity, metric, duration_num, duration_unit = match.groups()
        
        try:
            goal_input = GoalInput(
                quantity=float(quantity),
                metric=metric,
                duration=f"{duration_num} {duration_unit}",
                goal_type=goal_type
            )
            
            if context:
                context.goal = goal_input.dict()
            
            return {
                "status": "success",
                "goal": goal_input.dict(),
                "message": f"Great! I've noted your goal to {goal_type} {quantity}{metric} in {duration_num} {duration_unit}."
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }