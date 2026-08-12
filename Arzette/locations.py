from BaseClasses import Location
import typing
from .Names import locName, itemName

class ArzetteLocation(Location):
    game: str = "Arzette: The Jewel of Faramore"

class                    LocationData(typing.NamedTuple):
    arzid: int | None
    # Default client's item code at this location
    # The reason this is here and not in ItemData is because the only fungible items 
    # (rudy races and null bonus rewards) are at multiple locations by default
    # Since all other items are non-fungible, it was easier to give the same internal name
    # to items and locations and put the item_code here
    item_code: str
    # Client's location code
    location_code: str
    group: str = None
	# Can be a location for a spawner item
    can_spawner: bool = True
    locked: bool = False
    # If spawner item, this is the corresponding spawner location
    # If not, this is the level the item is in
    spawn_from: str = None

all_levels = [
    "Faramore",
    "Forest",
    "Caves",
    "Desert",
    "Canyon",
    "Swamp",
    "Peak",
    "Crypts",
    "Volcano",
    "Beach",
    "River",
    "Hills",
    "Fort",
    "Castle",
    "Lair"
]

faramore_locations = {
	locName.FaramoreKeyWell:             LocationData(367759001, "key_faramore_2",                  "Faramore Key (Well)",             "Key",         True, False, "Faramore"),
	locName.FaramoreKeyTavern:           LocationData(367759002, "key_faramore_1",                  "Faramore Key (Tavern)",           "Key",         True, False, "Faramore"),
	locName.FaramoreBonus:               LocationData(367759003, "obj_bonus_scroll_1",              "Faramore Bonus",                  "Scroll",      True, False, "Faramore"),
	locName.FaramoreCandleEmptyHouse:    LocationData(367759004, "obj_sacred_candle_24",            "Faramore Candle (Empty House)",   "Candle",      True, False, "Faramore"),
	locName.FaramoreCandleCypressHouse:  LocationData(367759005, "obj_sacred_candle_25",            "Faramore Candle (Cypress House)", "Candle",      True, False, "Faramore"),
	locName.FaramoreCoin:                LocationData(367759006, "obj_hidden_coin_faramore",        "Faramore Coin",                   "Coin",        True, False, "Faramore")
}

forest_locations = {
	locName.Bombs:                       LocationData(367759007, "obj_quest_bombs",                 "Bombs",                           "Quest",       True, False, "Forest"),
	locName.ForestBagFirstRoom1:         LocationData(367759008, "obj_item_bag_1",                  "Forest Bag (First Room 1)",       "Bag",         True, False, "Forest"),
	locName.ForestBagFirstRoom2:         LocationData(367759009, "obj_item_bag_2",                  "Forest Bag (First Room 2)",       "Bag",         True, False, "Forest"),
	locName.ForestKey:                   LocationData(367759010, "key_durridin",                    "Forest Key",                      "Key",         True, False, "Forest"),
	locName.ForestBonus:                 LocationData(367759011, "obj_bonus_scroll_2",              "Forest Bonus",                    "Scroll",      True, False, "Forest"),
	locName.ForestCandleTree:            LocationData(367759012, "obj_sacred_candle_1",             "Forest Candle (Tree)",            "Candle",      True, False, "Forest"),
	locName.ForestCandleCypress:         LocationData(367759013, "obj_sacred_candle_2",             "Forest Candle (Cypress)",         "Candle",      True, False, "Forest"),
	locName.ForestCoin:                  LocationData(367759014, "obj_hidden_coin_durridin",        "Forest Coin",                     "Coin",        True, False, "Forest"),
	locName.ForestBagSwordWave:          LocationData(367759015, "obj_item_bag_3",                  "Forest Bag (Sword Wave)",         "Bag",         True, False, "Forest"),
	locName.SwordWave:                   LocationData(367759016, "obj_quest_sword_wave",            "Sword Wave",                      "Quest",       True, False, "Forest"),
	locName.GoldenFly:                   LocationData(367759017, "obj_quest_golden_fly",            "Golden Fly",                      "Quest",       True, False, "Forest"),
	locName.ForestBagLastRoom:           LocationData(367759018, "obj_item_bag_4",                  "Forest Bag (Last Room)",          "Bag",         True, False, "Forest"),
	locName.ForestBeacon:                LocationData(367759019, "beacon_durridin",                 "Forest Beacon",                   "Beacon",      True, False, "Forest"),
	locName.ForestJewel:                 LocationData(367759020, "obj_jof_1",                       "Forest Jewel",                    "Jewel",       False, False, "Forest"),
	locName.MagicArmor:                  LocationData(367759021, "obj_quest_armor",                 "Magic Armor",                     "Quest",       True, False, "Forest")
}

caves_locations = {
	locName.SilverCricket:               LocationData(367759022, "obj_quest_silver_cricket",        "Silver Cricket",                  "Quest",       True, False, "Caves"),
	locName.RopeLadder:                  LocationData(367759023, "obj_quest_rope_ladder",           "Rope Ladder",                     "Quest",       True, False, "Caves"),
	locName.CavesBagRopeLadder:          LocationData(367759024, "obj_item_bag_5",                  "Caves Bag (Rope Ladder)",         "Bag",         True, False, "Caves"),
	locName.CavesCandleFirstDarkRoom:    LocationData(367759025, "obj_sacred_candle_5",             "Caves Candle (First Dark Room)",  "Candle",      True, False, "Caves"),
	locName.CavesCoin:                   LocationData(367759026, "obj_hidden_coin_cogwyn",          "Caves Coin",                      "Coin",        True, False, "Caves"),
	locName.CavesCandleSecondDarkRoom:   LocationData(367759027, "obj_sacred_candle_26",            "Caves Candle (Second Dark Room)", "Candle",      True, False, "Caves"),
	locName.CavesBonus:                  LocationData(367759028, "obj_bonus_scroll_3",              "Caves Bonus",                     "Scroll",      True, False, "Caves"),
	locName.CavesBagLastRoom:            LocationData(367759029, "obj_item_bag_6",                  "Caves Bag (Last Room)",           "Bag",         True, False, "Caves"),
	locName.ShieldRing:                  LocationData(367759030, "obj_quest_shield_ring",           "Shield Ring",                     "Quest",       True, False, "Caves")
}

