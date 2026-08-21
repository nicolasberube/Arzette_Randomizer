from ..items import upgrade_items
from ..options import ShuffleUpgrades
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledUpgrades(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_upgrades": ShuffleUpgrades.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in upgrade_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in upgrade_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaUpgrades(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_upgrades": ShuffleUpgrades.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in upgrade_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in upgrade_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledUpgradesCasual(TestShuffledUpgrades, CasualLogic):
    options = {
        **TestShuffledUpgrades.options,
        **CasualLogic.options,
    }

class TestShuffledUpgradesTrickyJumps(TestShuffledUpgrades, TrickyJumpsLogic):
    options = {
        **TestShuffledUpgrades.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledUpgradesNoLantern(TestShuffledUpgrades, NoLanternLogic):
    options = {
        **TestShuffledUpgrades.options,
        **NoLanternLogic.options,
    }

class TestShuffledUpgradesDamageBoost(TestShuffledUpgrades, DamageBoostLogic):
    options = {
        **TestShuffledUpgrades.options,
        **DamageBoostLogic.options,
    }

class TestShuffledUpgradesTrickyJumpsNoLantern(TestShuffledUpgrades, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledUpgrades.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledUpgradesTrickyJumpsDamageBoost(TestShuffledUpgrades, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledUpgrades.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledUpgradesNoLanternDamageBoost(TestShuffledUpgrades, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledUpgrades.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledUpgradesTrickyJumpsNoLanternDamageBoost(TestShuffledUpgrades, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledUpgrades.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaUpgradesCasual(TestVanillaUpgrades, CasualLogic):
    options = {
        **TestVanillaUpgrades.options,
        **CasualLogic.options,
    }

class TestVanillaUpgradesTrickyJumps(TestVanillaUpgrades, TrickyJumpsLogic):
    options = {
        **TestVanillaUpgrades.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaUpgradesNoLantern(TestVanillaUpgrades, NoLanternLogic):
    options = {
        **TestVanillaUpgrades.options,
        **NoLanternLogic.options,
    }

class TestVanillaUpgradesDamageBoost(TestVanillaUpgrades, DamageBoostLogic):
    options = {
        **TestVanillaUpgrades.options,
        **DamageBoostLogic.options,
    }

class TestVanillaUpgradesTrickyJumpsNoLantern(TestVanillaUpgrades, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaUpgrades.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaUpgradesTrickyJumpsDamageBoost(TestVanillaUpgrades, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaUpgrades.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaUpgradesNoLanternDamageBoost(TestVanillaUpgrades, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaUpgrades.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaUpgradesTrickyJumpsNoLanternDamageBoost(TestVanillaUpgrades, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaUpgrades.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

