from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ItemData(NamedTuple):
    arzid: int | None
    type: ItemClassification

bag_items = {
	"Forest Bag (First Room 1)":       ItemData(367759008, ItemClassification.filler),
	"Forest Bag (First Room 2)":       ItemData(367759009, ItemClassification.filler),
	"Forest Bag (Sword Wave)":         ItemData(367759015, ItemClassification.filler),
	"Forest Bag (Last Room)":          ItemData(367759018, ItemClassification.filler),
	"Caves Bag (Rope Ladder)":         ItemData(367759024, ItemClassification.filler),
	"Caves Bag (Last Room)":           ItemData(367759029, ItemClassification.filler),
	"Desert Bag (First Room 1)":       ItemData(367759032, ItemClassification.filler),
	"Desert Bag (First Room 2)":       ItemData(367759033, ItemClassification.filler),
	"Desert Bag (Last Room)":          ItemData(367759040, ItemClassification.filler),
	"Canyon Bag (Before Checkpoint)":  ItemData(367759043, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 1)": ItemData(367759044, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 2)": ItemData(367759045, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 3)": ItemData(367759046, ItemClassification.filler),
	"Canyon Bag (First Room End)":     ItemData(367759047, ItemClassification.filler),
	"Canyon Bag (After Zipline 1)":    ItemData(367759051, ItemClassification.filler),
	"Canyon Bag (After Zipline 2)":    ItemData(367759052, ItemClassification.filler),
	"Canyon Bag (After Zipline 3)":    ItemData(367759053, ItemClassification.filler),
	"Canyon Bag (Motte House)":        ItemData(367759055, ItemClassification.filler),
	"Swamp Bag (First Room)":          ItemData(367759058, ItemClassification.filler),
	"Peak Bag (First Cave 1)":         ItemData(367759068, ItemClassification.filler),
	"Peak Bag (First Cave 2)":         ItemData(367759069, ItemClassification.filler),
	"Peak Bag (Before Apatu)":         ItemData(367759074, ItemClassification.filler),
	"Peak Bag (After Apatu)":          ItemData(367759076, ItemClassification.filler),
	"Crypts Bag (Crypt)":              ItemData(367759081, ItemClassification.filler),
	"Crypts Bag (Skelvis)":            ItemData(367759085, ItemClassification.filler),
	"Beach Bag (First Room)":          ItemData(367759091, ItemClassification.filler),
	"River Bag (Last Room)":           ItemData(367759107, ItemClassification.filler),
	"Hills Bag (Barn)":                ItemData(367759114, ItemClassification.filler),
	"Hills Bag (Music Shrine)":        ItemData(367759116, ItemClassification.filler),
	"Fort Bag (Dungeon 1)":            ItemData(367759120, ItemClassification.filler),
	"Fort Bag (Dungeon 2)":            ItemData(367759121, ItemClassification.filler),
	"Fort Bag (Dungeon 3)":            ItemData(367759122, ItemClassification.filler),
	"Fort Bag (Dungeon 4)":            ItemData(367759123, ItemClassification.filler),
	"Fort Bag (Dark Room)":            ItemData(367759127, ItemClassification.filler),
	"Fort Bag (Top Room 1)":           ItemData(367759131, ItemClassification.filler),
	"Fort Bag (Top Room 2)":           ItemData(367759132, ItemClassification.filler),
	"Fort Bag (Top Room 3)":           ItemData(367759133, ItemClassification.filler),
	"Fort Bag (Last Room)":            ItemData(367759135, ItemClassification.filler),
	"Castle Bag (Entrance)":           ItemData(367759139, ItemClassification.filler),
	"Castle Bag (Top Room)":           ItemData(367759143, ItemClassification.filler),
	"Castle Bag (Bonus)":              ItemData(367759147, ItemClassification.filler),
	"Lair Bag (First Room)":           ItemData(367759153, ItemClassification.filler),
	"Lair Bag (Lava Room)":            ItemData(367759155, ItemClassification.filler),
	"Lair Bag (Final Room 1)":         ItemData(367759156, ItemClassification.filler),
	"Lair Bag (Final Room 2)":         ItemData(367759157, ItemClassification.filler),
	"Lair Bag (Final Room 3)":         ItemData(367759158, ItemClassification.filler)
}

