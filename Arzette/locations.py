from BaseClasses import Location
import typing

class ArzetteLocation(Location):
    game: str = "Arzette: The Jewel of Faramore"

class LocationData(typing.NamedTuple):
    arzid: int | None
    # Default vanilla item code at this location
    # The reason this is here and not in ItemData is because the only fungible items 
    # (rudy races and null bonus rewards) are at multiple locations by default
    # Since all other items are non-fungible, it was easier to give the same internal name
    # to items and locations and put the item_code here
    item_code: str
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
	"Faramore Key (Well)":             LocationData(2793883001, "key_faramore_2",                  "Key",         True, False, "Faramore"),
	"Faramore Key (Tavern)":           LocationData(2793883002, "key_faramore_1",                  "Key",         True, False, "Faramore"),
	"Faramore Bonus":                  LocationData(2793883003, "obj_bonus_scroll_1",              "Scroll",      True, False, "Faramore"),
	"Faramore Candle (Empty House)":   LocationData(2793883004, "obj_sacred_candle_24",            "Candle",      True, False, "Faramore"),
	"Faramore Candle (Cypress House)": LocationData(2793883005, "obj_sacred_candle_25",            "Candle",      True, False, "Faramore"),
	"Faramore Coin":                   LocationData(2793883006, "obj_hidden_coin_faramore",        "Coin",        True, False, "Faramore")
}

forest_locations = {
	"Bombs":                           LocationData(2793883007, "obj_quest_bombs",                 "Quest",       True, False, "Forest"),
	"Forest Bag (First Room 1)":       LocationData(2793883008, "obj_item_bag_1",                  "Bag",         True, False, "Forest"),
	"Forest Bag (First Room 2)":       LocationData(2793883009, "obj_item_bag_2",                  "Bag",         True, False, "Forest"),
	"Forest Key":                      LocationData(2793883010, "key_durridin",                    "Key",         True, False, "Forest"),
	"Forest Bonus":                    LocationData(2793883011, "obj_bonus_scroll_2",              "Scroll",      True, False, "Forest"),
	"Forest Candle (Tree)":            LocationData(2793883012, "obj_sacred_candle_1",             "Candle",      True, False, "Forest"),
	"Forest Candle (Cypress)":         LocationData(2793883013, "obj_sacred_candle_2",             "Candle",      True, False, "Forest"),
	"Forest Coin":                     LocationData(2793883014, "obj_hidden_coin_durridin",        "Coin",        True, False, "Forest"),
	"Forest Bag (Sword Wave)":         LocationData(2793883015, "obj_item_bag_3",                  "Bag",         True, False, "Forest"),
	"Sword Wave":                      LocationData(2793883016, "obj_quest_sword_wave",            "Quest",       True, False, "Forest"),
	"Golden Fly":                      LocationData(2793883017, "obj_quest_golden_fly",            "Quest",       True, False, "Forest"),
	"Forest Bag (Last Room)":          LocationData(2793883018, "obj_item_bag_4",                  "Bag",         True, False, "Forest"),
	"Forest Beacon":                   LocationData(2793883019, "beacon_durridin",                 "Beacon",      True, False, "Forest"),
	"Forest Jewel":                    LocationData(2793883020, "obj_jof_1",                       "Jewel",       False, False, "Forest"),
	"Magic Armor":                     LocationData(2793883021, "obj_quest_armor",                 "Quest",       True, False, "Forest")
}

caves_locations = {
	"Silver Cricket":                  LocationData(2793883022, "obj_quest_silver_cricket",        "Quest",       True, False, "Caves"),
	"Rope Ladder":                     LocationData(2793883023, "obj_quest_rope_ladder",           "Quest",       True, False, "Caves"),
	"Caves Bag (Rope Ladder)":         LocationData(2793883024, "obj_item_bag_5",                  "Bag",         True, False, "Caves"),
	"Caves Candle (First Dark Room)":  LocationData(2793883025, "obj_sacred_candle_5",             "Candle",      True, False, "Caves"),
	"Caves Coin":                      LocationData(2793883026, "obj_hidden_coin_cogwyn",          "Coin",        True, False, "Caves"),
	"Caves Candle (Second Dark Room)": LocationData(2793883027, "obj_sacred_candle_26",            "Candle",      True, False, "Caves"),
	"Caves Bonus":                     LocationData(2793883028, "obj_bonus_scroll_3",              "Scroll",      True, False, "Caves"),
	"Caves Bag (Last Room)":           LocationData(2793883029, "obj_item_bag_6",                  "Bag",         True, False, "Caves"),
	"Shield Ring":                     LocationData(2793883030, "obj_quest_shield_ring",           "Quest",       True, False, "Caves")
}