desert_locations = {
	locName.DesertCoin:                  LocationData(367759031, "obj_hidden_coin_anju",            "Desert Coin",                     "Coin",        True, False, "Desert"),
	locName.DesertBagFirstRoom1:         LocationData(367759032, "obj_item_bag_7",                  "Desert Bag (First Room 1)",       "Bag",         True, False, "Desert"),
	locName.DesertBagFirstRoom2:         LocationData(367759033, "obj_item_bag_8",                  "Desert Bag (First Room 2)",       "Bag",         True, False, "Desert"),
	locName.Compass:                     LocationData(367759034, "obj_quest_compass",               "Compass",                         "Quest",       True, False, "Desert"),
	locName.DesertCandlePit:             LocationData(367759035, "obj_sacred_candle_3",             "Desert Candle (Pit)",             "Candle",      True, False, "Desert"),
	locName.DesertBonus:                 LocationData(367759036, "obj_bonus_scroll_4",              "Desert Bonus",                    "Scroll",      True, False, "Desert"),
	locName.DesertKey:                   LocationData(367759037, "key_anju",                        "Desert Key",                      "Key",         True, False, "Desert"),
	locName.DesertCandleLastRoom:        LocationData(367759038, "obj_sacred_candle_4",             "Desert Candle (Last Room)",       "Candle",      False, False, "Desert"),
	locName.DesertLifeUp:                LocationData(367759039, "obj_lifeup_1",                    "Desert Life-Up",                  "LifeUp",      True, False, "Desert"),
	locName.DesertBagLastRoom:           LocationData(367759040, "obj_item_bag_9",                  "Desert Bag (Last Room)",          "Bag",         True, False, "Desert"),
	locName.DesertBeacon:                LocationData(367759041, "beacon_anju_desert",              "Desert Beacon",                   "Beacon",      True, False, "Desert")
}

canyon_locations = {
	locName.CanyonBonus:                 LocationData(367759042, "obj_bonus_scroll_5",              "Canyon Bonus",                    "Scroll",      True, False, "Canyon"),
	locName.CanyonBagBeforeCheckpoint:   LocationData(367759043, "obj_item_bag_10",                 "Canyon Bag (Before Checkpoint)",  "Bag",         True, False, "Canyon"),
	locName.CanyonBagAfterCheckpoint1:   LocationData(367759044, "obj_item_bag_11",                 "Canyon Bag (After Checkpoint 1)", "Bag",         True, False, "Canyon"),
	locName.CanyonBagAfterCheckpoint2:   LocationData(367759045, "obj_item_bag_12",                 "Canyon Bag (After Checkpoint 2)", "Bag",         True, False, "Canyon"),
	locName.CanyonBagAfterCheckpoint3:   LocationData(367759046, "obj_item_bag_13",                 "Canyon Bag (After Checkpoint 3)", "Bag",         True, False, "Canyon"),
	locName.CanyonBagFirstRoomEnd:       LocationData(367759047, "obj_item_bag_14",                 "Canyon Bag (First Room End)",     "Bag",         True, False, "Canyon"),
	locName.CanyonCandleFirstRoomEnd:    LocationData(367759048, "obj_sacred_candle_6",             "Canyon Candle (First Room End)",  "Candle",      True, False, "Canyon"),
	locName.CanyonJewel:                 LocationData(367759049, "obj_jof_2",                       "Canyon Jewel",                    "Jewel",       False, False, "Canyon"),
	locName.CanyonKey:                   LocationData(367759050, "key_creece",                      "Canyon Key",                      "Key",         True, False, "Canyon"),
	locName.CanyonBagAfterZipline1:      LocationData(367759051, "obj_item_bag_15",                 "Canyon Bag (After Zipline 1)",    "Bag",         True, False, "Canyon"),
	locName.CanyonBagAfterZipline2:      LocationData(367759052, "obj_item_bag_16",                 "Canyon Bag (After Zipline 2)",    "Bag",         True, False, "Canyon"),
	locName.CanyonBagAfterZipline3:      LocationData(367759053, "obj_item_bag_17",                 "Canyon Bag (After Zipline 3)",    "Bag",         True, False, "Canyon"),
	locName.CanyonCoin:                  LocationData(367759054, "obj_hidden_coin_creece",          "Canyon Coin",                     "Coin",        True, False, "Canyon"),
	locName.CanyonBagMotteHouse:         LocationData(367759055, "obj_item_bag_18",                 "Canyon Bag (Motte House)",        "Bag",         True, False, "Canyon"),
	locName.CanyonCandleMotteHouse:      LocationData(367759056, "obj_sacred_candle_7",             "Canyon Candle (Motte House)",     "Candle",      True, False, "Canyon")
}

swamp_locations = {
	locName.SwampCandleFirstRoom:        LocationData(367759057, "obj_sacred_candle_8",             "Swamp Candle (First Room)",       "Candle",      True, False, "Swamp"),
	locName.SwampBagFirstRoom:           LocationData(367759058, "obj_item_bag_19",                 "Swamp Bag (First Room)",          "Bag",         True, False, "Swamp"),
	locName.SwampCoin:                   LocationData(367759059, "obj_hidden_coin_norin",           "Swamp Coin",                      "Coin",        True, False, "Swamp"),
	locName.SwampKeyFrichHouse:          LocationData(367759060, "key_norin",                       "Swamp Key (Frich House)",         "Key",         True, False, "Swamp"),
	locName.SwampCandleFrichHouse:       LocationData(367759061, "obj_sacred_candle_27",            "Swamp Candle (Frich House)",      "Candle",      True, False, "Swamp"),
	locName.SwampKeyGriffinBoots:        LocationData(367759062, "key_norin_2",                     "Swamp Key (Griffin Boots)",       "Key",         True, False, "Swamp"),
	locName.GriffinBoots:                LocationData(367759063, "obj_quest_magic_boots",           "Griffin Boots",                   "Quest",       True, False, "Swamp"),
	locName.SwampPlant:                  LocationData(367759064, "obj_quest_plant_b",               "Swamp Plant",                     "Plant",       False, False, "Swamp"),
	locName.SwampBonus:                  LocationData(367759065, "obj_bonus_scroll_6",              "Swamp Bonus",                     "Scroll",      True, False, "Swamp"),
	locName.SwampBeacon:                 LocationData(367759066, "beacon_norin_swamp",              "Swamp Beacon",                    "Beacon",      True, False, "Swamp")
}

