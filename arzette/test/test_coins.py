from ..items import coin_items
from ..options import ShuffleCoins
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledCoins(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_coins": ShuffleCoins.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in coin_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in coin_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaCoins(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_coins": ShuffleCoins.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in coin_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in coin_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledCoinsCasual(TestShuffledCoins, CasualLogic):
    options = {
        **TestShuffledCoins.options,
        **CasualLogic.options,
    }

class TestShuffledCoinsTrickyJumps(TestShuffledCoins, TrickyJumpsLogic):
    options = {
        **TestShuffledCoins.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledCoinsNoLantern(TestShuffledCoins, NoLanternLogic):
    options = {
        **TestShuffledCoins.options,
        **NoLanternLogic.options,
    }

class TestShuffledCoinsDamageBoost(TestShuffledCoins, DamageBoostLogic):
    options = {
        **TestShuffledCoins.options,
        **DamageBoostLogic.options,
    }

class TestShuffledCoinsTrickyJumpsNoLantern(TestShuffledCoins, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledCoins.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledCoinsTrickyJumpsDamageBoost(TestShuffledCoins, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledCoins.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledCoinsNoLanternDamageBoost(TestShuffledCoins, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledCoins.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledCoinsTrickyJumpsNoLanternDamageBoost(TestShuffledCoins, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledCoins.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaCoinsCasual(TestVanillaCoins, CasualLogic):
    options = {
        **TestVanillaCoins.options,
        **CasualLogic.options,
    }

class TestVanillaCoinsTrickyJumps(TestVanillaCoins, TrickyJumpsLogic):
    options = {
        **TestVanillaCoins.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaCoinsNoLantern(TestVanillaCoins, NoLanternLogic):
    options = {
        **TestVanillaCoins.options,
        **NoLanternLogic.options,
    }

class TestVanillaCoinsDamageBoost(TestVanillaCoins, DamageBoostLogic):
    options = {
        **TestVanillaCoins.options,
        **DamageBoostLogic.options,
    }

class TestVanillaCoinsTrickyJumpsNoLantern(TestVanillaCoins, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaCoins.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaCoinsTrickyJumpsDamageBoost(TestVanillaCoins, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaCoins.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaCoinsNoLanternDamageBoost(TestVanillaCoins, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaCoins.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaCoinsTrickyJumpsNoLanternDamageBoost(TestVanillaCoins, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaCoins.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