desert_locations = {
	"Desert Coin":                     LocationData(2793883031, "obj_hidden_coin_anju",            "Coin",        True, False, "Desert"),
	"Desert Bag (First Room 1)":       LocationData(2793883032, "obj_item_bag_7",                  "Bag",         True, False, "Desert"),
	"Desert Bag (First Room 2)":       LocationData(2793883033, "obj_item_bag_8",                  "Bag",         True, False, "Desert"),
	"Compass":                         LocationData(2793883034, "obj_quest_compass",               "Quest",       True, False, "Desert"),
	"Desert Candle (Pit)":             LocationData(2793883035, "obj_sacred_candle_3",             "Candle",      True, False, "Desert"),
	"Desert Bonus":                    LocationData(2793883036, "obj_bonus_scroll_4",              "Scroll",      True, False, "Desert"),
	"Desert Key":                      LocationData(2793883037, "key_anju",                        "Key",         True, False, "Desert"),
	"Desert Candle (Last Room)":       LocationData(2793883038, "obj_sacred_candle_4",             "Candle",      False, False, "Desert"),
	"Desert Life-Up":                  LocationData(2793883039, "obj_lifeup_1",                    "LifeUp",      True, False, "Desert"),
	"Desert Bag (Last Room)":          LocationData(2793883040, "obj_item_bag_9",                  "Bag",         True, False, "Desert"),
	"Desert Beacon":                   LocationData(2793883041, "beacon_anju_desert",              "Beacon",      True, False, "Desert")
}

canyon_locations = {
	"Canyon Bonus":                    LocationData(2793883042, "obj_bonus_scroll_5",              "Scroll",      True, False, "Canyon"),
	"Canyon Bag (Before Checkpoint)":  LocationData(2793883043, "obj_item_bag_10",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 1)": LocationData(2793883044, "obj_item_bag_11",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 2)": LocationData(2793883045, "obj_item_bag_12",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 3)": LocationData(2793883046, "obj_item_bag_13",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (First Room End)":     LocationData(2793883047, "obj_item_bag_14",                 "Bag",         True, False, "Canyon"),
	"Canyon Candle (First Room End)":  LocationData(2793883048, "obj_sacred_candle_6",             "Candle",      True, False, "Canyon"),
	"Canyon Jewel":                    LocationData(2793883049, "obj_jof_2",                       "Jewel",       False, False, "Canyon"),
	"Canyon Key":                      LocationData(2793883050, "key_creece",                      "Key",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 1)":    LocationData(2793883051, "obj_item_bag_15",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 2)":    LocationData(2793883052, "obj_item_bag_16",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 3)":    LocationData(2793883053, "obj_item_bag_17",                 "Bag",         True, False, "Canyon"),
	"Canyon Coin":                     LocationData(2793883054, "obj_hidden_coin_creece",          "Coin",        True, False, "Canyon"),
	"Canyon Bag (Motte House)":        LocationData(2793883055, "obj_item_bag_18",                 "Bag",         True, False, "Canyon"),
	"Canyon Candle (Motte House)":     LocationData(2793883056, "obj_sacred_candle_7",             "Candle",      True, False, "Canyon")
}

swamp_locations = {
	"Swamp Candle (First Room)":       LocationData(2793883057, "obj_sacred_candle_8",             "Candle",      True, False, "Swamp"),
	"Swamp Bag (First Room)":          LocationData(2793883058, "obj_item_bag_19",                 "Bag",         True, False, "Swamp"),
	"Swamp Coin":                      LocationData(2793883059, "obj_hidden_coin_norin",           "Coin",        True, False, "Swamp"),
	"Swamp Key (Frich House)":         LocationData(2793883060, "key_norin",                       "Key",         True, False, "Swamp"),
	"Swamp Candle (Frich House)":      LocationData(2793883061, "obj_sacred_candle_27",            "Candle",      True, False, "Swamp"),
	"Swamp Key (Griffin Boots)":       LocationData(2793883062, "key_norin_2",                     "Key",         True, False, "Swamp"),
	"Griffin Boots":                   LocationData(2793883063, "obj_quest_magic_boots",           "Quest",       True, False, "Swamp"),
	"Swamp Plant":                     LocationData(2793883064, "obj_quest_plant_a",               "Plant",       False, False, "Swamp"),
	"Swamp Bonus":                     LocationData(2793883065, "obj_bonus_scroll_6",              "Scroll",      True, False, "Swamp"),
	"Swamp Beacon":                    LocationData(2793883066, "beacon_norin_swamp",              "Beacon",      True, False, "Swamp")
}