peak_locations = {
	locName.PeakCandleFirstCave:         LocationData(367759067, "obj_sacred_candle_9",             "Peak Candle (First Cave)",        "Candle",      True, False, "Peak"),
	locName.PeakBagFirstCave1:           LocationData(367759068, "obj_item_bag_20",                 "Peak Bag (First Cave 1)",         "Bag",         True, False, "Peak"),
	locName.PeakBagFirstCave2:           LocationData(367759069, "obj_item_bag_21",                 "Peak Bag (First Cave 2)",         "Bag",         True, False, "Peak"),
	locName.PeakBonus:                   LocationData(367759070, "obj_bonus_scroll_7",              "Peak Bonus",                      "Scroll",      True, False, "Peak"),
	locName.PeakCoin:                    LocationData(367759071, "obj_hidden_coin_chillinax",       "Peak Coin",                       "Coin",        True, False, "Peak"),
	locName.PeakKey:                     LocationData(367759072, "key_chillinax",                   "Peak Key",                        "Key",         True, False, "Peak"),
	locName.PeakCandleCiclenaCave:       LocationData(367759073, "obj_sacred_candle_10",            "Peak Candle (Ciclena Cave)",      "Candle",      True, False, "Peak"),
	locName.PeakBagBeforeApatu:          LocationData(367759074, "obj_item_bag_22",                 "Peak Bag (Before Apatu)",         "Bag",         True, False, "Peak"),
	locName.PeakJewel:                   LocationData(367759075, "obj_jof_3",                       "Peak Jewel",                      "Jewel",       False, False, "Peak"),
	locName.PeakBagAfterApatu:           LocationData(367759076, "obj_item_bag_23",                 "Peak Bag (After Apatu)",          "Bag",         True, False, "Peak")
}

crypts_locations = {
	locName.CryptsLifeUp:                LocationData(367759077, "obj_lifeup_2",                    "Crypts Life-Up",                  "LifeUp",      True, False, "Crypts"),
	locName.Bell:                        LocationData(367759078, "obj_quest_town_bell",             "Bell",                            "Quest",       True, False, "Crypts"),
	locName.CryptsBonus:                 LocationData(367759079, "obj_bonus_scroll_8",              "Crypts Bonus",                    "Scroll",      True, False, "Crypts"),
	locName.CryptsKey:                   LocationData(367759080, "key_boanjale",                    "Crypts Key",                      "Key",         True, False, "Crypts"),
	locName.CryptsBagCrypt:              LocationData(367759081, "obj_item_bag_46",                 "Crypts Bag (Crypt)",              "Bag",         True, False, "Crypts"),
	locName.CryptsCandleAfterCrypt:      LocationData(367759082, "obj_sacred_candle_28",            "Crypts Candle (After Crypt)",     "Candle",      True, False, "Crypts"),
	locName.CryptsCoin:                  LocationData(367759083, "obj_hidden_coin_boanjale",        "Crypts Coin",                     "Coin",        False, False, "Crypts"),
	locName.CryptsCandleSkelvis:         LocationData(367759084, "obj_sacred_candle_11",            "Crypts Candle (Skelvis)",         "Candle",      True, False, "Crypts"),
	locName.CryptsBagSkelvis:            LocationData(367759085, "obj_item_bag_24",                 "Crypts Bag (Skelvis)",            "Bag",         True, False, "Crypts")
}

volcano_locations = {
	locName.VolcanoBonus:                LocationData(367759086, "obj_bonus_scroll_9",              "Volcano Bonus",                   "Scroll",      True, False, "Volcano"),
	locName.VolcanoCandleFirstRoom:      LocationData(367759087, "obj_sacred_candle_12",            "Volcano Candle (First Room)",     "Candle",      True, False, "Volcano"),
	locName.VolcanoCoin:                 LocationData(367759088, "obj_hidden_coin_sprigum",         "Volcano Coin",                    "Coin",        True, False, "Volcano"),
	locName.VolcanoCandleLastRoom:       LocationData(367759089, "obj_sacred_candle_29",            "Volcano Candle (Last Room)",      "Candle",      True, False, "Volcano"),
	locName.CrystalofRefraction:         LocationData(367759090, "obj_quest_crystal_of_refraction", "Crystal of Refraction",           "Quest",       True, False, "Volcano")
}

beach_locations = {
	locName.BeachBagFirstRoom:           LocationData(367759091, "obj_item_bag_25",                 "Beach Bag (First Room)",          "Bag",         True, False, "Beach"),
	locName.BeachKeyFirstHouse:          LocationData(367759092, "key_badonc",                      "Beach Key (First House)",         "Key",         True, False, "Beach"),
	locName.BeachCoin:                   LocationData(367759093, "obj_hidden_coin_badonc",          "Beach Coin",                      "Coin",        True, False, "Beach"),
	locName.BeachKeyTorkCabin:           LocationData(367759094, "key_badonc_2",                    "Beach Key (Tork Cabin)",          "Key",         True, False, "Beach"),
	locName.BeachCandleTorkCabin:        LocationData(367759095, "obj_sacred_candle_14",            "Beach Candle (Tork Cabin)",       "Candle",      True, False, "Beach"),
	locName.BeachPlant:                  LocationData(367759096, "obj_quest_plant_a",               "Beach Plant",                     "Plant",       True, False, "Beach"),
	locName.BeachBonus:                  LocationData(367759097, "obj_bonus_scroll_10",             "Beach Bonus",                     "Scroll",      True, False, "Beach"),
	locName.BeachCandleCave:             LocationData(367759098, "obj_sacred_candle_13",            "Beach Candle (Cave)",             "Candle",      True, False, "Beach"),
	locName.FatalFlute:                  LocationData(367759099, "obj_quest_flute",                 "Fatal Flute",                     "Quest",       True, False, "Beach"),
	locName.BeachBeacon:                 LocationData(367759100, "beacon_badonc_beach",             "Beach Beacon",                    "Beacon",      True, False, "Beach")
}

