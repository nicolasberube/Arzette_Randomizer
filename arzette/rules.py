from typing import TYPE_CHECKING
from .locations import rock_locations, bonusreward_locations, all_locations, all_levels
from .Names import itemName, locName

from worlds.generic.Rules import set_rule, forbid_item, add_rule
from BaseClasses import CollectionState
if TYPE_CHECKING:
    from . import ArzetteWorld

level_to_locations = {
    level: [location for location, locdata in all_locations.items()
            if locdata.spawn_from == level]
    for level in all_levels
}

def has_color(color, state: CollectionState, world: "ArzetteWorld"):
    if color == "Red":
        return state.has_group("magic", world.player)
    elif color == "Blue":
        return state.has_group("magic", world.player) and state.has_group("blue", world.player)
    elif color == "Purple":
        return state.has_group("magic", world.player) and state.has(itemName.PurpleMagic, world.player)
    elif color == "Gauntlet":
        return state.has(itemName.BombGauntlet, world.player) and has_shop(state, world)
    elif color == "Flute":
        return state.has(itemName.FatalFlute, world.player) and has_shop(state, world)
    else:
        raise Exception(f"Invalid color {color}")

def level_access(level: str, state: CollectionState, world: "ArzetteWorld"):
    beacon = world.level_beacons[level]
    if beacon == "Default Beacon":
        return True
    return state.has(beacon, world.player)

def has_barrier(barrier_type: str, state: CollectionState, world: "ArzetteWorld") -> bool:
    return has_color(world.barrier_types[barrier_type], state, world)

def has_enemy(state: CollectionState, world: "ArzetteWorld") -> bool:
    return (state.has(itemName.ForestBonus, world.player) or
            state.has(itemName.CanyonBonus, world.player) or
            state.has(itemName.SwampBonus, world.player) or
            state.has(itemName.PeakBonus, world.player) or
            state.has(itemName.CryptsBonus, world.player) or
            state.has(itemName.BeachBonus, world.player) or
            state.has(itemName.RiverBonus, world.player) or
            (state.has(itemName.HillsBonus, world.player) and state.has(itemName.GriffinBoots, world.player)) or
            state.has(itemName.FortBonus, world.player) or
            state.has(itemName.LairBonus, world.player) or
            level_access("Forest", state, world) or
            level_access("Desert", state, world) or
            level_access("Canyon", state, world) or
            (level_access("Swamp", state, world) and world.options.tricky_jumps.value) or
            level_access("Peak", state, world) or
            (level_access("Crypts", state, world) and state.has(itemName.PowerPendant, world.player)) or
            level_access("Volcano", state, world) or
            level_access("Beach", state, world) or
            level_access("River", state, world) or
            (level_access("Hills", state, world) and state.has(itemName.GriffinBoots, world.player)) or
            (level_access("Fort", state, world) and state.has(itemName.PowerPendant, world.player)) or
            (level_access("Lair", state, world) and state.has(itemName.PowerPendant, world.player) and 
                state.has(itemName.GriffinBoots, world.player))
            )

def has_money(state: CollectionState, world: "ArzetteWorld") -> bool:
    # Caves, Castle and Lair need bombs and/or magic, which need money
    return (has_enemy(state, world) or
            state.has(itemName.FaramoreBonus, world.player) or
            state.has(itemName.DesertBonus, world.player) or
            state.has(itemName.VolcanoBonus, world.player) or
            state.has(itemName.CastleBonus, world.player))

def has_shop(state: CollectionState, world: "ArzetteWorld") -> bool:
    return (state.has_group("bags", world.player) or
            (level_access("Faramore", state, world) and has_money(state, world)))

def has_bombs(state: CollectionState, world: "ArzetteWorld") -> bool:
    return (state.has_group("bombs", world.player) and has_shop(state, world))

def has_lantern(state: CollectionState, world: "ArzetteWorld") -> bool:
    return ((state.has(itemName.Lantern, world.player) and has_shop(state, world)) or
            world.options.no_lantern.value)

def has_cloak(state: CollectionState, world: "ArzetteWorld") -> bool:
    return (state.has(itemName.MagicCloak, world.player) and has_shop(state, world))

def can_pass_boarfoon(color: str, state: CollectionState, world: "ArzetteWorld") -> bool:
    return (has_color(color, state, world) or state.has(itemName.GriffinBoots, world.player) or
            state.has(itemName.ReflectorRing, world.player) or has_cloak(state, world) or
            world.options.damage_boost.value)

def can_pass_poulture(color: str, state: CollectionState, world: "ArzetteWorld") -> bool:
    return (has_color(color, state, world) or state.has(itemName.FatalFlute, world.player) or
            has_cloak(state, world) or world.options.damage_boost.value)

def spawner_reach(spawner: str, state: CollectionState, world: "ArzetteWorld") -> bool:
    return world.get_location(world.early_lock[spawner]).can_reach(state)

def rock_quest(state: CollectionState, world: "ArzetteWorld"):
    return (spawner_reach(itemName.FaramoreMunhum, state, world) or
            state.has_group("rocks", world.player))

