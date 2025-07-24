from email.message import Message
from multiprocessing import context
from agents import Handoff, OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI
from agent import agent
from agents.tool import Tool
from typing import Optional, List, Dict
from .guardrails import EscalationReason
from .context import WellnessContext
from .agents.escalation_agent import EscalationAgent
from .agents.injury_support_agent import InjurySupportAgent
from .agents.nutrition_expert_agent import NutritionExpertAgent
from context import UserSessionContext
from tools.goal_analyzer import GoalAnalyzerTool
from .tools.meal_planner import MealPlannerTool
from .tools.workout_recommender import WorkoutRecommenderTool
from .tools.scheduler import CheckinSchedulerTool
from .tools.tracker import ProgressTrackerTool
from pydantic import BaseModel
from hooks import RunHooks, AgentHooks
from datetime import datetime
from guardrails import GoalInput
from context import WellnessContext
from dotenv import load_dotenv
import os
import sys



load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please define it in your .env file.")

external_client = AsyncOpenAI(
    api_key=openai_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

user_context = UserSessionContext(
    name="Rabail",
    uid=123,
)

class WellnessPlannerAgent(agent):
    name: str = "WellnessPlannerAgent"
    Instruction: str = "Main health and wellness planning agent"
    
    def __init__(self):
        super().__init__()
        self.tools = [
            GoalAnalyzerTool(),
            MealPlannerTool(),
            WorkoutRecommenderTool(),
            CheckinSchedulerTool(),
            ProgressTrackerTool()
        ]
        self.handoffs = {
            "human": EscalationAgent(),
            "nutrition": NutritionExpertAgent(),
            "injury": InjurySupportAgent()
        }
    
   # Define tools
class GoalAnalyzerTool(Tool):
    name = "analyze_goal"
    description = "Analyzes fitness goals and extracts structured information"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> Dict:
        # Implementation would parse goals like "lose 5kg in 2 months"
        return {"status": "success", "goal": input}

class MealPlannerTool(Tool):
    name = "meal_planner"
    description = "Generates meal plans based on dietary preferences"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> List[str]:
        # Implementation would generate meal plans
        return ["Day 1: Healthy breakfast", "Day 1: Balanced lunch"]

class WorkoutRecommenderTool(Tool):
    name = "workout_recommender"
    description = "Recommends workouts based on fitness goals"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> Dict:
        # Implementation would recommend workouts
        return {"Monday": "Cardio", "Tuesday": "Strength training"}

class CheckinSchedulerTool(Tool):
    name = "checkin_scheduler"
    description = "Schedules regular check-ins"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> str:
        return "Weekly check-ins scheduled every Monday"

class ProgressTrackerTool(Tool):
    name = "progress_tracker"
    description = "Tracks user progress toward goals"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> Dict:
        return {"progress": "50% towards goal", "next_steps": "Increase workout intensity"}

# Define specialized agents
class InjurySupportAgent(agent):
    name = "injury_support"
    description = "Provides injury-specific workout modifications"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> str:
        return f"Injury support: Recommended modifications for {input}"

class NutritionExpertAgent(agent):
    name = "nutrition_expert"
    description = "Provides specialized dietary advice"
    
    async def run(self, input: str, context: Optional[WellnessContext] = None) -> str:
        return f"Nutrition advice for {input}"

class EscalationAgent(agent):
    name = "escalation"
    description = "Handles requests for human assistance"
    
    async def run(self, input: EscalationReason, context: Optional[WellnessContext] = None) -> str:
        return f"Connecting you with a human {input.reason} (urgency: {input.urgency})"

# Handoff callback
async def on_escalation_handoff(reason: EscalationReason, context: WellnessContext):
    print(f"Escalating to human for reason: {reason.reason}")
    context.conversation_history.append({"role": "system", "content": f"Escalated to human for {reason.reason}"})

# Instantiate tools and agents
analyze_goal = GoalAnalyzerTool()
meal_planner_tool = MealPlannerTool()
workout_recommender_tool = WorkoutRecommenderTool()
checkin_scheduler_tool = CheckinSchedulerTool()
progress_tracker_tool = ProgressTrackerTool()

injury_support_agent = InjurySupportAgent()
nutrition_expert_agent = NutritionExpertAgent()
escalation_agent = EscalationAgent()

# Main health agent
health_planner_agent = agent(
    name="Health Planner",
    instructions="""
You are a health and wellness assistant. You will receive the full chat history as part of the input.
Use this history to understand the user's goals, remember what they said previously, and respond accordingly.

Handoff rules:
- If the user mentions injury-related terms (sprain, pain, broken bone, hurt, accident, etc), trigger the `injury_support` handoff.
- If the user mentions special diet needs (diabetic, keto, allergies), use the `nutrition_expert` handoff.
- If the user says they want a human coach or real person, use the `escalation` handoff.

After handing off, don't answer yourself — the handed-off agent will respond.

For fitness goals:
1. First extract goals using the analyze_goal tool
2. Then offer workout recommendations or meal plans as appropriate

Always be supportive and encouraging!
""",
    tools=[
        analyze_goal,
        meal_planner_tool,
        workout_recommender_tool,
        checkin_scheduler_tool,
        progress_tracker_tool
    ],
    handoffs={
        "injury_support": injury_support_agent,
        "nutrition_expert": nutrition_expert_agent,
        "escalation": Handoff(
            agent=escalation_agent,
            input_type=EscalationReason,
            on_handoff=on_escalation_handoff,
        )
    },
)

# Example usage
async def run_conversation():
    context = WellnessContext(user_id="user123")
    
    messages = [
        "I want to lose 5kg in 2 months",
        "I'm vegetarian",
        "I have knee pain from running",
        "I'd like to speak to a human trainer"
    ]
    
    # agents.py
class Runner:
    # Your implementation
    pass

try:
    from openai import AsyncOpenAI, ChatCompletion as OpenAIChatCompletionsModel
except ImportError:
    class AsyncOpenAI: pass
    class OpenAIChatCompletionsModel: pass

class RunConfig:
    # Your configuration
    pass
    
    for message in Message:
        print(f"User: {message}")
        response = "await" (health_planner_agent.run(message, context))
        print(f"Assistant: {response}")
        print("---")