river_locations = {
	locName.RiverKeyFrancine:            LocationData(367759101, "key_ryha",                        "River Key (Francine)",            "Key",         True, False, "River"),
	locName.RiverBonus:                  LocationData(367759102, "obj_bonus_scroll_11",             "River Bonus",                     "Scroll",      True, False, "River"),
	locName.RiverCandleBoat:             LocationData(367759103, "obj_sacred_candle_15",            "River Candle (Boat)",             "Candle",      True, False, "River"),
	locName.RiverKeySubmarine:           LocationData(367759104, "key_ryha_2",                      "River Key (Submarine)",           "Key",         False, False, "River"),
	locName.RiverCoin:                   LocationData(367759105, "obj_hidden_coin_ryha",            "River Coin",                      "Coin",        True, False, "River"),
	locName.BlueMagic:                   LocationData(367759106, "obj_quest_blue_beam",             "Blue Magic",                      "Quest",       True, False, "River"),
	locName.RiverBagLastRoom:            LocationData(367759107, "obj_item_bag_26",                 "River Bag (Last Room)",           "Bag",         True, False, "River"),
	locName.RiverCandleLastRoom:         LocationData(367759108, "obj_sacred_candle_16",            "River Candle (Last Room)",        "Candle",      True, False, "River"),
	locName.RiverLifeUp:                 LocationData(367759109, "obj_lifeup_3",                    "River Life-Up",                   "LifeUp",      True, False, "River")
}

hills_locations = {
	locName.HillsCandleCave:             LocationData(367759110, "obj_sacred_candle_30",            "Hills Candle (Cave)",             "Candle",      True, False, "Hills"),
	locName.LightningSword:              LocationData(367759111, "obj_quest_electric_sword",        "Lightning Sword",                 "Quest",       True, False, "Hills"),
	locName.HillsCoin:                   LocationData(367759112, "obj_hidden_coin_lichen",          "Hills Coin",                      "Coin",        True, False, "Hills"),
	locName.HillsBonus:                  LocationData(367759113, "obj_bonus_scroll_12",             "Hills Bonus",                     "Scroll",      True, False, "Hills"),
	locName.HillsBagBarn:                LocationData(367759114, "obj_item_bag_27",                 "Hills Bag (Barn)",                "Bag",         True, False, "Hills"),
	locName.HillsKey:                    LocationData(367759115, "key_lichen",                      "Hills Key",                       "Key",         True, False, "Hills"),
	locName.HillsBagMusicShrine:         LocationData(367759116, "obj_item_bag_28",                 "Hills Bag (Music Shrine)",        "Bag",         True, False, "Hills"),
	locName.HillsCandleMusicShrine:      LocationData(367759117, "obj_sacred_candle_17",            "Hills Candle (Music Shrine)",     "Candle",      True, False, "Hills"),
	locName.HillsPlant:                  LocationData(367759118, "obj_quest_plant_c",               "Hills Plant",                     "Plant",       True, False, "Hills"),
	locName.HillsBeacon:                 LocationData(367759119, "beacon_lichen_hills",             "Hills Beacon",                    "Beacon",      True, False, "Hills")
}

fort_locations = {
	locName.FortBagDungeon1:             LocationData(367759120, "obj_item_bag_29",                 "Fort Bag (Dungeon 1)",            "Bag",         True, False, "Fort"),
	locName.FortBagDungeon2:             LocationData(367759121, "obj_item_bag_30",                 "Fort Bag (Dungeon 2)",            "Bag",         True, False, "Fort"),
	locName.FortBagDungeon3:             LocationData(367759122, "obj_item_bag_31",                 "Fort Bag (Dungeon 3)",            "Bag",         True, False, "Fort"),
	locName.FortBagDungeon4:             LocationData(367759123, "obj_item_bag_32",                 "Fort Bag (Dungeon 4)",            "Bag",         True, False, "Fort"),
	locName.SacredOil:                   LocationData(367759124, "obj_quest_oil",                   "Sacred Oil",                      "Trading",     True, False, "Fort"),
	locName.FortKeyFirstRoom:            LocationData(367759125, "key_findula_1",                   "Fort Key (First Room)",           "Key",         True, False, "Fort"),
	locName.FortCandleDarkRoom:          LocationData(367759126, "obj_sacred_candle_18",            "Fort Candle (Dark Room)",         "Candle",      True, False, "Fort"),
	locName.FortBagDarkRoom:             LocationData(367759127, "obj_item_bag_33",                 "Fort Bag (Dark Room)",            "Bag",         True, False, "Fort"),
	locName.EnchantedShoes:              LocationData(367759128, "obj_quest_shoes",                 "Enchanted Shoes",                 "Quest",       True, False, "Fort"),
	locName.FortCoin:                    LocationData(367759129, "obj_hidden_coin_findula",         "Fort Coin",                       "Coin",        True, False, "Fort"),
	locName.FortKeyTopRoom:              LocationData(367759130, "key_findula_2",                   "Fort Key (Top Room)",             "Key",         True, False, "Fort"),
	locName.FortBagTopRoom1:             LocationData(367759131, "obj_item_bag_34",                 "Fort Bag (Top Room 1)",           "Bag",         True, False, "Fort"),
	locName.FortBagTopRoom2:             LocationData(367759132, "obj_item_bag_35",                 "Fort Bag (Top Room 2)",           "Bag",         True, False, "Fort"),
	locName.FortBagTopRoom3:             LocationData(367759133, "obj_item_bag_36",                 "Fort Bag (Top Room 3)",           "Bag",         True, False, "Fort"),
	locName.FortCandleLastRoom:          LocationData(367759134, "obj_sacred_candle_19",            "Fort Candle (Last Room)",         "Candle",      True, False, "Fort"),
	locName.FortBagLastRoom:             LocationData(367759135, "obj_item_bag_37",                 "Fort Bag (Last Room)",            "Bag",         True, False, "Fort"),
	locName.ReflectorRing:               LocationData(367759136, "obj_quest_reflecting_shield",     "Reflector Ring",                  "Quest",       True, False, "Fort"),
	locName.FortJewel:                   LocationData(367759137, "obj_jof_4",                       "Fort Jewel",                      "Jewel",       False, False, "Fort"),
	locName.FortBonus:                   LocationData(367759138, "obj_bonus_scroll_13",             "Fort Bonus",                      "Scroll",      True, False, "Fort")
}