peak_locations = {
	"Peak Candle (First Cave)":        LocationData(2793883067, "obj_sacred_candle_9",             "Candle",      True, False, "Peak"),
	"Peak Bag (First Cave 1)":         LocationData(2793883068, "obj_item_bag_20",                 "Bag",         True, False, "Peak"),
	"Peak Bag (First Cave 2)":         LocationData(2793883069, "obj_item_bag_21",                 "Bag",         True, False, "Peak"),
	"Peak Bonus":                      LocationData(2793883070, "obj_bonus_scroll_7",              "Scroll",      True, False, "Peak"),
	"Peak Coin":                       LocationData(2793883071, "obj_hidden_coin_chillinax",       "Coin",        True, False, "Peak"),
	"Peak Key":                        LocationData(2793883072, "key_chillinax",                   "Key",         True, False, "Peak"),
	"Peak Candle (Ciclena Cave)":      LocationData(2793883073, "obj_sacred_candle_10",            "Candle",      True, False, "Peak"),
	"Peak Bag (Before Apatu)":         LocationData(2793883074, "obj_item_bag_22",                 "Bag",         True, False, "Peak"),
	"Peak Jewel":                      LocationData(2793883075, "obj_jof_3",                       "Jewel",       False, False, "Peak"),
	"Peak Bag (After Apatu)":          LocationData(2793883076, "obj_item_bag_23",                 "Bag",         True, False, "Peak")
}

crypts_locations = {
	"Crypts Life-Up":                  LocationData(2793883077, "obj_lifeup_2",                    "LifeUp",      True, False, "Crypts"),
	"Bell":                            LocationData(2793883078, "obj_quest_town_bell",             "Quest",       True, False, "Crypts"),
	"Crypts Bonus":                    LocationData(2793883079, "obj_bonus_scroll_8",              "Scroll",      True, False, "Crypts"),
	"Crypts Key":                      LocationData(2793883080, "key_boanjale",                    "Key",         True, False, "Crypts"),
	"Crypts Bag (Crypt)":              LocationData(2793883081, "obj_item_bag_46",                 "Bag",         True, False, "Crypts"),
	"Crypts Candle (After Crypt)":     LocationData(2793883082, "obj_sacred_candle_28",            "Candle",      True, False, "Crypts"),
	"Crypts Coin":                     LocationData(2793883083, "obj_hidden_coin_boanjale",        "Coin",        True, False, "Crypts"),
	"Crypts Candle (Skelvis)":         LocationData(2793883084, "obj_sacred_candle_11",            "Candle",      True, False, "Crypts"),
	"Crypts Bag (Skelvis)":            LocationData(2793883085, "obj_item_bag_24",                 "Bag",         True, False, "Crypts")
}

volcano_locations = {
	"Volcano Bonus":                   LocationData(2793883086, "obj_bonus_scroll_9",              "Scroll",      True, False, "Volcano"),
	"Volcano Candle (First Room)":     LocationData(2793883087, "obj_sacred_candle_12",            "Candle",      True, False, "Volcano"),
	"Volcano Coin":                    LocationData(2793883088, "obj_hidden_coin_sprigum",         "Coin",        True, False, "Volcano"),
	"Volcano Candle (Last Room)":      LocationData(2793883089, "obj_sacred_candle_29",            "Candle",      True, False, "Volcano"),
	"Crystal of Refraction":           LocationData(2793883090, "obj_quest_crystal_of_refraction", "Quest",       True, False, "Volcano")
}

beach_locations = {
	"Beach Bag (First Room)":          LocationData(2793883091, "obj_item_bag_25",                 "Bag",         True, False, "Beach"),
	"Beach Key (First House)":         LocationData(2793883092, "key_badonc",                      "Key",         True, False, "Beach"),
	"Beach Coin":                      LocationData(2793883093, "obj_hidden_coin_badonc",          "Coin",        True, False, "Beach"),
	"Beach Key (Tork Cabin)":          LocationData(2793883094, "key_badonc_2",                    "Key",         True, False, "Beach"),
	"Beach Candle (Tork Cabin)":       LocationData(2793883095, "obj_sacred_candle_14",            "Candle",      True, False, "Beach"),
	"Beach Plant":                     LocationData(2793883096, "obj_quest_plant_b",               "Plant",       True, False, "Beach"),
	"Beach Bonus":                     LocationData(2793883097, "obj_bonus_scroll_10",             "Scroll",      True, False, "Beach"),
	"Beach Candle (Cave)":             LocationData(2793883098, "obj_sacred_candle_13",            "Candle",      True, False, "Beach"),
	"Fatal Flute":                     LocationData(2793883099, "obj_quest_flute",                 "Quest",       True, False, "Beach"),
	"Beach Beacon":                    LocationData(2793883100, "beacon_badonc_beach",             "Beacon",      True, False, "Beach")
}

