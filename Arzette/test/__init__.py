from test.bases import WorldTestBase
from .. import ArzetteWorld
from ..options import (
    ShuffleBarrierTypes,
    ShuffleBeacons,
    ShuffleBonusScrolls,
    ShuffleNPCs,
    TradingSequence,
)


class ArzetteTestBase(WorldTestBase):
    game = "Arzette: The Jewel of Faramore"
    world: ArzetteWorld
    no_early_lock_options = {
        "shuffle_npcs": ShuffleNPCs.option_false,
        "shuffle_bonus_scrolls": ShuffleBonusScrolls.option_false,
        "shuffle_beacons": ShuffleBeacons.option_false,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_false,
        "trading_sequence": TradingSequence.option_shuffle,
    }
    options = {
        **no_early_lock_options,
    }