key_items = {
	"Faramore Key (Well)":             ItemData(367759001, ItemClassification.progression),
	"Faramore Key (Tavern)":           ItemData(367759002, ItemClassification.progression),
	"Forest Key":                      ItemData(367759010, ItemClassification.progression),
	"Desert Key":                      ItemData(367759037, ItemClassification.progression),
	"Canyon Key":                      ItemData(367759050, ItemClassification.progression),
	"Swamp Key (Frich House)":         ItemData(367759060, ItemClassification.progression),
	"Swamp Key (Griffin Boots)":       ItemData(367759062, ItemClassification.progression),
	"Peak Key":                        ItemData(367759072, ItemClassification.progression),
	"Crypts Key":                      ItemData(367759080, ItemClassification.progression),
	"Beach Key (First House)":         ItemData(367759092, ItemClassification.progression),
	"Beach Key (Tork Cabin)":          ItemData(367759094, ItemClassification.progression),
	"River Key (Francine)":            ItemData(367759101, ItemClassification.progression),
	"River Key (Submarine)":           ItemData(367759104, ItemClassification.progression),
	"Hills Key":                       ItemData(367759115, ItemClassification.progression),
	"Fort Key (First Room)":           ItemData(367759125, ItemClassification.progression),
	"Fort Key (Top Room)":             ItemData(367759130, ItemClassification.progression),
	"Castle Key (Nodelki)":            ItemData(367759141, ItemClassification.progression),
	"Castle Key (Left Room)":          ItemData(367759146, ItemClassification.progression)
}

candle_items = {
	"Faramore Candle (Empty House)":   ItemData(367759004, ItemClassification.progression_deprioritized_skip_balancing),
	"Faramore Candle (Cypress House)": ItemData(367759005, ItemClassification.progression_deprioritized_skip_balancing),
	"Forest Candle (Tree)":            ItemData(367759012, ItemClassification.progression_deprioritized_skip_balancing),
	"Forest Candle (Cypress)":         ItemData(367759013, ItemClassification.progression_deprioritized_skip_balancing),
	"Caves Candle (First Dark Room)":  ItemData(367759025, ItemClassification.progression_deprioritized_skip_balancing),
	"Caves Candle (Second Dark Room)": ItemData(367759027, ItemClassification.progression_deprioritized_skip_balancing),
	"Desert Candle (Pit)":             ItemData(367759035, ItemClassification.progression_deprioritized_skip_balancing),
	"Desert Candle (Last Room)":       ItemData(367759038, ItemClassification.progression_deprioritized_skip_balancing),
	"Canyon Candle (First Room End)":  ItemData(367759048, ItemClassification.progression_deprioritized_skip_balancing),
	"Canyon Candle (Motte House)":     ItemData(367759056, ItemClassification.progression_deprioritized_skip_balancing),
	"Swamp Candle (First Room)":       ItemData(367759057, ItemClassification.progression_deprioritized_skip_balancing),
	"Swamp Candle (Frich House)":      ItemData(367759061, ItemClassification.progression_deprioritized_skip_balancing),
	"Peak Candle (First Cave)":        ItemData(367759067, ItemClassification.progression_deprioritized_skip_balancing),
	"Peak Candle (Ciclena Cave)":      ItemData(367759073, ItemClassification.progression_deprioritized_skip_balancing),
	"Crypts Candle (After Crypt)":     ItemData(367759082, ItemClassification.progression_deprioritized_skip_balancing),
	"Crypts Candle (Skelvis)":         ItemData(367759084, ItemClassification.progression_deprioritized_skip_balancing),
	"Volcano Candle (First Room)":     ItemData(367759087, ItemClassification.progression_deprioritized_skip_balancing),
	"Volcano Candle (Last Room)":      ItemData(367759089, ItemClassification.progression_deprioritized_skip_balancing),
	"Beach Candle (Tork Cabin)":       ItemData(367759095, ItemClassification.progression_deprioritized_skip_balancing),
	"Beach Candle (Cave)":             ItemData(367759098, ItemClassification.progression_deprioritized_skip_balancing),
	"River Candle (Boat)":             ItemData(367759103, ItemClassification.progression_deprioritized_skip_balancing),
	"River Candle (Last Room)":        ItemData(367759108, ItemClassification.progression_deprioritized_skip_balancing),
	"Hills Candle (Cave)":             ItemData(367759110, ItemClassification.progression_deprioritized_skip_balancing),
	"Hills Candle (Music Shrine)":     ItemData(367759117, ItemClassification.progression_deprioritized_skip_balancing),
	"Fort Candle (Dark Room)":         ItemData(367759126, ItemClassification.progression_deprioritized_skip_balancing),
	"Fort Candle (Last Room)":         ItemData(367759134, ItemClassification.progression_deprioritized_skip_balancing),
	"Castle Candle (Right Room)":      ItemData(367759140, ItemClassification.progression_deprioritized_skip_balancing),
	"Castle Candle (Top Room)":        ItemData(367759142, ItemClassification.progression_deprioritized_skip_balancing),
	"Lair Candle (Tree Trunk)":        ItemData(367759150, ItemClassification.progression_deprioritized_skip_balancing),
	"Lair Candle (Tree Top)":          ItemData(367759151, ItemClassification.progression_deprioritized_skip_balancing)
}