river_locations = {
	"River Key (Francine)":            LocationData(2793883101, "key_ryha",                        "Key",         True, False, "River"),
	"River Bonus":                     LocationData(2793883102, "obj_bonus_scroll_11",             "Scroll",      True, False, "River"),
	"River Candle (Boat)":             LocationData(2793883103, "obj_sacred_candle_15",            "Candle",      True, False, "River"),
	"River Key (Submarine)":           LocationData(2793883104, "key_ryha_2",                      "Key",         False, False, "River"),
	"River Coin":                      LocationData(2793883105, "obj_hidden_coin_ryha",            "Coin",        True, False, "River"),
	"Blue Magic":                      LocationData(2793883106, "obj_quest_blue_beam",             "Quest",       True, False, "River"),
	"River Bag (Last Room)":           LocationData(2793883107, "obj_item_bag_26",                 "Bag",         True, False, "River"),
	"River Candle (Last Room)":        LocationData(2793883108, "obj_sacred_candle_16",            "Candle",      True, False, "River"),
	"River Life-Up":                   LocationData(2793883109, "obj_lifeup_3",                    "LifeUp",      True, False, "River")
}

hills_locations = {
	"Hills Candle (Cave)":             LocationData(2793883110, "obj_sacred_candle_30",            "Candle",      True, False, "Hills"),
	"Lightning Sword":                 LocationData(2793883111, "obj_quest_electric_sword",        "Quest",       True, False, "Hills"),
	"Hills Coin":                      LocationData(2793883112, "obj_hidden_coin_lichen",          "Coin",        True, False, "Hills"),
	"Hills Bonus":                     LocationData(2793883113, "obj_bonus_scroll_12",             "Scroll",      True, False, "Hills"),
	"Hills Bag (Barn)":                LocationData(2793883114, "obj_item_bag_27",                 "Bag",         True, False, "Hills"),
	"Hills Key":                       LocationData(2793883115, "key_lichen",                      "Key",         True, False, "Hills"),
	"Hills Bag (Music Shrine)":        LocationData(2793883116, "obj_item_bag_28",                 "Bag",         True, False, "Hills"),
	"Hills Candle (Music Shrine)":     LocationData(2793883117, "obj_sacred_candle_17",            "Candle",      True, False, "Hills"),
	"Hills Plant":                     LocationData(2793883118, "obj_quest_plant_c",               "Plant",       True, False, "Hills"),
	"Hills Beacon":                    LocationData(2793883119, "beacon_lichen_hills",             "Beacon",      True, False, "Hills")
}

fort_locations = {
	"Fort Bag (Dungeon 1)":            LocationData(2793883120, "obj_item_bag_29",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 2)":            LocationData(2793883121, "obj_item_bag_30",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 3)":            LocationData(2793883122, "obj_item_bag_31",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 4)":            LocationData(2793883123, "obj_item_bag_32",                 "Bag",         True, False, "Fort"),
	"Sacred Oil":                      LocationData(2793883124, "obj_quest_oil",                   "Trading",     True, False, "Fort"),
	"Fort Key (First Room)":           LocationData(2793883125, "key_findula_1",                   "Key",         True, False, "Fort"),
	"Fort Candle (Dark Room)":         LocationData(2793883126, "obj_sacred_candle_18",            "Candle",      True, False, "Fort"),
	"Fort Bag (Dark Room)":            LocationData(2793883127, "obj_item_bag_33",                 "Bag",         True, False, "Fort"),
	"Enchanted Shoes":                 LocationData(2793883128, "obj_quest_shoes",                 "Quest",       True, False, "Fort"),
	"Fort Coin":                       LocationData(2793883129, "obj_hidden_coin_findula",         "Coin",        True, False, "Fort"),
	"Fort Key (Top Room)":             LocationData(2793883130, "key_findula_2",                   "Key",         True, False, "Fort"),
	"Fort Bag (Top Room 1)":           LocationData(2793883131, "obj_item_bag_34",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Top Room 2)":           LocationData(2793883132, "obj_item_bag_35",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Top Room 3)":           LocationData(2793883133, "obj_item_bag_36",                 "Bag",         True, False, "Fort"),
	"Fort Candle (Last Room)":         LocationData(2793883134, "obj_sacred_candle_19",            "Candle",      True, False, "Fort"),
	"Fort Bag (Last Room)":            LocationData(2793883135, "obj_item_bag_37",                 "Bag",         True, False, "Fort"),
	"Reflector Ring":                  LocationData(2793883136, "obj_quest_reflecting_shield",     "Quest",       True, False, "Fort"),
	"Fort Jewel":                      LocationData(2793883137, "obj_jof_4",                       "Jewel",       False, False, "Fort"),
	"Fort Bonus":                      LocationData(2793883138, "obj_bonus_scroll_13",             "Scroll",      True, False, "Fort")
}

