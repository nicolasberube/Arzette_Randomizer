from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class ArzetteItem(Item):
    game: str = "Arzette"

class ItemData(NamedTuple):
    btid: int | None
    qty: int
    type: ItemClassification
    default_location: str

bag_table = {
    "obj_item_bag_1":                  ItemData(2793883000, 1, ItemClassification.progression, "Forest_Bag_(First_Room_1)"),
	"obj_item_bag_2":                  ItemData(2793883001, 1, ItemClassification.progression, "Forest_Bag_(First_Room_2)"),
	"obj_item_bag_3":                  ItemData(2793883002, 1, ItemClassification.progression, "Forest_Bag_(Sword_Wave)"),
	"obj_item_bag_4":                  ItemData(2793883003, 1, ItemClassification.progression, "Forest_Bag_(Last_Room)"),
	"obj_item_bag_5":                  ItemData(2793883004, 1, ItemClassification.progression, "Caves_Bag_(Rope_Ladder)"),
	"obj_item_bag_6":                  ItemData(2793883005, 1, ItemClassification.progression, "Caves_Bag_(Last_Room)"),
	"obj_item_bag_7":                  ItemData(2793883006, 1, ItemClassification.progression, "Desert_Bag_(First_Room_1)"),
	"obj_item_bag_8":                  ItemData(2793883007, 1, ItemClassification.progression, "Desert_Bag_(First_Room_2)"),
	"obj_item_bag_9":                  ItemData(2793883008, 1, ItemClassification.progression, "Desert_Bag_(Last_Room)"),
	"obj_item_bag_10":                 ItemData(2793883009, 1, ItemClassification.progression, "Canyon_Bag_(Before_Checkpoint)"),
	"obj_item_bag_11":                 ItemData(2793883010, 1, ItemClassification.progression, "Canyon_Bag_(After_Checkpoint_1)"),
	"obj_item_bag_12":                 ItemData(2793883011, 1, ItemClassification.progression, "Canyon_Bag_(After_Checkpoint_2)"),
	"obj_item_bag_13":                 ItemData(2793883012, 1, ItemClassification.progression, "Canyon_Bag_(After_Checkpoint_3)"),
	"obj_item_bag_14":                 ItemData(2793883013, 1, ItemClassification.progression, "Canyon_Bag_(First_Room_End)"),
	"obj_item_bag_15":                 ItemData(2793883014, 1, ItemClassification.progression, "Canyon_Bag_(After_Zipline_1)"),
	"obj_item_bag_16":                 ItemData(2793883015, 1, ItemClassification.progression, "Canyon_Bag_(After_Zipline_2)"),
	"obj_item_bag_17":                 ItemData(2793883016, 1, ItemClassification.progression, "Canyon_Bag_(After_Zipline_3)"),
	"obj_item_bag_18":                 ItemData(2793883017, 1, ItemClassification.progression, "Canyon_Bag_(Motte_House)"),
	"obj_item_bag_19":                 ItemData(2793883018, 1, ItemClassification.progression, "Swamp_Bag_(First_Room)"),
	"obj_item_bag_20":                 ItemData(2793883019, 1, ItemClassification.progression, "Peak_Bag_(First_Cave_1)"),
	"obj_item_bag_21":                 ItemData(2793883020, 1, ItemClassification.progression, "Peak_Bag_(First_Cave_2)"),
	"obj_item_bag_22":                 ItemData(2793883021, 1, ItemClassification.progression, "Peak_Bag_(Before_Apatu)"),
	"obj_item_bag_23":                 ItemData(2793883022, 1, ItemClassification.progression, "Peak_Bag_(After_Apatu)"),
	"obj_item_bag_24":                 ItemData(2793883023, 1, ItemClassification.progression, "Crypts_Bag_(Skelvis)"),
	"obj_item_bag_25":                 ItemData(2793883024, 1, ItemClassification.progression, "Beach_Bag_(First_Room)"),
	"obj_item_bag_26":                 ItemData(2793883025, 1, ItemClassification.progression, "River_Bag_(Last_Room)"),
	"obj_item_bag_27":                 ItemData(2793883026, 1, ItemClassification.progression, "Hills_Bag_(Barn)"),
	"obj_item_bag_28":                 ItemData(2793883027, 1, ItemClassification.progression, "Hills_Bag_(Music_Shrine)"),
	"obj_item_bag_29":                 ItemData(2793883028, 1, ItemClassification.progression, "Fort_Bag_(Dungeon_1)"),
	"obj_item_bag_30":                 ItemData(2793883029, 1, ItemClassification.progression, "Fort_Bag_(Dungeon_2)"),
	"obj_item_bag_31":                 ItemData(2793883030, 1, ItemClassification.progression, "Fort_Bag_(Dungeon_3)"),
	"obj_item_bag_32":                 ItemData(2793883031, 1, ItemClassification.progression, "Fort_Bag_(Dungeon_4)"),
	"obj_item_bag_33":                 ItemData(2793883032, 1, ItemClassification.progression, "Fort_Bag_(Dark_Room)"),
	"obj_item_bag_34":                 ItemData(2793883033, 1, ItemClassification.progression, "Fort_Bag_(Top_Room_1)"),
	"obj_item_bag_35":                 ItemData(2793883034, 1, ItemClassification.progression, "Fort_Bag_(Top_Room_2)"),
	"obj_item_bag_36":                 ItemData(2793883035, 1, ItemClassification.progression, "Fort_Bag_(Top_Room_3)"),
	"obj_item_bag_37":                 ItemData(2793883036, 1, ItemClassification.progression, "Fort_Bag_(Last_Room)"),
	"obj_item_bag_38":                 ItemData(2793883037, 1, ItemClassification.progression, "Castle_Bag_(Entrance)"),
	"obj_item_bag_39":                 ItemData(2793883038, 1, ItemClassification.progression, "Castle_Bag_(Top_Room)"),
	"obj_item_bag_40":                 ItemData(2793883039, 1, ItemClassification.progression, "Castle_Bag_(Bonus)"),
	"obj_item_bag_41":                 ItemData(2793883040, 1, ItemClassification.progression, "Lair_Bag_(First_Room)"),
	"obj_item_bag_42":                 ItemData(2793883041, 1, ItemClassification.progression, "Lair_Bag_(Lava_Room)"),
	"obj_item_bag_43":                 ItemData(2793883042, 1, ItemClassification.progression, "Lair_Bag_(Final_Room_1)"),
	"obj_item_bag_44":                 ItemData(2793883043, 1, ItemClassification.progression, "Lair_Bag_(Final_Room_2)"),
	"obj_item_bag_45":                 ItemData(2793883044, 1, ItemClassification.progression, "Lair_Bag_(Final_Room_3)"),
	"obj_item_bag_46":                 ItemData(2793883045, 1, ItemClassification.progression, "Crypts_Bag_(Crypt)")
}
key_table = {
	"key_faramore_2":                  ItemData(2793883046, 1, ItemClassification.progression, "Faramore_Key_(Well)"),
	"key_faramore_1":                  ItemData(2793883047, 1, ItemClassification.progression, "Faramore_Key_(Tavern)"),
	"key_durridin":                    ItemData(2793883048, 1, ItemClassification.progression, "Forest_Key"),
	"key_anju":                        ItemData(2793883049, 1, ItemClassification.progression, "Desert_Key"),
	"key_creece":                      ItemData(2793883050, 1, ItemClassification.progression, "Canyon_Key"),
	"key_norin":                       ItemData(2793883051, 1, ItemClassification.progression, "Swamp_Key_(Frich_House)"),
	"key_norin_2":                     ItemData(2793883052, 1, ItemClassification.progression, "Swamp_Key_(Griffin_Boots)"),
	"key_chillinax":                   ItemData(2793883053, 1, ItemClassification.progression, "Peak_Key"),
	"key_boanjale":                    ItemData(2793883054, 1, ItemClassification.progression, "Crypts_Key"),
	"key_badonc":                      ItemData(2793883055, 1, ItemClassification.progression, "Beach_Key_(First_House)"),
	"key_badonc_2":                    ItemData(2793883056, 1, ItemClassification.progression, "Beach_Key_(Tork_Cabin)"),
	"key_ryha":                        ItemData(2793883057, 1, ItemClassification.progression, "River_Key_(Francine)"),
	"key_ryha_2":                      ItemData(2793883058, 1, ItemClassification.progression, "River_Key_(Submarine)"),
	"key_lichen":                      ItemData(2793883059, 1, ItemClassification.progression, "Hills_Key"),
	"key_findula_1":                   ItemData(2793883060, 1, ItemClassification.progression, "Fort_Key_(First_Room)"),
	"key_findula_2":                   ItemData(2793883061, 1, ItemClassification.progression, "Fort_Key_(Top_Room)"),
	"key_denny_2":                     ItemData(2793883062, 1, ItemClassification.progression, "Castle_Key_(Nodelki)"),
	"key_denny_1":                     ItemData(2793883063, 1, ItemClassification.progression, "Castle_Key_(Left_Room)")
}