castle_locations = {
	locName.CastleBagEntrance:           LocationData(367759139, "obj_item_bag_38",                 "Castle Bag (Entrance)",           "Bag",         True, False, "Castle"),
	locName.CastleCandleRightRoom:       LocationData(367759140, "obj_sacred_candle_20",            "Castle Candle (Right Room)",      "Candle",      True, False, "Castle"),
	locName.CastleKeyNodelki:            LocationData(367759141, "key_denny_2",                     "Castle Key (Nodelki)",            "Key",         True, False, "Castle"),
	locName.CastleCandleTopRoom:         LocationData(367759142, "obj_sacred_candle_21",            "Castle Candle (Top Room)",        "Candle",      True, False, "Castle"),
	locName.CastleBagTopRoom:            LocationData(367759143, "obj_item_bag_39",                 "Castle Bag (Top Room)",           "Bag",         True, False, "Castle"),
	locName.WingedBelt:                  LocationData(367759144, "obj_quest_winged_belt",           "Winged Belt",                     "Quest",       True, False, "Castle"),
	locName.CastleCoin:                  LocationData(367759145, "obj_hidden_coin_denny",           "Castle Coin",                     "Coin",        True, False, "Castle"),
	locName.CastleKeyLeftRoom:           LocationData(367759146, "key_denny_1",                     "Castle Key (Left Room)",          "Key",         True, False, "Castle"),
	locName.CastleBagBonus:              LocationData(367759147, "obj_item_bag_40",                 "Castle Bag (Bonus)",              "Bag",         True, False, "Castle"),
	locName.CastleBonus:                 LocationData(367759148, "obj_bonus_scroll_14",             "Castle Bonus",                    "Scroll",      True, False, "Castle"),
	locName.CastleJewel:                 LocationData(367759149, "obj_jof_5",                       "Castle Jewel",                    "Jewel",       False, False, "Castle")
}

lair_locations = {
	locName.LairCandleTreeTrunk:         LocationData(367759150, "obj_sacred_candle_22",            "Lair Candle (Tree Trunk)",        "Candle",      True, False, "Lair"),
	locName.LairCandleTreeTop:           LocationData(367759151, "obj_sacred_candle_23",            "Lair Candle (Tree Top)",          "Candle",      True, False, "Lair"),
	locName.LairBonus:                   LocationData(367759152, "obj_bonus_scroll_15",             "Lair Bonus",                      "Scroll",      True, False, "Lair"),
	locName.LairBagFirstRoom:            LocationData(367759153, "obj_item_bag_41",                 "Lair Bag (First Room)",           "Bag",         True, False, "Lair"),
	locName.LairCoin:                    LocationData(367759154, "obj_hidden_coin_daimur",          "Lair Coin",                       "Coin",        True, False, "Lair"),
	locName.LairBagLavaRoom:             LocationData(367759155, "obj_item_bag_42",                 "Lair Bag (Lava Room)",            "Bag",         True, False, "Lair"),
	locName.LairBagFinalRoom1:           LocationData(367759156, "obj_item_bag_43",                 "Lair Bag (Final Room 1)",         "Bag",         True, False, "Lair"),
	locName.LairBagFinalRoom2:           LocationData(367759157, "obj_item_bag_44",                 "Lair Bag (Final Room 2)",         "Bag",         True, False, "Lair"),
	locName.LairBagFinalRoom3:           LocationData(367759158, "obj_item_bag_45",                 "Lair Bag (Final Room 3)",         "Bag",         True, False, "Lair"),
	locName.Daimur:                      LocationData(367759159, "obj_boss_daimur",                 "Daimur",                          "Other",       False, True, "Lair")
}