castle_locations = {
	"Castle Bag (Entrance)":           LocationData(2793883139, "obj_item_bag_38",                 "Bag",         True, False, "Castle"),
	"Castle Candle (Right Room)":      LocationData(2793883140, "obj_sacred_candle_20",            "Candle",      True, False, "Castle"),
	"Castle Key (Nodelki)":            LocationData(2793883141, "key_denny_2",                     "Key",         True, False, "Castle"),
	"Castle Candle (Top Room)":        LocationData(2793883142, "obj_sacred_candle_21",            "Candle",      True, False, "Castle"),
	"Castle Bag (Top Room)":           LocationData(2793883143, "obj_item_bag_39",                 "Bag",         True, False, "Castle"),
	"Winged Belt":                     LocationData(2793883144, "obj_quest_winged_belt",           "Quest",       True, False, "Castle"),
	"Castle Coin":                     LocationData(2793883145, "obj_hidden_coin_denny",           "Coin",        True, False, "Castle"),
	"Castle Key (Left Room)":          LocationData(2793883146, "key_denny_1",                     "Key",         True, False, "Castle"),
	"Castle Bag (Bonus)":              LocationData(2793883147, "obj_item_bag_40",                 "Bag",         True, False, "Castle"),
	"Castle Bonus":                    LocationData(2793883148, "obj_bonus_scroll_14",             "Scroll",      True, False, "Castle"),
	"Castle Jewel":                    LocationData(2793883149, "obj_jof_5",                       "Jewel",       False, False, "Castle")
}

lair_locations = {
	"Lair Candle (Tree Trunk)":        LocationData(2793883150, "obj_sacred_candle_22",            "Candle",      True, False, "Lair"),
	"Lair Candle (Tree Top)":          LocationData(2793883151, "obj_sacred_candle_23",            "Candle",      True, False, "Lair"),
	"Lair Bonus":                      LocationData(2793883152, "obj_bonus_scroll_15",             "Scroll",      True, False, "Lair"),
	"Lair Bag (First Room)":           LocationData(2793883153, "obj_item_bag_41",                 "Bag",         True, False, "Lair"),
	"Lair Coin":                       LocationData(2793883154, "obj_hidden_coin_daimur",          "Coin",        True, False, "Lair"),
	"Lair Bag (Lava Room)":            LocationData(2793883155, "obj_item_bag_42",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 1)":         LocationData(2793883156, "obj_item_bag_43",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 2)":         LocationData(2793883157, "obj_item_bag_44",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 3)":         LocationData(2793883158, "obj_item_bag_45",                 "Bag",         True, False, "Lair"),
	"Daimur":                          LocationData(2793883159, "obj_boss_daimur",                 "Other",       False, True, "Lair")
}

