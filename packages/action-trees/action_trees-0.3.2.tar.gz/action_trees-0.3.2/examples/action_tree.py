#!/usr/bin/env python3
"""
Action tree example - actions with children

Explained with an example of a coffee making machine.

Action tree, items with "&" after them are parallel to following item.

- cappuccino order
    - prepare machine
        - intialize
        - clean
    - make cappuccino
        - boil water &
        - grind coffee
        - turn on pump for 2 seconds
        - add milk
    - goto standby

Note: for simplicity, pausing actions is not implemented here.

Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging
import coloredlogs

import action_trees
from action_trees import ActionItem, ActionState, ActionFailedException


class AtomicAction(ActionItem):
    """basic machine action. These actions have no children and are atomic"""

    def __init__(self, name: str, duration: float):
        super().__init__(name=name)
        self._duration = duration

    async def _on_run(self):
        """Run the action item."""
        self._log.info(f"Running {self.name}")
        try:
            await asyncio.sleep(self._duration)
        except asyncio.CancelledError:
            self._log.info(f"{self.name} running cancel tasks...")
            raise


class FailingGrindAction(AtomicAction):
    """crashing version of AtomicAction"""

    async def _on_run(self):
        """Run the action item."""
        self._log.info(f"Running {self.name}")
        try:
            raise ActionFailedException("No beans left!", self)
        except asyncio.CancelledError:
            self._log.warning(f"{self.name} cancelled")
            raise


class PrepareMachineAction(ActionItem):
    """prepare the machine"""

    def __init__(self):
        super().__init__(name="prepare")

    async def _on_init(self):
        self._log.info("initializing")
        await asyncio.sleep(1)

    async def _on_run(self):
        try:
            self._log.info("cleaning")
            await asyncio.sleep(1)
            self._log.info("cleaning done")
        except asyncio.CancelledError:
            self._log.warning("cancelling cleaning")
            self._log.info("performing cancel actions...")
            await asyncio.sleep(1)
            raise


class MakeCappuccinoAction(ActionItem):
    """make cappuccino"""

    def __init__(self):
        super().__init__(name="make_cappuccino")

        # add children
        self.add_child(AtomicAction(name="boil_water", duration=2))
        self.add_child(AtomicAction(name="grind_coffee", duration=1))
        self.add_child(AtomicAction(name="pump", duration=2))
        self.add_child(AtomicAction(name="add_milk", duration=1))

    async def _on_run(self):
        # try:
        self._log.info("making cappuccino")
        # parallel actions
        await asyncio.gather(
            self.get_child("boil_water").start(),
            self.get_child("grind_coffee").start(),
        )

        # sequential actions
        await self.get_child("pump").start()
        await self.get_child("add_milk").start()
        self._log.info("making cappuccino done")


class CappuccinoOrder(ActionItem):
    """make cappuccino, highest level action"""

    def __init__(self):
        super().__init__(name="cappuccino order")

        # add children
        self.add_child(PrepareMachineAction())
        self.add_child(MakeCappuccinoAction())
        self.add_child(AtomicAction(name="goto_standby", duration=1))

    async def _on_run(self):
        self._log.info("starting cappuccino order")
        try:
            for action_name in ["prepare", "make_cappuccino", "goto_standby"]:
                await self.get_child(action_name).start()

            self._log.info("Cappuccino is ready!")
        except ActionFailedException as e:
            # explicitly handle ActionFailedException here, as it is the higest level.
            # we can choose to how to cleanup here, like canceling children actions.
            self._log.error(f"Sorry, no cappuccino today: {e}")
            await self._cancel_children()
            self.state = ActionState.FAILED


async def main() -> None:
    """main coroutine"""

    logging.info("-------------------Example 1: normal execution------------------")
    order = CappuccinoOrder()
    await order.start()
    order.display_tree()

    logging.info("-------------------Example 2: one of actions fails------------------")
    order = CappuccinoOrder()

    # add a bad action  - grind_coffee will fail.
    action = order.get_child("make_cappuccino")
    action.remove_child("grind_coffee")
    action.add_child(FailingGrindAction(name="grind_coffee", duration=1))
    try:
        await order.start()
    except asyncio.CancelledError:
        logging.info("Cancelled")
    logging.info(f"order state: {order.state}")
    order.display_tree()

    logging.info("-------------------Example 3: cancelling------------------")
    order = CappuccinoOrder()
    order.start()
    await asyncio.sleep(3)
    logging.warning("cancelling order")
    await order.cancel()
    logging.info(f"order state: {order.state}")
    order.display_tree()


if __name__ == "__main__":
    coloredlogs.install(
        level="DEBUG",
        fmt=action_trees.LOG_FORMAT,
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("interrupted")
