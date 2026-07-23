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
	"Faramore Key (Well)":             LocationData(367759001, "key_faramore_2",                  "Key",         True, False, "Faramore"),
	"Faramore Key (Tavern)":           LocationData(367759002, "key_faramore_1",                  "Key",         True, False, "Faramore"),
	"Faramore Bonus":                  LocationData(367759003, "obj_bonus_scroll_1",              "Scroll",      True, False, "Faramore"),
	"Faramore Candle (Empty House)":   LocationData(367759004, "obj_sacred_candle_24",            "Candle",      True, False, "Faramore"),
	"Faramore Candle (Cypress House)": LocationData(367759005, "obj_sacred_candle_25",            "Candle",      True, False, "Faramore"),
	"Faramore Coin":                   LocationData(367759006, "obj_hidden_coin_faramore",        "Coin",        True, False, "Faramore")
}

forest_locations = {
	"Bombs":                           LocationData(367759007, "obj_quest_bombs",                 "Quest",       True, False, "Forest"),
	"Forest Bag (First Room 1)":       LocationData(367759008, "obj_item_bag_1",                  "Bag",         True, False, "Forest"),
	"Forest Bag (First Room 2)":       LocationData(367759009, "obj_item_bag_2",                  "Bag",         True, False, "Forest"),
	"Forest Key":                      LocationData(367759010, "key_durridin",                    "Key",         True, False, "Forest"),
	"Forest Bonus":                    LocationData(367759011, "obj_bonus_scroll_2",              "Scroll",      True, False, "Forest"),
	"Forest Candle (Tree)":            LocationData(367759012, "obj_sacred_candle_1",             "Candle",      True, False, "Forest"),
	"Forest Candle (Cypress)":         LocationData(367759013, "obj_sacred_candle_2",             "Candle",      True, False, "Forest"),
	"Forest Coin":                     LocationData(367759014, "obj_hidden_coin_durridin",        "Coin",        True, False, "Forest"),
	"Forest Bag (Sword Wave)":         LocationData(367759015, "obj_item_bag_3",                  "Bag",         True, False, "Forest"),
	"Sword Wave":                      LocationData(367759016, "obj_quest_sword_wave",            "Quest",       True, False, "Forest"),
	"Golden Fly":                      LocationData(367759017, "obj_quest_golden_fly",            "Quest",       True, False, "Forest"),
	"Forest Bag (Last Room)":          LocationData(367759018, "obj_item_bag_4",                  "Bag",         True, False, "Forest"),
	"Forest Beacon":                   LocationData(367759019, "beacon_durridin",                 "Beacon",      True, False, "Forest"),
	"Forest Jewel":                    LocationData(367759020, "obj_jof_1",                       "Jewel",       False, False, "Forest"),
	"Magic Armor":                     LocationData(367759021, "obj_quest_armor",                 "Quest",       True, False, "Forest")
}

caves_locations = {
	"Silver Cricket":                  LocationData(367759022, "obj_quest_silver_cricket",        "Quest",       True, False, "Caves"),
	"Rope Ladder":                     LocationData(367759023, "obj_quest_rope_ladder",           "Quest",       True, False, "Caves"),
	"Caves Bag (Rope Ladder)":         LocationData(367759024, "obj_item_bag_5",                  "Bag",         True, False, "Caves"),
	"Caves Candle (First Dark Room)":  LocationData(367759025, "obj_sacred_candle_5",             "Candle",      True, False, "Caves"),
	"Caves Coin":                      LocationData(367759026, "obj_hidden_coin_cogwyn",          "Coin",        True, False, "Caves"),
	"Caves Candle (Second Dark Room)": LocationData(367759027, "obj_sacred_candle_26",            "Candle",      True, False, "Caves"),
	"Caves Bonus":                     LocationData(367759028, "obj_bonus_scroll_3",              "Scroll",      True, False, "Caves"),
	"Caves Bag (Last Room)":           LocationData(367759029, "obj_item_bag_6",                  "Bag",         True, False, "Caves"),
	"Shield Ring":                     LocationData(367759030, "obj_quest_shield_ring",           "Quest",       True, False, "Caves")
}