from_npc_locations = {
	"Purple Magic":                    LocationData(2793883160, "obj_quest_sword",                 "Quest",       False, False, "Faramore Yukeen"),
	"Citizenship Papers":              LocationData(2793883161, "obj_quest_citizenship",           "Quest",       False, False, "Faramore Covenplate"),
	"Power Stone Upgrade":             LocationData(2793883162, "obj_quest_upgrade_power_stones",  "Upgrade",     False, False, "Faramore Kari Quest"),
	"Dungeon Key":                     LocationData(2793883163, "key_findula_dungeon",             "Trading",     False, False, "Faramore Alven"),
	"Chainsword":                      LocationData(2793883164, "obj_quest_chainsword",            "Trading",     False, False, "Faramore Alven"),
	"Canteen":                         LocationData(2793883165, "obj_quest_canteen",               "Quest",       False, False, "Faramore Brinda"),
	"Wallet Upgrade":                  LocationData(2793883166, "obj_quest_upgrade_wallet",        "Upgrade",     False, False, "Faramore Frich"),
	"Infinite Soulfire":               LocationData(2793883167, "obj_quest_infinite_soulfire",     "Upgrade",     False, False, "Faramore Rudy"),
	"Bomb Upgrade":                    LocationData(2793883168, "obj_quest_upgrade_bombs",         "Upgrade",     False, False, "Faramore Barnabuss"),
	"Calendar":                        LocationData(2793883169, "obj_quest_beach_calendar",        "Quest",       False, False, "Faramore Denny"),
	"200 Rupees":                      LocationData(2793883170, "obj_quest_dewey_reward",          "Quest",       False, False, "Faramore Dewey"),
	"Lamp Oil Upgrade":                LocationData(2793883171, "obj_quest_upgrade_lamp_oil",      "Upgrade",     False, False, "Faramore Cypress"),
	"Rope Upgrade":                    LocationData(2793883172, "obj_quest_upgrade_ropes",         "Upgrade",     False, False, "Faramore Munhum"),
	"Forest Race 100 Rupees":          LocationData(2793883173, "obj_quest_race_reward_1",         "Race",        False, False, "Faramore Rudy"),
	"Peak Race 100 Rupees":            LocationData(2793883174, "obj_quest_race_reward_2",         "Race",        False, False, "Faramore Rudy"),
	"Hills Race 100 Rupees":           LocationData(2793883175, "obj_quest_race_reward_3",         "Race",        False, False, "Faramore Rudy"),
	"Lantern":                         LocationData(2793883176, "obj_quest_lantern",               "Quest",       False, False, "Forest Cypress"),
	"Rope":                            LocationData(2793883177, "obj_quest_esc_rope",              "Quest",       False, False, "Caves Munhum"),
	"Snail Salt":                      LocationData(2793883178, "obj_quest_snail_salt",            "Trading",     False, False, "Caves Ellido"),
	"Fairy Dust":                      LocationData(2793883179, "obj_quest_fairy_dust",            "Quest",       False, False, "Desert Fairy"),
	"Backstep":                        LocationData(2793883180, "obj_quest_backstep",              "Quest",       False, False, "Canyon Crowdee"),
	"Smart Gun":                       LocationData(2793883181, "obj_quest_gun",                   "Quest",       False, False, "Canyon Motte"),
	"Star Earrings":                   LocationData(2793883182, "obj_quest_star_earrings",         "Quest",       False, False, "Canyon Odie"),
	"Ogre Hair":                       LocationData(2793883183, "obj_quest_ogre_hair",             "Trading",     False, False, "Swamp Glubbert"),
	"Power Pendant":                   LocationData(2793883184, "obj_quest_pendant",               "Quest",       False, False, "Peak Ciclena"),
	"Bomb Gauntlet":                   LocationData(2793883185, "obj_quest_pg",                    "Quest",       False, False, "Crypts Skelvis"),
	"Speedy Shoes":                    LocationData(2793883186, "obj_quest_speedy_shoes",          "Quest",       False, False, "Beach Fleetus"),
	"Magic Cloak":                     LocationData(2793883187, "obj_quest_magic_cloak",           "Quest",       False, False, "Beach Tork"),
	"Cleaver Shovel":                  LocationData(2793883188, "obj_quest_cleaver_shovel",        "Trading",     False, False, "River Francine"),
	"Oil and Chains":                  LocationData(2793883189, "obj_quest_refined_chains",        "Trading",     False, False, "River Morgh"),
	"Double Wave":                     LocationData(2793883190, "obj_quest_double_wave",           "Quest",       False, False, "Hills Milbert"),
	"Funky Fungus":                    LocationData(2793883191, "obj_quest_funky_fungus",          "Trading",     False, False, "Lair Zazie"),
	"Soul Upgrade":                    LocationData(2793883192, "obj_quest_upgrade_soul_bag",      "Upgrade",     False, False, "Lair Zazie")
}

