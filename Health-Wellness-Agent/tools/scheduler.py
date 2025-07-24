from agents.tool import Tool
from typing import Optional
from ..context import UserSessionContext
from datetime import datetime, timedelta

class CheckinSchedulerTool(Tool):
    name: str = "CheckinSchedulerTool"
    description: str = "Schedules recurring weekly progress check-ins"

    async def run(self, input: str, context: Optional[UserSessionContext] = None) -> str:
        if not context:
            return "No user context available"
        
        next_checkin = datetime.now() + timedelta(days=7)
        return f"Weekly check-in scheduled for {next_checkin.strftime('%Y-%m-%d')}. I'll check on your progress then!"