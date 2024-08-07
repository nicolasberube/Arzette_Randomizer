# Arzette Randomizer

This is a randomizer for Arzette: The Jewel of Faramore. It generates a .csv that is used as an input by a modified build of the game. It also generates a .txt file that identifies checks in order and helps with debugging or getting unstuck.

Note that the code is *not* currently Archipelago compatible. I tried my best to make a possible future Achipelago port as smooth as possible, while still keeping the code as simple as possible and not relying on the Archipelago libraries. I guess by doing so, I upheld Larry David's quote of "A good compromise is when both parties are dissatisfied".

Download the latest release on this page. You can view installation instructions here: [Link TBD]

# Configuration options

## level_order
This variable can take many values, as explained here.

#### random
Each beacon will still unlock the same number of levels. However, the unlocked levels will be random. The two levels that are unlocked at the start of the game will also be randomized. Be careful that activating this might lock the store away for a while, and force the player to farm bags to get power stones.

#### faramore
Each beacon will still unlock the same number of levels. However, the unlocked levels will be random. One of the two levels that are unlocked at the start of the game will also be randomized, Faramore being always unlocked. This helps with giving the player early access to the store to avoid farming bags.

#### vanilla
Each beacon will unlock the same levels. Note that depending on the beacons flag, those beacon could be at a random location.

## barrier_types
Will randomize the different barrier types. In other words, all barriers of a certain type will be changed to another type.

## NPC

## item_pool

Those options decide which item types to include in the item pool to randomize.

### npc
Include NPCs in the pool. NPCs cannot spawn from other NPCs (quest item locations) or by hitting rocks (rocks locations).

### bags
Include bags in the pool

### keys
Include keys in the pool. This does not include quest items like the Fort Findula Dungeon Key. This also does not include the Key in Lichen Hills.

### hills_key
Include the key to the barn from Lichen Hills in the pool. This key is treated differently since you need to play the Fatal Flute to spawn the Key. However, you cannot know where the key is before playing the Flute. Once would need to know every location check in the game, and play the Flute next to them if they are empty. The only other empty location would be the Shield Ring if you already collected the Reflector Ring.

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

### beacons
Includes the beacons location in the pool. Not to be confused with level_order, which decides which level is unlocked by hitting the beacon.

### jewels
Includes the Faramore jewel shards in the pool. This means that beating the bosses might not be required, and you could find jewel shards anywhere.

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

## logic

### tricky_jumps

Will permit some tricky jumps and techniques in logic. Nothing too hard, but maybe hard to find.

### no_lantern

Will permit going through dark rooms and dark bonus rooms without the lantern in logic.

### damage_boost

Will permit damage boosting to an extent where it would be possible in casual mode with health drops. Deactivating this means you could do logic without taking any damage.

# Game mod assumptions

Here are a list of the main modifications of the vanilla game to allow for a randomizer mod:

- Daimur has been modified to only take damage if you have collected the 5 Jewel Shards and has the Purple Magic, as opposed to the default vanilla game that only requires Purple Magic.

- An extra location for the Bombs has been coded in at the start of Forest. Bombs cannot spawn in the shop nor in item bags until the Bombs have been collected first at their assigned location.

- All keys are non-fungible (unique). They technically are in the vanilla game, but there is no actual way of knowing which one you collect except by going to the appropriate level and look for it in the bottom right corner - and test the specific door if there are multiple keys in the level. A modification of the key sprites has been done to accomodate this.

- All items in the trading sequence can be held simultaneously. This is not the case in the vanilla game. However, the trading quest menu will be glitched, so one has to remember which item have been collected - unless using the "vanilla" or "excluded" option for trading_sequence.

- All items can now be collected in the world. This includes NPC quest rewards, jewel shards, and rocks, which now spawn next to their spawner instead of in Arzette's inventory.

- NPC spawn rules are deactivated. Some NPCs need a prerequisite to spawn - Cypress in Faramore needing the lantern, Fairy needing to hit the switches. Those have been deactivated, and every NPC should spawn by default.

- NPC requirements are local. For example, normally, Cypress needs 3 plants to give the Lamp Oil Upgrade in Faramore. If Cypress' randomized location is now in Caves, then he will be there, but still ask for 3 plants to give an item.

- NPC requirements have been locked behind an appropriate order activation. For example, if you already have rocks before talking to Faramore Munhum, the rock quest will still be activated appropriately instead of being already completed. If you already have the Sacred Oil and Chains before talking to Alven, he will give you his first item (Fort Findula Dungeon Key in vanilla) before the Chainsword reward. If you already have 250 souls, Zazie will still ask for Sacred Oil before activating the souls quest, and so on.

- Faramore NPC that provide quests cannot be spawned from other objects (NPCs or Bonus scrolls). This might create glitches.

# Logic rules coding caveats

Since NPCs, the Hills Keys and quest items (Plants, Rocks, Compass and Bell) have local requirements, we cannot implement a logic rule to their location before they are assigned.

For the NPC, we do their assignment first, which will then dictate the rule for the location of interacting with them. This is mandatory since we cannot know the logic rules of an NPC interaction location before knowing where this NPC is.

For the objects, we assume that going to their location allows for their collection without considering their spawning equirements - which will be the case for Archipelago anyway. To fix this, we include the spawning requirements in *every* logic rules that expect to have those items in the collection state. This won't be Archipelago compatible - since if those item are in another world, they won't care about your spawning requirements unless such requirements are an item in itself - but even then it would only make the logic stricter than necessary.


# TODO

A lot of terrible code stems from iterating on the design, especially the treatment of NPCs. We need to group set_rules() and set_rules_quests() in a single function, as well as get_npc() and get_location(). Also, comment the code and split up functions into digestable chunks. This would also mean harmonizing the way npcs and bonus scrolls work. One work by checking the parent's access state through a dictionary, the other by treating the spawner as a collected item. Obviously the second way is better. We should also use sub function for common logic check (item refills for bombs and fatal flute, colored poulture and boarfoon combat, etc.), or maybe implement the Archipelago Region class to simplify this?

Explain how to start the randomizer and generate .csv file.
