from ..items import rock_items
from ..options import ShuffleRocks
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledRocks(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_rocks": ShuffleRocks.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in rock_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in rock_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaRocks(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_rocks": ShuffleRocks.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in rock_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in rock_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledRocksCasual(TestShuffledRocks, CasualLogic):
    options = {
        **TestShuffledRocks.options,
        **CasualLogic.options,
    }

class TestShuffledRocksTrickyJumps(TestShuffledRocks, TrickyJumpsLogic):
    options = {
        **TestShuffledRocks.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledRocksNoLantern(TestShuffledRocks, NoLanternLogic):
    options = {
        **TestShuffledRocks.options,
        **NoLanternLogic.options,
    }

class TestShuffledRocksDamageBoost(TestShuffledRocks, DamageBoostLogic):
    options = {
        **TestShuffledRocks.options,
        **DamageBoostLogic.options,
    }

class TestShuffledRocksTrickyJumpsNoLantern(TestShuffledRocks, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledRocks.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledRocksTrickyJumpsDamageBoost(TestShuffledRocks, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledRocks.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledRocksNoLanternDamageBoost(TestShuffledRocks, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledRocks.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledRocksTrickyJumpsNoLanternDamageBoost(TestShuffledRocks, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledRocks.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaRocksCasual(TestVanillaRocks, CasualLogic):
    options = {
        **TestVanillaRocks.options,
        **CasualLogic.options,
    }

class TestVanillaRocksTrickyJumps(TestVanillaRocks, TrickyJumpsLogic):
    options = {
        **TestVanillaRocks.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaRocksNoLantern(TestVanillaRocks, NoLanternLogic):
    options = {
        **TestVanillaRocks.options,
        **NoLanternLogic.options,
    }

class TestVanillaRocksDamageBoost(TestVanillaRocks, DamageBoostLogic):
    options = {
        **TestVanillaRocks.options,
        **DamageBoostLogic.options,
    }

class TestVanillaRocksTrickyJumpsNoLantern(TestVanillaRocks, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaRocks.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaRocksTrickyJumpsDamageBoost(TestVanillaRocks, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaRocks.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaRocksNoLanternDamageBoost(TestVanillaRocks, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaRocks.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaRocksTrickyJumpsNoLanternDamageBoost(TestVanillaRocks, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaRocks.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