npc_spawn_locations = {
	"Faramore Kari Quest":             LocationData(2793883193, "npc_kari_quest",                  "NPCSpawner",  True, False, "Faramore"),
	"Caves Ellido":                    LocationData(2793883194, "npc_ellido",                      "NPCSpawner",  True, False, "Caves"),
	"Canyon Crowdee":                  LocationData(2793883195, "npc_crowdee",                     "NPCSpawner",  True, False, "Canyon"),
	"Swamp Glubbert":                  LocationData(2793883196, "npc_glubbert",                    "NPCSpawner",  True, False, "Swamp"),
	"Faramore Barnabuss":              LocationData(2793883197, "npc_barnabuss_quest",             "NPCSpawner",  True, False, "Faramore"),
	"Faramore Dewey":                  LocationData(2793883198, "npc_dewey",                       "NPCSpawner",  True, False, "Faramore"),
	"Hills Milbert":                   LocationData(2793883199, "npc_milbert",                     "NPCSpawner",  True, False, "Hills"),
	"Canyon Odie":                     LocationData(2793883200, "npc_odie",                        "NPCSpawner",  True, False, "Canyon"),
	"Crypts Skelvis":                  LocationData(2793883201, "npc_skelvis",                     "NPCSpawner",  True, False, "Crypts"),
	"Beach Tork":                      LocationData(2793883202, "npc_tork",                        "NPCSpawner",  True, False, "Beach"),
	"Peak Ciclena":                    LocationData(2793883203, "npc_ciclena",                     "NPCSpawner",  True, False, "Peak"),
	"Forest Cypress":                  LocationData(2793883204, "npc_cypress",                     "NPCSpawner",  True, False, "Forest"),
	"River Morgh":                     LocationData(2793883205, "npc_morgh",                       "NPCSpawner",  True, False, "River"),
	"Desert Fairy":                    LocationData(2793883206, "npc_fairy",                       "NPCSpawner",  True, False, "Desert"),
	"Faramore Covenplate":             LocationData(2793883207, "npc_mayor",                       "NPCSpawner",  True, False, "Faramore"),
	"Faramore Rudy":                   LocationData(2793883208, "npc_rudy",                        "NPCSpawner",  True, False, "Faramore"),
	"Faramore Munhum":                 LocationData(2793883209, "npc_munhum_quest",                "NPCSpawner",  True, False, "Faramore"),
	"Canyon Motte":                    LocationData(2793883210, "npc_motte",                       "NPCSpawner",  True, False, "Canyon"),
	"Faramore Cypress":                LocationData(2793883211, "npc_cypress_quest",               "NPCSpawner",  True, False, "Faramore"),
	"River Francine":                  LocationData(2793883212, "npc_francine",                    "NPCSpawner",  True, False, "River"),
	"Faramore Alven":                  LocationData(2793883213, "npc_alven",                       "NPCSpawner",  True, False, "Faramore"),
	"Faramore Frich":                  LocationData(2793883214, "npc_frich_quest",                 "NPCSpawner",  True, False, "Faramore"),
	"Faramore Yukeen":                 LocationData(2793883215, "npc_yukeen",                      "NPCSpawner",  True, False, "Faramore"),
	"Lair Zazie":                      LocationData(2793883216, "npc_zazie",                       "NPCSpawner",  True, False, "Lair"),
	"Beach Fleetus":                   LocationData(2793883217, "npc_fleetus",                     "NPCSpawner",  True, False, "Beach"),
	"Faramore Brinda":                 LocationData(2793883218, "npc_brinda",                      "NPCSpawner",  True, False, "Faramore"),
	"Caves Munhum":                    LocationData(2793883219, "npc_munhum",                      "NPCSpawner",  True, False, "Caves"),
	"Faramore Denny":                  LocationData(2793883220, "npc_denny",                       "NPCSpawner",  True, False, "Faramore")
}

npc_foolish_locations = {
	"Faramore Boru":                   LocationData(2793883221, "npc_boru",                        "NPC",         True, False, "Faramore"),
	"Faramore Kari":                   LocationData(2793883222, "npc_kari",                        "NPC",         True, False, "Faramore"),
	"Faramore Univor":                 LocationData(2793883223, "npc_univor",                      "NPC",         True, False, "Faramore"),
	"Faramore Salvik":                 LocationData(2793883224, "npc_salvik",                      "NPC",         True, False, "Faramore"),
	"Faramore Maki":                   LocationData(2793883225, "npc_maki",                        "NPC",         True, False, "Faramore"),
	"Faramore Payop":                  LocationData(2793883226, "npc_payop",                       "NPC",         True, False, "Faramore"),
	"Volcano Joe":                     LocationData(2793883227, "npc_joe",                         "NPC",         True, False, "Volcano"),
	"River Barnabuss":                 LocationData(2793883228, "npc_barnabuss",                   "NPC",         True, False, "River")
}

npc_locked_locations = {
	"Faramore Mortar":                 LocationData(2793883229, "npc_mortar",                      "NPC",         False, True, "Faramore"),
	"Swamp Frich":                     LocationData(2793883230, "npc_frich",                       "NPC",         False, True, "Swamp"),
	"Forest Rudy (Start)":             LocationData(2793883231, "npc_rudy_start",                  "NPC",         False, True, "Forest"),
	"Forest Rudy (End)":               LocationData(2793883232, "npc_rudy_goal",                   "NPC",         False, True, "Forest"),
	"Peak Rudy (Start)":               LocationData(2793883233, "npc_rudy_start",                  "NPC",         False, True, "Peak"),
	"Peak Rudy (End)":                 LocationData(2793883234, "npc_rudy_goal",                   "NPC",         False, True, "Peak"),
	"Hills Rudy (Start)":              LocationData(2793883235, "npc_rudy_start",                  "NPC",         False, True, "Hills"),
	"Hills Rudy (End)":                LocationData(2793883236, "npc_rudy_goal",                   "NPC",         False, True, "Hills")
}

rock_locations = {
	"Orange Rock":                     LocationData(2793883237, "obj_quest_rock_orange",           "Rock",        False, False, None),
	"Brown Rock":                      LocationData(2793883238, "obj_quest_rock_brown",            "Rock",        False, False, None),
	"Gray Rock":                       LocationData(2793883239, "obj_quest_rock_grey",             "Rock",        False, False, None),
	"Blue Rock":                       LocationData(2793883240, "obj_quest_rock_blue",             "Rock",        False, False, None)
}