desert_locations = {
	"Desert Coin":                     LocationData(367759031, "obj_hidden_coin_anju",            "Coin",        True, False, "Desert"),
	"Desert Bag (First Room 1)":       LocationData(367759032, "obj_item_bag_7",                  "Bag",         True, False, "Desert"),
	"Desert Bag (First Room 2)":       LocationData(367759033, "obj_item_bag_8",                  "Bag",         True, False, "Desert"),
	"Compass":                         LocationData(367759034, "obj_quest_compass",               "Quest",       True, False, "Desert"),
	"Desert Candle (Pit)":             LocationData(367759035, "obj_sacred_candle_3",             "Candle",      True, False, "Desert"),
	"Desert Bonus":                    LocationData(367759036, "obj_bonus_scroll_4",              "Scroll",      True, False, "Desert"),
	"Desert Key":                      LocationData(367759037, "key_anju",                        "Key",         True, False, "Desert"),
	"Desert Candle (Last Room)":       LocationData(367759038, "obj_sacred_candle_4",             "Candle",      False, False, "Desert"),
	"Desert Life-Up":                  LocationData(367759039, "obj_lifeup_1",                    "LifeUp",      True, False, "Desert"),
	"Desert Bag (Last Room)":          LocationData(367759040, "obj_item_bag_9",                  "Bag",         True, False, "Desert"),
	"Desert Beacon":                   LocationData(367759041, "beacon_anju_desert",              "Beacon",      True, False, "Desert")
}

canyon_locations = {
	"Canyon Bonus":                    LocationData(367759042, "obj_bonus_scroll_5",              "Scroll",      True, False, "Canyon"),
	"Canyon Bag (Before Checkpoint)":  LocationData(367759043, "obj_item_bag_10",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 1)": LocationData(367759044, "obj_item_bag_11",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 2)": LocationData(367759045, "obj_item_bag_12",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Checkpoint 3)": LocationData(367759046, "obj_item_bag_13",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (First Room End)":     LocationData(367759047, "obj_item_bag_14",                 "Bag",         True, False, "Canyon"),
	"Canyon Candle (First Room End)":  LocationData(367759048, "obj_sacred_candle_6",             "Candle",      True, False, "Canyon"),
	"Canyon Jewel":                    LocationData(367759049, "obj_jof_2",                       "Jewel",       False, False, "Canyon"),
	"Canyon Key":                      LocationData(367759050, "key_creece",                      "Key",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 1)":    LocationData(367759051, "obj_item_bag_15",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 2)":    LocationData(367759052, "obj_item_bag_16",                 "Bag",         True, False, "Canyon"),
	"Canyon Bag (After Zipline 3)":    LocationData(367759053, "obj_item_bag_17",                 "Bag",         True, False, "Canyon"),
	"Canyon Coin":                     LocationData(367759054, "obj_hidden_coin_creece",          "Coin",        True, False, "Canyon"),
	"Canyon Bag (Motte House)":        LocationData(367759055, "obj_item_bag_18",                 "Bag",         True, False, "Canyon"),
	"Canyon Candle (Motte House)":     LocationData(367759056, "obj_sacred_candle_7",             "Candle",      True, False, "Canyon")
}

swamp_locations = {
	"Swamp Candle (First Room)":       LocationData(367759057, "obj_sacred_candle_8",             "Candle",      True, False, "Swamp"),
	"Swamp Bag (First Room)":          LocationData(367759058, "obj_item_bag_19",                 "Bag",         True, False, "Swamp"),
	"Swamp Coin":                      LocationData(367759059, "obj_hidden_coin_norin",           "Coin",        True, False, "Swamp"),
	"Swamp Key (Frich House)":         LocationData(367759060, "key_norin",                       "Key",         True, False, "Swamp"),
	"Swamp Candle (Frich House)":      LocationData(367759061, "obj_sacred_candle_27",            "Candle",      True, False, "Swamp"),
	"Swamp Key (Griffin Boots)":       LocationData(367759062, "key_norin_2",                     "Key",         True, False, "Swamp"),
	"Griffin Boots":                   LocationData(367759063, "obj_quest_magic_boots",           "Quest",       True, False, "Swamp"),
	"Swamp Plant":                     LocationData(367759064, "obj_quest_plant_b",               "Plant",       False, False, "Swamp"),
	"Swamp Bonus":                     LocationData(367759065, "obj_bonus_scroll_6",              "Scroll",      True, False, "Swamp"),
	"Swamp Beacon":                    LocationData(367759066, "beacon_norin_swamp",              "Beacon",      True, False, "Swamp")
}