coin_items = {
	"Faramore Coin":                   ItemData(367759006, ItemClassification.progression),
	"Forest Coin":                     ItemData(367759014, ItemClassification.progression),
	"Caves Coin":                      ItemData(367759026, ItemClassification.progression),
	"Desert Coin":                     ItemData(367759031, ItemClassification.progression),
	"Canyon Coin":                     ItemData(367759054, ItemClassification.progression),
	"Swamp Coin":                      ItemData(367759059, ItemClassification.progression),
	"Peak Coin":                       ItemData(367759071, ItemClassification.progression),
	"Crypts Coin":                     ItemData(367759083, ItemClassification.progression),
	"Volcano Coin":                    ItemData(367759088, ItemClassification.progression),
	"Beach Coin":                      ItemData(367759093, ItemClassification.progression),
	"River Coin":                      ItemData(367759105, ItemClassification.progression),
	"Hills Coin":                      ItemData(367759112, ItemClassification.progression),
	"Fort Coin":                       ItemData(367759129, ItemClassification.progression),
	"Castle Coin":                     ItemData(367759145, ItemClassification.progression),
	"Lair Coin":                       ItemData(367759154, ItemClassification.progression)
}

plant_items = {
	"Swamp Plant":                     ItemData(367759064, ItemClassification.progression),
	"Beach Plant":                     ItemData(367759096, ItemClassification.progression),
	"Hills Plant":                     ItemData(367759118, ItemClassification.progression)
}

upgrade_items = {
	"Power Stone Upgrade":             ItemData(367759162, ItemClassification.useful),
	"Wallet Upgrade":                  ItemData(367759166, ItemClassification.useful),
	"Infinite Soulfire":               ItemData(367759167, ItemClassification.useful),
	"Bomb Upgrade":                    ItemData(367759168, ItemClassification.useful),
	"Lamp Oil Upgrade":                ItemData(367759171, ItemClassification.useful),
	"Rope Upgrade":                    ItemData(367759172, ItemClassification.useful),
	"Soul Upgrade":                    ItemData(367759192, ItemClassification.useful)
}

lifeup_items = {
	"Desert Life-Up":                  ItemData(367759039, ItemClassification.useful),
	"Crypts Life-Up":                  ItemData(367759077, ItemClassification.useful),
	"River Life-Up":                   ItemData(367759109, ItemClassification.useful)
}

race_items = {
	"Forest Race 100 Rupees":          ItemData(367759173, ItemClassification.filler),
	"Peak Race 100 Rupees":            ItemData(367759174, ItemClassification.filler),
	"Hills Race 100 Rupees":           ItemData(367759175, ItemClassification.filler)
}

trading_items = {
	"Sacred Oil":                      ItemData(367759124, ItemClassification.progression),
	"Dungeon Key":                     ItemData(367759163, ItemClassification.progression),
	"Chainsword":                      ItemData(367759164, ItemClassification.progression),
	"Snail Salt":                      ItemData(367759178, ItemClassification.progression),
	"Ogre Hair":                       ItemData(367759183, ItemClassification.progression),
	"Cleaver Shovel":                  ItemData(367759188, ItemClassification.progression),
	"Oil and Chains":                  ItemData(367759189, ItemClassification.progression),
	"Funky Fungus":                    ItemData(367759191, ItemClassification.progression)
}

jewel_items = {
	"Forest Jewel":                    ItemData(367759020, ItemClassification.progression | ItemClassification.useful),
	"Canyon Jewel":                    ItemData(367759049, ItemClassification.progression | ItemClassification.useful),
	"Peak Jewel":                      ItemData(367759075, ItemClassification.progression | ItemClassification.useful),
	"Fort Jewel":                      ItemData(367759137, ItemClassification.progression | ItemClassification.useful),
	"Castle Jewel":                    ItemData(367759149, ItemClassification.progression | ItemClassification.useful)
}

