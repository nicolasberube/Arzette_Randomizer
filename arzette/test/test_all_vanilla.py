from ..options import LevelOrder, ShuffleBags, ShuffleBarrierTypes, ShuffleBeacons, ShuffleBonusScrollRewards, ShuffleBonusScrolls, ShuffleCandles, ShuffleCoins, ShuffleHillsKey, ShuffleJewels, ShuffleKeys, ShuffleLifeUps, ShuffleNPCs, ShufflePlants, ShuffleRaceRewards, ShuffleRocks, ShuffleUpgrades, TradingSequence
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase


class TestAllVanilla(ArzetteTestBase):
    options = {
        "level_order": LevelOrder.option_vanilla,
        "trading_sequence": TradingSequence.option_vanilla,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_false,
        "shuffle_npcs": ShuffleNPCs.option_false,
        "shuffle_bags": ShuffleBags.option_false,
        "shuffle_keys": ShuffleKeys.option_false,
        "shuffle_hills_key": ShuffleHillsKey.option_false,
        "shuffle_candles": ShuffleCandles.option_false,
        "shuffle_coins": ShuffleCoins.option_false,
        "shuffle_rocks": ShuffleRocks.option_false,
        "shuffle_plants": ShufflePlants.option_false,
        "shuffle_upgrades": ShuffleUpgrades.option_false,
        "shuffle_life_ups": ShuffleLifeUps.option_false,
        "shuffle_bonus_scrolls": ShuffleBonusScrolls.option_false,
        "shuffle_bonus_rewards": ShuffleBonusScrollRewards.option_false,
        "shuffle_race_rewards": ShuffleRaceRewards.option_false,
        "shuffle_beacons": ShuffleBeacons.option_false,
        "shuffle_jewels": ShuffleJewels.option_false,

    }


class TestAllVanillaCasual(TestAllVanilla, CasualLogic):
    options = {
        **TestAllVanilla.options,
        **CasualLogic.options,
    }


class TestAllVanillaTrickyJumps(TestAllVanilla, TrickyJumpsLogic):
    options = {
        **TestAllVanilla.options,
        **TrickyJumpsLogic.options,
    }


class TestAllVanillaNoLantern(TestAllVanilla, NoLanternLogic):
    options = {
        **TestAllVanilla.options,
        **NoLanternLogic.options,
    }


class TestAllVanillaDamageBoost(TestAllVanilla, DamageBoostLogic):
    options = {
        **TestAllVanilla.options,
        **DamageBoostLogic.options,
    }


class TestAllVanillaTrickyJumpsNoLantern(TestAllVanilla, TrickyJumpsNoLanternLogic):
    options = {
        **TestAllVanilla.options,
        **TrickyJumpsNoLanternLogic.options,
    }


class TestAllVanillaTrickyJumpsDamageBoost(TestAllVanilla, TrickyJumpsDamageBoostLogic):
    options = {
        **TestAllVanilla.options,
        **TrickyJumpsDamageBoostLogic.options,
    }


class TestAllVanillaNoLanternDamageBoost(TestAllVanilla, NoLanternDamageBoostLogic):
    options = {
        **TestAllVanilla.options,
        **NoLanternDamageBoostLogic.options,
    }


class TestAllVanillaTrickyJumpsNoLanternDamageBoost(TestAllVanilla, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestAllVanilla.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

