""" integral test by running an example action tree """

import pytest
from action_trees.examples import coffee_maker


@pytest.mark.asyncio
async def test_coffee_maker():
    await coffee_maker.main()