from_npc_locations = {
	locName.PurpleMagic:                 LocationData(367759160, "obj_quest_sword",                 "Purple Magic",                    "Quest",       False, False, itemName.FaramoreYukeen),
	locName.CitizenshipPapers:           LocationData(367759161, "obj_quest_citizenship",           "Citizenship Papers",              "Quest",       False, False, itemName.FaramoreCovenplate),
	locName.PowerStoneUpgrade:           LocationData(367759162, "obj_quest_upgrade_power_stones",  "Power Stone Upgrade",             "Upgrade",     False, False, itemName.FaramoreKariQuest),
	locName.DungeonKey:                  LocationData(367759163, "key_findula_dungeon",             "Dungeon Key",                     "Trading",     False, False, itemName.FaramoreAlven),
	locName.Chainsword:                  LocationData(367759164, "obj_quest_chainsword",            "Chainsword",                      "Trading",     False, False, itemName.FaramoreAlven),
	locName.Canteen:                     LocationData(367759165, "obj_quest_canteen",               "Canteen",                         "Quest",       False, False, itemName.FaramoreBrinda),
	locName.WalletUpgrade:               LocationData(367759166, "obj_quest_upgrade_wallet",        "Wallet Upgrade",                  "Upgrade",     False, False, itemName.FaramoreFrich),
	locName.InfiniteSoulfire:            LocationData(367759167, "obj_quest_infinite_soulfire",     "Infinite Soulfire",               "Upgrade",     False, False, itemName.FaramoreRudy),
	locName.BombUpgrade:                 LocationData(367759168, "obj_quest_upgrade_bombs",         "Bomb Upgrade",                    "Upgrade",     False, False, itemName.FaramoreBarnabuss),
	locName.Calendar:                    LocationData(367759169, "obj_quest_beach_calendar",        "Calendar",                        "Quest",       False, False, itemName.FaramoreDenny),
	locName.Rupees200:                   LocationData(367759170, "obj_quest_dewey_reward",          "200 Rupees",                      "Quest",       False, False, itemName.FaramoreDewey),
	locName.LampOilUpgrade:              LocationData(367759171, "obj_quest_upgrade_lamp_oil",      "Lamp Oil Upgrade",                "Upgrade",     False, False, itemName.FaramoreCypress),
	locName.RopeUpgrade:                 LocationData(367759172, "obj_quest_upgrade_ropes",         "Rope Upgrade",                    "Upgrade",     False, False, itemName.FaramoreMunhum),
	locName.ForestRace100Rupees:         LocationData(367759173, "obj_quest_race_reward_1",         "Forest Race 100 Rupees",          "Race",        False, False, itemName.FaramoreRudy),
	locName.PeakRace100Rupees:           LocationData(367759174, "obj_quest_race_reward_2",         "Peak Race 100 Rupees",            "Race",        False, False, itemName.FaramoreRudy),
	locName.HillsRace100Rupees:          LocationData(367759175, "obj_quest_race_reward_3",         "Hills Race 100 Rupees",           "Race",        False, False, itemName.FaramoreRudy),
	locName.Lantern:                     LocationData(367759176, "obj_quest_lantern",               "Lantern",                         "Quest",       False, False, itemName.ForestCypress),
	locName.Rope:                        LocationData(367759177, "obj_quest_esc_rope",              "Rope",                            "Quest",       False, False, itemName.CavesMunhum),
	locName.SnailSalt:                   LocationData(367759178, "obj_quest_snail_salt",            "Snail Salt",                      "Trading",     False, False, itemName.CavesEllido),
	locName.FairyDust:                   LocationData(367759179, "obj_quest_fairy_dust",            "Fairy Dust",                      "Quest",       False, False, itemName.DesertFairy),
	locName.Backstep:                    LocationData(367759180, "obj_quest_backstep",              "Backstep",                        "Quest",       False, False, itemName.CanyonCrowdee),
	locName.SmartGun:                    LocationData(367759181, "obj_quest_gun",                   "Smart Gun",                       "Quest",       False, False, itemName.CanyonMotte),
	locName.StarEarrings:                LocationData(367759182, "obj_quest_star_earrings",         "Star Earrings",                   "Quest",       False, False, itemName.CanyonOdie),
	locName.OgreHair:                    LocationData(367759183, "obj_quest_ogre_hair",             "Ogre Hair",                       "Trading",     False, False, itemName.SwampGlubbert),
	locName.PowerPendant:                LocationData(367759184, "obj_quest_pendant",               "Power Pendant",                   "Quest",       False, False, itemName.PeakCiclena),
	locName.BombGauntlet:                LocationData(367759185, "obj_quest_pg",                    "Bomb Gauntlet",                   "Quest",       False, False, itemName.CryptsSkelvis),
	locName.SpeedyShoes:                 LocationData(367759186, "obj_quest_speedy_shoes",          "Speedy Shoes",                    "Quest",       False, False, itemName.BeachFleetus),
	locName.MagicCloak:                  LocationData(367759187, "obj_quest_magic_cloak",           "Magic Cloak",                     "Quest",       False, False, itemName.BeachTork),
	locName.CleaverShovel:               LocationData(367759188, "obj_quest_cleaver_shovel",        "Cleaver Shovel",                  "Trading",     False, False, itemName.RiverFrancine),
	locName.OilandChains:                LocationData(367759189, "obj_quest_refined_chains",        "Oil and Chains",                  "Trading",     False, False, itemName.RiverMorgh),
	locName.DoubleWave:                  LocationData(367759190, "obj_quest_double_wave",           "Double Wave",                     "Quest",       False, False, itemName.HillsMilbert),
	locName.FunkyFungus:                 LocationData(367759191, "obj_quest_funky_fungus",          "Funky Fungus",                    "Trading",     False, False, itemName.LairZazie),
	locName.SoulUpgrade:                 LocationData(367759192, "obj_quest_upgrade_soul_bag",      "Soul Upgrade",                    "Upgrade",     False, False, itemName.LairZazie)
}

