from dataclasses import dataclass
from Options import (DefaultOnToggle, Toggle, Choice, PerGameCommonOptions, OptionGroup)

class LevelOrder(Choice):
    """
Determines which levels are unlocked with beacons. Each beacon will still unlock the same number of levels.
Vanilla: Each beacon will unlock its normal levels. Note that beacon locations may still be shuffled to random locations with Shuffle Beacons.
Faramore_Start_Shuffle: Each beacon will unlock 2 or 3 random levels, but Faramore Town is guaranteed to be one of your 2 starting levels to grant access to the shop.
Shuffle: Each beacon will unlock 2 or 3 random levels. Be careful that activating this might lock the store away for a while, and force the player to farm bags to get power stones.
    """
    internal_name = "level_order"
    display_name = "Level Order"
    option_vanilla = 0
    option_faramore_start_shuffle = 1
    option_shuffle = 2
    default = 1

class ShuffleBeacons(DefaultOnToggle):
    """
Include the Sacred Beacons in the item and location pools.
Sacred Beacons will stay in your local game, cannot spawn from other items, and will still unlock levels when hit.
Not to be confused with Level Order, which decides which level is unlocked by hitting the beacon.
Using Faramore_Start_Shuffle or Shuffle Level Order without Shuffle Beacons enabled will make it hard to get a successful generation.
    """
    internal_name = "shuffle_beacons"
    display_name = "Shuffle Beacons"

class ShuffleBarrierTypes(DefaultOnToggle):
    """
When enabled, will randomize the barrier types. All barriers of a certain type will be changed to another.
If enabled, then Shuffle Coins needs to be enabled as well, or else the Crypts Coin would be unreachable.
    """
    internal_name = "shuffle_barrier_types"
    display_name = "Shuffle Barrier Types"

class ShuffleNPCs(DefaultOnToggle):
    """Include NPCs in the item and location pools. NPCs will stay in your local game."""
    internal_name = "shuffle_npcs"
    display_name = "Shuffle NPCs"

class ShuffleBags(DefaultOnToggle):
    """Include bags in the item and location pools."""
    internal_name = "shuffle_bags"
    display_name = "Shuffle Bags"

class ShuffleKeys(DefaultOnToggle):
    """
Include all keys in the item and location pools.
This does not include quest items like the Fort Findula Dungeon Key.
This does also not include the Key in Lichen Hills' Music Shrine.
    """
    internal_name = "shuffle_keys"
    display_name = "Shuffle Keys"

class ShuffleHillsKey(Toggle):
    """
Add the Lichen Hills key and its Music Shrine location to the pool.
If spawned in your local game, this key is invisible until the Fatal Flute is played near it, making it difficult to find otherwise.
One would need to know every location check in the game, and play the Flute next to them if they are empty.
The only other empty location would be the Shield Ring if you already collected the Reflector Ring.
    """
    internal_name = "shuffle_hills_key"
    display_name = "Shuffle Hills Key"

class ShuffleCandles(DefaultOnToggle):
    """Include all candles in the item and location pools."""
    internal_name = "shuffle_candles"
    display_name = "Shuffle Candles"

class ShuffleCoins(DefaultOnToggle):
    """Include all secret coins in the item and location pools."""
    internal_name = "shuffle_coins"
    display_name = "Shuffle Coins"

class ShuffleRocks(DefaultOnToggle):
    """Include all four colored rocks in the item and location pools."""
    internal_name = "shuffle_rocks"
    display_name = "Shuffle Rocks"

class ShufflePlants(DefaultOnToggle):
    """Include all three of the Cypress' quest's plants in the item and location poolsl."""
    internal_name = "shuffle_plants"
    display_name = "Shuffle Plants"

class ShuffleUpgrades(DefaultOnToggle):
    """Include all the capacity upgrades in the item and location pools. This includes Infinite Soulfire."""
    internal_name = "shuffle_upgrades"
    display_name = "Shuffle Upgrades"

class ShuffleLifeUps(DefaultOnToggle):
    """Include all Life-Ups (extra hearts) in the item and location pools."""
    internal_name = "shuffle_lifeups"
    display_name = "Shuffle Life-Ups"

