from BaseClasses import Location
import typing

class ArzetteLocation(Location):
    game: str = "Arzette"

class LocationData(typing.NamedTuple):
    arzid: int | None
    # Default vanilla item code at this location
    # The reason this is here and not in ItemData is because the only fungible items 
    # (rudy races and null bonus rewards) are at multiple locations by default
    # Since all other items are non-fungible, it was easier to give the same internal name
    # to items and locations and put the item_code here
    item_code: str
    group: str = None
    can_spawner: bool = True
    locked: bool = False
    spawn_from: str = None

faramore_locations = {
	"Faramore Key (Well)":             LocationData(2793883001, "key_faramore_2",                  "Key",         True, False, None),
	"Faramore Key (Tavern)":           LocationData(2793883002, "key_faramore_1",                  "Key",         True, False, None),
	"Faramore Bonus":                  LocationData(2793883003, "obj_bonus_scroll_1",              "Scroll",      True, False, None),
	"Faramore Candle (Empty House)":   LocationData(2793883004, "obj_sacred_candle_24",            "Candle",      True, False, None),
	"Faramore Candle (Cypress House)": LocationData(2793883005, "obj_sacred_candle_25",            "Candle",      True, False, None),
	"Faramore Coin":                   LocationData(2793883006, "obj_hidden_coin_faramore",        "Coin",        True, False, None)
}

forest_locations = {
	"Bombs":                           LocationData(2793883007, "obj_quest_bombs",                 "Quest",       True, False, None),
	"Forest Bag (First Room 1)":       LocationData(2793883008, "obj_item_bag_1",                  "Bag",         True, False, None),
	"Forest Bag (First Room 2)":       LocationData(2793883009, "obj_item_bag_2",                  "Bag",         True, False, None),
	"Forest Key":                      LocationData(2793883010, "key_durridin",                    "Key",         True, False, None),
	"Forest Bonus":                    LocationData(2793883011, "obj_bonus_scroll_2",              "Scroll",      True, False, None),
	"Forest Candle (Tree)":            LocationData(2793883012, "obj_sacred_candle_1",             "Candle",      True, False, None),
	"Forest Candle (Cypress)":         LocationData(2793883013, "obj_sacred_candle_2",             "Candle",      True, False, None),
	"Forest Coin":                     LocationData(2793883014, "obj_hidden_coin_durridin",        "Coin",        True, False, None),
	"Forest Bag (Sword Wave)":         LocationData(2793883015, "obj_item_bag_3",                  "Bag",         True, False, None),
	"Sword Wave":                      LocationData(2793883016, "obj_quest_sword_wave",            "Quest",       True, False, None),
	"Golden Fly":                      LocationData(2793883017, "obj_quest_golden_fly",            "Quest",       True, False, None),
	"Forest Bag (Last Room)":          LocationData(2793883018, "obj_item_bag_4",                  "Bag",         True, False, None),
	"Forest Beacon":                   LocationData(2793883019, "beacon_durridin",                 "Beacon",      True, False, None),
	"Forest Jewel":                    LocationData(2793883020, "obj_jof_1",                       "Jewel",       False, False, None),
	"Magic Armor":                     LocationData(2793883021, "obj_quest_armor",                 "Quest",       True, False, None)
}

caves_locations = {
	"Silver Cricket":                  LocationData(2793883022, "obj_quest_silver_cricket",        "Quest",       True, False, None),
	"Rope Ladder":                     LocationData(2793883023, "obj_quest_rope_ladder",           "Quest",       True, False, None),
	"Caves Bag (Rope Ladder)":         LocationData(2793883024, "obj_item_bag_5",                  "Bag",         True, False, None),
	"Caves Candle (First Dark Room)":  LocationData(2793883025, "obj_sacred_candle_5",             "Candle",      True, False, None),
	"Caves Coin":                      LocationData(2793883026, "obj_hidden_coin_cogwyn",          "Coin",        True, False, None),
	"Caves Candle (Second Dark Room)": LocationData(2793883027, "obj_sacred_candle_26",            "Candle",      True, False, None),
	"Caves Bonus":                     LocationData(2793883028, "obj_bonus_scroll_3",              "Scroll",      True, False, None),
	"Caves Bag (Last Room)":           LocationData(2793883029, "obj_item_bag_6",                  "Bag",         True, False, None),
	"Shield Ring":                     LocationData(2793883030, "obj_quest_shield_ring",           "Quest",       True, False, None)
}