npc_spawn_locations = {
	locName.FaramoreCovenplate:          LocationData(367759193, "npc_mayor",                       "Faramore Covenplate",             "NPCSpawner",  True, False, "Faramore"),
	locName.CanyonCrowdee:               LocationData(367759194, "npc_crowdee",                     "Canyon Crowdee",                  "NPCSpawner",  True, False, "Canyon"),
	locName.PeakCiclena:                 LocationData(367759195, "npc_ciclena",                     "Peak Ciclena",                    "NPCSpawner",  True, False, "Peak"),
	locName.BeachFleetus:                LocationData(367759196, "npc_fleetus",                     "Beach Fleetus",                   "NPCSpawner",  True, False, "Beach"),
	locName.ForestCypress:               LocationData(367759197, "npc_cypress",                     "Forest Cypress",                  "NPCSpawner",  True, False, "Forest"),
	locName.FaramoreYukeen:              LocationData(367759198, "npc_yukeen",                      "Faramore Yukeen",                 "NPCSpawner",  True, False, "Faramore"),
	locName.FaramoreRudy:                LocationData(367759199, "npc_rudy",                        "Faramore Rudy",                   "NPCSpawner",  True, False, "Faramore"),
	locName.DesertFairy:                 LocationData(367759200, "npc_fairy",                       "Desert Fairy",                    "NPCSpawner",  True, False, "Desert"),
	locName.BeachTork:                   LocationData(367759201, "npc_tork",                        "Beach Tork",                      "NPCSpawner",  True, False, "Beach"),
	locName.FaramoreAlven:               LocationData(367759202, "npc_alven",                       "Faramore Alven",                  "NPCSpawner",  True, False, "Faramore"),
	locName.CavesEllido:                 LocationData(367759203, "npc_ellido",                      "Caves Ellido",                    "NPCSpawner",  True, False, "Caves"),
	locName.CanyonMotte:                 LocationData(367759204, "npc_motte",                       "Canyon Motte",                    "NPCSpawner",  True, False, "Canyon"),
	locName.FaramoreBarnabuss:           LocationData(367759205, "npc_barnabuss_quest",             "Faramore Barnabuss",              "NPCSpawner",  True, False, "Faramore"),
	locName.FaramoreDenny:               LocationData(367759206, "npc_denny",                       "Faramore Denny",                  "NPCSpawner",  True, False, "Faramore"),
	locName.FaramoreDewey:               LocationData(367759207, "npc_dewey",                       "Faramore Dewey",                  "NPCSpawner",  True, False, "Faramore"),
	locName.CryptsSkelvis:               LocationData(367759208, "npc_skelvis",                     "Crypts Skelvis",                  "NPCSpawner",  True, False, "Crypts"),
	locName.FaramoreFrich:               LocationData(367759209, "npc_frich_quest",                 "Faramore Frich",                  "NPCSpawner",  True, False, "Faramore"),
	locName.LairZazie:                   LocationData(367759210, "npc_zazie",                       "Lair Zazie",                      "NPCSpawner",  True, False, "Lair"),
	locName.CavesMunhum:                 LocationData(367759211, "npc_munhum",                      "Caves Munhum",                    "NPCSpawner",  True, False, "Caves"),
	locName.FaramoreBrinda:              LocationData(367759212, "npc_brinda",                      "Faramore Brinda",                 "NPCSpawner",  True, False, "Faramore"),
	locName.SwampGlubbert:               LocationData(367759213, "npc_glubbert",                    "Swamp Glubbert",                  "NPCSpawner",  True, False, "Swamp"),
	locName.HillsMilbert:                LocationData(367759214, "npc_milbert",                     "Hills Milbert",                   "NPCSpawner",  True, False, "Hills"),
	locName.FaramoreCypress:             LocationData(367759215, "npc_cypress_quest",               "Faramore Cypress",                "NPCSpawner",  True, False, "Faramore"),
	locName.CanyonOdie:                  LocationData(367759216, "npc_odie",                        "Canyon Odie",                     "NPCSpawner",  True, False, "Canyon"),
	locName.FaramoreKariQuest:           LocationData(367759217, "npc_kari_quest",                  "Faramore Kari Quest",             "NPCSpawner",  True, False, "Faramore"),
	locName.RiverMorgh:                  LocationData(367759218, "npc_morgh",                       "River Morgh",                     "NPCSpawner",  True, False, "River"),
	locName.RiverFrancine:               LocationData(367759219, "npc_francine",                    "River Francine",                  "NPCSpawner",  True, False, "River"),
	locName.FaramoreMunhum:              LocationData(367759220, "npc_munhum_quest",                "Faramore Munhum",                 "NPCSpawner",  True, False, "Faramore")
}

npc_foolish_locations = {
	locName.FaramoreBoru:                LocationData(367759221, "npc_boru",                        "Faramore Boru",                   "NPC",         True, False, "Faramore"),
	locName.FaramoreKari:                LocationData(367759222, "npc_kari",                        "Faramore Kari",                   "NPC",         True, False, "Faramore"),
	locName.FaramoreUnivor:              LocationData(367759223, "npc_univor",                      "Faramore Univor",                 "NPC",         True, False, "Faramore"),
	locName.FaramoreSalvik:              LocationData(367759224, "npc_salvik",                      "Faramore Salvik",                 "NPC",         True, False, "Faramore"),
	locName.FaramoreMaki:                LocationData(367759225, "npc_maki",                        "Faramore Maki",                   "NPC",         True, False, "Faramore"),
	locName.FaramorePayop:               LocationData(367759226, "npc_payop",                       "Faramore Payop",                  "NPC",         True, False, "Faramore"),
	locName.VolcanoJoe:                  LocationData(367759227, "npc_joe",                         "Volcano Joe",                     "NPC",         True, False, "Volcano"),
	locName.RiverBarnabuss:              LocationData(367759228, "npc_barnabuss",                   "River Barnabuss",                 "NPC",         True, False, "River")
}

npc_locked_locations = {
	locName.FaramoreMortar:              LocationData(367759229, "npc_mortar",                      "Faramore Mortar",                 "NPC",         False, True, "Faramore"),
	locName.SwampFrich:                  LocationData(367759230, "npc_frich",                       "Swamp Frich",                     "NPC",         False, True, "Swamp"),
	locName.ForestRudyStart:             LocationData(367759231, "npc_rudy_start",                  "Forest Rudy (Start)",             "NPC",         False, True, "Forest"),
	locName.ForestRudyEnd:               LocationData(367759232, "npc_rudy_goal",                   "Forest Rudy (End)",               "NPC",         False, True, "Forest"),
	locName.PeakRudyStart:               LocationData(367759233, "npc_rudy_start",                  "Peak Rudy (Start)",               "NPC",         False, True, "Peak"),
	locName.PeakRudyEnd:                 LocationData(367759234, "npc_rudy_goal",                   "Peak Rudy (End)",                 "NPC",         False, True, "Peak"),
	locName.HillsRudyStart:              LocationData(367759235, "npc_rudy_start",                  "Hills Rudy (Start)",              "NPC",         False, True, "Hills"),
	locName.HillsRudyEnd:                LocationData(367759236, "npc_rudy_goal",                   "Hills Rudy (End)",                "NPC",         False, True, "Hills")
}

rock_locations = {
	locName.OrangeRock:                  LocationData(367759237, "obj_quest_rock_orange",           "Orange Rock",                     "Rock",        False, False, None),
	locName.BrownRock:                   LocationData(367759238, "obj_quest_rock_brown",            "Brown Rock",                      "Rock",        False, False, None),
	locName.GrayRock:                    LocationData(367759239, "obj_quest_rock_grey",             "Gray Rock",                       "Rock",        False, False, None),
	locName.BlueRock:                    LocationData(367759240, "obj_quest_rock_blue",             "Blue Rock",                       "Rock",        False, False, None)
}

