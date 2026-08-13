from ..items import candle_items
from ..options import ShuffleCandles
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledCandles(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_candles": ShuffleCandles.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in candle_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in candle_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaCandles(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_candles": ShuffleCandles.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in candle_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in candle_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledCandlesCasual(TestShuffledCandles, CasualLogic):
    options = {
        **TestShuffledCandles.options,
        **CasualLogic.options,
    }

class TestShuffledCandlesTrickyJumps(TestShuffledCandles, TrickyJumpsLogic):
    options = {
        **TestShuffledCandles.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledCandlesNoLantern(TestShuffledCandles, NoLanternLogic):
    options = {
        **TestShuffledCandles.options,
        **NoLanternLogic.options,
    }

class TestShuffledCandlesDamageBoost(TestShuffledCandles, DamageBoostLogic):
    options = {
        **TestShuffledCandles.options,
        **DamageBoostLogic.options,
    }

class TestShuffledCandlesTrickyJumpsNoLantern(TestShuffledCandles, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledCandles.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledCandlesTrickyJumpsDamageBoost(TestShuffledCandles, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledCandles.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledCandlesNoLanternDamageBoost(TestShuffledCandles, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledCandles.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledCandlesTrickyJumpsNoLanternDamageBoost(TestShuffledCandles, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledCandles.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaCandlesCasual(TestVanillaCandles, CasualLogic):
    options = {
        **TestVanillaCandles.options,
        **CasualLogic.options,
    }

class TestVanillaCandlesTrickyJumps(TestVanillaCandles, TrickyJumpsLogic):
    options = {
        **TestVanillaCandles.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaCandlesNoLantern(TestVanillaCandles, NoLanternLogic):
    options = {
        **TestVanillaCandles.options,
        **NoLanternLogic.options,
    }

class TestVanillaCandlesDamageBoost(TestVanillaCandles, DamageBoostLogic):
    options = {
        **TestVanillaCandles.options,
        **DamageBoostLogic.options,
    }

class TestVanillaCandlesTrickyJumpsNoLantern(TestVanillaCandles, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaCandles.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaCandlesTrickyJumpsDamageBoost(TestVanillaCandles, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaCandles.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaCandlesNoLanternDamageBoost(TestVanillaCandles, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaCandles.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaCandlesTrickyJumpsNoLanternDamageBoost(TestVanillaCandles, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaCandles.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

