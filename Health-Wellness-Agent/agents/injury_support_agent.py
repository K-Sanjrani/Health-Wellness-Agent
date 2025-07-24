from agent import Agent
from typing import Optional
from ..context import UserSessionContext

class InjurySupportAgent(Agent):
    name: str = "InjurySupportAgent"
    description: str = "Provides workout modifications for injuries or physical limitations"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if context:
            context.handoff_logs.append(f"Handled by {self.name} at current_time")
            context.injury_notes = input
        
        response = "I'll help you with injury-appropriate exercises. "
        
        if "knee" in input.lower():
            response += "For knee pain, focus on low-impact exercises like swimming or cycling, and avoid deep squats."
        elif "back" in input.lower():
            response += "For back issues, core strengthening and proper form are essential. Avoid heavy lifting."
        
        return response