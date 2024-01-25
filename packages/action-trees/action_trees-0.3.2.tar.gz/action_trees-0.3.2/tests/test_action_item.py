import asyncio

import pytest

from action_trees.action_item import (
    ActionItem,
    ActionState,
    BlockingType,
    StateTransitionException,
    ActionFailedException,
    check_state_transition,
)

# pylint: disable=redefined-outer-name, protected-access


class ForcedException(Exception):
    """Test exception for testing"""


class ConcreteActionItem(ActionItem):
    """Concrete implementation of ActionItem for testing"""

    def __init__(self, name: str):
        super().__init__(name=name)
        self.initialized = False
        self.done = False

    async def _on_init(self):
        """initialize"""
        self._log.info("initializing")
        self.initialized = True

    async def _on_run(self):
        """run all children if any, otherwise just wait a bit"""
        try:
            if self.children:
                self._log.info("running children")
                for child in self.children:
                    await child.start()
            else:
                self._log.info("running self")
                for _ in range(5):
                    await self._wait_if_paused()
                    await asyncio.sleep(0.1)
        except ActionFailedException:
            if self.parent is not None:
                raise
            else:
                self._log.error("action failed")
                self.state = ActionState.FAILED
        except StateTransitionException:
            self._log.error("state transition failed")
            raise

        self.done = True


class SimpleActionItem(ActionItem):
    """action that does nothing, no init"""

    async def _on_run(self):
        pass


class FailingActionItem(ActionItem):
    """action that fails on run"""

    async def _on_run(self):
        raise ActionFailedException("Bummer!", self)


class BadActionItem(ActionItem):
    """action that fails on run"""

    async def _on_run(self):
        raise ForcedException("Failed without even trying")


def test_smoke():
    """basic smoke test"""
    state = ActionState.WAITING
    assert str(state) == "WAITING"

    blocking_type = BlockingType.HARD
    assert str(blocking_type) == "HARD"

    a1 = ConcreteActionItem(name="action1")
    a2 = ConcreteActionItem(name="action2")

    a1.add_child(a2)

    a1.display_tree()

    assert a1.get_exception() is None

    a1.state = a1.state


def test_transition_check():
    check_state_transition(ActionState.WAITING, ActionState.RUNNING)

    with pytest.raises(StateTransitionException):
        check_state_transition(ActionState.RUNNING, ActionState.PAUSED)

    with pytest.raises(StateTransitionException):
        check_state_transition(ActionState.WAITING, ActionState.FINISHED)


@pytest.fixture
def action_item():
    return ConcreteActionItem(name="action")


@pytest.mark.asyncio
async def test_initialization(action_item: ConcreteActionItem):
    assert action_item.state == ActionState.WAITING


@pytest.mark.asyncio
async def test_start(action_item: ConcreteActionItem):
    action_item.start()
    action_item.start()  # Should be a no-op
    await asyncio.sleep(0.01)  # Allow some time for the coroutine to start
    assert action_item.initialized
    assert action_item.state == ActionState.RUNNING
    await action_item.cancel()


@pytest.mark.asyncio
async def test_pause_and_resume(action_item: ConcreteActionItem):
    action_item.start()
    await asyncio.sleep(0.01)
    action_item.pause()
    assert action_item.state == ActionState.PAUSED
    await asyncio.sleep(0.1)
    action_item.resume()
    assert action_item.state == ActionState.RUNNING
    await asyncio.sleep(0.5)
    assert action_item.done
    assert action_item.state == ActionState.FINISHED
    assert action_item.get_exception() is None


@pytest.mark.asyncio
async def test_cancel(action_item: ConcreteActionItem):
    action_item.start()
    await asyncio.sleep(0.01)
    await action_item.cancel()
    await asyncio.sleep(0.01)  # Allow time for cancellation to propagate
    assert action_item.state == ActionState.FAILED
    await action_item.cancel()


@pytest.mark.asyncio
async def test_invalid_transition_pause(action_item: ConcreteActionItem):
    with pytest.raises(StateTransitionException):
        action_item.pause()


@pytest.mark.asyncio
async def test_invalid_transition_resume(action_item: ConcreteActionItem):
    with pytest.raises(StateTransitionException):
        action_item.resume()


@pytest.mark.asyncio
async def test_invalid_transition_cancel(action_item: ConcreteActionItem):
    action_item.start()
    await asyncio.sleep(0.01)
    action_item.pause()
    await asyncio.sleep(0.01)
    with pytest.raises(StateTransitionException):
        await action_item.cancel()

    action_item.resume()
    await asyncio.sleep(0.01)
    await action_item.cancel()

    exc = action_item.get_exception()
    assert isinstance(exc, asyncio.CancelledError)


@pytest.mark.asyncio
async def test_failed_action():
    action_item = BadActionItem(name="bad")

    action_item.start()
    await asyncio.sleep(0.01)

    assert action_item.state == ActionState.FAILED

    exc = action_item.get_exception()
    assert isinstance(exc, ForcedException)


def test_children():
    """test children"""
    action = ConcreteActionItem(name="parent")
    action.add_child(ConcreteActionItem(name="child1"))
    action.add_child(ConcreteActionItem(name="child2"))

    assert len(action.children) == 2

    assert action.get_child("child1").name == "child1"

    with pytest.raises(ValueError):
        action.get_child("child3")

    assert action.get_child("child2").name == "child2"


def test_parent():
    """test parent"""
    action = ConcreteActionItem(name="parent")
    child = ConcreteActionItem(name="child")
    action.add_child(child)

    assert child.parent == action
    action.remove_child("child")
    assert child.parent is None


@pytest.mark.asyncio
async def test_group_cancel():
    """failing child action must cancel its children and parent"""
    parent = ConcreteActionItem(name="parent")
    child = FailingActionItem(name="child")
    parent.add_child(child)
    grandchild = ConcreteActionItem(name="grandchild")
    child.add_child(grandchild)

    parent.start()
    await asyncio.sleep(0.1)

    assert parent.state == ActionState.FAILED
    assert child.state == ActionState.FAILED
    assert grandchild.state == ActionState.FAILED


@pytest.mark.asyncio
async def test_paused_cancel(action_item: ConcreteActionItem):
    """test cancelling a paused action"""

    child = SimpleActionItem(name="child")
    child._state = ActionState.PAUSED

    action_item.add_child(child)

    action_item.start()
    await asyncio.sleep(0.01)

    await action_item.cancel()
    await asyncio.sleep(0.01)
    exc = action_item.get_exception()
    assert isinstance(exc, StateTransitionException)

    assert child.state == ActionState.PAUSED
    assert isinstance(child.get_exception(), StateTransitionException)
