
from agents.StoryFlowAgent import StoryFlowAgent
from agents.subagents import story_generator, critic, reviser, grammar_check, tone_check

root_agent =  StoryFlowAgent(
    name="StoryFlowAgent",
    story_generator=story_generator,
    critic=critic,
    reviser=reviser,
    grammar_check=grammar_check,
    tone_check=tone_check,
)
