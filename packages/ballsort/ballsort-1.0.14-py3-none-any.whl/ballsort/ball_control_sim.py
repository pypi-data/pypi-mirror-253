import asyncio
from dataclasses import replace

from ball_control import BallControl
from scenario import Scenario, ScenarioProgress
from state_manager import StateManager
from scenario_control import ScenarioControl
from state_update_model import StateModel, StatePosition, StateUpdateModel, get_default_state
from update_reporter import UpdateReporter

class BallControlSim(BallControl, ScenarioControl):

    delay_mult: float
    update_reporter: UpdateReporter
    state_manager: StateManager
    state: StateModel

    def __init__(self, update_reporter: UpdateReporter, delay_multiplier: float = 1.0):
        self.update_reporter = update_reporter
        self.state_manager = StateManager()
        self.delay_mult = delay_multiplier
        self.state = get_default_state()

    async def __aenter__(self):
        pass
    
    async def __aexit__(self, *_):
        await self.update_reporter.shutdown()

    async def __send_update(self, include_balls: bool = False, include_dimensions: bool = False):
        state_to_send = self.state if include_balls else replace(self.state, balls = None)
        state_to_send = state_to_send if include_dimensions else replace(state_to_send, max_x = 0, max_y = 0)

        state_update: StateUpdateModel = StateUpdateModel(
                userId="glen",
                state=state_to_send,
                delay_multiplier=self.delay_mult
            )

        await self.update_reporter.send_update(state_update)
   
    async def _delay(self, duration: float):
        end_time = self.state.elapsed + duration
        await asyncio.sleep(duration * self.delay_mult)
        if end_time > self.state.elapsed:
            self.state.elapsed = end_time

    async def _move_relative(self, x: int, y: int, delay: float = 1.0):
        delayTask = asyncio.create_task(self._delay(delay))
        await self.__send_update()
        await delayTask

    async def move_horizontally(self, distance: int, claw_index: int = 0):
        if (0 == distance):
            return
        
        try:
            self.state = self.state_manager.move_horizontally_start(state=self.state, distance=distance, claw_index=claw_index)
            await self._move_relative(x=distance, y=0, delay=1.0)            
        finally:
            self.state = self.state_manager.move_horizontally_end(state=self.state, claw_index=claw_index)
            await self.__send_update()

    async def move_vertically(self, distance: int, claw_index: int = 0) -> None:
        if (0 == distance):
            return
        
        try:
            self.state = self.state_manager.move_vertically_start(state=self.state, distance=distance, claw_index=claw_index)
            await self._move_relative(x=0, y=distance, delay=1.5)
        finally:
            self.state = self.state_manager.move_vertically_end(state=self.state, claw_index=claw_index)
            await self.__send_update()

    def get_position(self, claw_index: int = 0) -> StatePosition:
        return self.state.claws[claw_index].pos

    async def open_claw(self, claw_index: int = 0):
        dropping_ball = self.state.claws[claw_index].ball != None
        try:
            delayTask = asyncio.create_task(self._delay(0.3))
            self.state = self.state_manager.open_claw_start(state=self.state, claw_index=claw_index)

            await self.__send_update()
            await delayTask
        finally:
            self.state, dirty = self.state_manager.open_claw_end(state=self.state, claw_index=claw_index, ball_dropped=dropping_ball)
            if dirty:
                await self.__send_update(include_balls=True)

    async def close_claw(self, claw_index: int = 0):
        try:
            delayTask = asyncio.create_task(self._delay(0.3))
            self.state = self.state_manager.close_claw_start(state=self.state, claw_index=claw_index)

            await self.__send_update()
            await delayTask
        finally:
            self.state = self.state_manager.close_claw_end(state=self.state, claw_index=claw_index)

    async def set_scenario(self, scenario: Scenario):
        self.state = self.state_manager.set_scenario(state=self.state, scenario=scenario)
        await self.__send_update(include_balls = True, include_dimensions = True)

    def get_progress(self) -> ScenarioProgress:
        if not self.state_manager.scenario:
            return ScenarioProgress(completed=0, total=0)
        return self.state_manager.scenario.get_progress(self.state)

    def is_in_goal_state(self) -> bool:
        if not self.state_manager.scenario:
            return False
        return self.state_manager.scenario.is_in_goal_state(self.state)
    
    def get_state(self) -> StateModel:
        return replace(self.state, balls=[replace(ball, value=ball.value if ball.value_visible else None) for ball in self.state.balls])