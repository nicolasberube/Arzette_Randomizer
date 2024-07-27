# Arzette Randomizer

This is a proof of concept of a randomizer for Arzette: The Jewel of Faramore. For now, it only experiments with the logic of the items and locations, and assigns them adequately for the game to still be beatable. This code will produce a .txt file that include the locations and items assignment.

The first section is the level order unlock.
The key is the level containing the beacon.
The value is a list of the levels that will be unlocked by hitting the beacon in the level in the key.

The second section is the barrier types assignement.
The key (barrier type on the left) is the location of the barriers in the vanilla game.
The value (barrier type on the right) is the replacement, meaning that this is the barrier type that is replacing the barrier in the key.

The third section is the NPC location assignment.
The key (NPC on the left) is the location, meaning that this is where you would find the NPC in the vanilla game.
The value (NPC on the right) is the item, meaning that this is the NPC you will see if you go to this location.

The fourth section is the item location assignment.
The key (item on the left) is the location, meaning that this is where you would find the item in the vanilla game.
The value (item on the right) is the item, meaning that this is the item you will get if you go to this location.

Note that the code is *not* currently Archipelago compatible. I tried my best to make a possible future Achipelago port as smooth as possible, while still keeping the code as simple as possible and not relying on the Archipelago libraries. I guess by doing so, I upheld Larry David's quote of "A good compromise is when both parties are dissatisfied".

# Configuration options

## level_order
Each beacon will still unlock the same number of levels. However, the unlocked levels will be random. The two levels that are unlocked at the start of the game will also be randomised.

## barrier_types
Will randomise the different barrier types. In other words, all barriers of a certain type will be changed to another type.

## NPC

### randomize
Each NPC location will also be randomised. NPC locations can only be randomised within other NPC locations. We could probably include the possibility to spawn an NPC at any item location in the future, though. This would require separating locations in the world from locations as rewards. Doing this would also enable bonus_scolls inclusion in the item_pool options.

### include_foolish
Include the useless (the ones that don't give out any item) NPC locations in the pool. Activating this will put a lot of progression NPCs in Faramore.

## item_pool

Those options decide which item types to include in the item pool to randomise.

### bags
Include bags in the pool

### keys
Include keys in the pool. This does not include quest items like the Fort Findula Dungeon Key. This also does not include the Key in Lichen Hills.

### hills_key
Include the key to the barn from Lichen Hills in the pool. This key is treated differently since you need to play the Fatal Flute to spawn the Key. However, you cannot know where the key is before playing the Flute. Once would need to know every location check in the game, and play the Flute next to them if they are empty. Note that empty locations could also be NPCs with their own spawn rules.

### candles
Include candles in the pool.

### coins
Include Arzette secret coins in the pool.

### plants
Include the three Cypress' quest's plants in the pool.

### upgrades
Include all the capacity upgrades in the pool. This does include the Infinite Soulfire.

### life_ups
Include life-ups (extra hearts) in the pool.

### bonus_scrolls
Includes the bonus minigame scrolls location in the pool. The scrolls will only spawn in open locations, not as quest rewards - even though they probably could be given as quest rewards without crashing with the current game mod. Also, each bonus scroll is automatically linked to the level they are in, so there will be one and only one bonus scroll per level.

### bonus_rewards
Includes the rupees rewards of the bonus minigame scrolls in the pool.

### race_rewards
Includes the 100 rupees rewards of the Rudy races in the pool.

### trading_sequence
This variable can take many values, as explained here.

#### excluded
This means that the trading sequence will only put the Fort Findula Dungeon Key, the Sacred Oil and Refined Chains and the Chainsword in the pool. The locations that will be put in the pool are both the moose Alven's interaction (the first one being always present, and the second being when offered the Sacred Oil and Chains), as well as the vanilla Sacred Oil location at the end of the Fort Findula Dungeon.

In other words, talking to Alven once will give you random item, talking to Alven with the Sacred Oil and Refined Chains will give you a random item, and going to the end of the Fort Findula Dungeon will give you a random item. Every other NPC interaction in the sequence will ask for an item that you cannot obtain, and will therefore be foolish. This also mean that whatever item that will get attributed to Zazie's Soul Upgrade location will never be obtainable.

#### included
This will include all items in the Chainsword trading sequence, starting with the Fort Findula Dungeon Key to the Chainsword. The game has been modified so you can hold multiple items of the trading sequence at the same time, but they might not show up in the inventory.

#### vanilla
Activating the vanilla flag will lock all items in the trading sequence to their vanilla locations, including the Chainsword, except for the Fort Findula Dungeon Key. The only location included in the pool will be Alven's first interaction.

In other words, talking to Alven once will give you random item. Finding the Fort Findula Dungeon Key will kickstart the trading sequence, which will always lead to the Chainsword in the end.

## enemy_spawn
This would theoretically spawn random enemies instead of their vanilla placement. This is not currently implemented since the logic rules include red/blue enemies placement.

# Logic rules game assumptions

Daimur has been modified to only take damage if you have collected the 5 Jewel Shards and has the Purple Magic, as opposed to the default vanilla game that only requires Purple Magic.

The trading sequence has been modified so you can hold multiple items from it at a time. If this is not the case, we can still include flag "excluded" and "vanilla" in the config file.

An extra location for the Bombs has been coded in (preferably at the start of Forest or Faramore). Bombs cannot spawn in the shop nor in item bags until the Bombs have been collected first at their assigned location.

All keys are non-fungible (unique). They technically are in the vanilla game, but there is no actual way of knowing which one you collect except by going to the appropriate location and test it. A modification of the key sprites might be needed before activating the inclusion of the keys in the item pool.

All items in the trading sequence can be held simultaneously. This is not the case in the vanilla game.

Cypress' spawning rules in Faramore is changed to having given his the Citizenship Papers in Forest. In the vanilla game, this requirement is only obtaining the Lantern.

NPC spawn rules are local. For example, Cypress needs you to have the Lantern for him to spawn in Faramore. If Cypress' randomised location is now in Caves, then this Caves location will be left empty until you get the Lantern.

NPC requirements are local. For example, Cypress needs 3 plants to give the Lamp Oil Upgrade in Faramore. If Cypress' randomised location is now in Caves, then he will be there, but still ask for 3 plants to give an item.

Enemy spawns are not randomised for now.


# Logic rules caveats

Since NPC, the Hills Keys and quest items (Plants, Rocks, Compass and Bell) have local requirements, we cannot implement a logic rule to their location before they are assigned.

For the NPC, we do their assignment first, which will then dictate the rule for the location of interacting with them. This is mandatory since we cannot know the logic rules of an NPC interaction location before knowing where this NPC is.

For the objects, we assume that going to their location allows for their collection without considering their spawning equirements - which will be the case for Archipelago anyway. To fix this, we include the spawning requirements in *every* logic rules that expect to have those items in the collection state. This won't be Archipelago compatible - since if those item are in another world, they won't care about your spawning requirements unless such requirements are an item in itself - but even then it would only make the logic stricter than necessary.


# TODO

Merge NPC pool and item pool so thw former can spawn in the latter (level_location except Jewel and Beacon) and vice-versa.

We need to clean vanilla.csv (comments, useless rows like "Default_Beacon", etc.)