candle_table = {
	"obj_sacred_candle_24":            ItemData(2793883064, 1, ItemClassification.progression, "Faramore_Candle_(Empty_House)"),
	"obj_sacred_candle_25":            ItemData(2793883065, 1, ItemClassification.progression, "Faramore_Candle_(Cypress_House)"),
	"obj_sacred_candle_1":             ItemData(2793883066, 1, ItemClassification.progression, "Forest_Candle_(Tree)"),
	"obj_sacred_candle_2":             ItemData(2793883067, 1, ItemClassification.progression, "Forest_Candle_(Cypress)"),
	"obj_sacred_candle_5":             ItemData(2793883068, 1, ItemClassification.progression, "Caves_Candle_(First_Dark_Room)"),
	"obj_sacred_candle_26":            ItemData(2793883069, 1, ItemClassification.progression, "Caves_Candle_(Second_Dark_Room)"),
	"obj_sacred_candle_3":             ItemData(2793883070, 1, ItemClassification.progression, "Desert_Candle_(Pit)"),
	"obj_sacred_candle_4":             ItemData(2793883071, 1, ItemClassification.progression, "Desert_Candle_(Last_Room)"),
	"obj_sacred_candle_6":             ItemData(2793883072, 1, ItemClassification.progression, "Canyon_Candle_(First_Room_End)"),
	"obj_sacred_candle_7":             ItemData(2793883073, 1, ItemClassification.progression, "Canyon_Candle_(Motte_House)"),
	"obj_sacred_candle_8":             ItemData(2793883074, 1, ItemClassification.progression, "Swamp_Candle_(First_Room)"),
	"obj_sacred_candle_27":            ItemData(2793883075, 1, ItemClassification.progression, "Swamp_Candle_(Frich_House)"),
	"obj_sacred_candle_9":             ItemData(2793883076, 1, ItemClassification.progression, "Peak_Candle_(First_Cave)"),
	"obj_sacred_candle_10":            ItemData(2793883077, 1, ItemClassification.progression, "Peak_Candle_(Ciclena_Cave)"),
	"obj_sacred_candle_28":            ItemData(2793883078, 1, ItemClassification.progression, "Crypts_Candle_(After_Crypt)"),
	"obj_sacred_candle_11":            ItemData(2793883079, 1, ItemClassification.progression, "Crypts_Candle_(Skelvis)"),
	"obj_sacred_candle_12":            ItemData(2793883080, 1, ItemClassification.progression, "Volcano_Candle_(First_Room)"),
	"obj_sacred_candle_29":            ItemData(2793883081, 1, ItemClassification.progression, "Volcano_Candle_(Last_Room)"),
	"obj_sacred_candle_14":            ItemData(2793883082, 1, ItemClassification.progression, "Beach_Candle_(Tork_Cabin)"),
	"obj_sacred_candle_13":            ItemData(2793883083, 1, ItemClassification.progression, "Beach_Candle_(Cave)"),
	"obj_sacred_candle_15":            ItemData(2793883084, 1, ItemClassification.progression, "River_Candle_(Boat)"),
	"obj_sacred_candle_16":            ItemData(2793883085, 1, ItemClassification.progression, "River_Candle_(Last_Room)"),
	"obj_sacred_candle_30":            ItemData(2793883086, 1, ItemClassification.progression, "Hills_Candle_(Cave)"),
	"obj_sacred_candle_17":            ItemData(2793883087, 1, ItemClassification.progression, "Hills_Candle_(Music_Shrine)"),
	"obj_sacred_candle_18":            ItemData(2793883088, 1, ItemClassification.progression, "Fort_Candle_(Dark_Room)"),
	"obj_sacred_candle_19":            ItemData(2793883089, 1, ItemClassification.progression, "Fort_Candle_(Last_Room)"),
	"obj_sacred_candle_20":            ItemData(2793883090, 1, ItemClassification.progression, "Castle_Candle_(Right_Room)"),
	"obj_sacred_candle_21":            ItemData(2793883091, 1, ItemClassification.progression, "Castle_Candle_(Top_Room)"),
	"obj_sacred_candle_22":            ItemData(2793883092, 1, ItemClassification.progression, "Lair_Candle_(Tree_Trunk)"),
	"obj_sacred_candle_23":            ItemData(2793883093, 1, ItemClassification.progression, "Lair_Candle_(Tree_Top)")
}