desert_locations = {
	"Desert Coin":                     LocationData(2793883031, "obj_hidden_coin_anju",            "Coin",        True, False, None),
	"Desert Bag (First Room 1)":       LocationData(2793883032, "obj_item_bag_7",                  "Bag",         True, False, None),
	"Desert Bag (First Room 2)":       LocationData(2793883033, "obj_item_bag_8",                  "Bag",         True, False, None),
	"Compass":                         LocationData(2793883034, "obj_quest_compass",               "Quest",       True, False, None),
	"Desert Candle (Pit)":             LocationData(2793883035, "obj_sacred_candle_3",             "Candle",      True, False, None),
	"Desert Bonus":                    LocationData(2793883036, "obj_bonus_scroll_4",              "Scroll",      True, False, None),
	"Desert Key":                      LocationData(2793883037, "key_anju",                        "Key",         True, False, None),
	"Desert Candle (Last Room)":       LocationData(2793883038, "obj_sacred_candle_4",             "Candle",      False, False, None),
	"Desert Life-Up":                  LocationData(2793883039, "obj_lifeup_1",                    "LifeUp",      True, False, None),
	"Desert Bag (Last Room)":          LocationData(2793883040, "obj_item_bag_9",                  "Bag",         True, False, None),
	"Desert Beacon":                   LocationData(2793883041, "beacon_anju_desert",              "Beacon",      True, False, None)
}

canyon_locations = {
	"Canyon Bonus":                    LocationData(2793883042, "obj_bonus_scroll_5",              "Scroll",      True, False, None),
	"Canyon Bag (Before Checkpoint)":  LocationData(2793883043, "obj_item_bag_10",                 "Bag",         True, False, None),
	"Canyon Bag (After Checkpoint 1)": LocationData(2793883044, "obj_item_bag_11",                 "Bag",         True, False, None),
	"Canyon Bag (After Checkpoint 2)": LocationData(2793883045, "obj_item_bag_12",                 "Bag",         True, False, None),
	"Canyon Bag (After Checkpoint 3)": LocationData(2793883046, "obj_item_bag_13",                 "Bag",         True, False, None),
	"Canyon Bag (First Room End)":     LocationData(2793883047, "obj_item_bag_14",                 "Bag",         True, False, None),
	"Canyon Candle (First Room End)":  LocationData(2793883048, "obj_sacred_candle_6",             "Candle",      True, False, None),
	"Canyon Jewel":                    LocationData(2793883049, "obj_jof_2",                       "Jewel",       False, False, None),
	"Canyon Key":                      LocationData(2793883050, "key_creece",                      "Key",         True, False, None),
	"Canyon Bag (After Zipline 1)":    LocationData(2793883051, "obj_item_bag_15",                 "Bag",         True, False, None),
	"Canyon Bag (After Zipline 2)":    LocationData(2793883052, "obj_item_bag_16",                 "Bag",         True, False, None),
	"Canyon Bag (After Zipline 3)":    LocationData(2793883053, "obj_item_bag_17",                 "Bag",         True, False, None),
	"Canyon Coin":                     LocationData(2793883054, "obj_hidden_coin_creece",          "Coin",        True, False, None),
	"Canyon Bag (Motte House)":        LocationData(2793883055, "obj_item_bag_18",                 "Bag",         True, False, None),
	"Canyon Candle (Motte House)":     LocationData(2793883056, "obj_sacred_candle_7",             "Candle",      True, False, None)
}

swamp_locations = {
	"Swamp Candle (First Room)":       LocationData(2793883057, "obj_sacred_candle_8",             "Candle",      True, False, None),
	"Swamp Bag (First Room)":          LocationData(2793883058, "obj_item_bag_19",                 "Bag",         True, False, None),
	"Swamp Coin":                      LocationData(2793883059, "obj_hidden_coin_norin",           "Coin",        True, False, None),
	"Swamp Key (Frich House)":         LocationData(2793883060, "key_norin",                       "Key",         True, False, None),
	"Swamp Candle (Frich House)":      LocationData(2793883061, "obj_sacred_candle_27",            "Candle",      True, False, None),
	"Swamp Key (Griffin Boots)":       LocationData(2793883062, "key_norin_2",                     "Key",         True, False, None),
	"Griffin Boots":                   LocationData(2793883063, "obj_quest_magic_boots",           "Quest",       True, False, None),
	"Swamp Plant":                     LocationData(2793883064, "obj_quest_plant_a",               "Plant",       False, False, None),
	"Swamp Bonus":                     LocationData(2793883065, "obj_bonus_scroll_6",              "Scroll",      True, False, None),
	"Swamp Beacon":                    LocationData(2793883066, "beacon_norin_swamp",              "Beacon",      True, False, None)
}