bonusreward_locations = {
	locName.FaramoreBonusReward:         LocationData(367759241, "obj_null",                        "Faramore Bonus Reward",           "BonusReward", False, True, itemName.FaramoreBonus),
	locName.ForestBonusReward:           LocationData(367759242, "obj_quest_rubie_bag_25_1",        "Forest Bonus Reward",             "BonusReward", False, False, itemName.ForestBonus),
	locName.CavesBonusReward:            LocationData(367759243, "obj_quest_rubie_bag_25_2",        "Caves Bonus Reward",              "BonusReward", False, False, itemName.CavesBonus),
	locName.DesertBonusReward:           LocationData(367759244, "obj_quest_rubie_bag_30_1",        "Desert Bonus Reward",             "BonusReward", False, False, itemName.DesertBonus),
	locName.CanyonBonusReward:           LocationData(367759245, "obj_quest_rubie_bag_30_2",        "Canyon Bonus Reward",             "BonusReward", False, False, itemName.CanyonBonus),
	locName.SwampBonusReward:            LocationData(367759246, "obj_quest_rubie_bag_30_3",        "Swamp Bonus Reward",              "BonusReward", False, False, itemName.SwampBonus),
	locName.PeakBonusReward:             LocationData(367759247, "obj_quest_rubie_bag_40",          "Peak Bonus Reward",               "BonusReward", False, False, itemName.PeakBonus),
	locName.CryptsBonusReward:           LocationData(367759248, "obj_quest_rubie_bag_50_1",        "Crypts Bonus Reward",             "BonusReward", False, False, itemName.CryptsBonus),
	locName.VolcanoBonusReward:          LocationData(367759249, "obj_null",                        "Volcano Bonus Reward",            "BonusReward", False, True, itemName.VolcanoBonus),
	locName.BeachBonusReward:            LocationData(367759250, "obj_quest_rubie_bag_50_2",        "Beach Bonus Reward",              "BonusReward", False, False, itemName.BeachBonus),
	locName.RiverBonusReward:            LocationData(367759251, "obj_quest_rubie_bag_50_3",        "River Bonus Reward",              "BonusReward", False, False, itemName.RiverBonus),
	locName.HillsBonusReward:            LocationData(367759252, "obj_quest_rubie_bag_75_1",        "Hills Bonus Reward",              "BonusReward", False, False, itemName.HillsBonus),
	locName.FortBonusReward:             LocationData(367759253, "obj_quest_rubie_bag_75_2",        "Fort Bonus Reward",               "BonusReward", False, False, itemName.FortBonus),
	locName.CastleBonusReward:           LocationData(367759254, "obj_null",                        "Castle Bonus Reward",             "BonusReward", False, True, itemName.CastleBonus),
	locName.LairBonusReward:             LocationData(367759255, "obj_quest_rubie_bag_100",         "Lair Bonus Reward",               "BonusReward", False, False, itemName.LairBonus)
}

levelunlock_locations = {
	locName.Default1:                    LocationData(367759256, "world_faramore_town_unlocked",    "Default 1",                       "LevelUnlock", False, False, None),
	locName.Default2:                    LocationData(367759257, "world_durridin_forest_unlocked",  "Default 2",                       "LevelUnlock", False, False, None),
	locName.ForestBeacon1:               LocationData(367759258, "world_cogwyn_caves_unlocked",     "Forest Beacon 1",                 "LevelUnlock", False, False, itemName.ForestBeacon),
	locName.ForestBeacon2:               LocationData(367759259, "world_anju_desert_unlocked",      "Forest Beacon 2",                 "LevelUnlock", False, False, itemName.ForestBeacon),
	locName.ForestBeacon3:               LocationData(367759260, "world_creece_canyon_unlocked",    "Forest Beacon 3",                 "LevelUnlock", False, False, itemName.ForestBeacon),
	locName.DesertBeacon1:               LocationData(367759261, "world_norin_swamp_unlocked",      "Desert Beacon 1",                 "LevelUnlock", False, False, itemName.DesertBeacon),
	locName.DesertBeacon2:               LocationData(367759262, "world_chillinax_peaks_unlocked",  "Desert Beacon 2",                 "LevelUnlock", False, False, itemName.DesertBeacon),
	locName.DesertBeacon3:               LocationData(367759263, "world_boanjale_crypts_unlocked",  "Desert Beacon 3",                 "LevelUnlock", False, False, itemName.DesertBeacon),
	locName.SwampBeacon1:                LocationData(367759264, "world_sprigum_volcano_unlocked",  "Swamp Beacon 1",                  "LevelUnlock", False, False, itemName.SwampBeacon),
	locName.SwampBeacon2:                LocationData(367759265, "world_badonc_beach_unlocked",     "Swamp Beacon 2",                  "LevelUnlock", False, False, itemName.SwampBeacon),
	locName.SwampBeacon3:                LocationData(367759266, "world_ryha_river_unlocked",       "Swamp Beacon 3",                  "LevelUnlock", False, False, itemName.SwampBeacon),
	locName.BeachBeacon1:                LocationData(367759267, "world_lichen_hills_unlocked",     "Beach Beacon 1",                  "LevelUnlock", False, False, itemName.BeachBeacon),
	locName.BeachBeacon2:                LocationData(367759268, "world_fort_findula_unlocked",     "Beach Beacon 2",                  "LevelUnlock", False, False, itemName.BeachBeacon),
	locName.HillsBeacon1:                LocationData(367759269, "world_dennys_castle_unlocked",    "Hills Beacon 1",                  "LevelUnlock", False, False, itemName.HillsBeacon),
	locName.HillsBeacon2:                LocationData(367759270, "world_daimurs_lair_unlocked",     "Hills Beacon 2",                  "LevelUnlock", False, False, itemName.HillsBeacon)
}

all_locations = {
    **faramore_locations,
	**forest_locations,
	**caves_locations,
	**desert_locations,
	**canyon_locations,
	**swamp_locations,
	**peak_locations,
	**crypts_locations,
	**volcano_locations,
	**beach_locations,
	**river_locations,
	**hills_locations,
	**fort_locations,
	**castle_locations,
	**lair_locations,
    **from_npc_locations,
    **npc_spawn_locations,
    **npc_foolish_locations,
    **npc_locked_locations,
    **rock_locations,
    **bonusreward_locations,
    **levelunlock_locations
}