coin_table = {
	"obj_hidden_coin_faramore":        ItemData(2793883094, 1, ItemClassification.progression, "Faramore_Coin"),
	"obj_hidden_coin_durridin":        ItemData(2793883095, 1, ItemClassification.progression, "Forest_Coin"),
	"obj_hidden_coin_cogwyn":          ItemData(2793883096, 1, ItemClassification.progression, "Caves_Coin"),
	"obj_hidden_coin_anju":            ItemData(2793883097, 1, ItemClassification.progression, "Desert_Coin"),
	"obj_hidden_coin_creece":          ItemData(2793883098, 1, ItemClassification.progression, "Canyon_Coin"),
	"obj_hidden_coin_norin":           ItemData(2793883099, 1, ItemClassification.progression, "Swamp_Coin"),
	"obj_hidden_coin_chillinax":       ItemData(2793883100, 1, ItemClassification.progression, "Peak_Coin"),
	"obj_hidden_coin_boanjale":        ItemData(2793883101, 1, ItemClassification.progression, "Crypts_Coin"),
	"obj_hidden_coin_sprigum":         ItemData(2793883102, 1, ItemClassification.progression, "Volcano_Coin"),
	"obj_hidden_coin_badonc":          ItemData(2793883103, 1, ItemClassification.progression, "Beach_Coin"),
	"obj_hidden_coin_ryha":            ItemData(2793883104, 1, ItemClassification.progression, "River_Coin"),
	"obj_hidden_coin_lichen":          ItemData(2793883105, 1, ItemClassification.progression, "Hills_Coin"),
	"obj_hidden_coin_findula":         ItemData(2793883106, 1, ItemClassification.progression, "Fort_Coin"),
	"obj_hidden_coin_denny":           ItemData(2793883107, 1, ItemClassification.progression, "Castle_Coin"),
	"obj_hidden_coin_daimur":          ItemData(2793883108, 1, ItemClassification.progression, "Lair_Coin")
}