peak_locations = {
	"Peak Candle (First Cave)":        LocationData(2793883067, "obj_sacred_candle_9",             "Candle",      True, False, None),
	"Peak Bag (First Cave 1)":         LocationData(2793883068, "obj_item_bag_20",                 "Bag",         True, False, None),
	"Peak Bag (First Cave 2)":         LocationData(2793883069, "obj_item_bag_21",                 "Bag",         True, False, None),
	"Peak Bonus":                      LocationData(2793883070, "obj_bonus_scroll_7",              "Scroll",      True, False, None),
	"Peak Coin":                       LocationData(2793883071, "obj_hidden_coin_chillinax",       "Coin",        True, False, None),
	"Peak Key":                        LocationData(2793883072, "key_chillinax",                   "Key",         True, False, None),
	"Peak Candle (Ciclena Cave)":      LocationData(2793883073, "obj_sacred_candle_10",            "Candle",      True, False, None),
	"Peak Bag (Before Apatu)":         LocationData(2793883074, "obj_item_bag_22",                 "Bag",         True, False, None),
	"Peak Jewel":                      LocationData(2793883075, "obj_jof_3",                       "Jewel",       False, False, None),
	"Peak Bag (After Apatu)":          LocationData(2793883076, "obj_item_bag_23",                 "Bag",         True, False, None)
}

crypts_locations = {
	"Crypts Life-Up":                  LocationData(2793883077, "obj_lifeup_2",                    "LifeUp",      True, False, None),
	"Bell":                            LocationData(2793883078, "obj_quest_town_bell",             "Quest",       True, False, None),
	"Crypts Bonus":                    LocationData(2793883079, "obj_bonus_scroll_8",              "Scroll",      True, False, None),
	"Crypts Key":                      LocationData(2793883080, "key_boanjale",                    "Key",         True, False, None),
	"Crypts Bag (Crypt)":              LocationData(2793883081, "obj_item_bag_46",                 "Bag",         True, False, None),
	"Crypts Candle (After Crypt)":     LocationData(2793883082, "obj_sacred_candle_28",            "Candle",      True, False, None),
	"Crypts Coin":                     LocationData(2793883083, "obj_hidden_coin_boanjale",        "Coin",        True, False, None),
	"Crypts Candle (Skelvis)":         LocationData(2793883084, "obj_sacred_candle_11",            "Candle",      True, False, None),
	"Crypts Bag (Skelvis)":            LocationData(2793883085, "obj_item_bag_24",                 "Bag",         True, False, None)
}

volcano_locations = {
	"Volcano Bonus":                   LocationData(2793883086, "obj_bonus_scroll_9",              "Scroll",      True, False, None),
	"Volcano Candle (First Room)":     LocationData(2793883087, "obj_sacred_candle_12",            "Candle",      True, False, None),
	"Volcano Coin":                    LocationData(2793883088, "obj_hidden_coin_sprigum",         "Coin",        True, False, None),
	"Volcano Candle (Last Room)":      LocationData(2793883089, "obj_sacred_candle_29",            "Candle",      True, False, None),
	"Crystal of Refraction":           LocationData(2793883090, "obj_quest_crystal_of_refraction", "Quest",       True, False, None)
}

beach_locations = {
	"Beach Bag (First Room)":          LocationData(2793883091, "obj_item_bag_25",                 "Bag",         True, False, None),
	"Beach Key (First House)":         LocationData(2793883092, "key_badonc",                      "Key",         True, False, None),
	"Beach Coin":                      LocationData(2793883093, "obj_hidden_coin_badonc",          "Coin",        True, False, None),
	"Beach Key (Tork Cabin)":          LocationData(2793883094, "key_badonc_2",                    "Key",         True, False, None),
	"Beach Candle (Tork Cabin)":       LocationData(2793883095, "obj_sacred_candle_14",            "Candle",      True, False, None),
	"Beach Plant":                     LocationData(2793883096, "obj_quest_plant_b",               "Plant",       True, False, None),
	"Beach Bonus":                     LocationData(2793883097, "obj_bonus_scroll_10",             "Scroll",      True, False, None),
	"Beach Candle (Cave)":             LocationData(2793883098, "obj_sacred_candle_13",            "Candle",      True, False, None),
	"Fatal Flute":                     LocationData(2793883099, "obj_quest_flute",                 "Quest",       True, False, None),
	"Beach Beacon":                    LocationData(2793883100, "beacon_badonc_beach",             "Beacon",      True, False, None)
}