class ShuffleBonusScrolls(DefaultOnToggle):
    """
Include Bonus Scrolls in the item and location pools.
Bonus Scrolls will stay in your local game, and cannot spawn from other items.
    """
    internal_name = "shuffle_bonus_scrolls"
    display_name = "Shuffle Bonus Scrolls"

class ShuffleBonusScrollRewards(DefaultOnToggle):
    """
Include the Rubies rewards from the bonus minigame scrolls in the item and location pools.
Note that Faramore, Volcano and Castle Bonus do not have any rewards.
"""
    internal_name = "shuffle_bonus_rewards"
    display_name = "Shuffle Bonus Scroll Rewards"

class ShuffleRaceRewards(DefaultOnToggle):
    """Include the 100 Rubies rewards from the Rudy races in the item and location pools."""
    internal_name = "shuffle_race_rewards"
    display_name = "Shuffle Race Rewards"

class ShuffleJewels(Toggle):
    """Include the Faramore Jewel shards in the item and location pools. Beating the five bosses will now grant random items."""
    internal_name = "shuffle_jewels"
    display_name = "Shuffle Jewel Shards"

class TradingSequence(Choice):
    """
Determine how the Chainsword trading sequence is randomized:
Vanilla: All items except the Dungeon Key will be in their vanilla locations, including the Chainsword. In other words, talking to Alven once will give you random item. Finding the Fort Findula Dungeon Key will kickstart the trading sequence, which will always lead to the Chainsword in the end.
Random_Start: One random item of the trading sequence will be shuffled, and the rest of the sequence from that item will be in their vanilla locations, including the Chainsword. The start of the trade quest will be avoided entirely, including Zazie's Soul Upgrade if it doesn't start with the Sacred Oil.
Excluded: The Dungeon Key, the Sacred Oil & Refined Chains, and the Chainsword items will be shuffled, as well as the locations for the Dungeon Key, the Sacred Oil and the Chainsword. The rest of the trade quest will be avoided entirely, including Zazie's Soul Upgrade. In other words, talking to Alven once will give you random item, talking to Alven with the Sacred Oil and Refined Chains will give you a random item, and going to the end of the Fort Findula Dungeon will give you a random item. Every other NPC interaction in the sequence will ask for an item that you cannot obtain.
Shuffle: Every item in the Chainsword trading sequence is added to the item and location pools. The game has been modified so you can hold multiple items of the trading sequence at the same time, but they might not show up in the inventory.
    """
    internal_name = "trading_sequence"
    display_name = "Trading Sequence"
    option_vanilla = 0
    option_random_start = 1
    option_excluded = 2
    option_shuffle = 3
    default = 2

class TrickyJumps(Toggle):
    """When enabled, some jumps and movement techniques that are much more difficult than usual may be considered in logic. See documentation for more information."""
    internal_name = "tricky_jumps"
    display_name = "Tricky Jumps"

class NoLantern(Toggle):
    """When enabled, you may be expected to navigate dark areas without the lantern."""
    internal_name = "no_lantern"
    display_name = "No Lantern"

class DamageBoost(Toggle):
    """When enabled, you may be expected to damage boost to an extent that will be possible in casual mode with health drops. When disabled, you can collect everything logically without taking damage."""
    internal_name = "damage_boost"
    display_name = "Damage Boosting"

@dataclass
class ArzetteOptions(PerGameCommonOptions):
    level_order: LevelOrder
    shuffle_barrier_types: ShuffleBarrierTypes
    shuffle_npcs: ShuffleNPCs
    shuffle_bags: ShuffleBags
    shuffle_keys: ShuffleKeys
    shuffle_hills_key: ShuffleHillsKey
    shuffle_candles: ShuffleCandles
    shuffle_coins: ShuffleCoins
    shuffle_rocks: ShuffleRocks
    shuffle_plants: ShufflePlants
    shuffle_upgrades: ShuffleUpgrades
    shuffle_life_ups: ShuffleLifeUps
    shuffle_bonus_scrolls: ShuffleBonusScrolls
    shuffle_bonus_rewards: ShuffleBonusScrollRewards
    shuffle_race_rewards: ShuffleRaceRewards
    shuffle_beacons: ShuffleBeacons
    shuffle_jewels: ShuffleJewels
    trading_sequence: TradingSequence
    tricky_jumps: TrickyJumps
    no_lantern: NoLantern
    damage_boost: DamageBoost

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
        ShuffleRocks,
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