plant_table = {
	"obj_quest_plant_a":               ItemData(2793883109, 1, ItemClassification.progression, "Swamp_Plant"),
	"obj_quest_plant_b":               ItemData(2793883110, 1, ItemClassification.progression, "Beach_Plant"),
	"obj_quest_plant_c":               ItemData(2793883111, 1, ItemClassification.progression, "Hills_Plant")
}

upgrade_table = {
	"obj_quest_upgrade_power_stones":  ItemData(2793883112, 1, ItemClassification.progression, "Power_Stone_Upgrade"),
	"obj_quest_upgrade_wallet":        ItemData(2793883113, 1, ItemClassification.progression, "Wallet_Upgrade"),
	"obj_quest_upgrade_bombs":         ItemData(2793883114, 1, ItemClassification.progression, "Bomb_Upgrade"),
	"obj_quest_upgrade_lamp_oil":      ItemData(2793883115, 1, ItemClassification.progression, "Lamp_Oil_Upgrade"),
	"obj_quest_upgrade_ropes":         ItemData(2793883116, 1, ItemClassification.progression, "Rope_Upgrade"),
	"obj_quest_upgrade_soul_bag":      ItemData(2793883117, 1, ItemClassification.progression, "Soul_Upgrade"),
	"obj_quest_infinite_soulfire":     ItemData(2793883118, 1, ItemClassification.progression, "Infinite_Soulfire")
}

life_table = {
	"obj_lifeup_1":                    ItemData(2793883119, 1, ItemClassification.progression, "Desert_Life-Up"),
	"obj_lifeup_2":                    ItemData(2793883120, 1, ItemClassification.progression, "Crypts_Life-Up"),
	"obj_lifeup_3":                    ItemData(2793883121, 1, ItemClassification.progression, "River_Life-Up")
}

race_table = {
	"obj_quest_race_reward_1":         ItemData(2793883122, 1, ItemClassification.progression, "Forest_Race_100_Rupees"),
	"obj_quest_race_reward_2":         ItemData(2793883123, 1, ItemClassification.progression, "Peak_Race_100_Rupees"),
	"obj_quest_race_reward_3":         ItemData(2793883124, 1, ItemClassification.progression, "Hills_Race_100_Rupees")
}

trading_table = {
	"key_findula_dungeon":             ItemData(2793883125, 1, ItemClassification.progression, "Dungeon_Key"),
	"obj_quest_funky_fungus":          ItemData(2793883126, 1, ItemClassification.progression, "Funky_Fungus"),
	"obj_quest_snail_salt":            ItemData(2793883127, 1, ItemClassification.progression, "Snail_Salt"),
	"obj_quest_cleaver_shovel":        ItemData(2793883128, 1, ItemClassification.progression, "Cleaver_Shovel"),
	"obj_quest_ogre_hair":             ItemData(2793883129, 1, ItemClassification.progression, "Ogre_Hair"),
	"obj_quest_refined_chains":        ItemData(2793883130, 1, ItemClassification.progression, "Oil_and_Chains"),
	"obj_quest_chainsword":            ItemData(2793883131, 1, ItemClassification.progression, "Chainsword"),
	"obj_quest_oil":                   ItemData(2793883132, 1, ItemClassification.progression, "Sacred_Oil")
}