river_locations = {
	"River Key (Francine)":            LocationData(2793883101, "key_ryha",                        "Key",         True, False, None),
	"River Bonus":                     LocationData(2793883102, "obj_bonus_scroll_11",             "Scroll",      True, False, None),
	"River Candle (Boat)":             LocationData(2793883103, "obj_sacred_candle_15",            "Candle",      True, False, None),
	"River Key (Submarine)":           LocationData(2793883104, "key_ryha_2",                      "Key",         False, False, None),
	"River Coin":                      LocationData(2793883105, "obj_hidden_coin_ryha",            "Coin",        True, False, None),
	"Blue Magic":                      LocationData(2793883106, "obj_quest_blue_beam",             "Quest",       True, False, None),
	"River Bag (Last Room)":           LocationData(2793883107, "obj_item_bag_26",                 "Bag",         True, False, None),
	"River Candle (Last Room)":        LocationData(2793883108, "obj_sacred_candle_16",            "Candle",      True, False, None),
	"River Life-Up":                   LocationData(2793883109, "obj_lifeup_3",                    "LifeUp",      True, False, None)
}

hills_locations = {
	"Hills Candle (Cave)":             LocationData(2793883110, "obj_sacred_candle_30",            "Candle",      True, False, None),
	"Lightning Sword":                 LocationData(2793883111, "obj_quest_electric_sword",        "Quest",       True, False, None),
	"Hills Coin":                      LocationData(2793883112, "obj_hidden_coin_lichen",          "Coin",        True, False, None),
	"Hills Bonus":                     LocationData(2793883113, "obj_bonus_scroll_12",             "Scroll",      True, False, None),
	"Hills Bag (Barn)":                LocationData(2793883114, "obj_item_bag_27",                 "Bag",         True, False, None),
	"Hills Key":                       LocationData(2793883115, "key_lichen",                      "Key",         True, False, None),
	"Hills Bag (Music Shrine)":        LocationData(2793883116, "obj_item_bag_28",                 "Bag",         True, False, None),
	"Hills Candle (Music Shrine)":     LocationData(2793883117, "obj_sacred_candle_17",            "Candle",      True, False, None),
	"Hills Plant":                     LocationData(2793883118, "obj_quest_plant_c",               "Plant",       True, False, None),
	"Hills Beacon":                    LocationData(2793883119, "beacon_lichen_hills",             "Beacon",      True, False, None)
}

fort_locations = {
	"Fort Bag (Dungeon 1)":            LocationData(2793883120, "obj_item_bag_29",                 "Bag",         True, False, None),
	"Fort Bag (Dungeon 2)":            LocationData(2793883121, "obj_item_bag_30",                 "Bag",         True, False, None),
	"Fort Bag (Dungeon 3)":            LocationData(2793883122, "obj_item_bag_31",                 "Bag",         True, False, None),
	"Fort Bag (Dungeon 4)":            LocationData(2793883123, "obj_item_bag_32",                 "Bag",         True, False, None),
	"Sacred Oil":                      LocationData(2793883124, "obj_quest_oil",                   "Trading",     True, False, None),
	"Fort Key (First Room)":           LocationData(2793883125, "key_findula_1",                   "Key",         True, False, None),
	"Fort Candle (Dark Room)":         LocationData(2793883126, "obj_sacred_candle_18",            "Candle",      True, False, None),
	"Fort Bag (Dark Room)":            LocationData(2793883127, "obj_item_bag_33",                 "Bag",         True, False, None),
	"Enchanted Shoes":                 LocationData(2793883128, "obj_quest_shoes",                 "Quest",       True, False, None),
	"Fort Coin":                       LocationData(2793883129, "obj_hidden_coin_findula",         "Coin",        True, False, None),
	"Fort Key (Top Room)":             LocationData(2793883130, "key_findula_2",                   "Key",         True, False, None),
	"Fort Bag (Top Room 1)":           LocationData(2793883131, "obj_item_bag_34",                 "Bag",         True, False, None),
	"Fort Bag (Top Room 2)":           LocationData(2793883132, "obj_item_bag_35",                 "Bag",         True, False, None),
	"Fort Bag (Top Room 3)":           LocationData(2793883133, "obj_item_bag_36",                 "Bag",         True, False, None),
	"Fort Candle (Last Room)":         LocationData(2793883134, "obj_sacred_candle_19",            "Candle",      True, False, None),
	"Fort Bag (Last Room)":            LocationData(2793883135, "obj_item_bag_37",                 "Bag",         True, False, None),
	"Reflector Ring":                  LocationData(2793883136, "obj_quest_reflecting_shield",     "Quest",       True, False, None),
	"Fort Jewel":                      LocationData(2793883137, "obj_jof_4",                       "Jewel",       False, False, None),
	"Fort Bonus":                      LocationData(2793883138, "obj_bonus_scroll_13",             "Scroll",      True, False, None)
}

