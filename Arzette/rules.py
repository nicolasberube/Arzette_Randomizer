from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item, add_rule
from BaseClasses import CollectionState
if TYPE_CHECKING:
    from . import ArzetteWorld

def has_color(color, state: CollectionState, world: "ArzetteWorld"):
    if color == "Red":
        return state.has_group("magic", world.player)
    elif color == "Blue":
        return state.has_group("magic", world.player) and state.has_group("blue", world.player)
    elif color == "Purple":
        return state.has_group("magic", world.player) and state.has("Purple Magic", world.player)
    elif color == "Gauntlet":
        return state.has("Bomb Gauntlet", world.player) and has_shop(state, world)
    elif color == "Flute":
        return state.has("Fatal Flute", world.player) and has_shop(state, world)
    else:
        raise Exception(f"Invalid color {color}")

def has_barrier(barrier_type: str, state: CollectionState, world: "ArzetteWorld") -> bool:
    return has_color(world.barrier_types[barrier_type], state, world)

def has_shop(state: CollectionState, world: "ArzetteWorld"):
    return (state.has_group("bags", world.player) or
            state.has(world.level_beacons["Faramore"], world.player))

def has_bombs(state: CollectionState, world: "ArzetteWorld"):
    return (state.has_group("bombs", world.player) and has_shop(state, world))

def has_lantern(state: CollectionState, world: "ArzetteWorld"):
    return ((state.has("Lantern", world.player) and has_shop(state, world)) or
            world.options.no_lantern)

def has_cloak(state: CollectionState, world: "ArzetteWorld"):
    return (state.has("Magic Cloak", world.player) and has_shop(state, world))

def can_pass_boarfoon(color: str, state: CollectionState, world: "ArzetteWorld"):
    return (has_color(color, state, world) or state.has("Griffin Boots", world.player) or
            state.has("Reflector Ring", world.player) or has_cloak(state, world) or
            world.options.damage_boost)

def can_pass_poulture(color: str, state: CollectionState, world: "ArzetteWorld"):
    return (has_color(color, state, world) or state.has("Fatal Flute", world.player) or
            has_cloak(state, world) or world.options.damage_boost)

# This supposes that the world class has barrier_types and level_beacons attributes
# Maybe treat those as events instead of functions?