jewel_table = {
	"obj_jof_1":                       ItemData(2793883133, 1, ItemClassification.progression, "Forest_Jewel"),
	"obj_jof_2":                       ItemData(2793883134, 1, ItemClassification.progression, "Canyon_Jewel"),
	"obj_jof_3":                       ItemData(2793883135, 1, ItemClassification.progression, "Peak_Jewel"),
	"obj_jof_4":                       ItemData(2793883136, 1, ItemClassification.progression, "Fort_Jewel"),
	"obj_jof_5":                       ItemData(2793883137, 1, ItemClassification.progression, "Castle_Jewel")
}

quest_table = {
	"obj_quest_bombs":                 ItemData(2793883138, 1, ItemClassification.progression, "Bombs"),
	"obj_quest_sword_wave":            ItemData(2793883139, 1, ItemClassification.progression, "Sword_Wave"),
	"obj_quest_golden_fly":            ItemData(2793883140, 1, ItemClassification.progression, "Golden_Fly"),
	"obj_quest_armor":                 ItemData(2793883141, 1, ItemClassification.progression, "Magic_Armor"),
	"obj_quest_silver_cricket":        ItemData(2793883142, 1, ItemClassification.progression, "Silver_Cricket"),
	"obj_quest_rope_ladder":           ItemData(2793883143, 1, ItemClassification.progression, "Rope_Ladder"),
	"obj_quest_shield_ring":           ItemData(2793883144, 1, ItemClassification.progression, "Shield_Ring"),
	"obj_quest_compass":               ItemData(2793883145, 1, ItemClassification.progression, "Compass"),
	"obj_quest_magic_boots":           ItemData(2793883146, 1, ItemClassification.progression, "Griffin_Boots"),
	"obj_quest_town_bell":             ItemData(2793883147, 1, ItemClassification.progression, "Bell"),
	"obj_quest_crystal_of_refraction": ItemData(2793883148, 1, ItemClassification.progression, "Crystal_of_Refraction"),
	"obj_quest_flute":                 ItemData(2793883149, 1, ItemClassification.progression, "Fatal_Flute"),
	"obj_quest_blue_beam":             ItemData(2793883150, 1, ItemClassification.progression, "Blue_Magic"),
	"obj_quest_electric_sword":        ItemData(2793883151, 1, ItemClassification.progression, "Lightning_Sword"),
	"obj_quest_shoes":                 ItemData(2793883152, 1, ItemClassification.progression, "Enchanted_Shoes"),
	"obj_quest_reflecting_shield":     ItemData(2793883153, 1, ItemClassification.progression, "Reflector_Ring"),
	"obj_quest_winged_belt":           ItemData(2793883154, 1, ItemClassification.progression, "Winged_Belt"),
	"obj_quest_sword":                 ItemData(2793883155, 1, ItemClassification.progression, "Purple_Magic"),
	"obj_quest_citizenship":           ItemData(2793883156, 1, ItemClassification.progression, "Citizenship_Papers"),
	"obj_quest_canteen":               ItemData(2793883157, 1, ItemClassification.progression, "Canteen"),
	"obj_quest_beach_calendar":        ItemData(2793883158, 1, ItemClassification.progression, "Calendar"),
	"obj_quest_dewey_reward":          ItemData(2793883159, 1, ItemClassification.progression, "200_Rupees"),
	"obj_quest_lantern":               ItemData(2793883160, 1, ItemClassification.progression, "Lantern"),
	"obj_quest_esc_rope":              ItemData(2793883161, 1, ItemClassification.progression, "Rope"),
	"obj_quest_fairy_dust":            ItemData(2793883162, 1, ItemClassification.progression, "Fairy_Dust"),
	"obj_quest_backstep":              ItemData(2793883163, 1, ItemClassification.progression, "Backstep"),
	"obj_quest_gun":                   ItemData(2793883164, 1, ItemClassification.progression, "Smart_Gun"),
	"obj_quest_star_earrings":         ItemData(2793883165, 1, ItemClassification.progression, "Star_Earrings"),
	"obj_quest_pendant":               ItemData(2793883166, 1, ItemClassification.progression, "Power_Pendant"),
	"obj_quest_pg":                    ItemData(2793883167, 1, ItemClassification.progression, "Bomb_Gauntlet"),
	"obj_quest_speedy_shoes":          ItemData(2793883168, 1, ItemClassification.progression, "Speedy_Shoes"),
	"obj_quest_magic_cloak":           ItemData(2793883169, 1, ItemClassification.progression, "Magic_Cloak"),
	"obj_quest_double_wave":           ItemData(2793883170, 1, ItemClassification.progression, "Double_Wave")
}

