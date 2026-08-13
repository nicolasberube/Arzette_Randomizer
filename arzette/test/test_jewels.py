from ..items import jewel_items
from ..options import ShuffleJewels
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledJewels(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_jewels": ShuffleJewels.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in jewel_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in jewel_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaJewels(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_jewels": ShuffleJewels.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in jewel_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in jewel_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledJewelsCasual(TestShuffledJewels, CasualLogic):
    options = {
        **TestShuffledJewels.options,
        **CasualLogic.options,
    }

class TestShuffledJewelsTrickyJumps(TestShuffledJewels, TrickyJumpsLogic):
    options = {
        **TestShuffledJewels.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledJewelsNoLantern(TestShuffledJewels, NoLanternLogic):
    options = {
        **TestShuffledJewels.options,
        **NoLanternLogic.options,
    }

class TestShuffledJewelsDamageBoost(TestShuffledJewels, DamageBoostLogic):
    options = {
        **TestShuffledJewels.options,
        **DamageBoostLogic.options,
    }

class TestShuffledJewelsTrickyJumpsNoLantern(TestShuffledJewels, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledJewels.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledJewelsTrickyJumpsDamageBoost(TestShuffledJewels, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledJewels.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledJewelsNoLanternDamageBoost(TestShuffledJewels, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledJewels.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledJewelsTrickyJumpsNoLanternDamageBoost(TestShuffledJewels, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledJewels.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaJewelsCasual(TestVanillaJewels, CasualLogic):
    options = {
        **TestVanillaJewels.options,
        **CasualLogic.options,
    }

class TestVanillaJewelsTrickyJumps(TestVanillaJewels, TrickyJumpsLogic):
    options = {
        **TestVanillaJewels.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaJewelsNoLantern(TestVanillaJewels, NoLanternLogic):
    options = {
        **TestVanillaJewels.options,
        **NoLanternLogic.options,
    }

class TestVanillaJewelsDamageBoost(TestVanillaJewels, DamageBoostLogic):
    options = {
        **TestVanillaJewels.options,
        **DamageBoostLogic.options,
    }

class TestVanillaJewelsTrickyJumpsNoLantern(TestVanillaJewels, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaJewels.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaJewelsTrickyJumpsDamageBoost(TestVanillaJewels, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaJewels.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaJewelsNoLanternDamageBoost(TestVanillaJewels, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaJewels.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaJewelsTrickyJumpsNoLanternDamageBoost(TestVanillaJewels, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaJewels.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

