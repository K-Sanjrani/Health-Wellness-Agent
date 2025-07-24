# Health-Wellness-Agent
A digital wellness assistant that provides personalized health plans through natural language conversations, with real-time streaming and specialized agent handoffs.

## Features

- 🗣️ **Natural Language Interaction**: Multi-turn conversations to understand user goals
- 🥗 **Personalized Planning**: Generates meal plans and workout routines
- ⏱️ **Real-time Streaming**: Chatbot-like responsive experience
- 🤝 **Specialized Handoffs**: Nutrition experts, injury support, and human escalation
- 🛡️ **Input/Output Guardrails**: Ensures valid and structured data
- 📊 **Progress Tracking**: Maintains context across sessions

## Folder Structure
health_wellness_agent/
├── main.py
├── agent.py
├── context.py
├── guardrails.py
├── hooks.py
├── tools/
│   ├── goal_analyzer.py
│   ├── meal_planner.py
│   ├── workout_recommender.py
│   ├── scheduler.py
│   ├── tracker.py
├── agents/
│   ├── escalation_agent.py
│   ├── nutrition_expert_agent.py
│   └── injury_support_agent.py
├── utils/
│   └── streaming.py
└── README.md

## Context Class
class UserSessionContext(BaseModel):
    name: str
    uid: int
    goal: Optional[dict] = None
    diet_preferences: Optional[str] = None
    workout_plan: Optional[dict] = None
    meal_plan: Optional[List[str]] = None
    injury_notes: Optional[str] = None
    handoff_logs: List[str] = []
    progress_logs: List[Dict[str, str]] = []

## Requirements
Python 3.8+
OpenAI API key
OpenAI Agents SDK
OPENAI API Key 
Other dependencies: pydantic, python-dotenv, etc.

## Usage Examples
__Setting a Fitness Goal
User: I want to lose 5kg in 2 months
Agent: Great! I've recorded your goal to lose 5kg by [date]. Would you like me to:
1. Create a meal plan
2. Suggest workouts
3. Schedule progress check-ins

__Getting a Meal Plan
User: I'm vegetarian
Agent: Here's your 7-day vegetarian meal plan:
1. Monday: Lentil curry with brown rice
2. Tuesday: A ful bowl of mix salad vegetbles you like to eat.

__Injury Support
User: I have knee pain
Agent: [HANDOFF TO INJURY SUPPORT]
Injury Specialist: For knee pain, I recommend low-impact exercises like...


## Resourses
OpenAI Agents SDK Documentation,
Pydantic Docs,
Python Dotenv.
