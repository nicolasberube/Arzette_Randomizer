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
Include keys in the pool. This does not include quest items like the Fort Findula Dungeon Key.

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
Includes the bonus minigame scrolls location in the pool. This is not implemented yet, since we need to separate locations in the world and locations as rewards. Doing this would make including NPCs in the general item pool possible.

### bonus_rewards
Includes the rupees rewards of the bonus minigame scrolls in the pool.

### race_rewards
Includes the 100 rupees rewards of the Rudy races in the pool.

### trading_sequence
Deactivating the inclusion of the trading squence means that the Sacred Oil location at the end of the Fort's Dungeon will be included in the pool, as well as the Sacred Oil and Refined Chains item. All other locations in the trading sequence are gonna remain vanilla, except for the Morgh reward (the vanilla Sacred Oil and Refined Chains item) which will be replaced with the Sacred Oil item. In other words, all other locations in the trading sequence will be inaccessible.

This means that the Soul Upgrade location will also be inaccessible, since it is normally available after starting the trading sequence.

## enemy_spawn
This would theoretically spawn random enemies instead of their vanilla placement. This is not currently implemented since the logic rules include red/blue enemies placement.

# Logic rules assumptions
Daimur has been modified to only take damage if you have collected the 5 Jewel Shards and has the Purple Magic, as opposed to the default vanilla game that only requires Purple Magic.

All keys are non-fungible (unique). They technically are in the vanilla game, but there is no actual way of knowing which one you collect except by going to the appropriate location and test it. A modification of the key sprites might be needed before activating the inclusion of the keys in the item pool.

NPC spawn rules are local. For example, Cypress needs you to have the Lantern for him to spawn in Faramore. If Cypress' randomised location is now in Caves, then this Caves location will be left empty until you get the Lantern.

NPC requirements are local. For example, Cypress needs 3 plants to give the Lamp Oil Upgrade in Faramore. If Cypress' randomised location is now in Caves, then he will be there, but still ask for 3 plants to give an item.

Enemy spawns are not randomised for now.