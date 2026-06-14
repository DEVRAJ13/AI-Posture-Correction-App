from typing import TypedDict

from langgraph.graph import StateGraph
from langgraph.graph import END


class GraphState(TypedDict):

    posture: str
    bad_count: int
    advice: str


def posture_node(state):

    from agents.posture_agent import PostureAgent

    return PostureAgent().execute(state)


def coach_node(state):

    from agents.coach_agent import CoachAgent

    return CoachAgent().execute(state)


def notify_node(state):

    from agents.notification_agent import NotificationAgent

    return NotificationAgent().execute(state)


builder = StateGraph(GraphState)

builder.add_node(
    "posture",
    posture_node
)

builder.add_node(
    "coach",
    coach_node
)

builder.add_node(
    "notify",
    notify_node
)

builder.set_entry_point(
    "posture"
)

builder.add_edge(
    "posture",
    "coach"
)

builder.add_edge(
    "coach",
    "notify"
)

builder.add_edge(
    "notify",
    END
)

workflow = builder.compile()