rock_table = {
	"obj_quest_rock_orange":           ItemData(2793883171, 1, ItemClassification.progression, "Orange_Rock"),
	"obj_quest_rock_brown":            ItemData(2793883172, 1, ItemClassification.progression, "Brown_Rock"),
	"obj_quest_rock_grey":             ItemData(2793883173, 1, ItemClassification.progression, "Gray_Rock"),
	"obj_quest_rock_blue":             ItemData(2793883174, 1, ItemClassification.progression, "Blue_Rock")
}

scroll_table = {
	"obj_bonus_scroll_1":              ItemData(2793883175, 1, ItemClassification.progression, "Faramore_Bonus"),
	"obj_bonus_scroll_2":              ItemData(2793883176, 1, ItemClassification.progression, "Forest_Bonus"),
	"obj_bonus_scroll_3":              ItemData(2793883177, 1, ItemClassification.progression, "Caves_Bonus"),
	"obj_bonus_scroll_4":              ItemData(2793883178, 1, ItemClassification.progression, "Desert_Bonus"),
	"obj_bonus_scroll_5":              ItemData(2793883179, 1, ItemClassification.progression, "Canyon_Bonus"),
	"obj_bonus_scroll_6":              ItemData(2793883180, 1, ItemClassification.progression, "Swamp_Bonus"),
	"obj_bonus_scroll_7":              ItemData(2793883181, 1, ItemClassification.progression, "Peak_Bonus"),
	"obj_bonus_scroll_8":              ItemData(2793883182, 1, ItemClassification.progression, "Crypts_Bonus"),
	"obj_bonus_scroll_9":              ItemData(2793883183, 1, ItemClassification.progression, "Volcano_Bonus"),
	"obj_bonus_scroll_10":             ItemData(2793883184, 1, ItemClassification.progression, "Beach_Bonus"),
	"obj_bonus_scroll_11":             ItemData(2793883185, 1, ItemClassification.progression, "River_Bonus"),
	"obj_bonus_scroll_12":             ItemData(2793883186, 1, ItemClassification.progression, "Hills_Bonus"),
	"obj_bonus_scroll_13":             ItemData(2793883187, 1, ItemClassification.progression, "Fort_Bonus"),
	"obj_bonus_scroll_14":             ItemData(2793883188, 1, ItemClassification.progression, "Castle_Bonus"),
	"obj_bonus_scroll_15":             ItemData(2793883189, 1, ItemClassification.progression, "Lair_Bonus")
}

reward_table = {
	"obj_quest_rubie_bag_25_1":        ItemData(2793883190, 1, ItemClassification.progression, "Forest_Bonus_Reward"),
	"obj_quest_rubie_bag_25_2":        ItemData(2793883191, 1, ItemClassification.progression, "Caves_Bonus_Reward"),
	"obj_quest_rubie_bag_30_1":        ItemData(2793883192, 1, ItemClassification.progression, "Desert_Bonus_Reward"),
	"obj_quest_rubie_bag_30_2":        ItemData(2793883193, 1, ItemClassification.progression, "Canyon_Bonus_Reward"),
	"obj_quest_rubie_bag_30_3":        ItemData(2793883194, 1, ItemClassification.progression, "Swamp_Bonus_Reward"),
	"obj_quest_rubie_bag_40":          ItemData(2793883195, 1, ItemClassification.progression, "Peak_Bonus_Reward"),
	"obj_quest_rubie_bag_50_1":        ItemData(2793883196, 1, ItemClassification.progression, "Crypts_Bonus_Reward"),
	"obj_quest_rubie_bag_50_2":        ItemData(2793883197, 1, ItemClassification.progression, "Beach_Bonus_Reward"),
	"obj_quest_rubie_bag_50_3":        ItemData(2793883198, 1, ItemClassification.progression, "River_Bonus_Reward"),
	"obj_quest_rubie_bag_75_1":        ItemData(2793883199, 1, ItemClassification.progression, "Hills_Bonus_Reward"),
	"obj_quest_rubie_bag_75_2":        ItemData(2793883200, 1, ItemClassification.progression, "Fort_Bonus_Reward"),
	"obj_quest_rubie_bag_100":         ItemData(2793883201, 1, ItemClassification.progression, "Lair_Bonus_Reward")
}