peak_locations = {
	"Peak Candle (First Cave)":        LocationData(367759067, "obj_sacred_candle_9",             "Candle",      True, False, "Peak"),
	"Peak Bag (First Cave 1)":         LocationData(367759068, "obj_item_bag_20",                 "Bag",         True, False, "Peak"),
	"Peak Bag (First Cave 2)":         LocationData(367759069, "obj_item_bag_21",                 "Bag",         True, False, "Peak"),
	"Peak Bonus":                      LocationData(367759070, "obj_bonus_scroll_7",              "Scroll",      True, False, "Peak"),
	"Peak Coin":                       LocationData(367759071, "obj_hidden_coin_chillinax",       "Coin",        True, False, "Peak"),
	"Peak Key":                        LocationData(367759072, "key_chillinax",                   "Key",         True, False, "Peak"),
	"Peak Candle (Ciclena Cave)":      LocationData(367759073, "obj_sacred_candle_10",            "Candle",      True, False, "Peak"),
	"Peak Bag (Before Apatu)":         LocationData(367759074, "obj_item_bag_22",                 "Bag",         True, False, "Peak"),
	"Peak Jewel":                      LocationData(367759075, "obj_jof_3",                       "Jewel",       False, False, "Peak"),
	"Peak Bag (After Apatu)":          LocationData(367759076, "obj_item_bag_23",                 "Bag",         True, False, "Peak")
}

crypts_locations = {
	"Crypts Life-Up":                  LocationData(367759077, "obj_lifeup_2",                    "LifeUp",      True, False, "Crypts"),
	"Bell":                            LocationData(367759078, "obj_quest_town_bell",             "Quest",       True, False, "Crypts"),
	"Crypts Bonus":                    LocationData(367759079, "obj_bonus_scroll_8",              "Scroll",      True, False, "Crypts"),
	"Crypts Key":                      LocationData(367759080, "key_boanjale",                    "Key",         True, False, "Crypts"),
	"Crypts Bag (Crypt)":              LocationData(367759081, "obj_item_bag_46",                 "Bag",         True, False, "Crypts"),
	"Crypts Candle (After Crypt)":     LocationData(367759082, "obj_sacred_candle_28",            "Candle",      True, False, "Crypts"),
	"Crypts Coin":                     LocationData(367759083, "obj_hidden_coin_boanjale",        "Coin",        False, False, "Crypts"),
	"Crypts Candle (Skelvis)":         LocationData(367759084, "obj_sacred_candle_11",            "Candle",      True, False, "Crypts"),
	"Crypts Bag (Skelvis)":            LocationData(367759085, "obj_item_bag_24",                 "Bag",         True, False, "Crypts")
}

volcano_locations = {
	"Volcano Bonus":                   LocationData(367759086, "obj_bonus_scroll_9",              "Scroll",      True, False, "Volcano"),
	"Volcano Candle (First Room)":     LocationData(367759087, "obj_sacred_candle_12",            "Candle",      True, False, "Volcano"),
	"Volcano Coin":                    LocationData(367759088, "obj_hidden_coin_sprigum",         "Coin",        True, False, "Volcano"),
	"Volcano Candle (Last Room)":      LocationData(367759089, "obj_sacred_candle_29",            "Candle",      True, False, "Volcano"),
	"Crystal of Refraction":           LocationData(367759090, "obj_quest_crystal_of_refraction", "Quest",       True, False, "Volcano")
}

beach_locations = {
	"Beach Bag (First Room)":          LocationData(367759091, "obj_item_bag_25",                 "Bag",         True, False, "Beach"),
	"Beach Key (First House)":         LocationData(367759092, "key_badonc",                      "Key",         True, False, "Beach"),
	"Beach Coin":                      LocationData(367759093, "obj_hidden_coin_badonc",          "Coin",        True, False, "Beach"),
	"Beach Key (Tork Cabin)":          LocationData(367759094, "key_badonc_2",                    "Key",         True, False, "Beach"),
	"Beach Candle (Tork Cabin)":       LocationData(367759095, "obj_sacred_candle_14",            "Candle",      True, False, "Beach"),
	"Beach Plant":                     LocationData(367759096, "obj_quest_plant_a",               "Plant",       True, False, "Beach"),
	"Beach Bonus":                     LocationData(367759097, "obj_bonus_scroll_10",             "Scroll",      True, False, "Beach"),
	"Beach Candle (Cave)":             LocationData(367759098, "obj_sacred_candle_13",            "Candle",      True, False, "Beach"),
	"Fatal Flute":                     LocationData(367759099, "obj_quest_flute",                 "Quest",       True, False, "Beach"),
	"Beach Beacon":                    LocationData(367759100, "beacon_badonc_beach",             "Beacon",      True, False, "Beach")
}