quest_items = {
	"Bombs":                           ItemData(367759007, ItemClassification.progression | ItemClassification.useful),
	"Sword Wave":                      ItemData(367759016, ItemClassification.progression | ItemClassification.useful),
	"Golden Fly":                      ItemData(367759017, ItemClassification.progression),
	"Magic Armor":                     ItemData(367759021, ItemClassification.progression),
	"Silver Cricket":                  ItemData(367759022, ItemClassification.progression),
	"Rope Ladder":                     ItemData(367759023, ItemClassification.progression),
	"Shield Ring":                     ItemData(367759030, ItemClassification.progression),
	"Compass":                         ItemData(367759034, ItemClassification.progression),
	"Griffin Boots":                   ItemData(367759063, ItemClassification.progression | ItemClassification.useful),
	"Bell":                            ItemData(367759078, ItemClassification.progression),
	"Crystal of Refraction":           ItemData(367759090, ItemClassification.progression),
	"Fatal Flute":                     ItemData(367759099, ItemClassification.progression),
	"Blue Magic":                      ItemData(367759106, ItemClassification.progression),
	"Lightning Sword":                 ItemData(367759111, ItemClassification.progression),
	"Enchanted Shoes":                 ItemData(367759128, ItemClassification.progression),
	"Reflector Ring":                  ItemData(367759136, ItemClassification.progression),
	"Winged Belt":                     ItemData(367759144, ItemClassification.progression | ItemClassification.useful),
	"Purple Magic":                    ItemData(367759160, ItemClassification.progression | ItemClassification.useful),
	"Citizenship Papers":              ItemData(367759161, ItemClassification.progression),
	"Canteen":                         ItemData(367759165, ItemClassification.progression),
	"Calendar":                        ItemData(367759169, ItemClassification.progression),
	"200 Rupees":                      ItemData(367759170, ItemClassification.filler),
	"Lantern":                         ItemData(367759176, ItemClassification.progression | ItemClassification.useful),
	"Rope":                            ItemData(367759177, ItemClassification.useful),
	"Fairy Dust":                      ItemData(367759179, ItemClassification.progression),
	"Backstep":                        ItemData(367759180, ItemClassification.useful),
	"Smart Gun":                       ItemData(367759181, ItemClassification.progression | ItemClassification.useful),
	"Star Earrings":                   ItemData(367759182, ItemClassification.progression),
	"Power Pendant":                   ItemData(367759184, ItemClassification.progression | ItemClassification.useful),
	"Bomb Gauntlet":                   ItemData(367759185, ItemClassification.progression | ItemClassification.useful),
	"Speedy Shoes":                    ItemData(367759186, ItemClassification.progression),
	"Magic Cloak":                     ItemData(367759187, ItemClassification.progression),
	"Double Wave":                     ItemData(367759190, ItemClassification.progression | ItemClassification.useful)
}

rock_items = {
	"Orange Rock":                     ItemData(367759237, ItemClassification.progression),
	"Brown Rock":                      ItemData(367759238, ItemClassification.progression),
	"Gray Rock":                       ItemData(367759239, ItemClassification.progression),
	"Blue Rock":                       ItemData(367759240, ItemClassification.progression)
}

scroll_items = {
	"Faramore Bonus":                  ItemData(367759003, ItemClassification.progression),
	"Forest Bonus":                    ItemData(367759011, ItemClassification.progression),
	"Caves Bonus":                     ItemData(367759028, ItemClassification.progression),
	"Desert Bonus":                    ItemData(367759036, ItemClassification.progression),
	"Canyon Bonus":                    ItemData(367759042, ItemClassification.progression),
	"Swamp Bonus":                     ItemData(367759065, ItemClassification.progression),
	"Peak Bonus":                      ItemData(367759070, ItemClassification.progression),
	"Crypts Bonus":                    ItemData(367759079, ItemClassification.progression),
	"Volcano Bonus":                   ItemData(367759086, ItemClassification.progression),
	"Beach Bonus":                     ItemData(367759097, ItemClassification.progression),
	"River Bonus":                     ItemData(367759102, ItemClassification.progression),
	"Hills Bonus":                     ItemData(367759113, ItemClassification.progression),
	"Fort Bonus":                      ItemData(367759138, ItemClassification.progression),
	"Castle Bonus":                    ItemData(367759148, ItemClassification.progression),
	"Lair Bonus":                      ItemData(367759152, ItemClassification.progression)
}