castle_locations = {
	"Castle Bag (Entrance)":           LocationData(2793883139, "obj_item_bag_38",                 "Bag",         True, False, None),
	"Castle Candle (Right Room)":      LocationData(2793883140, "obj_sacred_candle_20",            "Candle",      True, False, None),
	"Castle Key (Nodelki)":            LocationData(2793883141, "key_denny_2",                     "Key",         True, False, None),
	"Castle Candle (Top Room)":        LocationData(2793883142, "obj_sacred_candle_21",            "Candle",      True, False, None),
	"Castle Bag (Top Room)":           LocationData(2793883143, "obj_item_bag_39",                 "Bag",         True, False, None),
	"Winged Belt":                     LocationData(2793883144, "obj_quest_winged_belt",           "Quest",       True, False, None),
	"Castle Coin":                     LocationData(2793883145, "obj_hidden_coin_denny",           "Coin",        True, False, None),
	"Castle Key (Left Room)":          LocationData(2793883146, "key_denny_1",                     "Key",         True, False, None),
	"Castle Bag (Bonus)":              LocationData(2793883147, "obj_item_bag_40",                 "Bag",         True, False, None),
	"Castle Bonus":                    LocationData(2793883148, "obj_bonus_scroll_14",             "Scroll",      True, False, None),
	"Castle Jewel":                    LocationData(2793883149, "obj_jof_5",                       "Jewel",       False, False, None)
}