river_locations = {
	"River Key (Francine)":            LocationData(367759101, "key_ryha",                        "Key",         True, False, "River"),
	"River Bonus":                     LocationData(367759102, "obj_bonus_scroll_11",             "Scroll",      True, False, "River"),
	"River Candle (Boat)":             LocationData(367759103, "obj_sacred_candle_15",            "Candle",      True, False, "River"),
	"River Key (Submarine)":           LocationData(367759104, "key_ryha_2",                      "Key",         False, False, "River"),
	"River Coin":                      LocationData(367759105, "obj_hidden_coin_ryha",            "Coin",        True, False, "River"),
	"Blue Magic":                      LocationData(367759106, "obj_quest_blue_beam",             "Quest",       True, False, "River"),
	"River Bag (Last Room)":           LocationData(367759107, "obj_item_bag_26",                 "Bag",         True, False, "River"),
	"River Candle (Last Room)":        LocationData(367759108, "obj_sacred_candle_16",            "Candle",      True, False, "River"),
	"River Life-Up":                   LocationData(367759109, "obj_lifeup_3",                    "LifeUp",      True, False, "River")
}

hills_locations = {
	"Hills Candle (Cave)":             LocationData(367759110, "obj_sacred_candle_30",            "Candle",      True, False, "Hills"),
	"Lightning Sword":                 LocationData(367759111, "obj_quest_electric_sword",        "Quest",       True, False, "Hills"),
	"Hills Coin":                      LocationData(367759112, "obj_hidden_coin_lichen",          "Coin",        True, False, "Hills"),
	"Hills Bonus":                     LocationData(367759113, "obj_bonus_scroll_12",             "Scroll",      True, False, "Hills"),
	"Hills Bag (Barn)":                LocationData(367759114, "obj_item_bag_27",                 "Bag",         True, False, "Hills"),
	"Hills Key":                       LocationData(367759115, "key_lichen",                      "Key",         True, False, "Hills"),
	"Hills Bag (Music Shrine)":        LocationData(367759116, "obj_item_bag_28",                 "Bag",         True, False, "Hills"),
	"Hills Candle (Music Shrine)":     LocationData(367759117, "obj_sacred_candle_17",            "Candle",      True, False, "Hills"),
	"Hills Plant":                     LocationData(367759118, "obj_quest_plant_c",               "Plant",       True, False, "Hills"),
	"Hills Beacon":                    LocationData(367759119, "beacon_lichen_hills",             "Beacon",      True, False, "Hills")
}

fort_locations = {
	"Fort Bag (Dungeon 1)":            LocationData(367759120, "obj_item_bag_29",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 2)":            LocationData(367759121, "obj_item_bag_30",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 3)":            LocationData(367759122, "obj_item_bag_31",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Dungeon 4)":            LocationData(367759123, "obj_item_bag_32",                 "Bag",         True, False, "Fort"),
	"Sacred Oil":                      LocationData(367759124, "obj_quest_oil",                   "Trading",     True, False, "Fort"),
	"Fort Key (First Room)":           LocationData(367759125, "key_findula_1",                   "Key",         True, False, "Fort"),
	"Fort Candle (Dark Room)":         LocationData(367759126, "obj_sacred_candle_18",            "Candle",      True, False, "Fort"),
	"Fort Bag (Dark Room)":            LocationData(367759127, "obj_item_bag_33",                 "Bag",         True, False, "Fort"),
	"Enchanted Shoes":                 LocationData(367759128, "obj_quest_shoes",                 "Quest",       True, False, "Fort"),
	"Fort Coin":                       LocationData(367759129, "obj_hidden_coin_findula",         "Coin",        True, False, "Fort"),
	"Fort Key (Top Room)":             LocationData(367759130, "key_findula_2",                   "Key",         True, False, "Fort"),
	"Fort Bag (Top Room 1)":           LocationData(367759131, "obj_item_bag_34",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Top Room 2)":           LocationData(367759132, "obj_item_bag_35",                 "Bag",         True, False, "Fort"),
	"Fort Bag (Top Room 3)":           LocationData(367759133, "obj_item_bag_36",                 "Bag",         True, False, "Fort"),
	"Fort Candle (Last Room)":         LocationData(367759134, "obj_sacred_candle_19",            "Candle",      True, False, "Fort"),
	"Fort Bag (Last Room)":            LocationData(367759135, "obj_item_bag_37",                 "Bag",         True, False, "Fort"),
	"Reflector Ring":                  LocationData(367759136, "obj_quest_reflecting_shield",     "Quest",       True, False, "Fort"),
	"Fort Jewel":                      LocationData(367759137, "obj_jof_4",                       "Jewel",       False, False, "Fort"),
	"Fort Bonus":                      LocationData(367759138, "obj_bonus_scroll_13",             "Scroll",      True, False, "Fort")
}

