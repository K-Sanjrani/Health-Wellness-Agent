from agent import Agent
from typing import Optional
from ..context import UserSessionContext

class NutritionExpertAgent(Agent):
    name: str = "NutritionExpertAgent"
    description: str = "Provides specialized nutrition advice for complex dietary needs"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if context:
            context.handoff_logs.append(f"Handled by {self.name} at current_time")
        
        response = "As your nutrition expert, I can help with specialized dietary needs. "
        
        if "diabet" in input.lower():
            response += "For diabetes management, focus on low glycemic index foods and consistent meal timing."
        elif "allerg" in input.lower():
            response += "Let's carefully plan meals to avoid your allergens while maintaining nutrition."
        
        return response