lair_locations = {
	"Lair Candle (Tree Trunk)":        LocationData(2793883150, "obj_sacred_candle_22",            "Candle",      True, False, None),
	"Lair Candle (Tree Top)":          LocationData(2793883151, "obj_sacred_candle_23",            "Candle",      True, False, None),
	"Lair Bonus":                      LocationData(2793883152, "obj_bonus_scroll_15",             "Scroll",      True, False, None),
	"Lair Bag (First Room)":           LocationData(2793883153, "obj_item_bag_41",                 "Bag",         True, False, None),
	"Lair Coin":                       LocationData(2793883154, "obj_hidden_coin_daimur",          "Coin",        True, False, None),
	"Lair Bag (Lava Room)":            LocationData(2793883155, "obj_item_bag_42",                 "Bag",         True, False, None),
	"Lair Bag (Final Room 1)":         LocationData(2793883156, "obj_item_bag_43",                 "Bag",         True, False, None),
	"Lair Bag (Final Room 2)":         LocationData(2793883157, "obj_item_bag_44",                 "Bag",         True, False, None),
	"Lair Bag (Final Room 3)":         LocationData(2793883158, "obj_item_bag_45",                 "Bag",         True, False, None),
	"Daimur":                          LocationData(2793883159, "obj_boss_daimur",                 "Other",       False, True, None)
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
	"Swamp Glubbert":                  LocationData(2793883193, "npc_glubbert",                    "NPCSpawner",  True, False, None),
	"Peak Ciclena":                    LocationData(2793883194, "npc_ciclena",                     "NPCSpawner",  True, False, None),
	"Caves Munhum":                    LocationData(2793883195, "npc_munhum",                      "NPCSpawner",  True, False, None),
	"Faramore Denny":                  LocationData(2793883196, "npc_denny",                       "NPCSpawner",  True, False, None),
	"Faramore Dewey":                  LocationData(2793883197, "npc_dewey",                       "NPCSpawner",  True, False, None),
	"Faramore Frich":                  LocationData(2793883198, "npc_frich_quest",                 "NPCSpawner",  True, False, None),
	"Canyon Crowdee":                  LocationData(2793883199, "npc_crowdee",                     "NPCSpawner",  True, False, None),
	"Hills Milbert":                   LocationData(2793883200, "npc_milbert",                     "NPCSpawner",  True, False, None),
	"Faramore Barnabuss":              LocationData(2793883201, "npc_barnabuss_quest",             "NPCSpawner",  True, False, None),
	"Faramore Kari Quest":             LocationData(2793883202, "npc_kari_quest",                  "NPCSpawner",  True, False, None),
	"Faramore Yukeen":                 LocationData(2793883203, "npc_yukeen",                      "NPCSpawner",  True, False, None),
	"Forest Cypress":                  LocationData(2793883204, "npc_cypress",                     "NPCSpawner",  True, False, None),
	"Caves Ellido":                    LocationData(2793883205, "npc_ellido",                      "NPCSpawner",  True, False, None),
	"Canyon Motte":                    LocationData(2793883206, "npc_motte",                       "NPCSpawner",  True, False, None),
	"Faramore Brinda":                 LocationData(2793883207, "npc_brinda",                      "NPCSpawner",  True, False, None),
	"Faramore Alven":                  LocationData(2793883208, "npc_alven",                       "NPCSpawner",  True, False, None),
	"Desert Fairy":                    LocationData(2793883209, "npc_fairy",                       "NPCSpawner",  True, False, None),
	"Faramore Cypress":                LocationData(2793883210, "npc_cypress_quest",               "NPCSpawner",  True, False, None),
	"River Morgh":                     LocationData(2793883211, "npc_morgh",                       "NPCSpawner",  True, False, None),
	"Faramore Munhum":                 LocationData(2793883212, "npc_munhum_quest",                "NPCSpawner",  True, False, None),
	"Canyon Odie":                     LocationData(2793883213, "npc_odie",                        "NPCSpawner",  True, False, None),
	"Lair Zazie":                      LocationData(2793883214, "npc_zazie",                       "NPCSpawner",  True, False, None),
	"Crypts Skelvis":                  LocationData(2793883215, "npc_skelvis",                     "NPCSpawner",  True, False, None),
	"Beach Tork":                      LocationData(2793883216, "npc_tork",                        "NPCSpawner",  True, False, None),
	"Faramore Covenplate":             LocationData(2793883217, "npc_mayor",                       "NPCSpawner",  True, False, None),
	"Beach Fleetus":                   LocationData(2793883218, "npc_fleetus",                     "NPCSpawner",  True, False, None),
	"River Francine":                  LocationData(2793883219, "npc_francine",                    "NPCSpawner",  True, False, None),
	"Faramore Rudy":                   LocationData(2793883220, "npc_rudy",                        "NPCSpawner",  True, False, None)
}

npc_foolish_locations = {
	"Faramore Boru":                   LocationData(2793883221, "npc_boru",                        "NPC",         True, False, None),
	"Faramore Kari":                   LocationData(2793883222, "npc_kari",                        "NPC",         True, False, None),
	"Faramore Univor":                 LocationData(2793883223, "npc_univor",                      "NPC",         True, False, None),
	"Faramore Salvik":                 LocationData(2793883224, "npc_salvik",                      "NPC",         True, False, None),
	"Faramore Maki":                   LocationData(2793883225, "npc_maki",                        "NPC",         True, False, None),
	"Faramore Payop":                  LocationData(2793883226, "npc_payop",                       "NPC",         True, False, None),
	"Volcano Joe":                     LocationData(2793883227, "npc_joe",                         "NPC",         True, False, None),
	"River Barnabuss":                 LocationData(2793883228, "npc_barnabuss",                   "NPC",         True, False, None)
}

npc_locked_locations = {
	"Faramore Mortar":                 LocationData(2793883229, "npc_mortar",                      "NPC",         False, True, None),
	"Swamp Frich":                     LocationData(2793883230, "npc_frich",                       "NPC",         False, True, None),
	"Forest Rudy (Start)":             LocationData(2793883231, "npc_rudy_start",                  "NPC",         False, True, None),
	"Forest Rudy (End)":               LocationData(2793883232, "npc_rudy_goal",                   "NPC",         False, True, None),
	"Peak Rudy (Start)":               LocationData(2793883233, "npc_rudy_start",                  "NPC",         False, True, None),
	"Peak Rudy (End)":                 LocationData(2793883234, "npc_rudy_goal",                   "NPC",         False, True, None),
	"Hills Rudy (Start)":              LocationData(2793883235, "npc_rudy_start",                  "NPC",         False, True, None),
	"Hills Rudy (End)":                LocationData(2793883236, "npc_rudy_goal",                   "NPC",         False, True, None)
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