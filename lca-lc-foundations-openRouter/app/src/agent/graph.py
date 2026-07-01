"""LangGraph entrypoint: exposes the personal chef agent."""

from agent.agents.personal_chef import personal_chef_agent

# LangGraph Platform expects a `graph` variable in this module.
graph = personal_chef_agent