# This supposes that the world class has barrier_types, level_beacons and early_lock attributes
def set_location_rules(world: "ArzetteWorld") -> None:
    player = world.player
    options = world.options

    # Level access rules
    for level, locations in level_to_locations.items():
        for location in locations:
            add_rule(world.get_location(location), lambda state, level=level:
                level_access(level, state, world))
            if level in ["Crypts", "Fort", "Castle", "Lair"]:
                add_rule(world.get_location(location), lambda state:
                    state.has(itemName.PowerPendant, player))

    # Faramore Rules
    add_rule(world.get_location(locName.FaramoreKeyWell), lambda state:
        state.has(itemName.FaramoreKeyWell, player) or state.has(itemName.FaramoreKeyTavern, player) or
        state.has(itemName.GriffinBoots, player))

    for item in [locName.FaramoreBonus, locName.FaramoreCandleEmptyHouse, locName.FaramoreMaki]:
        add_rule(world.get_location(item), lambda state:
            ((state.has(itemName.FaramoreKeyWell, player) or state.has(itemName.FaramoreKeyTavern, player)) and
             (has_barrier("Blue", state, world) or (state.has(itemName.WingedBelt, player) and options.tricky_jumps.value))) or
            state.has(itemName.GriffinBoots, player))

    for item in [locName.FaramoreKariQuest, locName.FaramoreBarnabuss]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.FaramoreKeyWell, player) or state.has(itemName.FaramoreKeyTavern, player) or
            state.has(itemName.GriffinBoots, player))

    add_rule(world.get_location(locName.FaramorePayop), lambda state:
        ((state.has(itemName.FaramoreKeyWell, player) or state.has(itemName.FaramoreKeyTavern, player)) and
         has_barrier("Red", state, world)) or
        state.has(itemName.GriffinBoots, player))

    for item in [locName.FaramoreDewey, locName.FaramoreCoin]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GriffinBoots, player) and has_barrier("Purple", state, world))
    # Purple Magic requirement for Dewey has been deactivated in the mod.

    add_rule(world.get_location(locName.FaramoreCandleCypressHouse), lambda state:
        state.has(itemName.GriffinBoots, player) and
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world))

    for item in [locName.FaramoreDenny, locName.FaramoreCypress]:
        add_rule(world.get_location(item), lambda state: state.has(itemName.GriffinBoots, player))

    add_rule(world.get_location(locName.FaramoreRudy), lambda state:
        state.has_group("bombs", player))

    # Forest Rules
    for item in [locName.ForestCoin, locName.ForestBagSwordWave, locName.GoldenFly,
                 locName.SwordWave, locName.ForestBagLastRoom, locName.ForestBeacon,
                 locName.ForestJewel, locName.MagicArmor, locName.ForestCypress]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.ForestKey, player) or state.has(itemName.GriffinBoots, player))
    add_rule(world.get_location(locName.ForestRudyEnd), lambda state:
        state.has(itemName.ForestKey, player) or
        (state.has(itemName.GriffinBoots, player) and options.tricky_jumps.value))

    add_rule(world.get_location(locName.GoldenFly), lambda state:
        has_bombs(state, world) and has_barrier("Red", state, world))
    add_rule(world.get_location(locName.ForestJewel), lambda state:
        state.has_group("candles", player, 17))
    add_rule(world.get_location(locName.MagicArmor), lambda state:
        state.has_group("candles", player, 20) and has_barrier("Gauntlet", state, world))
    for item in [locName.SwordWave, locName.ForestBagSwordWave]:
        add_rule(world.get_location(item), lambda state: has_lantern(state, world))

    add_rule(world.get_location(locName.ForestCandleTree), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location(locName.ForestCandleCypress), lambda state:
        state.has(itemName.GriffinBoots, player))

    # Caves Rules
    for item in [locName.SilverCricket, locName.RopeLadder, locName.CavesBagRopeLadder,
                 locName.CavesCandleFirstDarkRoom, locName.CavesCoin,
                 locName.CavesCandleSecondDarkRoom, locName.CavesBonus,
                 locName.ShieldRing, locName.CavesBagLastRoom, locName.CavesEllido]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.Bombs, player) and has_shop(state, world))

    for item in [locName.CavesCandleFirstDarkRoom, locName.CavesCoin,
                 locName.CavesCandleSecondDarkRoom, locName.CavesBonus,
                 locName.ShieldRing, locName.CavesBagLastRoom, locName.CavesEllido]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    for item in [locName.SilverCricket, locName.RopeLadder,
                 locName.CavesBagRopeLadder, locName.CavesEllido]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Blue", state, world))

    for item in [locName.RopeLadder, locName.CavesBagRopeLadder]:
        add_rule(world.get_location(item), lambda state:
             has_barrier("Purple", state, world))

    add_rule(world.get_location(locName.CavesCandleFirstDarkRoom), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location(locName.CavesCoin), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player))

    # Desert Rules
    add_rule(world.get_location(locName.DesertKey), lambda state:
        has_bombs(state, world) or
        ((state.has(itemName.GriffinBoots, player) or
          (state.has(itemName.WingedBelt, player) and state.has(itemName.SpeedyShoes, player))) and
         has_barrier("Red", state, world) and
         options.tricky_jumps.value))

    for item in [locName.DesertKey, locName.DesertCandleLastRoom, locName.DesertLifeUp,
                 locName.DesertBagLastRoom, locName.DesertBeacon, locName.DesertFairy]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    for item in [locName.DesertCandleLastRoom, locName.DesertLifeUp,
                 locName.DesertBagLastRoom,locName.DesertBeacon, locName.DesertFairy]:
        add_rule(world.get_location(item), lambda state: state.has(itemName.DesertKey, player))

    add_rule(world.get_location(locName.DesertCandleLastRoom), lambda state:
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world))

    add_rule(world.get_location(locName.DesertLifeUp), lambda state:
        state.has_group("candles", player, 20) and
        has_barrier("Red", state, world))

    add_rule(world.get_location(locName.DesertBeacon), lambda state:
        has_barrier("Red", state, world) or
        (state.has(itemName.GriffinBoots, player) and options.tricky_jumps.value))

    # Canyon Rules
    add_rule(world.get_location(locName.CanyonBonus), lambda state:
        has_barrier("Red", state, world))

    add_rule(world.get_location(locName.CanyonCandleFirstRoomEnd), lambda state:
        (state.has(itemName.SpeedyShoes, player) and state.has(itemName.WingedBelt, player) and
         options.tricky_jumps.value) or
        state.has(itemName.GriffinBoots, player))

    for item in [locName.CanyonJewel, locName.CanyonCrowdee]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("candles", player, 20) and
            can_pass_boarfoon("Red", state, world))

    for item in [locName.CanyonKey, locName.CanyonBagAfterZipline1,
                 locName.CanyonBagAfterZipline2, locName.CanyonBagAfterZipline3,
                 locName.CanyonCoin, locName.CanyonBagMotteHouse,
                 locName.CanyonCandleMotteHouse, locName.CanyonMotte, locName.CanyonOdie]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world) and has_lantern(state, world))

    for item in [locName.CanyonCandleMotteHouse, locName.CanyonMotte, locName.CanyonOdie]:
        add_rule(world.get_location(item), lambda state: state.has(itemName.CanyonKey, player))

    for item in [locName.CanyonCandleMotteHouse, locName.CanyonOdie]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) or
            state.has(itemName.GriffinBoots, player))

    add_rule(world.get_location(locName.CanyonCandleMotteHouse), lambda state:
        has_barrier("Blue", state, world))

    # Swamp Rules
    for item in [locName.SwampCandleFirstRoom, locName.SwampBagFirstRoom,
                 locName.SwampCoin, locName.SwampKeyFrichHouse,
                 locName.SwampCandleFrichHouse, locName.SwampFrich, locName.SwampGlubbert]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Red", state, world))

    for item in [locName.SwampKeyGriffinBoots, locName.GriffinBoots, locName.SwampPlant,
                 locName.SwampBonus, locName.SwampBeacon]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world))

    for item in [locName.SwampCandleFirstRoom, locName.SwampBagFirstRoom,
                 locName.SwampCandleFrichHouse]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GriffinBoots, player))

    for item in [locName.SwampCoin, locName.SwampKeyFrichHouse,
                 locName.SwampCandleFrichHouse, locName.SwampKeyGriffinBoots,
                 locName.GriffinBoots, locName.SwampPlant, locName.SwampBonus,
                 locName.SwampBeacon, locName.SwampGlubbert]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GoldenFly, player))  # This is only because Frich is locked for now

    for item in [locName.SwampCandleFrichHouse, locName.SwampKeyGriffinBoots,
                 locName.GriffinBoots, locName.SwampPlant, locName.SwampBonus,
                 locName.SwampBeacon, locName.SwampGlubbert]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.SwampKeyFrichHouse, player))

    add_rule(world.get_location(locName.SwampKeyGriffinBoots), lambda state:
        has_barrier("Blue", state, world))

    for item in [locName.GriffinBoots, locName.SwampPlant, locName.SwampBonus]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.SwampKeyGriffinBoots, player) or
            state.has(itemName.GriffinBoots, player) or
            has_barrier("Red", state, world))
    add_rule(world.get_location(locName.SwampBonus), lambda state:
        state.has(itemName.GriffinBoots, player) or
        (state.has(itemName.WingedBelt, player) and state.has(itemName.SpeedyShoes, player) and
         options.tricky_jumps.value))

    add_rule(world.get_location(locName.SwampBeacon), lambda state:
        has_bombs(state, world))

    # Peak Rules
    add_rule(world.get_location(locName.PeakCandleFirstCave), lambda state:
        has_barrier("Red", state, world) and has_barrier("Blue", state, world))

    for item in [locName.PeakBagFirstCave1, locName.PeakBagFirstCave2,
                 locName.PeakBonus, locName.PeakCoin]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) and
            can_pass_boarfoon("Red", state, world))

    for item in [locName.PeakRudyEnd, locName.PeakKey, locName.PeakCandleCiclenaCave,
                 locName.PeakBagBeforeApatu, locName.PeakJewel, locName.PeakBagAfterApatu,
                 locName.PeakCiclena]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world) and
            can_pass_boarfoon("Red", state, world) and
            can_pass_poulture("Red", state, world))

    for item in [locName.PeakRudyEnd, locName.PeakCoin, locName.PeakKey,
                 locName.PeakCandleCiclenaCave, locName.PeakBagBeforeApatu,
                 locName.PeakJewel, locName.PeakBagAfterApatu, locName.PeakCiclena]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location(locName.PeakCoin), lambda state:
        has_barrier("Purple", state, world))

    add_rule(world.get_location(locName.PeakCiclena), lambda state:
        state.has(itemName.PeakKey, player))

    add_rule(world.get_location(locName.PeakCandleCiclenaCave), lambda state:
        state.has(itemName.PeakKey, player) and state.has(itemName.GriffinBoots, player))

    for item in [locName.PeakJewel, locName.PeakBagAfterApatu]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("candles", player, 20))

    add_rule(world.get_location(locName.PeakBagAfterApatu), lambda state:
        state.has(itemName.PeakJewel, player))

    # Crypts Rules
    for item in [locName.CryptsLifeUp, locName.Bell, locName.CryptsBonus, locName.CryptsKey,
                 locName.CryptsBagCrypt, locName.CryptsCandleAfterCrypt, locName.CryptsCoin,
                 locName.CryptsCandleSkelvis, locName.CryptsBagSkelvis, locName.CryptsSkelvis]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Red", state, world) and
            has_lantern(state, world))

    add_rule(world.get_location(locName.CryptsLifeUp), lambda state:
        has_bombs(state, world) and state.has_group("candles", player, 20) and
        state.has(itemName.GriffinBoots, player))

    add_rule(world.get_location(locName.Bell), lambda state:
        has_bombs(state, world) and
        (has_barrier("Blue", state, world) or
         (state.has_group("candles", player, 20) and state.has(itemName.GriffinBoots, player))))

    for item in [locName.CryptsCandleAfterCrypt, locName.CryptsCoin,
                 locName.CryptsCandleSkelvis, locName.CryptsBagSkelvis, locName.CryptsSkelvis]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.CryptsKey, player))

    add_rule(world.get_location(locName.CryptsCandleAfterCrypt), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player))

    add_rule(world.get_location(locName.CryptsCoin), lambda state:
        has_barrier("Flute", state, world) and (
            (world.barrier_types["Flute"] == "Flute") or
            ((world.barrier_types["Flute"] in ["Red", "Blue", "Purple"]) and
             (state.has(itemName.SwordWave, player)) and
             world.options.tricky_jumps.value)))

    for item in [locName.CryptsCandleSkelvis, locName.CryptsBagSkelvis, locName.CryptsSkelvis]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world))

    add_rule(world.get_location(locName.CryptsCandleSkelvis), lambda state:
        has_barrier("Blue", state, world))

    add_rule(world.get_location(locName.CryptsBagSkelvis), lambda state:
        has_barrier("Gauntlet", state, world))

    # Volcano Rules
    add_rule(world.get_location(locName.VolcanoBonus), lambda state:
        has_barrier("Gauntlet", state, world))

    for item in [locName.VolcanoCandleFirstRoom, locName.VolcanoCoin,
                 locName.VolcanoCandleLastRoom, locName.CrystalofRefraction]:
        add_rule(world.get_location(item), lambda state:
            state.has_group("magic", player) or options.tricky_jumps.value or
            options.damage_boost.value)

    add_rule(world.get_location(locName.VolcanoCoin), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player) or
        (state.has(itemName.Backstep, player) and options.tricky_jumps.value))

    # Beach Rules
    add_rule(world.get_location(locName.BeachKeyFirstHouse), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player))

    add_rule(world.get_location(locName.BeachCoin), lambda state:
        state.has(itemName.GriffinBoots, player) and
        has_barrier("Blue", state, world))

    for item in [locName.BeachKeyTorkCabin, locName.BeachCandleTorkCabin, locName.BeachPlant,
                 locName.BeachBonus, locName.BeachCandleCave, locName.FatalFlute,
                 locName.BeachBeacon, locName.BeachFleetus, locName.BeachTork]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.BeachKeyFirstHouse, player) and
            has_barrier("Blue", state, world))
            
    for item in [locName.FatalFlute, locName.BeachBeacon]:
        add_rule(world.get_location(item), lambda state:
            can_pass_boarfoon("Blue", state, world) or state.has(itemName.WingedBelt))

    add_rule(world.get_location(locName.BeachKeyTorkCabin), lambda state:
        state.has(itemName.GriffinBoots, player) or
        ((state.has_group("magic", player) or
          (state.has(itemName.Bombs, player) and has_shop(state, world) and options.tricky_jumps.value)) and
         (state.has(itemName.WingedBelt, player) or
          (state.has(itemName.SpeedyShoes, player) and options.tricky_jumps.value))))

    add_rule(world.get_location(locName.BeachCandleTorkCabin), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player))

    for item in [locName.BeachPlant, locName.BeachBonus, locName.BeachTork]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.BeachKeyTorkCabin, player))

    add_rule(world.get_location(locName.BeachCandleCave), lambda state:
        has_barrier("Flute", state, world) and
        (state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player)))

    add_rule(world.get_location(locName.FatalFlute), lambda state:
        has_bombs(state, world))

    add_rule(world.get_location(locName.BeachBeacon), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has_group("magic", player) or
        state.has(itemName.WingedBelt, player))

    # River Rules
    for item in [locName.RiverBonus, locName.RiverFrancine]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.RiverKeyFrancine, player))

    add_rule(world.get_location(locName.RiverCandleBoat), lambda state:
        state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player))

    for item in [locName.RiverKeyFrancine, locName.RiverCandleBoat,
                 locName.RiverKeySubmarine, locName.RiverCoin, locName.BlueMagic,
                 locName.RiverBagLastRoom, locName.RiverCandleLastRoom, locName.RiverLifeUp,
                 locName.RiverBarnabuss, locName.RiverMorgh]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world))
    add_rule(world.get_location(locName.RiverKeySubmarine), lambda state:
        has_barrier("Blue", state, world))
    add_rule(world.get_location(locName.RiverCoin), lambda state:
        has_barrier("Purple", state, world))

    for item in [locName.RiverKeySubmarine, locName.RiverCoin, locName.BlueMagic,
                 locName.RiverBagLastRoom, locName.RiverCandleLastRoom,
                 locName.RiverLifeUp, locName.RiverMorgh]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world) and has_bombs(state, world))

    add_rule(world.get_location(locName.BlueMagic), lambda state:
        has_barrier("Red", state, world))

    for item in [locName.RiverBagLastRoom, locName.RiverCandleLastRoom,
                 locName.RiverLifeUp, locName.RiverMorgh]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.RiverKeySubmarine, player))
    add_rule(world.get_location(locName.RiverCandleLastRoom), lambda state:
        state.has(itemName.GriffinBoots, player))
    add_rule(world.get_location(locName.RiverLifeUp), lambda state:
        state.has_group("candles", player, 20))

    # Hills Rules
    for item in [locName.HillsCandleCave, locName.LightningSword]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world) and has_lantern(state, world) and
            (can_pass_boarfoon("Blue", state, world) or state.has(itemName.WingedBelt, player)))
    add_rule(world.get_location(locName.LightningSword), lambda state:
        has_barrier("Red", state, world) and has_barrier("Blue", state, world))

    for item in [locName.HillsCoin, locName.HillsBonus, locName.HillsBagBarn,
                 locName.HillsKey, locName.HillsBagMusicShrine, locName.HillsCandleMusicShrine,
                 locName.HillsPlant, locName.HillsBeacon, locName.HillsRudyEnd, locName.HillsMilbert]:
        add_rule(world.get_location(item), lambda state:
            (has_color("Blue", state, world) or
             has_cloak(state, world) or options.damage_boost.value) and
            (state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player)))

    for item in [locName.HillsCandleMusicShrine, locName.HillsKey]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GriffinBoots, player))

    add_rule(world.get_location(locName.HillsCoin), lambda state:
        has_barrier("Purple", state, world))

    for item in [locName.HillsBagBarn, locName.HillsKey,
                 locName.HillsBagMusicShrine, locName.HillsCandleMusicShrine]:
        add_rule(world.get_location(item), lambda state:
            has_bombs(state, world))

    for item in [locName.HillsPlant, locName.HillsBeacon, locName.HillsMilbert]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.HillsKey, player) and state.has(itemName.FatalFlute, player))

    # Fort Rules
    for item in [locName.FortBagDungeon1, locName.FortBagDungeon2,
                 locName.FortBagDungeon3, locName.FortBagDungeon4, locName.SacredOil]:
        add_rule(world.get_location(item), lambda state: state.has(itemName.DungeonKey, player))

    for item in [locName.FortBagDungeon1, locName.FortBagDungeon2,
                 locName.FortBagDungeon3, locName.FortBagDungeon4,
                 locName.SacredOil, locName.FortCandleDarkRoom, locName.FortBagDarkRoom]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location(locName.FortKeyFirstRoom), lambda state:
        can_pass_poulture("Red", state, world))

    add_rule(world.get_location(locName.EnchantedShoes), lambda state:
        has_barrier("Flute", state, world))

    for item in [locName.EnchantedShoes, locName.FortCoin, locName.FortKeyTopRoom,
                 locName.FortBagTopRoom1, locName.FortBagTopRoom2, locName.FortBagTopRoom3,
                 locName.FortCandleLastRoom, locName.FortBagLastRoom, locName.ReflectorRing,
                 locName.FortJewel, locName.FortBonus]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GriffinBoots, player) and
            state.has(itemName.FortKeyFirstRoom, player) and
            has_lantern(state, world))

    for item in [locName.FortCandleLastRoom, locName.FortBagLastRoom, locName.ReflectorRing,
                 locName.FortJewel, locName.FortBonus]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.FortKeyTopRoom, player) and
            has_barrier("Blue", state, world))

    for item in [locName.FortBagLastRoom, locName.ReflectorRing, locName.FortJewel, locName.FortBonus]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Red", state, world))
    add_rule(world.get_location(locName.ReflectorRing), lambda state:
        has_barrier("Gauntlet", state, world))

    for item in [locName.FortJewel, locName.FortBonus]:
        add_rule(world.get_location(item), lambda state:
                state.has_group("candles", player, 20))
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Blue", state, world))

    add_rule(world.get_location(locName.FortBonus), lambda state:
        state.has(itemName.FortJewel, player))

    # Castle Rules
    add_rule(world.get_location(locName.CastleBagEntrance), lambda state:
        state.has(itemName.GriffinBoots, player))

    for item in [locName.CastleCandleRightRoom, locName.CastleKeyNodelki,
                 locName.CastleCandleTopRoom, locName.CastleBagTopRoom,
                 locName.WingedBelt, locName.CastleCoin, locName.CastleKeyLeftRoom,
                 locName.CastleBagBonus, locName.CastleBonus, locName.CastleJewel]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))

    add_rule(world.get_location(locName.CastleCandleRightRoom), lambda state:
        has_barrier("Red", state, world) and
        has_barrier("Blue", state, world) and
        state.has(itemName.GriffinBoots, player) and
        can_pass_poulture("Red", state, world))

    add_rule(world.get_location(locName.CastleKeyNodelki), lambda state:
        (has_barrier("Red", state, world) and
         (state.has(itemName.GriffinBoots, player) or
          (has_barrier("Blue", state, world) and
           has_barrier("Gauntlet", state, world))) and
         (can_pass_poulture("Red", state, world) and
          can_pass_boarfoon("Blue", state, world))
        ) or
        (has_barrier("Blue", state, world) and
         has_barrier("Gauntlet", state, world) and
         state.has(itemName.GriffinBoots, player)
        ))

    add_rule(world.get_location(locName.CastleCandleTopRoom), lambda state:
        state.has(itemName.GriffinBoots, player) and
        has_bombs(state, world) and
        ((has_barrier("Red", state, world) and
         can_pass_poulture("Red", state, world)) or
        (has_barrier("Blue", state, world) and
         has_barrier("Gauntlet", state, world))))

    for item in [locName.CastleBagTopRoom, locName.CastleJewel]:
        add_rule(world.get_location(item), lambda state:
            (has_barrier("Red", state, world) and
             (state.has(itemName.GriffinBoots, player) or
              has_barrier("Blue", state, world)) and
             (has_bombs(state, world) or
              has_barrier("Gauntlet", state, world)) and
             (can_pass_poulture("Red", state, world) and
              can_pass_boarfoon("Blue", state, world))
            ) or
            (has_barrier("Blue", state, world) and
             state.has(itemName.GriffinBoots, player) and
             (has_barrier("Gauntlet", state, world) or
              can_pass_poulture("Blue", state, world))))

    for item in [locName.WingedBelt, locName.CastleCoin, locName.CastleKeyLeftRoom,
                 locName.CastleBagBonus, locName.CastleBonus]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Blue", state, world) and
            ((has_barrier("Red", state, world) and
              (has_bombs(state, world) or has_barrier("Gauntlet", state, world)) and
              can_pass_poulture("Red", state, world) and
              can_pass_boarfoon("Blue", state, world)
              ) or
              (state.has(itemName.GriffinBoots, player) and 
               (has_barrier("Gauntlet", state, world) or
                can_pass_poulture("Blue", state, world)))
            ))
    add_rule(world.get_location(locName.WingedBelt), lambda state:
        (state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player)) and
        state.has_group("candles", player, 20) and
        has_barrier("Flute", state, world))

    add_rule(world.get_location(locName.CastleJewel), lambda state:
        state.has_group("candles", player, 20) and
        state.has(itemName.CastleKeyNodelki, player))

    for item in [locName.CastleBagBonus, locName.CastleBonus]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.CastleKeyLeftRoom, player))

    # Lair Rules
    add_rule(world.get_location(locName.LairCandleTreeTrunk), lambda state:
        has_bombs(state, world))

    add_rule(world.get_location(locName.LairCandleTreeTop), lambda state:
        state.has(itemName.GriffinBoots, player) and
        ((has_bombs(state, world) and has_barrier("Flute", state, world)) or
         (has_barrier("Purple", state, world) and
          state.has(itemName.SpeedyShoes, player) and state.has(itemName.WingedBelt, player)) and
          can_pass_poulture("Red", state, world)))

    for item in [locName.LairBonus, locName.LairBagFirstRoom, locName.LairCoin,
                 locName.LairBagLavaRoom, locName.LairBagFinalRoom1, locName.LairBagFinalRoom2,
                 locName.LairBagFinalRoom3, locName.Daimur]:
        add_rule(world.get_location(item), lambda state:
            has_barrier("Purple", state, world))
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Blue", state, world) or
            (state.has(itemName.GriffinBoots, player) and state.has(itemName.WingedBelt, player) and
             has_barrier("Flute", state, world)))

    for item in [locName.LairBagFinalRoom2, locName.Daimur]:
        add_rule(world.get_location(item), lambda state:
            can_pass_poulture("Red", state, world) or
            has_barrier("Gauntlet", state, world))

    for item in [locName.LairBonus, locName.LairBagFirstRoom, locName.LairCoin]:
        add_rule(world.get_location(item), lambda state:
            state.has(itemName.GriffinBoots, player))
    add_rule(world.get_location(locName.LairCoin), lambda state:
        has_lantern(state, world))

    for item in [locName.LairBagLavaRoom, locName.LairBagFinalRoom1,
                 locName.LairBagFinalRoom2, locName.LairBagFinalRoom3, locName.Daimur]:
        add_rule(world.get_location(item), lambda state:
            (state.has(itemName.GriffinBoots, player) or state.has(itemName.WingedBelt, player)) and
            has_lantern(state, world))

    # The jewels rule is not in vanilla game and should be added
    add_rule(world.get_location(locName.Daimur), lambda state:
        state.has(itemName.PurpleMagic, player) and state.has_group("jewels", player, 5))


    # Locations depending on NPC locations

    # Faramore Rules
    add_rule(world.get_location(locName.RopeUpgrade), lambda state:
        spawner_reach(itemName.FaramoreMunhum, state, world) and
        state.has_group("rocks", player, 4))
    # Rope and unlocking Swamp requirement has been deactivated in the mod.

    add_rule(world.get_location(locName.PurpleMagic), lambda state:
        spawner_reach(itemName.FaramoreYukeen, state, world) and
        state.has_group("jewels", player, 5))

    add_rule(world.get_location(locName.CitizenshipPapers), lambda state:
        spawner_reach(itemName.FaramoreCovenplate, state, world) and
        spawner_reach(itemName.ForestCypress, state, world))

    add_rule(world.get_location(locName.PowerStoneUpgrade), lambda state:
        spawner_reach(itemName.FaramoreKariQuest, state, world) and
        state.has(itemName.Bell, player))
    # Bomb Gauntlet and unlocking Castle requirement has been deactivated in the mod.

    add_rule(world.get_location(locName.DungeonKey), lambda state:
        spawner_reach(itemName.FaramoreAlven, state, world))

    add_rule(world.get_location(locName.Chainsword), lambda state:
        spawner_reach(itemName.FaramoreAlven, state, world) and
        state.has(itemName.OilandChains, player))

    add_rule(world.get_location(locName.Canteen), lambda state:
        spawner_reach(itemName.FaramoreBrinda, state, world) and
        state.has(itemName.StarEarrings, player))

    add_rule(world.get_location(locName.WalletUpgrade), lambda state:
        spawner_reach(itemName.FaramoreFrich, state, world) and
        state.has(itemName.SilverCricket, player))
    # Frich's first quest and unlocking Volcano requirement have been deactivated in the mod.

    add_rule(world.get_location(locName.InfiniteSoulfire), lambda state:
        spawner_reach(itemName.FaramoreRudy, state, world) and
        world.get_location(locName.HillsRace100Rupees).can_reach(state))

    add_rule(world.get_location(locName.BombUpgrade), lambda state:
        spawner_reach(itemName.FaramoreBarnabuss, state, world) and
        state.has(itemName.Compass, player))
    # Griffin Boots and unlocking Hills requirement have been deactivated in the mod.

    add_rule(world.get_location(locName.Rupees200), lambda state:
        spawner_reach(itemName.FaramoreDewey, state, world) and
        state.has(itemName.RopeLadder, player))

    add_rule(world.get_location(locName.LampOilUpgrade), lambda state:
        spawner_reach(itemName.FaramoreCypress, state, world) and
        state.has_group("plants", player, 3))
    # Lantern and unlocking Swamp requirement have been deactivated in the mod.

    add_rule(world.get_location(locName.Calendar), lambda state:
        spawner_reach(itemName.FaramoreDenny, state, world) and
        world.get_location(locName.CastleJewel).can_reach(state))

    # Forest Rules
    add_rule(world.get_location(locName.Lantern), lambda state:
        spawner_reach(itemName.ForestCypress, state, world) and
        state.has(itemName.CitizenshipPapers, player))

    add_rule(world.get_location(locName.ForestRace100Rupees), lambda state:
        spawner_reach(itemName.ForestRudyStart) and
        spawner_reach(itemName.ForestRudyEnd) and
        level_access("Faramore", state, world) and
        state.has_group("bombs", player) and
        state.has_group("coins", player, 1))

    # Caves Rules
    add_rule(world.get_location(locName.Rope), lambda state:
        spawner_reach(itemName.CavesMunhum, state, world))

    add_rule(world.get_location(locName.SnailSalt), lambda state:
        spawner_reach(itemName.CavesEllido, state, world) and
        state.has(itemName.FunkyFungus, player))

    # Desert Rules
    add_rule(world.get_location(locName.FairyDust), lambda state:
        spawner_reach(itemName.DesertFairy, state, world))

    # Canyon Rules
    add_rule(world.get_location(locName.Backstep), lambda state:
        spawner_reach(itemName.CanyonCrowdee, state, world))
    # Defeating Cornrad requirement has been deactivated in the mod.

    add_rule(world.get_location(locName.StarEarrings), lambda state:
        spawner_reach(itemName.CanyonOdie, state, world))

    add_rule(world.get_location(locName.SmartGun), lambda state:
        spawner_reach(itemName.CanyonMotte, state, world) and
        state.has(itemName.FairyDust, player))

    # Swamp Rules
    add_rule(world.get_location(locName.OgreHair), lambda state:
        spawner_reach(itemName.SwampGlubbert, state, world) and
        state.has(itemName.CleaverShovel, player))

    # Peak Rules
    add_rule(world.get_location(locName.PowerPendant), lambda state:
        spawner_reach(itemName.PeakCiclena, state, world) and
        state.has(itemName.CrystalofRefraction, player))

    add_rule(world.get_location(locName.PeakRace100Rupees), lambda state:
        spawner_reach(itemName.PeakRudyStart) and
        spawner_reach(itemName.PeakRudyEnd) and
        state.has_group("coins", player, 5) and
        world.get_location(locName.ForestRace100Rupees).can_reach(state))

    # Crypts Rules
    add_rule(world.get_location(locName.BombGauntlet), lambda state:
        spawner_reach(itemName.CryptsSkelvis, state, world))

    # Beach Rules
    add_rule(world.get_location(locName.SpeedyShoes), lambda state:
        spawner_reach(itemName.BeachFleetus, state, world) and
        state.has(itemName.EnchantedShoes, player))

    add_rule(world.get_location(locName.MagicCloak), lambda state:
        spawner_reach(itemName.BeachTork, state, world) and
        state.has(itemName.Calendar, player))

    # River Rules
    add_rule(world.get_location(locName.CleaverShovel), lambda state:
        spawner_reach(itemName.RiverFrancine, state, world) and
        state.has(itemName.SnailSalt, player))

    add_rule(world.get_location(locName.OilandChains), lambda state:
        spawner_reach(itemName.RiverMorgh, state, world) and
        state.has(itemName.OgreHair, player))

    # Hills Rules
    add_rule(world.get_location(locName.DoubleWave), lambda state:
        spawner_reach(itemName.HillsMilbert, state, world) and
        state.has(itemName.SwordWave, player))

    add_rule(world.get_location(locName.HillsRace100Rupees), lambda state:
        spawner_reach(itemName.HillsRudyStart) and
        spawner_reach(itemName.HillsRudyEnd) and
        state.has_group("coins", player, 10) and
        state.has(itemName.SmartGun, player) and  # Yes you need the smartgun for this race to spawn
        world.get_location(locName.PeakRace100Rupees).can_reach(state))

    # Lair Rules
    add_rule(world.get_location(locName.FunkyFungus), lambda state:
        spawner_reach(itemName.LairZazie, state, world) and
        state.has(itemName.SacredOil, player))
    add_rule(world.get_location(locName.SoulUpgrade), lambda state:
        spawner_reach(itemName.LairZazie, state, world) and
        has_enemy(state, world) and
        state.has(itemName.SacredOil, player) and
        (state.has(itemName.SmartGun, player) or
         state.has(itemName.InfiniteSoulfire, player)))

    # Bonus Rewards Rules
    for item, locdata in bonusreward_locations.items():
        parent = locdata.spawn_from
        add_rule(world.get_location(item), lambda state, parent=parent:
            world.get_location(world.early_lock[parent]).can_reach(state))
    for item in [locName.DesertBonusReward,
                 locName.SwampBonusReward,
                 locName.FortBonusReward]:
        add_rule(world.get_location(item), lambda state:
            has_lantern(state, world))
    add_rule(world.get_location(locName.HillsBonusReward), lambda state:
        state.has(itemName.GriffinBoots, player) or
        (state.has(itemName.FatalFlute, player) and has_shop(state, world)) or
            options.tricky_jumps.value)

    # Rocks Rules
    for item in rock_locations:
        add_rule(world.get_location(item), lambda state:
            rock_quest(state, world))

    add_rule(world.get_location(locName.OrangeRock), lambda state:
        level_access("Caves", state, world) and
        state.has(itemName.Bombs, player) and has_shop(state, world))

    add_rule(world.get_location(locName.BrownRock), lambda state:
        (level_access("Canyon", state, world) and
         has_lantern(state, world)) or
        (level_access("Lair", state, world) and
         state.has(itemName.PowerPendant, player) and
         (can_pass_poulture("Blue", state, world) or
          (state.has(itemName.GriffinBoots, player) and
           state.has(itemName.WingedBelt, player) and
           has_barrier("Flute", state, world))) and
         has_lantern(state, world) and
         has_barrier("Purple", state, world)) or
        spawner_reach(itemName.LairBonus, state, world))

    add_rule(world.get_location(locName.GrayRock), lambda state:
        (level_access("Peak", state, world) and
         has_barrier("Red", state, world)) or
        (level_access("Fort", state, world) and
         state.has(itemName.PowerPendant, player)))

    add_rule(world.get_location(locName.BlueRock), lambda state:
        level_access("Beach", state, world) and
        state.has(itemName.BeachKeyFirstHouse, player) and
        has_barrier("Blue", state, world))