from ..options import LevelOrder, ShuffleBags, ShuffleBarrierTypes, ShuffleBeacons, ShuffleBonusScrollRewards, ShuffleBonusScrolls, ShuffleCandles, ShuffleCoins, ShuffleHillsKey, ShuffleJewels, ShuffleKeys, ShuffleLifeUps, ShuffleNPCs, ShufflePlants, ShuffleRaceRewards, ShuffleRocks, ShuffleUpgrades, TradingSequence
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase


class TestAllShuffled(ArzetteTestBase):
    options = {
        "level_order": LevelOrder.option_randomize,
        "trading_sequence": TradingSequence.option_shuffle,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_true,
        "shuffle_npcs": ShuffleNPCs.option_true,
        "shuffle_bags": ShuffleBags.option_true,
        "shuffle_keys": ShuffleKeys.option_true,
        "shuffle_hills_key": ShuffleHillsKey.option_true,
        "shuffle_candles": ShuffleCandles.option_true,
        "shuffle_coins": ShuffleCoins.option_true,
        "shuffle_rocks": ShuffleRocks.option_true,
        "shuffle_plants": ShufflePlants.option_true,
        "shuffle_upgrades": ShuffleUpgrades.option_true,
        "shuffle_life_ups": ShuffleLifeUps.option_true,
        "shuffle_bonus_scrolls": ShuffleBonusScrolls.option_true,
        "shuffle_bonus_rewards": ShuffleBonusScrollRewards.option_true,
        "shuffle_race_rewards": ShuffleRaceRewards.option_true,
        "shuffle_beacons": ShuffleBeacons.option_true,
        "shuffle_jewels": ShuffleJewels.option_true,

    }


class TestAllShuffledCasual(TestAllShuffled, CasualLogic):
    options = {
        **TestAllShuffled.options,
        **CasualLogic.options,
    }


class TestAllShuffledTrickyJumps(TestAllShuffled, TrickyJumpsLogic):
    options = {
        **TestAllShuffled.options,
        **TrickyJumpsLogic.options,
    }


class TestAllShuffledNoLantern(TestAllShuffled, NoLanternLogic):
    options = {
        **TestAllShuffled.options,
        **NoLanternLogic.options,
    }


class TestAllShuffledDamageBoost(TestAllShuffled, DamageBoostLogic):
    options = {
        **TestAllShuffled.options,
        **DamageBoostLogic.options,
    }


class TestAllShuffledTrickyJumpsNoLantern(TestAllShuffled, TrickyJumpsNoLanternLogic):
    options = {
        **TestAllShuffled.options,
        **TrickyJumpsNoLanternLogic.options,
    }


class TestAllShuffledTrickyJumpsDamageBoost(TestAllShuffled, TrickyJumpsDamageBoostLogic):
    options = {
        **TestAllShuffled.options,
        **TrickyJumpsDamageBoostLogic.options,
    }


class TestAllShuffledNoLanternDamageBoost(TestAllShuffled, NoLanternDamageBoostLogic):
    options = {
        **TestAllShuffled.options,
        **NoLanternDamageBoostLogic.options,
    }


class TestAllShuffledTrickyJumpsNoLanternDamageBoost(TestAllShuffled, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestAllShuffled.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

