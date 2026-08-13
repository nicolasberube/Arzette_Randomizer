from test.bases import WorldTestBase
from .. import ArzetteWorld
from ..options import (
    LevelOrder,
    ShuffleBarrierTypes,
    ShuffleBeacons,
    ShuffleBonusScrolls,
    ShuffleNPCs,
    TradingSequence,
)


class ArzetteTestBase(WorldTestBase):
    game = "Arzette: The Jewel of Faramore"
    world: ArzetteWorld
    # No early-lock options, and vanilla level order so generation can happen without randomising beacons.
    base_options = {
        "level_order": LevelOrder.option_vanilla,
        "shuffle_npcs": ShuffleNPCs.option_false,
        "shuffle_bonus_scrolls": ShuffleBonusScrolls.option_false,
        "shuffle_beacons": ShuffleBeacons.option_false,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_false,
        "trading_sequence": TradingSequence.option_shuffle,
    }
    options = {
        **base_options,
    }
