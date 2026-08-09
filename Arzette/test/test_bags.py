from ..items import bag_items
from ..options import ShuffleBags
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledBags(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_bags": ShuffleBags.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in bag_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in bag_items:
            assert item_name in world_location_names
            location = self.world.get_location(item_name)
            assert not location.is_event

class TestVanillaBags(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_bags": ShuffleBags.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in bag_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        vanilla_locations = [
            location for location in self.world.get_locations()
            if location.name in bag_items
        ]
        for location in vanilla_locations:
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == location.name

class TestShuffledBagsCasual(TestShuffledBags, CasualLogic):
    options = {
        **TestShuffledBags.options,
        **CasualLogic.options,
    }

class TestShuffledBagsTrickyJumps(TestShuffledBags, TrickyJumpsLogic):
    options = {
        **TestShuffledBags.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledBagsNoLantern(TestShuffledBags, NoLanternLogic):
    options = {
        **TestShuffledBags.options,
        **NoLanternLogic.options,
    }

class TestShuffledBagsDamageBoost(TestShuffledBags, DamageBoostLogic):
    options = {
        **TestShuffledBags.options,
        **DamageBoostLogic.options,
    }

class TestShuffledBagsTrickyJumpsNoLantern(TestShuffledBags, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledBags.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledBagsTrickyJumpsDamageBoost(TestShuffledBags, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledBags.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledBagsNoLanternDamageBoost(TestShuffledBags, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledBags.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledBagsTrickyJumpsNoLanternDamageBoost(TestShuffledBags, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledBags.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaBagsCasual(TestVanillaBags, CasualLogic):
    options = {
        **TestVanillaBags.options,
        **CasualLogic.options,
    }

class TestVanillaBagsTrickyJumps(TestVanillaBags, TrickyJumpsLogic):
    options = {
        **TestVanillaBags.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaBagsNoLantern(TestVanillaBags, NoLanternLogic):
    options = {
        **TestVanillaBags.options,
        **NoLanternLogic.options,
    }

class TestVanillaBagsDamageBoost(TestVanillaBags, DamageBoostLogic):
    options = {
        **TestVanillaBags.options,
        **DamageBoostLogic.options,
    }

class TestVanillaBagsTrickyJumpsNoLantern(TestVanillaBags, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaBags.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaBagsTrickyJumpsDamageBoost(TestVanillaBags, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaBags.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaBagsNoLanternDamageBoost(TestVanillaBags, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaBags.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaBagsTrickyJumpsNoLanternDamageBoost(TestVanillaBags, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaBags.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

