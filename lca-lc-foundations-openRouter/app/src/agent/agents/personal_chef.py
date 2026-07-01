"""Personal chef agent: wires together model + prompt + tools."""

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model

from agent.prompts.personal_chef_prompt import SYSTEM_PROMPT
from agent.tools.web_search import web_search

model = init_chat_model(
    model="google/gemma-4-31b-it:free",
    model_provider="openrouter",
)

# create_agent ya devuelve un grafo compilado (CompiledStateGraph).
#
# No pasamos checkpointer acá: LangGraph Platform (langgraph dev / cloud)
# inyecta el suyo automáticamente. Si corrés este agente por fuera de la
# plataforma (script/notebook), agregá checkpointer=InMemorySaver() ahí.
personal_chef_agent = create_agent(
    model=model,
    tools=[web_search],
    system_prompt=SYSTEM_PROMPT,
)
