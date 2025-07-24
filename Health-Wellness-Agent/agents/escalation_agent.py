from agent import Agent
from typing import Optional
from ..context import UserSessionContext

class EscalationAgent(Agent):
    name: str = "EscalationAgent"
    description: str = "Handles requests to speak with human coaches or support"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if context:
            context.handoff_logs.append(f"Handled by {self.name} at current_time")
        
        return "I've connected you with a human coach. They'll be with you shortly. In the meantime, is there anything else I can help with?"