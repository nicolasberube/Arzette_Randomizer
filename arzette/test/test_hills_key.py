from ..Names import itemName
from ..options import ShuffleHillsKey
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledHillsKey(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_hills_key": ShuffleHillsKey.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        assert itemName.HillsKey in item_pool_names

    def test_locations(self) -> None:
        location = self.world.get_location(self.world.item_to_loc[itemName.HillsKey])
        assert not location.is_event

class TestVanillaHillsKey(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_hills_key": ShuffleHillsKey.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        assert itemName.HillsKey not in item_pool_names

    def test_prefills(self) -> None:
        location = self.world.get_location(self.world.item_to_loc[itemName.HillsKey])
        assert location.is_event
        assert location.item is not None
        assert location.item.is_event
        assert location.item.name == itemName.HillsKey

class TestShuffledHillsKeyCasual(TestShuffledHillsKey, CasualLogic):
    options = {
        **TestShuffledHillsKey.options,
        **CasualLogic.options,
    }

class TestShuffledHillsKeyTrickyJumps(TestShuffledHillsKey, TrickyJumpsLogic):
    options = {
        **TestShuffledHillsKey.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledHillsKeyNoLantern(TestShuffledHillsKey, NoLanternLogic):
    options = {
        **TestShuffledHillsKey.options,
        **NoLanternLogic.options,
    }

class TestShuffledHillsKeyDamageBoost(TestShuffledHillsKey, DamageBoostLogic):
    options = {
        **TestShuffledHillsKey.options,
        **DamageBoostLogic.options,
    }

class TestShuffledHillsKeyTrickyJumpsNoLantern(TestShuffledHillsKey, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledHillsKey.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledHillsKeyTrickyJumpsDamageBoost(TestShuffledHillsKey, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledHillsKey.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledHillsKeyNoLanternDamageBoost(TestShuffledHillsKey, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledHillsKey.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledHillsKeyTrickyJumpsNoLanternDamageBoost(TestShuffledHillsKey, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledHillsKey.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaHillsKeyCasual(TestVanillaHillsKey, CasualLogic):
    options = {
        **TestVanillaHillsKey.options,
        **CasualLogic.options,
    }

class TestVanillaHillsKeyTrickyJumps(TestVanillaHillsKey, TrickyJumpsLogic):
    options = {
        **TestVanillaHillsKey.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaHillsKeyNoLantern(TestVanillaHillsKey, NoLanternLogic):
    options = {
        **TestVanillaHillsKey.options,
        **NoLanternLogic.options,
    }

class TestVanillaHillsKeyDamageBoost(TestVanillaHillsKey, DamageBoostLogic):
    options = {
        **TestVanillaHillsKey.options,
        **DamageBoostLogic.options,
    }

class TestVanillaHillsKeyTrickyJumpsNoLantern(TestVanillaHillsKey, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaHillsKey.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaHillsKeyTrickyJumpsDamageBoost(TestVanillaHillsKey, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaHillsKey.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaHillsKeyNoLanternDamageBoost(TestVanillaHillsKey, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaHillsKey.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaHillsKeyTrickyJumpsNoLanternDamageBoost(TestVanillaHillsKey, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaHillsKey.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }
