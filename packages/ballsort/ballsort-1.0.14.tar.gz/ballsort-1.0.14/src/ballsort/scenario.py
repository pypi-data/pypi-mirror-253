from dataclasses import dataclass
from state_update_model import StateBall, StateModel

@dataclass
class ScenarioProgress(object):
    """Represents how many are completed out of a total number of steps."""
    completed: int
    total: int

class Scenario(object):
    """Interface for a specific scenario"""

    _seed: int | None = None

    def __init__(self, seed:int | None = None):
        self._seed = seed

    def get_initial_state(self) -> StateModel:
        """Returns the initial state for the scenario."""
        raise NotImplementedError
    
    def get_progress(self, state: StateModel) -> ScenarioProgress:
        """Returns progress toward goal state."""
        raise NotImplementedError

    def is_in_goal_state(self, state: StateModel) -> bool:
        """Returns true only if state fulfills the goal state criteria."""
        raise NotImplementedError

    def get_goal_state_description(self) -> str:
        """Returns a natural language specification of goal state."""
        raise NotImplementedError
    
    def get_dimensions_description(self) -> str:
        init_state = self.get_initial_state()
        return f"maxX={init_state.max_x}, maxY={init_state.max_y}"

    def on_ball_dropped(self, state: StateModel, ball: StateBall) -> tuple[StateModel, bool]:
        """Overridable state processing after a ball has been dropped."""
        return state, False