bonusreward_items = {
	"Faramore Bonus Reward":           ItemData(367759241, ItemClassification.filler),
	"Forest Bonus Reward":             ItemData(367759242, ItemClassification.filler),
	"Caves Bonus Reward":              ItemData(367759243, ItemClassification.filler),
	"Desert Bonus Reward":             ItemData(367759244, ItemClassification.filler),
	"Canyon Bonus Reward":             ItemData(367759245, ItemClassification.filler),
	"Swamp Bonus Reward":              ItemData(367759246, ItemClassification.filler),
	"Peak Bonus Reward":               ItemData(367759247, ItemClassification.filler),
	"Crypts Bonus Reward":             ItemData(367759248, ItemClassification.filler),
	"Volcano Bonus Reward":            ItemData(367759249, ItemClassification.filler),
	"Beach Bonus Reward":              ItemData(367759250, ItemClassification.filler),
	"River Bonus Reward":              ItemData(367759251, ItemClassification.filler),
	"Hills Bonus Reward":              ItemData(367759252, ItemClassification.filler),
	"Fort Bonus Reward":               ItemData(367759253, ItemClassification.filler),
	"Castle Bonus Reward":             ItemData(367759254, ItemClassification.filler),
	"Lair Bonus Reward":               ItemData(367759255, ItemClassification.filler)
}

npcspawner_items = {
	"Faramore Covenplate":             ItemData(367759193, ItemClassification.progression),
	"Canyon Crowdee":                  ItemData(367759194, ItemClassification.progression),
	"Peak Ciclena":                    ItemData(367759195, ItemClassification.progression),
	"Beach Fleetus":                   ItemData(367759196, ItemClassification.progression),
	"Forest Cypress":                  ItemData(367759197, ItemClassification.progression),
	"Faramore Yukeen":                 ItemData(367759198, ItemClassification.progression),
	"Faramore Rudy":                   ItemData(367759199, ItemClassification.progression),
	"Desert Fairy":                    ItemData(367759200, ItemClassification.progression),
	"Beach Tork":                      ItemData(367759201, ItemClassification.progression),
	"Faramore Alven":                  ItemData(367759202, ItemClassification.progression),
	"Caves Ellido":                    ItemData(367759203, ItemClassification.progression),
	"Canyon Motte":                    ItemData(367759204, ItemClassification.progression),
	"Faramore Barnabuss":              ItemData(367759205, ItemClassification.progression),
	"Faramore Denny":                  ItemData(367759206, ItemClassification.progression),
	"Faramore Dewey":                  ItemData(367759207, ItemClassification.progression),
	"Crypts Skelvis":                  ItemData(367759208, ItemClassification.progression),
	"Faramore Frich":                  ItemData(367759209, ItemClassification.progression),
	"Lair Zazie":                      ItemData(367759210, ItemClassification.progression),
	"Caves Munhum":                    ItemData(367759211, ItemClassification.progression),
	"Faramore Brinda":                 ItemData(367759212, ItemClassification.progression),
	"Swamp Glubbert":                  ItemData(367759213, ItemClassification.progression),
	"Hills Milbert":                   ItemData(367759214, ItemClassification.progression),
	"Faramore Cypress":                ItemData(367759215, ItemClassification.progression),
	"Canyon Odie":                     ItemData(367759216, ItemClassification.progression),
	"Faramore Kari Quest":             ItemData(367759217, ItemClassification.progression),
	"River Morgh":                     ItemData(367759218, ItemClassification.progression),
	"River Francine":                  ItemData(367759219, ItemClassification.progression),
	"Faramore Munhum":                 ItemData(367759220, ItemClassification.progression)
}