castle_locations = {
	"Castle Bag (Entrance)":           LocationData(367759139, "obj_item_bag_38",                 "Bag",         True, False, "Castle"),
	"Castle Candle (Right Room)":      LocationData(367759140, "obj_sacred_candle_20",            "Candle",      True, False, "Castle"),
	"Castle Key (Nodelki)":            LocationData(367759141, "key_denny_2",                     "Key",         True, False, "Castle"),
	"Castle Candle (Top Room)":        LocationData(367759142, "obj_sacred_candle_21",            "Candle",      True, False, "Castle"),
	"Castle Bag (Top Room)":           LocationData(367759143, "obj_item_bag_39",                 "Bag",         True, False, "Castle"),
	"Winged Belt":                     LocationData(367759144, "obj_quest_winged_belt",           "Quest",       True, False, "Castle"),
	"Castle Coin":                     LocationData(367759145, "obj_hidden_coin_denny",           "Coin",        True, False, "Castle"),
	"Castle Key (Left Room)":          LocationData(367759146, "key_denny_1",                     "Key",         True, False, "Castle"),
	"Castle Bag (Bonus)":              LocationData(367759147, "obj_item_bag_40",                 "Bag",         True, False, "Castle"),
	"Castle Bonus":                    LocationData(367759148, "obj_bonus_scroll_14",             "Scroll",      True, False, "Castle"),
	"Castle Jewel":                    LocationData(367759149, "obj_jof_5",                       "Jewel",       False, False, "Castle")
}

lair_locations = {
	"Lair Candle (Tree Trunk)":        LocationData(367759150, "obj_sacred_candle_22",            "Candle",      True, False, "Lair"),
	"Lair Candle (Tree Top)":          LocationData(367759151, "obj_sacred_candle_23",            "Candle",      True, False, "Lair"),
	"Lair Bonus":                      LocationData(367759152, "obj_bonus_scroll_15",             "Scroll",      True, False, "Lair"),
	"Lair Bag (First Room)":           LocationData(367759153, "obj_item_bag_41",                 "Bag",         True, False, "Lair"),
	"Lair Coin":                       LocationData(367759154, "obj_hidden_coin_daimur",          "Coin",        True, False, "Lair"),
	"Lair Bag (Lava Room)":            LocationData(367759155, "obj_item_bag_42",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 1)":         LocationData(367759156, "obj_item_bag_43",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 2)":         LocationData(367759157, "obj_item_bag_44",                 "Bag",         True, False, "Lair"),
	"Lair Bag (Final Room 3)":         LocationData(367759158, "obj_item_bag_45",                 "Bag",         True, False, "Lair"),
	"Daimur":                          LocationData(367759159, "obj_boss_daimur",                 "Other",       False, True, "Lair")
}

