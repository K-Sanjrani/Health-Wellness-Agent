from agents.tool import Tool
from typing import Optional, List
from ..context import UserSessionContext
import asyncio

class MealPlannerTool(Tool):
    name: str = "MealPlannerTool"
    description: str = "Generates a 7-day meal plan based on dietary preferences"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> List[str]:
        if not context or not context.diet_preferences:
            raise ValueError("No dietary preferences set. Please specify your dietary needs first.")
        
        # Simulate async processing
        await asyncio.sleep(1)
        
        # Generate sample meal plan based on preferences
        if "vegetarian" in context.diet_preferences.lower():
            meal_plan = [
                "Day 1: Lentil soup with whole grain bread, Greek yogurt with berries",
                "Day 2: Chickpea curry with rice, Mixed green salad",
                # ... more days
            ]
        else:
            meal_plan = [
                "Day 1: Grilled chicken with quinoa, Steamed vegetables",
                "Day 2: Baked salmon with sweet potato, Asparagus",
                # ... more days
            ]
        
        if context:
            context.meal_plan = meal_plan
        
        return meal_plan