npc_table = {
	"npc_boru":                        ItemData(2793883202, 1, ItemClassification.progression, "Faramore_Boru"),
	"npc_univor":                      ItemData(2793883203, 1, ItemClassification.progression, "Faramore_Univor"),
	"npc_salvik":                      ItemData(2793883204, 1, ItemClassification.progression, "Faramore_Salvik"),
	"npc_maki":                        ItemData(2793883205, 1, ItemClassification.progression, "Faramore_Maki"),
	"npc_payop":                       ItemData(2793883206, 1, ItemClassification.progression, "Faramore_Payop"),
	"npc_yukeen":                      ItemData(2793883207, 1, ItemClassification.progression, "Faramore_Yukeen"),
	"npc_mayor":                       ItemData(2793883208, 1, ItemClassification.progression, "Faramore_Covenplate"),
	"npc_kari":                        ItemData(2793883209, 1, ItemClassification.progression, "Faramore_Kari"),
	"npc_kari_quest":                  ItemData(2793883210, 1, ItemClassification.progression, "Faramore_Kari_Quest"),
	"npc_alven":                       ItemData(2793883211, 1, ItemClassification.progression, "Faramore_Alven"),
	"npc_brinda":                      ItemData(2793883212, 1, ItemClassification.progression, "Faramore_Brinda"),
	"npc_frich_quest":                 ItemData(2793883213, 1, ItemClassification.progression, "Faramore_Frich"),
	"npc_rudy":                        ItemData(2793883214, 1, ItemClassification.progression, "Faramore_Rudy"),
	"npc_barnabuss_quest":             ItemData(2793883215, 1, ItemClassification.progression, "Faramore_Barnabuss"),
	"npc_denny":                       ItemData(2793883216, 1, ItemClassification.progression, "Faramore_Denny"),
	"npc_dewey":                       ItemData(2793883217, 1, ItemClassification.progression, "Faramore_Dewey"),
	"npc_cypress_quest":               ItemData(2793883218, 1, ItemClassification.progression, "Faramore_Cypress"),
	"npc_munhum_quest":                ItemData(2793883219, 1, ItemClassification.progression, "Faramore_Munhum"),
	"npc_cypress":                     ItemData(2793883220, 1, ItemClassification.progression, "Forest_Cypress"),
	"npc_munhum":                      ItemData(2793883221, 1, ItemClassification.progression, "Caves_Munhum"),
	"npc_ellido":                      ItemData(2793883222, 1, ItemClassification.progression, "Caves_Ellido"),
	"npc_fairy":                       ItemData(2793883223, 1, ItemClassification.progression, "Desert_Fairy"),
	"npc_crowdee":                     ItemData(2793883224, 1, ItemClassification.progression, "Canyon_Crowdee"),
	"npc_motte":                       ItemData(2793883225, 1, ItemClassification.progression, "Canyon_Motte"),
	"npc_odie":                        ItemData(2793883226, 1, ItemClassification.progression, "Canyon_Odie"),
	"npc_glubbert":                    ItemData(2793883227, 1, ItemClassification.progression, "Swamp_Glubbert"),
	"npc_ciclena":                     ItemData(2793883228, 1, ItemClassification.progression, "Peak_Ciclena"),
	"npc_skelvis":                     ItemData(2793883229, 1, ItemClassification.progression, "Crypts_Skelvis"),
	"npc_fleetus":                     ItemData(2793883230, 1, ItemClassification.progression, "Beach_Fleetus"),
	"npc_tork":                        ItemData(2793883231, 1, ItemClassification.progression, "Beach_Tork"),
	"npc_barnabuss":                   ItemData(2793883232, 1, ItemClassification.progression, "River_Barnabuss"),
	"npc_francine":                    ItemData(2793883233, 1, ItemClassification.progression, "River_Francine"),
	"npc_morgh":                       ItemData(2793883234, 1, ItemClassification.progression, "River_Morgh"),
	"npc_milbert":                     ItemData(2793883235, 1, ItemClassification.progression, "Hills_Milbert"),
	"npc_zazie":                       ItemData(2793883236, 1, ItemClassification.progression, "Lair_Zazie"),
	"npc_joe":                         ItemData(2793883237, 1, ItemClassification.progression, "Volcano_Joe")}

locked_npc_table = {
	"npc_mortar":                      ItemData(2793883238, 1, ItemClassification.progression, "Faramore_Mortar"),
	"npc_frich":                       ItemData(2793883239, 1, ItemClassification.progression, "Swamp_Frich"),
	"npc_rudy_start":                  ItemData(2793883240, 3, ItemClassification.progression, ""),
	"npc_rudy_goal":                   ItemData(2793883241, 3, ItemClassification.progression, ""),
}

beacon_table = {
	"beacon_default":                  ItemData(2793883242, 1, ItemClassification.progression, "Default_Beacon"),
	"beacon_durridin":                 ItemData(2793883243, 1, ItemClassification.progression, "Forest_Beacon"),
	"beacon_anju_desert":              ItemData(2793883244, 1, ItemClassification.progression, "Desert_Beacon"),
	"beacon_norin_swamp":              ItemData(2793883245, 1, ItemClassification.progression, "Swamp_Beacon"),
	"beacon_badonc_beach":             ItemData(2793883246, 1, ItemClassification.progression, "Beach_Beacon"),
	"beacon_lichen_hills":             ItemData(2793883247, 1, ItemClassification.progression, "Hills_Beacon")
}

