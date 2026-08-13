from ..items import key_items
from ..Names import itemName
from ..options import ShuffleKeys
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

# Hills key has its own option.
SHUFFLED_KEYS = [key for key in key_items if key != itemName.HillsKey]

class TestShuffledKeys(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_keys": ShuffleKeys.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for key in SHUFFLED_KEYS:
            assert key in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for key in SHUFFLED_KEYS:
            loc_name = self.world.item_to_loc[key]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaKeys(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_keys": ShuffleKeys.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for key in SHUFFLED_KEYS:
            assert key not in item_pool_names

    def test_prefills(self) -> None:
        for key in SHUFFLED_KEYS:
            location = self.world.get_location(self.world.item_to_loc[key])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == key

class TestShuffledKeysCasual(TestShuffledKeys, CasualLogic):
    options = {
        **TestShuffledKeys.options,
        **CasualLogic.options,
    }

class TestShuffledKeysTrickyJumps(TestShuffledKeys, TrickyJumpsLogic):
    options = {
        **TestShuffledKeys.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledKeysNoLantern(TestShuffledKeys, NoLanternLogic):
    options = {
        **TestShuffledKeys.options,
        **NoLanternLogic.options,
    }

class TestShuffledKeysDamageBoost(TestShuffledKeys, DamageBoostLogic):
    options = {
        **TestShuffledKeys.options,
        **DamageBoostLogic.options,
    }

class TestShuffledKeysTrickyJumpsNoLantern(TestShuffledKeys, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledKeys.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledKeysTrickyJumpsDamageBoost(TestShuffledKeys, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledKeys.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledKeysNoLanternDamageBoost(TestShuffledKeys, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledKeys.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledKeysTrickyJumpsNoLanternDamageBoost(TestShuffledKeys, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledKeys.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaKeysCasual(TestVanillaKeys, CasualLogic):
    options = {
        **TestVanillaKeys.options,
        **CasualLogic.options,
    }

class TestVanillaKeysTrickyJumps(TestVanillaKeys, TrickyJumpsLogic):
    options = {
        **TestVanillaKeys.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaKeysNoLantern(TestVanillaKeys, NoLanternLogic):
    options = {
        **TestVanillaKeys.options,
        **NoLanternLogic.options,
    }

class TestVanillaKeysDamageBoost(TestVanillaKeys, DamageBoostLogic):
    options = {
        **TestVanillaKeys.options,
        **DamageBoostLogic.options,
    }

class TestVanillaKeysTrickyJumpsNoLantern(TestVanillaKeys, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaKeys.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaKeysTrickyJumpsDamageBoost(TestVanillaKeys, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaKeys.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaKeysNoLanternDamageBoost(TestVanillaKeys, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaKeys.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaKeysTrickyJumpsNoLanternDamageBoost(TestVanillaKeys, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaKeys.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }
