from dataclasses import dataclass, replace
from scenario import Scenario
from state_update_model import (
    MIN_X,
    Highlight,
    StateBall,
    StateModel,
    StatePosition,
    get_default_state,
)


@dataclass
class Ch2Scenario(Scenario):
    """Challenge Implementation"""

    def get_goal_state_description(self) -> str:
        return f"Sort balls by weight in leftmost column. Heaviest at the bottom.\n{self.get_dimensions_description()}"
    
    def get_initial_state(self) -> StateModel:
        balls = [
            StateBall(pos=StatePosition(x=1, y=2), color="yellow"),
            StateBall(pos=StatePosition(x=1, y=3), color="blue"),
            StateBall(pos=StatePosition(x=1, y=4), color="green"),
        ]
        highlights = [Highlight(xMin=2, xMax=3, yMin=0, yMax=4, color="lightblue")]
        return replace(get_default_state(), balls = balls, highlights=highlights, max_x=3, max_y=4)

    def is_in_goal_state(self, state: StateModel) -> bool:

        # No ball in claw
        if state.claws[0].ball:
            return False
        
        # yellow at bottom
        if not any(y_ball.pos == StatePosition(x=MIN_X, y=state.max_y) for y_ball in state.balls if y_ball.color == "yellow"):
            return False

        # green in the middle
        if not any(g_ball.pos == StatePosition(x=MIN_X, y=state.max_y-1) for g_ball in state.balls if g_ball.color == "green"):
            return False
        
        # blue on top
        if not any(b_ball.pos == StatePosition(x=MIN_X, y=state.max_y-2) for b_ball in state.balls if b_ball.color == "blue"):
            return False
        
        return True
    
    