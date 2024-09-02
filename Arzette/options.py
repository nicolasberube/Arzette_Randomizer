from dataclasses import dataclass
from Options import (DefaultOnToggle, Toggle, Choice, PerGameCommonOptions, OptionGroup)

class LevelOrder(Choice):
    """
Determines which levels are unlocked with beacons.
Random: Each beacon will unlock 2 or 3 random levels.
Faramore: As random, but Faramore Town is guaranteed to be one of your starting levels.
Vanilla: Each beacon will unlock its normal levels. Note that beacon locations may still be shuffled to random locations.
    """
    internal_name = "level_order"
    display_name = "Level Order"
    option_vanilla = 0
    option_faramore = 1
    option_random = 2
    default = 1

class ShuffleBarrierTypes(Toggle):
    """When enabled, will randomize the barrier types. All barriers of a certain type will be changed to another.
    """
    internal_name = "shuffle_barrier_types"
    display_name = "Shuffle Barrier Types"

class ShuffleNPCs(Toggle):
    """Include NPCs in the item and location pools. NPCs are always local, and can never spawn from other NPCs or from hitting rocks."""
    internal_name = "shuffle_npcs"
    display_name = "Shuffle NPCs"

class ShuffleBags(DefaultOnToggle):
    """Include all bag locations in the item pool."""
    internal_name = "shuffle_bags"
    display_name = "Shuffle Bags"

class ShuffleKeys(DefaultOnToggle):
    """Include all keys and key locations in the item and location pools. This does not include quest items like the Dungeon Key. This does also not include the Key in Lichen Hills."""
    internal_name = "shuffle_keys"
    display_name = "Shuffle Keys"

class ShuffleHillsKey(Toggle):  # in multiworld, we might just force this to spawn non-locally, eliminating most of its weirdness. (and forcing it to vanilla location when it must be local)
    """Allows the Lichen Hills key to spawn locally in locations other than its vanilla location. This key is invisible until the Fatal Flute is played near it, making it difficult to find otherwise."""
    internal_name = "shuffle_hills_key"
    display_name = "Shuffle Hills Key"

class ShuffleCandles(DefaultOnToggle):
    """Include all candles and candle locations in the pool."""
    internal_name = "shuffle_candles"
    display_name = "Shuffle Candles"

class ShuffleCoins(DefaultOnToggle):
    """Include all coins and coin locations in the pool."""
    internal_name = "shuffle_coins"
    display_name = "Shuffle Coins"

class ShufflePlants(DefaultOnToggle):
    """Include all three of the Cypress' quest's plants (and their locations) in the pool."""
    internal_name = "shuffle_plants"
    display_name = "Shuffle Plants"

class ShuffleUpgrades(DefaultOnToggle):
    """Include all the capacity upgrades (and their locations) in the pool. This includes Infinite Soulfire."""
    internal_name = "shuffle_upgrades"
    display_name = "Shuffle Upgrades"

class ShuffleLifeUps(DefaultOnToggle):
    """Include all Life-Ups and Life-Up locations in the pool."""
    internal_name = "shuffle_lifeups"
    display_name = "Shuffle Life-Ups"

class ShuffleBonusScrolls(Toggle):
    """Include Bonus Scrolls in the item and location pools. Bonus Scrolls are always local, and always spawn in the open."""
    internal_name = "shuffle_bonus_scrolls"
    display_name = "Shuffle Bonus Scrolls"

class ShuffleBonusScrollRewards(Toggle):
    """Include the ruby rewards from the bonus minigame scrolls in the item and location pools."""
    internal_name = "shuffle_bonus_rewards"
    display_name = "Shuffle Bonus Scroll Rewards"

class ShuffleRaceRewards(Toggle):
    """Include the 100 ruby rewards from the Rudy races in the item and location pools."""
    internal_name = "shuffle_race_rewards"
    display_name = "Shuffle Race Rewards"

class ShuffleBeacons(DefaultOnToggle):
    """Include the Sacred Beacons in the item and location pools."""
    internal_name = "shuffle_beacons"
    display_name = "Shuffle Beacons"

class ShuffleJewels(Toggle):
    """Include the Faramore Jewel shards in the item and location pools. Beating the five bosses will now grant random items."""
    internal_name = "shuffle_jewels"
    display_name = "Shuffle Jewel Shards"

class TradingSequence(Choice):
    """
Determine how the Chainsword trading sequence is randomized:
Vanilla: All items except the Dungeon Key will be in their vanilla locations, including the Chainsword.
Excluded: The Dungeon Key, the Sacred Oil & Refined Chains, and the Chainsword items will be shuffled, as well as the locations for the Dungeon Key, the Sacred Oil and the Chainsword. The rest of the trade quest will be avoided entirely, including Zazie's Soul Upgrade.
Included: Every item in the Chainsword trading sequence is added to the item and location pools.
    """
    internal_name = "trading_sequence"
    display_name = "Trading Sequence"
    option_vanilla = 0
    option_excluded = 1
    option_included = 2
    default = 1

class TrickyJumps(Toggle):
    """When enabled, some jumps and movement techniques that are much more difficult than usual may be considered in logic."""
    internal_name = "tricky_jumps"
    display_name = "Tricky Jumps"

class NoLantern(Toggle):
    """When enabled, you may be expected to navigate dark areas without the lantern."""
    internal_name = "no_lantern"
    display_name = "No Lantern"

class DamageBoost(Toggle):
    """When enabled, you may be expected to damage boost to an extent that will be possible in casual mode with health drops. When disabled, you can do all things logically without taking damage."""
    internal_name = "damage_boost"
    display_name = "Damage Boosting"

@dataclass
class ArzetteOptions(PerGameCommonOptions):
    level_order = LevelOrder
    shuffle_barrier_types = ShuffleBarrierTypes
    shuffle_npcs = ShuffleNPCs
    shuffle_bags = ShuffleBags
    shuffle_keys = ShuffleKeys
    shuffle_hills_key = ShuffleHillsKey
    shuffle_candles = ShuffleCandles
    shuffle_coins = ShuffleCoins
    shuffle_plants = ShufflePlants
    shuffle_upgrades = ShuffleUpgrades
    shuffle_life_ups = ShuffleLifeUps
    shuffle_bonus_scrolls = ShuffleBonusScrolls
    shuffle_bonus_rewards = ShuffleBonusScrollRewards
    shuffle_race_rewards = ShuffleRaceRewards
    shuffle_beacons = ShuffleBeacons
    shuffle_jewels = ShuffleJewels
    trading_sequence = TradingSequence
    tricky_jumps = TrickyJumps
    no_lantern = NoLantern
    damage_boost = DamageBoost

arzette_option_groups = [
    OptionGroup("Logic Options", [
        TrickyJumps,
        NoLantern,
        DamageBoost
    ]),
    OptionGroup("Shuffle Options", [
        LevelOrder,
        ShuffleKeys,
        ShuffleHillsKey,
        ShuffleBags,
        ShuffleCandles,
        ShuffleCoins,
        ShuffleUpgrades,
        ShufflePlants,
        ShuffleLifeUps,
        ShuffleBonusScrollRewards,
        ShuffleRaceRewards,
        ShuffleBeacons,
        ShuffleJewels,
        ShuffleNPCs,
        ShuffleBonusScrolls,
        ShuffleBarrierTypes,
        TradingSequence
    ]),
]