bonusreward_locations = {
	"Faramore Bonus Reward":           LocationData(2793883241, "obj_null",                        "BonusReward", False, True, "Faramore Bonus"),
	"Forest Bonus Reward":             LocationData(2793883242, "obj_quest_rubie_bag_25_1",        "BonusReward", False, False, "Forest Bonus"),
	"Caves Bonus Reward":              LocationData(2793883243, "obj_quest_rubie_bag_25_2",        "BonusReward", False, False, "Caves Bonus"),
	"Desert Bonus Reward":             LocationData(2793883244, "obj_quest_rubie_bag_30_1",        "BonusReward", False, False, "Desert Bonus"),
	"Canyon Bonus Reward":             LocationData(2793883245, "obj_quest_rubie_bag_30_2",        "BonusReward", False, False, "Canyon Bonus"),
	"Swamp Bonus Reward":              LocationData(2793883246, "obj_quest_rubie_bag_30_3",        "BonusReward", False, False, "Swamp Bonus"),
	"Peak Bonus Reward":               LocationData(2793883247, "obj_quest_rubie_bag_40",          "BonusReward", False, False, "Peak Bonus"),
	"Crypts Bonus Reward":             LocationData(2793883248, "obj_quest_rubie_bag_50_1",        "BonusReward", False, False, "Crypts Bonus"),
	"Volcano Bonus Reward":            LocationData(2793883249, "obj_null",                        "BonusReward", False, True, "Volcano Bonus"),
	"Beach Bonus Reward":              LocationData(2793883250, "obj_quest_rubie_bag_50_2",        "BonusReward", False, False, "Beach Bonus"),
	"River Bonus Reward":              LocationData(2793883251, "obj_quest_rubie_bag_50_3",        "BonusReward", False, False, "River Bonus"),
	"Hills Bonus Reward":              LocationData(2793883252, "obj_quest_rubie_bag_75_1",        "BonusReward", False, False, "Hills Bonus"),
	"Fort Bonus Reward":               LocationData(2793883253, "obj_quest_rubie_bag_75_2",        "BonusReward", False, False, "Fort Bonus"),
	"Castle Bonus Reward":             LocationData(2793883254, "obj_null",                        "BonusReward", False, True, "Castle Bonus"),
	"Lair Bonus Reward":               LocationData(2793883255, "obj_quest_rubie_bag_100",         "BonusReward", False, False, "Lair Bonus")
}

levelunlock_locations = {
	"Default 1":                       LocationData(2793883256, "world_faramore_town_unlocked",    "LevelUnlock", False, False, None),
	"Default 2":                       LocationData(2793883257, "world_durridin_forest_unlocked",  "LevelUnlock", False, False, None),
	"Forest Beacon 1":                 LocationData(2793883258, "world_cogwyn_caves_unlocked",     "LevelUnlock", False, False, "Forest Beacon"),
	"Forest Beacon 2":                 LocationData(2793883259, "world_anju_desert_unlocked",      "LevelUnlock", False, False, "Forest Beacon"),
	"Forest Beacon 3":                 LocationData(2793883260, "world_creece_canyon_unlocked",    "LevelUnlock", False, False, "Forest Beacon"),
	"Desert Beacon 1":                 LocationData(2793883261, "world_norin_swamp_unlocked",      "LevelUnlock", False, False, "Desert Beacon"),
	"Desert Beacon 2":                 LocationData(2793883262, "world_chillinax_peaks_unlocked",  "LevelUnlock", False, False, "Desert Beacon"),
	"Desert Beacon 3":                 LocationData(2793883263, "world_boanjale_crypts_unlocked",  "LevelUnlock", False, False, "Desert Beacon"),
	"Swamp Beacon 1":                  LocationData(2793883264, "world_sprigum_volcano_unlocked",  "LevelUnlock", False, False, "Swamp Beacon"),
	"Swamp Beacon 2":                  LocationData(2793883265, "world_badonc_beach_unlocked",     "LevelUnlock", False, False, "Swamp Beacon"),
	"Swamp Beacon 3":                  LocationData(2793883266, "world_ryha_river_unlocked",       "LevelUnlock", False, False, "Swamp Beacon"),
	"Beach Beacon 1":                  LocationData(2793883267, "world_lichen_hills_unlocked",     "LevelUnlock", False, False, "Beach Beacon"),
	"Beach Beacon 2":                  LocationData(2793883268, "world_fort_findula_unlocked",     "LevelUnlock", False, False, "Beach Beacon"),
	"Hills Beacon 1":                  LocationData(2793883269, "world_dennys_castle_unlocked",    "LevelUnlock", False, False, "Hills Beacon"),
	"Hills Beacon 2":                  LocationData(2793883270, "world_daimurs_lair_unlocked",     "LevelUnlock", False, False, "Hills Beacon")
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