def set_location_rules(world: "ArzetteWorld") -> None:
    player = world.player
    options = world.options

    # Faramore Rules

    add_rule(world.get_location("Faramore Key (Well)"), lambda state:
        state.has("Faramore Key (Well)", player) or state.has("Faramore Key (Tavern)", player) or
        state.has("Griffin Boots", player))

    for item in ["Faramore Bonus", "Faramore Candle (Empty House)", "Faramore Maki"]:
        add_rule(world.get_location(item), lambda state:
            ((state.has("Faramore Key (Well)", player) or state.has("Faramore Key (Tavern)", player)) and
             (has_barrier("Blue", state, world) or (state.has("Winged Belt", player) and options.tricky_jumps))) or
            state.has("Griffin Boots", player))

    for item in ["Faramore Kari Quest", "Faramore Barnabuss"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Faramore Key (Well)", player) or state.has("Faramore Key (Tavern)", player) or
            state.has("Griffin Boots", player))

    add_rule(world.get_location("Faramore Payop"), lambda state:
        ((state.has("Faramore Key (Well)", player) or state.has("Faramore Key (Tavern)", player)) and
         has_barrier("Red", state, world)) or
        state.has("Griffin Boots", player))

    for item in ["Faramore Dewey", "Faramore Coin"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Griffin Boots", player) and has_barrier("Purple", state, world))
    # Purple Magic requirement for Dewey has been deactivated in the mod.

    add_rule(world.get_location("Faramore Candle (Cypress House)"), lambda state:
        state.has("Griffin Boots", player) and
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world))

    for item in ["Faramore Denny", "Faramore Cypress"]:
        add_rule(world.get_location(item), lambda state: state.has("Griffin Boots", player))

    add_rule(world.get_location("Faramore Rudy"), lambda state:
        state.has_group("bombs", player))

    # Forest Rules
    for item in ["Forest Coin", "Forest Bag (Sword Wave)", "Golden Fly", "Sword Wave",
            "Forest Bag (Last Room)", "Forest Beacon", "Forest Jewel", "Magic Armor",
            "Forest Cypress"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Forest Key", player) or state.has("Griffin Boots", player))
    add_rule(world.get_location("Forest Rudy (End)"), lambda state:
        state.has("Forest Key", player) or
        (state.has("Griffin Boots", player) and options.tricky_jumps))

    add_rule(world.get_location("Golden Fly"), lambda state:
        has_bombs(state, world) and has_barrier("Red", state, world))
    add_rule(world.get_location("Forest Jewel"), lambda state:
        state.has_group("candles", player, 17))
    add_rule(world.get_location("Magic Armor"), lambda state:
        state.has_group("candles", player, 20) and has_barrier("Gauntlet", state, world))
    for item in ["Sword Wave", "Forest Bag (Sword Wave)"]:
        add_rule(world.get_location(item), lambda state: has_lantern(state, world))

    add_rule(world.get_location("Forest Candle (Tree)"), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location("Forest Candle (Cypress)"), lambda state:
        state.has("Griffin Boots", player))

    # Caves Rules
    for item in ["Silver Cricket", "Rope Ladder", "Caves Bag (Rope Ladder)",
            "Caves Candle (First Dark Room)", "Caves Coin",
            "Caves Candle (Second Dark Room)", "Caves Bonus", "Shield Ring",
            "Caves Bag (Last Room)", "Caves Ellido"]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world))

    for item in ["Caves Candle (First Dark Room)", "Caves Coin",
            "Caves Candle (Second Dark Room)", "Caves Bonus", "Shield Ring",
            "Caves Bag (Last Room)", "Caves Ellido"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    for item in ["Silver Cricket", "Rope Ladder",
            "Caves Bag (Rope Ladder)", "Caves Ellido"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Blue", state, world))

    for item in ["Rope Ladder", "Caves Bag (Rope Ladder)"]:
        add_rule(world.get_location(item), lambda state:
             has_barrier("Purple", state, world))

    add_rule(world.get_location("Caves Candle (First Dark Room)"), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location("Caves Coin"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player))

    # Desert Rules
    add_rule(world.get_location("Desert Key"), lambda state:
        has_bombs(state, world) or
        ((state.has("Griffin Boots", player) or
          (state.has("Winged Belt", player) and state.has("Speedy Shoes", player))) and
         has_barrier("Red", state, world) and
         options.tricky_jumps))

    for item in ["Desert Key", "Desert Candle (Last Room)", "Desert Life-Up",
            "Desert Bag (Last Room)", "Desert Beacon", "Desert Fairy"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    for item in ["Desert Candle (Last Room)", "Desert Life-Up",
            "Desert Bag (Last Room)", "Desert Beacon", "Desert Fairy"]:
        add_rule(world.get_location(item), lambda state: state.has("Desert Key", player))

    add_rule(world.get_location("Desert Candle (Last Room)"), lambda state:
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world))

    add_rule(world.get_location("Desert Life-Up"), lambda state:
        state.has_group("candles", player, 20))

    add_rule(world.get_location("Desert Beacon"), lambda state:
        has_barrier("Red", state, world) or
        (state.has("Griffin Boots", player) and options.tricky_jumps))

    # Canyon Rules
    add_rule(world.get_location("Canyon Bonus"), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location("Canyon Candle (First Room End)"), lambda state:
        (state.has("Speedy Shoes", player) and state.has("Winged Belt", player)) or
        state.has("Griffin Boots", player))

    for item in ["Canyon Jewel", "Canyon Crowdee"]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("candles", player, 20) and
            can_pass_boarfoon("Red", state, world))

    for item in ["Canyon Key", "Canyon Bag (After Zipline 1)",
            "Canyon Bag (After Zipline 2)", "Canyon Bag (After Zipline 3)",
            "Canyon Coin", "Canyon Bag (Motte House)", "Canyon Candle (Motte House)",
            "Canyon Motte", "Canyon Odie"]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world) and has_lantern(state, world))

    for item in ["Canyon Candle (Motte House)", "Canyon Motte", "Canyon Odie"]:
        add_rule(world.get_location(item), lambda state: state.has("Canyon Key", player))

    for item in ["Canyon Candle (Motte House)", "Canyon Odie"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) or
            state.has("Griffin Boots", player))

    add_rule(world.get_location("Canyon Candle (Motte House)"), lambda state:
        has_barrier("Blue", state, world))

    # Swamp Rules
    for item in ["Swamp Candle (First Room)", "Swamp Bag (First Room)", "Swamp Coin",
            "Swamp Key (Frich House)", "Swamp Candle (Frich House)",
            "Swamp Frich", "Swamp Glubbert"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Red", state, world))

    for item in ["Swamp Key (Griffin Boots)", "Griffin Boots", "Swamp Plant",
            "Swamp Bonus", "Swamp Beacon"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world))

    for item in ["Swamp Candle (First Room)", "Swamp Bag (First Room)",
                    "Swamp Candle (Frich House)"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Griffin Boots", player))

    for item in ["Swamp Coin", "Swamp Key (Frich House)", "Swamp Candle (Frich House)",
            "Swamp Key (Griffin Boots)", "Griffin Boots", "Swamp Plant",
            "Swamp Bonus", "Swamp Beacon", "Swamp Glubbert"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Golden Fly", player))  # This is only because Frich is locked for now

    for item in ["Swamp Candle (Frich House)", "Swamp Key (Griffin Boots)",
            "Griffin Boots", "Swamp Plant", "Swamp Bonus", "Swamp Beacon",
            "Swamp Glubbert"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Swamp Key (Frich House)", player))

    add_rule(world.get_location("Swamp Key (Griffin Boots)"), lambda state:
        has_barrier("Blue", state, world))

    for item in ["Griffin Boots", "Swamp Plant", "Swamp Bonus"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Swamp Key (Griffin Boots)", player) or
            state.has("Griffin Boots", player) or
            has_barrier("Red", state, world))

    add_rule(world.get_location("Swamp Beacon"), lambda state:
        has_bombs(state, world))

    # Peak Rules
    add_rule(world.get_location("Peak Candle (First Cave)"), lambda state:
        has_barrier("Red", state, world) and has_barrier("Blue", state, world))

    for item in ["Peak Bag (First Cave 1)",
            "Peak Bag (First Cave 2)", "Peak Bonus", "Peak Coin"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) and
            can_pass_boarfoon("Red", state, world))

    for item in ["Peak Rudy (End)", "Peak Key",
            "Peak Candle (Ciclena Cave)", "Peak Bag (Before Apatu)",
            "Peak Jewel", "Peak Bag (After Apatu)", "Peak Ciclena"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) and
            can_pass_boarfoon("Red", state, world) and
            can_pass_poulture("Red", state, world))

    for item in ["Peak Rudy (End)", "Peak Coin", "Peak Key",
            "Peak Candle (Ciclena Cave)", "Peak Bag (Before Apatu)",
            "Peak Jewel", "Peak Bag (After Apatu)", "Peak Ciclena"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location("Peak Coin"), lambda state:
        has_barrier("Purple", state, world))

    add_rule(world.get_location("Peak Ciclena"), lambda state:
        state.has("Peak Key", player))

    add_rule(world.get_location("Peak Candle (Ciclena Cave)"), lambda state:
        state.has("Peak Key", player) and state.has("Griffin Boots", player))

    for item in ["Peak Jewel", "Peak Bag (After Apatu)"]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("candles", player, 20))

    add_rule(world.get_location("Peak Bag (After Apatu)"), lambda state:
        state.has("Peak Jewel", player))

    # Crypts Rules
    for item in ["Crypts Life-Up", "Bell", "Crypts Bonus", "Crypts Key",
            "Crypts Bag (Crypt)", "Crypts Candle (After Crypt)", "Crypts Coin",
            "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)",
            "Crypts Skelvis"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Red", state, world))

    add_rule(world.get_location("Crypts Life-Up"), lambda state:
        has_bombs(state, world) and state.has_group("candles", player, 20) and
        state.has("Griffin Boots", player))

    add_rule(world.get_location("Bell"), lambda state:
        has_bombs(state, world) and
        (has_barrier("Blue", state, world) or
         (state.has_group("candles", player, 20) and state.has("Griffin Boots", player))))

    for item in ["Crypts Bonus", "Crypts Key", "Crypts Bag (Crypt)",
            "Crypts Candle (After Crypt)", "Crypts Coin",
            "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)", "Crypts Skelvis"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    for item in ["Crypts Candle (After Crypt)", "Crypts Coin",
            "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)", "Crypts Skelvis"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Crypts Key", player))
    
    add_rule(world.get_location("Crypts Candle (After Crypt)"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player))

    add_rule(world.get_location("Crypts Coin"), lambda state:
        has_barrier("Flute", state, world) and
        world.barrier_types["Flute"] == "Flute")

    for item in ["Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)", "Crypts Skelvis"]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world))

    add_rule(world.get_location("Crypts Candle (Skelvis)"), lambda state:
        has_barrier("Blue", state, world))

    add_rule(world.get_location("Crypts Bag (Skelvis)"), lambda state:
        has_barrier("Gauntlet", state, world))

    # Volcano Rules
    add_rule(world.get_location("Volcano Bonus"), lambda state:
        has_barrier("Gauntlet", state, world))

    for item in ["Volcano Candle (First Room)", "Volcano Coin",
            "Volcano Candle (Last Room)", "Crystal of Refraction"]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("magic", player) or options.tricky_jumps or
            options.damage_boost)

    add_rule(world.get_location("Volcano Coin"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player) or
        (state.has("Backstep", player) and options.tricky_jumps))

    # Beach Rules
    add_rule(world.get_location("Beach Key (First House)"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player))

    add_rule(world.get_location("Beach Coin"), lambda state:
        state.has("Griffin Boots", player) and
        has_barrier("Blue", state, world))

    for item in ["Beach Key (Tork Cabin)", "Beach Candle (Tork Cabin)", "Beach Plant",
            "Beach Bonus", "Beach Candle (Cave)", "Fatal Flute", "Beach Beacon",
            "Beach Fleetus", "Beach Tork"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Beach Key (First House)", player) and
            has_barrier("Blue", state, world))
            
    for item in ["Fatal Flute", "Beach Beacon"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Blue", state, world))

    add_rule(world.get_location("Beach Key (Tork Cabin)"), lambda state:
        state.has("Griffin Boots", player) or
        ((state.has_group("magic", player) or
          (state.has("Bombs", player) and options.tricky_jumps)) and
         (state.has("Winged Belt", player) or
          (state.has("Speedy Shoes", player) and options.tricky_jumps))))

    add_rule(world.get_location("Beach Candle (Tork Cabin)"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player))

    for item in ["Beach Plant", "Beach Bonus", "Beach Tork"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Beach Key (Tork Cabin)", player))

    add_rule(world.get_location("Beach Candle (Cave)"), lambda state:
        has_barrier("Flute", state, world) and
        (state.has("Griffin Boots", player) or state.has("Winged Belt", player)))

    add_rule(world.get_location("Fatal Flute"), lambda state:
        has_bombs(state, world))

    add_rule(world.get_location("Beach Beacon"), lambda state:
        state.has("Griffin Boots", player) or state.has_group("magic", player) or
        state.has("Winged Belt", player))

    # River Rules
    for item in ["River Bonus", "River Francine"]:
        add_rule(world.get_location(item), lambda state:
            state.has("River Key (Francine)", player))

    add_rule(world.get_location("River Candle (Boat)"), lambda state:
        state.has("Griffin Boots", player) or state.has("Winged Belt", player))

    for item in ["River Key (Francine)", "River Candle (Boat)",
            "River Key (Submarine)", "River Coin",
            "Blue Magic", "River Bag (Last Room)", "River Candle (Last Room)",
            "River Life-Up", "River Barnabuss", "River Morgh"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world))
    add_rule(world.get_location("River Key (Submarine)"), lambda state:
        has_barrier("Blue", state, world))
    add_rule(world.get_location("River Coin"), lambda state:
        has_barrier("Purple", state, world))

    for item in ["River Key (Submarine)", "River Coin",
            "Blue Magic", "River Bag (Last Room)", "River Candle (Last Room)",
            "River Life-Up", "River Morgh"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world) and has_bombs(state, world))

    add_rule(world.get_location("Blue Magic"), lambda state:
        has_barrier("Red", state, world))

    for item in ["River Bag (Last Room)",
            "River Candle (Last Room)", "River Life-Up", "River Morgh"]:
        add_rule(world.get_location(item), lambda state:
            state.has("River Key (Submarine)", player))
    add_rule(world.get_location("River Candle (Last Room)"), lambda state:
        state.has("Griffin Boots", player))
    add_rule(world.get_location("River Life-Up"), lambda state:
        state.has_group("candles", player, 20))

    # Hills Rules
    for item in ["Hills Candle (Cave)", "Lightning Sword"]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world) and has_lantern(state, world) and
            (can_pass_boarfoon("Blue", state, world) or state.has("Winged Belt", player)))
    add_rule(world.get_location("Lightning Sword"), lambda state:
        has_barrier("Red", state, world) and has_barrier("Blue", state, world))

    for item in ["Hills Coin", "Hills Bonus", "Hills Bag (Barn)", "Hills Key",
            "Hills Bag (Music Shrine)", "Hills Candle (Music Shrine)",
            "Hills Plant", "Hills Beacon", "Hills Rudy (End)", "Hills Milbert"]:
        add_rule(world.get_location(item), lambda state:
            (has_color("Blue", state, world) or
             has_cloak(state, world) or options.damage_boost) and
            (state.has("Griffin Boots", player) or state.has("Winged Belt", player)))

    for item in ["Hills Candle (Music Shrine)", "Hills Key"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Griffin Boots", player))

    add_rule(world.get_location("Hills Coin"), lambda state:
        has_color("Purple", state, world))

    for item in ["Hills Bag (Barn)", "Hills Key", "Hills Bag (Music Shrine)",
            "Hills Candle (Music Shrine)"]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world))

    for item in ["Hills Plant", "Hills Beacon", "Hills Milbert"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Hills Key", player) and state.has("Fatal Flute", player))

    # Fort Rules
    for item in ["Fort Bag (Dungeon 1)", "Fort Bag (Dungeon 2)", "Fort Bag (Dungeon 3)",
            "Fort Bag (Dungeon 4)", "Sacred Oil"]:
        add_rule(world.get_location(item), lambda state: state.has("Dungeon Key", player))

    for item in ["Fort Bag (Dungeon 1)", "Fort Bag (Dungeon 2)", "Fort Bag (Dungeon 3)",
            "Fort Bag (Dungeon 4)", "Sacred Oil", "Fort Candle (Dark Room)",
            "Fort Bag (Dark Room)"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location("Fort Key (First Room)"), lambda state:
        can_pass_poulture("Red", state, world))

    add_rule(world.get_location("Enchanted Shoes"), lambda state:
        has_barrier("Flute", state, world))

    for item in ["Enchanted Shoes", "Fort Coin", "Fort Key (Top Room)",
            "Fort Bag (Top Room 1)", "Fort Bag (Top Room 2)", "Fort Bag (Top Room 3)",
            "Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
            "Fort Jewel", "Fort Bonus"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Griffin Boots", player) and state.has("Fort Key (First Room)", player))

    for item in ["Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
            "Fort Jewel", "Fort Bonus"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Fort Key (Top Room)", player) and
            has_barrier("Blue", state, world))

    for item in ["Fort Bag (Last Room)", "Reflector Ring",
            "Fort Jewel", "Fort Bonus"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world))
    add_rule(world.get_location("Reflector Ring"), lambda state:
        has_barrier("Gauntlet", state, world))

    for item in ["Fort Jewel", "Fort Bonus"]:
        add_rule(world.get_location(item), lambda state:
                state.has_group("candles", player, 20))
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Blue", state, world))

    add_rule(world.get_location("Fort Bonus"), lambda state:
        state.has("Fort Jewel", player))

    # Castle Rules
    add_rule(world.get_location("Castle Bag (Entrance)"), lambda state:
        state.has("Griffin Boots", player))

    for item in ["Castle Candle (Right Room)",
            "Castle Key (Nodelki)", "Castle Candle (Top Room)", "Castle Bag (Top Room)",
            "Winged Belt", "Castle Coin", "Castle Key (Left Room)", "Castle Bag (Bonus)",
            "Castle Bonus", "Castle Jewel"]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location("Castle Candle (Right Room)"), lambda state:
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world) and
        state.has("Griffin Boots", player) and
        can_pass_poulture("Red", state, world))

    add_rule(world.get_location("Castle Key (Nodelki)"), lambda state:
        (has_barrier("Red", state, world) and
         (state.has("Griffin Boots", player) or
          (has_barrier("Blue", state, world) and
           has_barrier("Gauntlet", state, world))) and
         (can_pass_poulture("Red", state, world) and
          can_pass_boarfoon("Blue", state, world))
        ) or
        (has_barrier("Blue", state, world) and
         has_barrier("Gauntlet", state, world) and
         state.has("Griffin Boots", player)
        ))

    add_rule(world.get_location("Castle Candle (Top Room)"), lambda state:
        state.has("Griffin Boots", player) and
        (has_barrier("Red", state, world) and
         can_pass_poulture("Red", state, world)) or
        (has_barrier("Blue", state, world) and
         has_barrier("Gauntlet", state, world)))

    for item in ["Castle Bag (Top Room)", "Castle Jewel"]:
        add_rule(world.get_location(item), lambda state:
            (has_barrier("Red", state, world) and
             (state.has("Griffin Boots", player) or
              has_barrier("Blue", state, world)) and
             (has_bombs(state, world) or
              has_barrier("Gauntlet", state, world)) and
             (can_pass_poulture("Red", state, world) and
              can_pass_boarfoon("Blue", state, world))
            ) or
            (has_barrier("Blue", state, world) and
             state.has("Griffin Boots", player) and
             (has_barrier("Gauntlet", state, world) or
              can_pass_poulture("Blue", state, world))))

    for item in ["Winged Belt", "Castle Coin", "Castle Key (Left Room)",
            "Castle Bag (Bonus)", "Castle Bonus"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Blue", state, world) and
            ((has_barrier("Red", state, world) and
              (has_bombs(state, world) or has_barrier("Gauntlet", state, world)) and
              can_pass_poulture("Red", state, world) and
              can_pass_boarfoon("Blue", state, world)
              ) or
              (state.has("Griffin Boots", player) and 
               (has_barrier("Gauntlet", state, world) or
                can_pass_poulture("Blue", state, world)))
            ))
    add_rule(world.get_location("Winged Belt"), lambda state:
        (state.has("Griffin Boots", player) or state.has("Winged Belt", player)) and
        state.has_group("candles", player, 20) and
        has_barrier("Flute", state, world))

    add_rule(world.get_location("Castle Jewel"), lambda state:
        state.has_group("candles", player, 20) and
        state.has("Castle Key (Nodelki)", player))

    for item in ["Castle Bag (Bonus)", "Castle Bonus"]:
        add_rule(world.get_location("Castle Bonus"), lambda state:
            state.has("Castle Key (Left Room)", player))

    # Lair Rules
    add_rule(world.get_location("Lair Candle (Tree Trunk)"), lambda state:
        has_bombs(state, world))

    add_rule(world.get_location("Lair Candle (Tree Top)"), lambda state:
        state.has("Griffin Boots", player) and
        ((has_bombs(state, world) and has_barrier("Flute", state, world)) or
         (has_barrier("Purple", state, world) and
          state.has("Speedy Shoes", player) and state.has("Winged Belt", player)) and
          can_pass_poulture("Red")))

    for item in ["Lair Bonus",
        "Lair Bag (First Room)", "Lair Coin", "Lair Bag (Lava Room)",
        "Lair Bag (Final Room 1)", "Lair Bag (Final Room 2)",
        "Lair Bag (Final Room 3)", "Daimur"]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Purple", state, world))
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Blue", state, world) or
            (state.has("Griffin Boots", player) and state.has("Winged Belt", player) and
             has_barrier("Flute", state, world)))

    for item in ["Lair Bag (Final Room 2)", "Daimur"]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world) or
            has_barrier("Gauntlet", state, world))

    for item in ["Lair Bonus", "Lair Bag (First Room)", "Lair Coin"]:
        add_rule(world.get_location(item), lambda state:
            state.has("Griffin Boots", player))
    add_rule(world.get_location("Lair Coin"), lambda state:
        has_lantern(state, world))

    for item in ["Lair Bag (Lava Room)",
            "Lair Bag (Final Room 1)", "Lair Bag (Final Room 2)",
            "Lair Bag (Final Room 3)", "Daimur"]:
        add_rule(world.get_location(item), lambda state:
            (state.has("Griffin Boots", player) or state.has("Winged Belt", player)) and
            has_lantern(state, world))

    # The jewels rule is not in vanilla game and should be added
    add_rule(world.get_location("Daimur"), lambda state:
        state.has("Purple Magic", player) and state.has_group("jewels", player, 5))
