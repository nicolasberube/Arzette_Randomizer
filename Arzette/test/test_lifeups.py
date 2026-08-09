from ..items import lifeup_items
from ..options import ShuffleLifeUps
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledLifeUps(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_life_ups": ShuffleLifeUps.option_true,


    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in lifeup_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in lifeup_items:
            assert item_name in world_location_names
            location = self.world.get_location(item_name)
            assert not location.is_event

class TestVanillaLifeUps(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_life_ups": ShuffleLifeUps.option_false,


    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in lifeup_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        vanilla_locations = [
            location for location in self.world.get_locations()
            if location.name in lifeup_items
        ]
        for location in vanilla_locations:
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == location.name

class TestShuffledLifeUpsCasual(TestShuffledLifeUps, CasualLogic):
    options = {
        **TestShuffledLifeUps.options,
        **CasualLogic.options,
    }

class TestShuffledLifeUpsTrickyJumps(TestShuffledLifeUps, TrickyJumpsLogic):
    options = {
        **TestShuffledLifeUps.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledLifeUpsNoLantern(TestShuffledLifeUps, NoLanternLogic):
    options = {
        **TestShuffledLifeUps.options,
        **NoLanternLogic.options,
    }

class TestShuffledLifeUpsDamageBoost(TestShuffledLifeUps, DamageBoostLogic):
    options = {
        **TestShuffledLifeUps.options,
        **DamageBoostLogic.options,
    }

class TestShuffledLifeUpsTrickyJumpsNoLantern(TestShuffledLifeUps, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledLifeUps.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledLifeUpsTrickyJumpsDamageBoost(TestShuffledLifeUps, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledLifeUps.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledLifeUpsNoLanternDamageBoost(TestShuffledLifeUps, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledLifeUps.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledLifeUpsTrickyJumpsNoLanternDamageBoost(TestShuffledLifeUps, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledLifeUps.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaLifeUpsCasual(TestVanillaLifeUps, CasualLogic):
    options = {
        **TestVanillaLifeUps.options,
        **CasualLogic.options,
    }

class TestVanillaLifeUpsTrickyJumps(TestVanillaLifeUps, TrickyJumpsLogic):
    options = {
        **TestVanillaLifeUps.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaLifeUpsNoLantern(TestVanillaLifeUps, NoLanternLogic):
    options = {
        **TestVanillaLifeUps.options,
        **NoLanternLogic.options,
    }

class TestVanillaLifeUpsDamageBoost(TestVanillaLifeUps, DamageBoostLogic):
    options = {
        **TestVanillaLifeUps.options,
        **DamageBoostLogic.options,
    }

class TestVanillaLifeUpsTrickyJumpsNoLantern(TestVanillaLifeUps, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaLifeUps.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaLifeUpsTrickyJumpsDamageBoost(TestVanillaLifeUps, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaLifeUps.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaLifeUpsNoLanternDamageBoost(TestVanillaLifeUps, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaLifeUps.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaLifeUpsTrickyJumpsNoLanternDamageBoost(TestVanillaLifeUps, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaLifeUps.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

