from hooks import RunHooks, AgentHooks
from typing import Optional
from .context import UserSessionContext

class WellnessHooks(RunHooks):
    async def on_agent_start(self, agent, input: str, context: Optional[UserSessionContext] = None):
        print(f"Agent {agent.name} started with input: {input}")
    
    async def on_tool_end(self, tool, output: str, context: Optional[UserSessionContext] = None):
        print(f"Tool {tool.name} completed with output: {output[:100]}...")
    
    async def on_handoff(self, from_agent, to_agent, context: Optional[UserSessionContext] = None):
        print(f"Handoff from {from_agent.name} to {to_agent.name}")
        if context:
            context.handoff_logs.append(f"Handoff to {to_agent.name} at current_time")

class MainAgentHooks(AgentHooks):
    async def on_start(self, agent, input: str, context: Optional[UserSessionContext] = None):
        if context and not context.name:
            context.name = "User"  # Default name if not set