npc_items = {
	"Faramore Boru":                   ItemData(367759221, ItemClassification.filler),
	"Faramore Kari":                   ItemData(367759222, ItemClassification.filler),
	"Faramore Univor":                 ItemData(367759223, ItemClassification.filler),
	"Faramore Salvik":                 ItemData(367759224, ItemClassification.filler),
	"Faramore Maki":                   ItemData(367759225, ItemClassification.filler),
	"Faramore Payop":                  ItemData(367759226, ItemClassification.filler),
	"Volcano Joe":                     ItemData(367759227, ItemClassification.filler),
	"River Barnabuss":                 ItemData(367759228, ItemClassification.filler),
	"Faramore Mortar":                 ItemData(367759229, ItemClassification.progression),
	"Swamp Frich":                     ItemData(367759230, ItemClassification.progression),
	"Forest Rudy (Start)":             ItemData(367759231, ItemClassification.progression),
	"Forest Rudy (End)":               ItemData(367759232, ItemClassification.progression),
	"Peak Rudy (Start)":               ItemData(367759233, ItemClassification.progression),
	"Peak Rudy (End)":                 ItemData(367759234, ItemClassification.progression),
	"Hills Rudy (Start)":              ItemData(367759235, ItemClassification.progression),
	"Hills Rudy (End)":                ItemData(367759236, ItemClassification.progression)
}

beacon_items = {
	"Forest Beacon":                   ItemData(367759019, ItemClassification.progression | ItemClassification.useful),
	"Desert Beacon":                   ItemData(367759041, ItemClassification.progression | ItemClassification.useful),
	"Swamp Beacon":                    ItemData(367759066, ItemClassification.progression | ItemClassification.useful),
	"Beach Beacon":                    ItemData(367759100, ItemClassification.progression | ItemClassification.useful),
	"Hills Beacon":                    ItemData(367759119, ItemClassification.progression | ItemClassification.useful)
}

levelunlock_items = {
	"Default 1":                       ItemData(367759256, ItemClassification.progression | ItemClassification.useful),
	"Default 2":                       ItemData(367759257, ItemClassification.progression | ItemClassification.useful),
	"Forest Beacon 1":                 ItemData(367759258, ItemClassification.progression | ItemClassification.useful),
	"Forest Beacon 2":                 ItemData(367759259, ItemClassification.progression | ItemClassification.useful),
	"Forest Beacon 3":                 ItemData(367759260, ItemClassification.progression | ItemClassification.useful),
	"Desert Beacon 1":                 ItemData(367759261, ItemClassification.progression | ItemClassification.useful),
	"Desert Beacon 2":                 ItemData(367759262, ItemClassification.progression | ItemClassification.useful),
	"Desert Beacon 3":                 ItemData(367759263, ItemClassification.progression | ItemClassification.useful),
	"Swamp Beacon 1":                  ItemData(367759264, ItemClassification.progression | ItemClassification.useful),
	"Swamp Beacon 2":                  ItemData(367759265, ItemClassification.progression | ItemClassification.useful),
	"Swamp Beacon 3":                  ItemData(367759266, ItemClassification.progression | ItemClassification.useful),
	"Beach Beacon 1":                  ItemData(367759267, ItemClassification.progression | ItemClassification.useful),
	"Beach Beacon 2":                  ItemData(367759268, ItemClassification.progression | ItemClassification.useful),
	"Hills Beacon 1":                  ItemData(367759269, ItemClassification.progression | ItemClassification.useful),
	"Hills Beacon 2":                  ItemData(367759270, ItemClassification.progression | ItemClassification.useful)
}

other_items = {
	"Daimur":                          ItemData(367759159, ItemClassification.progression | ItemClassification.useful)
}

all_item_table: Dict[str, ItemData] = {
	**bag_items,
	**key_items,
	**candle_items,
	**coin_items,
	**plant_items,
	**upgrade_items,
	**lifeup_items,
	**race_items,
	**trading_items,
	**jewel_items,
	**quest_items,
	**rock_items,
	**scroll_items,
	**bonusreward_items,
	**npcspawner_items,
	**npc_items,
	**beacon_items,
	**levelunlock_items,
	**other_items
}

all_group_table: Dict[str, Dict[str, ItemData]] = {
	"bag": bag_items,
	"key": key_items,
	"candle": candle_items,
	"coin": coin_items,
	"plant": plant_items,
	"upgrade": upgrade_items,
	"lifeup": lifeup_items,
	"race": race_items,
	"trading": trading_items,
	"jewel": jewel_items,
	"quest": quest_items,
	"rock": rock_items,
	"scroll": scroll_items,
	"bonusreward": bonusreward_items,
	"npcspawner": npcspawner_items,
	"npc": npc_items,
	"beacon": beacon_items,
	"levelunlock": levelunlock_items,
	"other": other_items
}