from_npc_locations = {
	"Purple Magic":                    LocationData(367759160, "obj_quest_sword",                 "Quest",       False, False, "Faramore Yukeen"),
	"Citizenship Papers":              LocationData(367759161, "obj_quest_citizenship",           "Quest",       False, False, "Faramore Covenplate"),
	"Power Stone Upgrade":             LocationData(367759162, "obj_quest_upgrade_power_stones",  "Upgrade",     False, False, "Faramore Kari Quest"),
	"Dungeon Key":                     LocationData(367759163, "key_findula_dungeon",             "Trading",     False, False, "Faramore Alven"),
	"Chainsword":                      LocationData(367759164, "obj_quest_chainsword",            "Trading",     False, False, "Faramore Alven"),
	"Canteen":                         LocationData(367759165, "obj_quest_canteen",               "Quest",       False, False, "Faramore Brinda"),
	"Wallet Upgrade":                  LocationData(367759166, "obj_quest_upgrade_wallet",        "Upgrade",     False, False, "Faramore Frich"),
	"Infinite Soulfire":               LocationData(367759167, "obj_quest_infinite_soulfire",     "Upgrade",     False, False, "Faramore Rudy"),
	"Bomb Upgrade":                    LocationData(367759168, "obj_quest_upgrade_bombs",         "Upgrade",     False, False, "Faramore Barnabuss"),
	"Calendar":                        LocationData(367759169, "obj_quest_beach_calendar",        "Quest",       False, False, "Faramore Denny"),
	"200 Rupees":                      LocationData(367759170, "obj_quest_dewey_reward",          "Quest",       False, False, "Faramore Dewey"),
	"Lamp Oil Upgrade":                LocationData(367759171, "obj_quest_upgrade_lamp_oil",      "Upgrade",     False, False, "Faramore Cypress"),
	"Rope Upgrade":                    LocationData(367759172, "obj_quest_upgrade_ropes",         "Upgrade",     False, False, "Faramore Munhum"),
	"Forest Race 100 Rupees":          LocationData(367759173, "obj_quest_race_reward_1",         "Race",        False, False, "Faramore Rudy"),
	"Peak Race 100 Rupees":            LocationData(367759174, "obj_quest_race_reward_2",         "Race",        False, False, "Faramore Rudy"),
	"Hills Race 100 Rupees":           LocationData(367759175, "obj_quest_race_reward_3",         "Race",        False, False, "Faramore Rudy"),
	"Lantern":                         LocationData(367759176, "obj_quest_lantern",               "Quest",       False, False, "Forest Cypress"),
	"Rope":                            LocationData(367759177, "obj_quest_esc_rope",              "Quest",       False, False, "Caves Munhum"),
	"Snail Salt":                      LocationData(367759178, "obj_quest_snail_salt",            "Trading",     False, False, "Caves Ellido"),
	"Fairy Dust":                      LocationData(367759179, "obj_quest_fairy_dust",            "Quest",       False, False, "Desert Fairy"),
	"Backstep":                        LocationData(367759180, "obj_quest_backstep",              "Quest",       False, False, "Canyon Crowdee"),
	"Smart Gun":                       LocationData(367759181, "obj_quest_gun",                   "Quest",       False, False, "Canyon Motte"),
	"Star Earrings":                   LocationData(367759182, "obj_quest_star_earrings",         "Quest",       False, False, "Canyon Odie"),
	"Ogre Hair":                       LocationData(367759183, "obj_quest_ogre_hair",             "Trading",     False, False, "Swamp Glubbert"),
	"Power Pendant":                   LocationData(367759184, "obj_quest_pendant",               "Quest",       False, False, "Peak Ciclena"),
	"Bomb Gauntlet":                   LocationData(367759185, "obj_quest_pg",                    "Quest",       False, False, "Crypts Skelvis"),
	"Speedy Shoes":                    LocationData(367759186, "obj_quest_speedy_shoes",          "Quest",       False, False, "Beach Fleetus"),
	"Magic Cloak":                     LocationData(367759187, "obj_quest_magic_cloak",           "Quest",       False, False, "Beach Tork"),
	"Cleaver Shovel":                  LocationData(367759188, "obj_quest_cleaver_shovel",        "Trading",     False, False, "River Francine"),
	"Oil and Chains":                  LocationData(367759189, "obj_quest_refined_chains",        "Trading",     False, False, "River Morgh"),
	"Double Wave":                     LocationData(367759190, "obj_quest_double_wave",           "Quest",       False, False, "Hills Milbert"),
	"Funky Fungus":                    LocationData(367759191, "obj_quest_funky_fungus",          "Trading",     False, False, "Lair Zazie"),
	"Soul Upgrade":                    LocationData(367759192, "obj_quest_upgrade_soul_bag",      "Upgrade",     False, False, "Lair Zazie")
}