level_table = {
	"world_faramore_town_unlocked":    ItemData(2793883248, 1, ItemClassification.progression, "Default_1"),
	"world_durridin_forest_unlocked":  ItemData(2793883249, 1, ItemClassification.progression, "Default_2"),
	"world_cogwyn_caves_unlocked":     ItemData(2793883250, 1, ItemClassification.progression, "Forest_Beacon_1"),
	"world_anju_desert_unlocked":      ItemData(2793883251, 1, ItemClassification.progression, "Forest_Beacon_2"),
	"world_creece_canyon_unlocked":    ItemData(2793883252, 1, ItemClassification.progression, "Forest_Beacon_3"),
	"world_norin_swamp_unlocked":      ItemData(2793883253, 1, ItemClassification.progression, "Desert_Beacon_1"),
	"world_chillinax_peaks_unlocked":  ItemData(2793883254, 1, ItemClassification.progression, "Desert_Beacon_2"),
	"world_boanjale_crypts_unlocked":  ItemData(2793883255, 1, ItemClassification.progression, "Desert_Beacon_3"),
	"world_sprigum_volcano_unlocked":  ItemData(2793883256, 1, ItemClassification.progression, "Swamp_Beacon_1"),
	"world_badonc_beach_unlocked":     ItemData(2793883257, 1, ItemClassification.progression, "Swamp_Beacon_2"),
	"world_ryha_river_unlocked":       ItemData(2793883258, 1, ItemClassification.progression, "Swamp_Beacon_3"),
	"world_lichen_hills_unlocked":     ItemData(2793883259, 1, ItemClassification.progression, "Beach_Beacon_1"),
	"world_fort_findula_unlocked":     ItemData(2793883260, 1, ItemClassification.progression, "Beach_Beacon_2"),
	"world_dennys_castle_unlocked":    ItemData(2793883261, 1, ItemClassification.progression, "Hills_Beacon_1"),
	"world_daimurs_lair_unlocked":     ItemData(2793883262, 1, ItemClassification.progression, "Hills_Beacon_2")
}

other_table = {
	"obj_boss_daimur":                 ItemData(2793883263, 1, ItemClassification.progression, "Daimur"),
	"obj_null":                        ItemData(2793883264, 3, ItemClassification.progression, "")
}

# Forest_Rudy_(Start)
# Peak_Rudy_(Start)
# Hills_Rudy_(Start)

# Faramore_Bonus_Reward
# Volcano_Bonus_Reward
# Castle_Bonus_Reward

all_item_table: Dict[str, ItemData] = {
    **bag_table,
    **key_table,
    **candle_table,
    **coin_table,
    **plant_table,
    **upgrade_table,
    **life_table,
    **race_table,
    **trading_table,
    **jewel_table,
    **quest_table,
    **rock_table,
    **scroll_table,
    **reward_table,
    **npc_table,
    **locked_npc_table,
    **beacon_table,
    **level_table,
    **other_table,
}

all_group_table: Dict[str, Dict[str, ItemData]] = {
    "bag": bag_table,
    "key": key_table,
    "candle": candle_table,
    "coin": coin_table,
    "plant": plant_table,
    "upgrade": upgrade_table,
    "life": life_table,
    "race": race_table,
    "trading": trading_table,
    "jewel": jewel_table,
    "quest": quest_table,
    "rock": rock_table,
    "scroll": scroll_table,
    "reward": reward_table,
    "npc": npc_table,
    "locked_npc": locked_npc_table,
    "beacon": beacon_table,
    "level": level_table,
    "other": other_table
}



"""
import csv
with open("../vanilla.csv", "r") as csvfile:
    vanilla_output = [row for row in csv.reader(csvfile, delimiter=",")]

variable_dictionary = {}
for i_r, row in enumerate(vanilla_output):
    if (i_r == 0 or row[0] == "" or row[0].startswith("[")):
        continue
    if row[0] in variable_dictionary:
        raise Exception("Cannot import vanilla.csv")
    variable_dictionary[row[0]] = row[1].split("//")[0]

string = []
i = -1
for key, value in variable_dictionary.items():
    i += 1
    add = f'"{value+"\":":33s} ItemData(2793883{i:003}, 1, ItemClassification.progression, "{key}")'
    string.append(add)
string = ',\n\t'.join(string)
print(string)
"""