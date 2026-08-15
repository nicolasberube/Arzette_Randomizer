# Arzette Randomizer

This is a randomizer for Arzette: The Jewel of Faramore. This repository includes both the currently maintained [Archipelago randomizer](arzette/), as well as the deprecated [standalone randomizer](Standalone/).

It is only available for the Windows Steam version of the game.

# [Setup Guide](arzette/docs/setup_en.md)

How to set up the client on your computer.

# [Randomizer Information](arzette/docs/en_Arzette.md)

Various information about the randomizer, differences with the vanilla game, bugs, techniques, etc.

# Future plans

- Race Rewards logic seems broken and needs to be tested. Possibly same with Calendar.
- Logic/Options changes
    - Implement Canteen as the alternative to damage_boost option.
    - Implement Magic Cloak as Power Pendant alternative.
    - Add [Bonus Scroll level warp bug](arzette/en_Arzette.md#known-bugs) trick in logic.
    - Investigate the high generation failure rate for the level_order = faramore or shuffle + shuffle_beacon = False combination.
- A way to find where some key NPCs are without looking at the spoiler log (Faramore Munhum, Forest Cypress)
- A way to fix the [Shield Ring not spawning bug](arzette/en_Arzette.md#known-bugs).
- Clean slot_data. Most of universal_tracker_info could be reconstructed from unpingable_locations
- WebWorld and Poptracker support?

# CREDITS

- APworld Development - Lightmopp
- Game Client - Dopply
- Support and Tests - g0goTBC
- Play Testing - JustCallMeGio, RoobyRoo, Dynomation, FinalFlame, Vicas
