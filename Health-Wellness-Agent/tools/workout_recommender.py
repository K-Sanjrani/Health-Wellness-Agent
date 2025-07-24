from agents.tool import Tool
from typing import Optional, Dict
from ..context import UserSessionContext
import asyncio

class WorkoutRecommenderTool(Tool):
    name: str = "WorkoutRecommenderTool"
    description: str = "Recommends a workout plan based on fitness goals and experience level"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> Dict:
        if not context or not context.goal:
            raise ValueError("No fitness goal set. Please specify your goals first.")
        
        await asyncio.sleep(1)
        
        goal_type = context.goal.get('goal_type', 'maintain')
        
        if goal_type == 'lose':
            plan = {
                "Monday": "30 min cardio + full body strength",
                "Tuesday": "HIIT workout",
                # ... more days
            }
        elif goal_type == 'build':
            plan = {
                "Monday": "Upper body strength training",
                "Tuesday": "Lower body strength training",
                # ... more days
            }
        else:
            plan = {
                "Monday": "30 min moderate cardio",
                "Tuesday": "Yoga or stretching",
                # ... more days
            }
        
        if context:
            context.workout_plan = plan
        
        return plan