npc_spawn_locations = {
	"Faramore Covenplate":             LocationData(367759193, "npc_mayor",                       "NPCSpawner",  True, False, "Faramore"),
	"Canyon Crowdee":                  LocationData(367759194, "npc_crowdee",                     "NPCSpawner",  True, False, "Canyon"),
	"Peak Ciclena":                    LocationData(367759195, "npc_ciclena",                     "NPCSpawner",  True, False, "Peak"),
	"Beach Fleetus":                   LocationData(367759196, "npc_fleetus",                     "NPCSpawner",  True, False, "Beach"),
	"Forest Cypress":                  LocationData(367759197, "npc_cypress",                     "NPCSpawner",  True, False, "Forest"),
	"Faramore Yukeen":                 LocationData(367759198, "npc_yukeen",                      "NPCSpawner",  True, False, "Faramore"),
	"Faramore Rudy":                   LocationData(367759199, "npc_rudy",                        "NPCSpawner",  True, False, "Faramore"),
	"Desert Fairy":                    LocationData(367759200, "npc_fairy",                       "NPCSpawner",  True, False, "Desert"),
	"Beach Tork":                      LocationData(367759201, "npc_tork",                        "NPCSpawner",  True, False, "Beach"),
	"Faramore Alven":                  LocationData(367759202, "npc_alven",                       "NPCSpawner",  True, False, "Faramore"),
	"Caves Ellido":                    LocationData(367759203, "npc_ellido",                      "NPCSpawner",  True, False, "Caves"),
	"Canyon Motte":                    LocationData(367759204, "npc_motte",                       "NPCSpawner",  True, False, "Canyon"),
	"Faramore Barnabuss":              LocationData(367759205, "npc_barnabuss_quest",             "NPCSpawner",  True, False, "Faramore"),
	"Faramore Denny":                  LocationData(367759206, "npc_denny",                       "NPCSpawner",  True, False, "Faramore"),
	"Faramore Dewey":                  LocationData(367759207, "npc_dewey",                       "NPCSpawner",  True, False, "Faramore"),
	"Crypts Skelvis":                  LocationData(367759208, "npc_skelvis",                     "NPCSpawner",  True, False, "Crypts"),
	"Faramore Frich":                  LocationData(367759209, "npc_frich_quest",                 "NPCSpawner",  True, False, "Faramore"),
	"Lair Zazie":                      LocationData(367759210, "npc_zazie",                       "NPCSpawner",  True, False, "Lair"),
	"Caves Munhum":                    LocationData(367759211, "npc_munhum",                      "NPCSpawner",  True, False, "Caves"),
	"Faramore Brinda":                 LocationData(367759212, "npc_brinda",                      "NPCSpawner",  True, False, "Faramore"),
	"Swamp Glubbert":                  LocationData(367759213, "npc_glubbert",                    "NPCSpawner",  True, False, "Swamp"),
	"Hills Milbert":                   LocationData(367759214, "npc_milbert",                     "NPCSpawner",  True, False, "Hills"),
	"Faramore Cypress":                LocationData(367759215, "npc_cypress_quest",               "NPCSpawner",  True, False, "Faramore"),
	"Canyon Odie":                     LocationData(367759216, "npc_odie",                        "NPCSpawner",  True, False, "Canyon"),
	"Faramore Kari Quest":             LocationData(367759217, "npc_kari_quest",                  "NPCSpawner",  True, False, "Faramore"),
	"River Morgh":                     LocationData(367759218, "npc_morgh",                       "NPCSpawner",  True, False, "River"),
	"River Francine":                  LocationData(367759219, "npc_francine",                    "NPCSpawner",  True, False, "River"),
	"Faramore Munhum":                 LocationData(367759220, "npc_munhum_quest",                "NPCSpawner",  True, False, "Faramore")
}

npc_foolish_locations = {
	"Faramore Boru":                   LocationData(367759221, "npc_boru",                        "NPC",         True, False, "Faramore"),
	"Faramore Kari":                   LocationData(367759222, "npc_kari",                        "NPC",         True, False, "Faramore"),
	"Faramore Univor":                 LocationData(367759223, "npc_univor",                      "NPC",         True, False, "Faramore"),
	"Faramore Salvik":                 LocationData(367759224, "npc_salvik",                      "NPC",         True, False, "Faramore"),
	"Faramore Maki":                   LocationData(367759225, "npc_maki",                        "NPC",         True, False, "Faramore"),
	"Faramore Payop":                  LocationData(367759226, "npc_payop",                       "NPC",         True, False, "Faramore"),
	"Volcano Joe":                     LocationData(367759227, "npc_joe",                         "NPC",         True, False, "Volcano"),
	"River Barnabuss":                 LocationData(367759228, "npc_barnabuss",                   "NPC",         True, False, "River")
}

npc_locked_locations = {
	"Faramore Mortar":                 LocationData(367759229, "npc_mortar",                      "NPC",         False, True, "Faramore"),
	"Swamp Frich":                     LocationData(367759230, "npc_frich",                       "NPC",         False, True, "Swamp"),
	"Forest Rudy (Start)":             LocationData(367759231, "npc_rudy_start",                  "NPC",         False, True, "Forest"),
	"Forest Rudy (End)":               LocationData(367759232, "npc_rudy_goal",                   "NPC",         False, True, "Forest"),
	"Peak Rudy (Start)":               LocationData(367759233, "npc_rudy_start",                  "NPC",         False, True, "Peak"),
	"Peak Rudy (End)":                 LocationData(367759234, "npc_rudy_goal",                   "NPC",         False, True, "Peak"),
	"Hills Rudy (Start)":              LocationData(367759235, "npc_rudy_start",                  "NPC",         False, True, "Hills"),
	"Hills Rudy (End)":                LocationData(367759236, "npc_rudy_goal",                   "NPC",         False, True, "Hills")
}

rock_locations = {
	"Orange Rock":                     LocationData(367759237, "obj_quest_rock_orange",           "Rock",        False, False, None),
	"Brown Rock":                      LocationData(367759238, "obj_quest_rock_brown",            "Rock",        False, False, None),
	"Gray Rock":                       LocationData(367759239, "obj_quest_rock_grey",             "Rock",        False, False, None),
	"Blue Rock":                       LocationData(367759240, "obj_quest_rock_blue",             "Rock",        False, False, None)
}

