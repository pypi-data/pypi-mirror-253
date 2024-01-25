#!/usr/bin/env python3
"""
 Basic action item example

 Copyright (c) 2024 ROX Automation - Jev Kuznetsov
"""

import asyncio
import logging
import coloredlogs

from action_trees import ActionItem
from action_trees.protocols import ActionItemProtocol
from action_trees import LOG_FORMAT


class MyFirstAction(ActionItem):
    """Example of an action item."""

    def __init__(self):
        super().__init__(name="action1")

    async def _on_init(self):
        """Initialize the action item."""
        self._log.info("Starting init")
        try:
            for idx in range(3):
                self._log.info(f"init {idx}")
                await self._wait_if_paused()
                await asyncio.sleep(0.1)
            self._log.info("Finished init")
        except asyncio.CancelledError:
            self._log.warning("on_init cancelled")
            # do some cleanup here
            raise

    async def _on_run(self):
        """Run the action item."""
        self._log.info("Running")
        idx = 0
        try:
            while True:
                self._log.info(f"run {idx}")
                await self._wait_if_paused()
                idx += 1
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            self._log.warning("on_run cancelled")
            raise


class InstantAction(ActionItem):
    """action item that runs instantly"""

    def __init__(self):
        super().__init__(name="action2")
        self.start()

    async def _on_run(self):
        """Run the action item."""
        self._log.info("Running")
        idx = 0
        try:
            for idx in range(3):
                self._log.info(f"run {idx}")
                await self._wait_if_paused()
                idx += 1
                await asyncio.sleep(1)
            self._log.info("Finished")
        except asyncio.CancelledError:
            self._log.warning("on_run cancelled")
            raise


async def command_action(action: ActionItemProtocol):
    """send some actions to the action item"""
    await asyncio.sleep(2)
    action.pause()
    await asyncio.sleep(2)
    action.resume()
    await asyncio.sleep(3)
    await action.cancel()
    await asyncio.sleep(2)
    logging.info("Done.")


async def main() -> None:
    """main coroutine"""

    action1: ActionItemProtocol = MyFirstAction()
    tsk1 = action1.start()

    action2: ActionItemProtocol = InstantAction()
    tsk2 = action2.start()  # noop - already started

    await command_action(action1)

    # check task status
    logging.info(f"{tsk1.done()=}, {tsk2.done()=}")

    # get exception if any
    for action in (action1, action2):
        exc = action.get_exception()
        logging.info(f"action {action.name} {action.state}  exception: {exc}")


if __name__ == "__main__":
    coloredlogs.install(
        level="DEBUG",
        fmt=LOG_FORMAT,
    )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("interrupted")
