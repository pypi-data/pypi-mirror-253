from dataclasses import dataclass, replace
from scenario import Scenario
from state_update_model import (
    StateBall,
    StateModel,
    StatePosition,
    get_default_state,
)


@dataclass
class Ch5Scenario(Scenario):
    """Challenge Implementation"""

    def get_goal_state_description(self) -> str:
        return f"Bicolor Towers of Hanoi\nMove all marbles to two separate columns, one of each color. A marble can not be placed on top of a marble of lower value.\n{self.get_dimensions_description()}"
    
    def get_initial_state(self) -> StateModel:
        balls: list[StateBall] = []
        max_x = 3
        max_y = 5
        for y in range(3):
            value=y+1
            label=f"{y+1}"
            balls.append(StateBall(pos=StatePosition(x=0, y=2*y), color="lightblue", value=value, label=label))
            balls.append(StateBall(pos=StatePosition(x=0, y=2*y+1), color="lightgreen", value=value, label=label))
        
        return replace(get_default_state(), balls = balls, max_x=max_x, max_y=max_y)

    def is_in_goal_state(self, state: StateModel) -> bool:

        # No ball in claw
        if state.claws[0].ball:
            return False
        
        columns: list[list[StateBall]] = [[] for _ in range(state.max_x + 1)]
        for ball in state.balls:
            columns[ball.pos.x].append(ball)

        def column_is_goal_state_compliant(x: int) -> bool:
            column = columns[x]
            if len(column) == 0:
                return True # empty column is ok
            
            bottom_ball = column[0]
            return all(ball.color == bottom_ball.color for ball in column)
        
        # There shall be exactly two populated columns
        if len([True for column in columns if len(column) > 0]) != 2:
            return False

        return all(column_is_goal_state_compliant(x) for x in range(state.max_x + 1))
    