bonusreward_locations = {
	"Faramore Bonus Reward":           LocationData(367759241, "obj_null",                        "BonusReward", False, True, "Faramore Bonus"),
	"Forest Bonus Reward":             LocationData(367759242, "obj_quest_rubie_bag_25_1",        "BonusReward", False, False, "Forest Bonus"),
	"Caves Bonus Reward":              LocationData(367759243, "obj_quest_rubie_bag_25_2",        "BonusReward", False, False, "Caves Bonus"),
	"Desert Bonus Reward":             LocationData(367759244, "obj_quest_rubie_bag_30_1",        "BonusReward", False, False, "Desert Bonus"),
	"Canyon Bonus Reward":             LocationData(367759245, "obj_quest_rubie_bag_30_2",        "BonusReward", False, False, "Canyon Bonus"),
	"Swamp Bonus Reward":              LocationData(367759246, "obj_quest_rubie_bag_30_3",        "BonusReward", False, False, "Swamp Bonus"),
	"Peak Bonus Reward":               LocationData(367759247, "obj_quest_rubie_bag_40",          "BonusReward", False, False, "Peak Bonus"),
	"Crypts Bonus Reward":             LocationData(367759248, "obj_quest_rubie_bag_50_1",        "BonusReward", False, False, "Crypts Bonus"),
	"Volcano Bonus Reward":            LocationData(367759249, "obj_null",                        "BonusReward", False, True, "Volcano Bonus"),
	"Beach Bonus Reward":              LocationData(367759250, "obj_quest_rubie_bag_50_2",        "BonusReward", False, False, "Beach Bonus"),
	"River Bonus Reward":              LocationData(367759251, "obj_quest_rubie_bag_50_3",        "BonusReward", False, False, "River Bonus"),
	"Hills Bonus Reward":              LocationData(367759252, "obj_quest_rubie_bag_75_1",        "BonusReward", False, False, "Hills Bonus"),
	"Fort Bonus Reward":               LocationData(367759253, "obj_quest_rubie_bag_75_2",        "BonusReward", False, False, "Fort Bonus"),
	"Castle Bonus Reward":             LocationData(367759254, "obj_null",                        "BonusReward", False, True, "Castle Bonus"),
	"Lair Bonus Reward":               LocationData(367759255, "obj_quest_rubie_bag_100",         "BonusReward", False, False, "Lair Bonus")
}

levelunlock_locations = {
	"Default 1":                       LocationData(367759256, "world_faramore_town_unlocked",    "LevelUnlock", False, False, None),
	"Default 2":                       LocationData(367759257, "world_durridin_forest_unlocked",  "LevelUnlock", False, False, None),
	"Forest Beacon 1":                 LocationData(367759258, "world_cogwyn_caves_unlocked",     "LevelUnlock", False, False, "Forest Beacon"),
	"Forest Beacon 2":                 LocationData(367759259, "world_anju_desert_unlocked",      "LevelUnlock", False, False, "Forest Beacon"),
	"Forest Beacon 3":                 LocationData(367759260, "world_creece_canyon_unlocked",    "LevelUnlock", False, False, "Forest Beacon"),
	"Desert Beacon 1":                 LocationData(367759261, "world_norin_swamp_unlocked",      "LevelUnlock", False, False, "Desert Beacon"),
	"Desert Beacon 2":                 LocationData(367759262, "world_chillinax_peaks_unlocked",  "LevelUnlock", False, False, "Desert Beacon"),
	"Desert Beacon 3":                 LocationData(367759263, "world_boanjale_crypts_unlocked",  "LevelUnlock", False, False, "Desert Beacon"),
	"Swamp Beacon 1":                  LocationData(367759264, "world_sprigum_volcano_unlocked",  "LevelUnlock", False, False, "Swamp Beacon"),
	"Swamp Beacon 2":                  LocationData(367759265, "world_badonc_beach_unlocked",     "LevelUnlock", False, False, "Swamp Beacon"),
	"Swamp Beacon 3":                  LocationData(367759266, "world_ryha_river_unlocked",       "LevelUnlock", False, False, "Swamp Beacon"),
	"Beach Beacon 1":                  LocationData(367759267, "world_lichen_hills_unlocked",     "LevelUnlock", False, False, "Beach Beacon"),
	"Beach Beacon 2":                  LocationData(367759268, "world_fort_findula_unlocked",     "LevelUnlock", False, False, "Beach Beacon"),
	"Hills Beacon 1":                  LocationData(367759269, "world_dennys_castle_unlocked",    "LevelUnlock", False, False, "Hills Beacon"),
	"Hills Beacon 2":                  LocationData(367759270, "world_daimurs_lair_unlocked",     "LevelUnlock", False, False, "Hills Beacon")
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