from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ItemData(NamedTuple):
    arzid: int | None
    type: ItemClassification

bag_items = {
	"Forest Bag (First Room 1)":       ItemData(2793883008, ItemClassification.filler),
	"Forest Bag (First Room 2)":       ItemData(2793883009, ItemClassification.filler),
	"Forest Bag (Sword Wave)":         ItemData(2793883015, ItemClassification.filler),
	"Forest Bag (Last Room)":          ItemData(2793883018, ItemClassification.filler),
	"Caves Bag (Rope Ladder)":         ItemData(2793883024, ItemClassification.filler),
	"Caves Bag (Last Room)":           ItemData(2793883029, ItemClassification.filler),
	"Desert Bag (First Room 1)":       ItemData(2793883032, ItemClassification.filler),
	"Desert Bag (First Room 2)":       ItemData(2793883033, ItemClassification.filler),
	"Desert Bag (Last Room)":          ItemData(2793883040, ItemClassification.filler),
	"Canyon Bag (Before Checkpoint)":  ItemData(2793883043, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 1)": ItemData(2793883044, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 2)": ItemData(2793883045, ItemClassification.filler),
	"Canyon Bag (After Checkpoint 3)": ItemData(2793883046, ItemClassification.filler),
	"Canyon Bag (First Room End)":     ItemData(2793883047, ItemClassification.filler),
	"Canyon Bag (After Zipline 1)":    ItemData(2793883051, ItemClassification.filler),
	"Canyon Bag (After Zipline 2)":    ItemData(2793883052, ItemClassification.filler),
	"Canyon Bag (After Zipline 3)":    ItemData(2793883053, ItemClassification.filler),
	"Canyon Bag (Motte House)":        ItemData(2793883055, ItemClassification.filler),
	"Swamp Bag (First Room)":          ItemData(2793883058, ItemClassification.filler),
	"Peak Bag (First Cave 1)":         ItemData(2793883068, ItemClassification.filler),
	"Peak Bag (First Cave 2)":         ItemData(2793883069, ItemClassification.filler),
	"Peak Bag (Before Apatu)":         ItemData(2793883074, ItemClassification.filler),
	"Peak Bag (After Apatu)":          ItemData(2793883076, ItemClassification.filler),
	"Crypts Bag (Crypt)":              ItemData(2793883081, ItemClassification.filler),
	"Crypts Bag (Skelvis)":            ItemData(2793883085, ItemClassification.filler),
	"Beach Bag (First Room)":          ItemData(2793883091, ItemClassification.filler),
	"River Bag (Last Room)":           ItemData(2793883107, ItemClassification.filler),
	"Hills Bag (Barn)":                ItemData(2793883114, ItemClassification.filler),
	"Hills Bag (Music Shrine)":        ItemData(2793883116, ItemClassification.filler),
	"Fort Bag (Dungeon 1)":            ItemData(2793883120, ItemClassification.filler),
	"Fort Bag (Dungeon 2)":            ItemData(2793883121, ItemClassification.filler),
	"Fort Bag (Dungeon 3)":            ItemData(2793883122, ItemClassification.filler),
	"Fort Bag (Dungeon 4)":            ItemData(2793883123, ItemClassification.filler),
	"Fort Bag (Dark Room)":            ItemData(2793883127, ItemClassification.filler),
	"Fort Bag (Top Room 1)":           ItemData(2793883131, ItemClassification.filler),
	"Fort Bag (Top Room 2)":           ItemData(2793883132, ItemClassification.filler),
	"Fort Bag (Top Room 3)":           ItemData(2793883133, ItemClassification.filler),
	"Fort Bag (Last Room)":            ItemData(2793883135, ItemClassification.filler),
	"Castle Bag (Entrance)":           ItemData(2793883139, ItemClassification.filler),
	"Castle Bag (Top Room)":           ItemData(2793883143, ItemClassification.filler),
	"Castle Bag (Bonus)":              ItemData(2793883147, ItemClassification.filler),
	"Lair Bag (First Room)":           ItemData(2793883153, ItemClassification.filler),
	"Lair Bag (Lava Room)":            ItemData(2793883155, ItemClassification.filler),
	"Lair Bag (Final Room 1)":         ItemData(2793883156, ItemClassification.filler),
	"Lair Bag (Final Room 2)":         ItemData(2793883157, ItemClassification.filler),
	"Lair Bag (Final Room 3)":         ItemData(2793883158, ItemClassification.filler)
}

key_items = {
	"Faramore Key (Well)":             ItemData(2793883001, ItemClassification.progression),
	"Faramore Key (Tavern)":           ItemData(2793883002, ItemClassification.progression),
	"Forest Key":                      ItemData(2793883010, ItemClassification.progression),
	"Desert Key":                      ItemData(2793883037, ItemClassification.progression),
	"Canyon Key":                      ItemData(2793883050, ItemClassification.progression),
	"Swamp Key (Frich House)":         ItemData(2793883060, ItemClassification.progression),
	"Swamp Key (Griffin Boots)":       ItemData(2793883062, ItemClassification.progression),
	"Peak Key":                        ItemData(2793883072, ItemClassification.progression),
	"Crypts Key":                      ItemData(2793883080, ItemClassification.progression),
	"Beach Key (First House)":         ItemData(2793883092, ItemClassification.progression),
	"Beach Key (Tork Cabin)":          ItemData(2793883094, ItemClassification.progression),
	"River Key (Francine)":            ItemData(2793883101, ItemClassification.progression),
	"River Key (Submarine)":           ItemData(2793883104, ItemClassification.progression),
	"Hills Key":                       ItemData(2793883115, ItemClassification.progression),
	"Fort Key (First Room)":           ItemData(2793883125, ItemClassification.progression),
	"Fort Key (Top Room)":             ItemData(2793883130, ItemClassification.progression),
	"Castle Key (Nodelki)":            ItemData(2793883141, ItemClassification.progression),
	"Castle Key (Left Room)":          ItemData(2793883146, ItemClassification.progression)
}

candle_items = {
	"Faramore Candle (Empty House)":   ItemData(2793883004, ItemClassification.progression),
	"Faramore Candle (Cypress House)": ItemData(2793883005, ItemClassification.progression),
	"Forest Candle (Tree)":            ItemData(2793883012, ItemClassification.progression),
	"Forest Candle (Cypress)":         ItemData(2793883013, ItemClassification.progression),
	"Caves Candle (First Dark Room)":  ItemData(2793883025, ItemClassification.progression),
	"Caves Candle (Second Dark Room)": ItemData(2793883027, ItemClassification.progression),
	"Desert Candle (Pit)":             ItemData(2793883035, ItemClassification.progression),
	"Desert Candle (Last Room)":       ItemData(2793883038, ItemClassification.progression),
	"Canyon Candle (First Room End)":  ItemData(2793883048, ItemClassification.progression),
	"Canyon Candle (Motte House)":     ItemData(2793883056, ItemClassification.progression),
	"Swamp Candle (First Room)":       ItemData(2793883057, ItemClassification.progression),
	"Swamp Candle (Frich House)":      ItemData(2793883061, ItemClassification.progression),
	"Peak Candle (First Cave)":        ItemData(2793883067, ItemClassification.progression),
	"Peak Candle (Ciclena Cave)":      ItemData(2793883073, ItemClassification.progression),
	"Crypts Candle (After Crypt)":     ItemData(2793883082, ItemClassification.progression),
	"Crypts Candle (Skelvis)":         ItemData(2793883084, ItemClassification.progression),
	"Volcano Candle (First Room)":     ItemData(2793883087, ItemClassification.progression),
	"Volcano Candle (Last Room)":      ItemData(2793883089, ItemClassification.progression),
	"Beach Candle (Tork Cabin)":       ItemData(2793883095, ItemClassification.progression),
	"Beach Candle (Cave)":             ItemData(2793883098, ItemClassification.progression),
	"River Candle (Boat)":             ItemData(2793883103, ItemClassification.progression),
	"River Candle (Last Room)":        ItemData(2793883108, ItemClassification.progression),
	"Hills Candle (Cave)":             ItemData(2793883110, ItemClassification.progression),
	"Hills Candle (Music Shrine)":     ItemData(2793883117, ItemClassification.progression),
	"Fort Candle (Dark Room)":         ItemData(2793883126, ItemClassification.progression),
	"Fort Candle (Last Room)":         ItemData(2793883134, ItemClassification.progression),
	"Castle Candle (Right Room)":      ItemData(2793883140, ItemClassification.progression),
	"Castle Candle (Top Room)":        ItemData(2793883142, ItemClassification.progression),
	"Lair Candle (Tree Trunk)":        ItemData(2793883150, ItemClassification.progression),
	"Lair Candle (Tree Top)":          ItemData(2793883151, ItemClassification.progression)
}

coin_items = {
	"Faramore Coin":                   ItemData(2793883006, ItemClassification.progression),
	"Forest Coin":                     ItemData(2793883014, ItemClassification.progression),
	"Caves Coin":                      ItemData(2793883026, ItemClassification.progression),
	"Desert Coin":                     ItemData(2793883031, ItemClassification.progression),
	"Canyon Coin":                     ItemData(2793883054, ItemClassification.progression),
	"Swamp Coin":                      ItemData(2793883059, ItemClassification.progression),
	"Peak Coin":                       ItemData(2793883071, ItemClassification.progression),
	"Crypts Coin":                     ItemData(2793883083, ItemClassification.progression),
	"Volcano Coin":                    ItemData(2793883088, ItemClassification.progression),
	"Beach Coin":                      ItemData(2793883093, ItemClassification.progression),
	"River Coin":                      ItemData(2793883105, ItemClassification.progression),
	"Hills Coin":                      ItemData(2793883112, ItemClassification.progression),
	"Fort Coin":                       ItemData(2793883129, ItemClassification.progression),
	"Castle Coin":                     ItemData(2793883145, ItemClassification.progression),
	"Lair Coin":                       ItemData(2793883154, ItemClassification.progression)
}

plant_items = {
	"Swamp Plant":                     ItemData(2793883064, ItemClassification.progression),
	"Beach Plant":                     ItemData(2793883096, ItemClassification.progression),
	"Hills Plant":                     ItemData(2793883118, ItemClassification.progression)
}

upgrade_items = {
	"Power Stone Upgrade":             ItemData(2793883162, ItemClassification.useful),
	"Wallet Upgrade":                  ItemData(2793883166, ItemClassification.useful),
	"Infinite Soulfire":               ItemData(2793883167, ItemClassification.useful),
	"Bomb Upgrade":                    ItemData(2793883168, ItemClassification.useful),
	"Lamp Oil Upgrade":                ItemData(2793883171, ItemClassification.useful),
	"Rope Upgrade":                    ItemData(2793883172, ItemClassification.useful),
	"Soul Upgrade":                    ItemData(2793883192, ItemClassification.useful)
}

lifeup_items = {
	"Desert Life-Up":                  ItemData(2793883039, ItemClassification.useful),
	"Crypts Life-Up":                  ItemData(2793883077, ItemClassification.useful),
	"River Life-Up":                   ItemData(2793883109, ItemClassification.useful)
}

race_items = {
	"Forest Race 100 Rupees":          ItemData(2793883173, ItemClassification.filler),
	"Peak Race 100 Rupees":            ItemData(2793883174, ItemClassification.filler),
	"Hills Race 100 Rupees":           ItemData(2793883175, ItemClassification.filler)
}

trading_items = {
	"Sacred Oil":                      ItemData(2793883124, ItemClassification.progression),
	"Dungeon Key":                     ItemData(2793883163, ItemClassification.progression),
	"Chainsword":                      ItemData(2793883164, ItemClassification.progression),
	"Snail Salt":                      ItemData(2793883178, ItemClassification.progression),
	"Ogre Hair":                       ItemData(2793883183, ItemClassification.progression),
	"Cleaver Shovel":                  ItemData(2793883188, ItemClassification.progression),
	"Oil and Chains":                  ItemData(2793883189, ItemClassification.progression),
	"Funky Fungus":                    ItemData(2793883191, ItemClassification.progression)
}

jewel_items = {
	"Forest Jewel":                    ItemData(2793883020, ItemClassification.progression),
	"Canyon Jewel":                    ItemData(2793883049, ItemClassification.progression),
	"Peak Jewel":                      ItemData(2793883075, ItemClassification.progression),
	"Fort Jewel":                      ItemData(2793883137, ItemClassification.progression),
	"Castle Jewel":                    ItemData(2793883149, ItemClassification.progression)
}

quest_items = {
	"Bombs":                           ItemData(2793883007, ItemClassification.progression),
	"Sword Wave":                      ItemData(2793883016, ItemClassification.progression),
	"Golden Fly":                      ItemData(2793883017, ItemClassification.progression),
	"Magic Armor":                     ItemData(2793883021, ItemClassification.progression),
	"Silver Cricket":                  ItemData(2793883022, ItemClassification.progression),
	"Rope Ladder":                     ItemData(2793883023, ItemClassification.progression),
	"Shield Ring":                     ItemData(2793883030, ItemClassification.progression),
	"Compass":                         ItemData(2793883034, ItemClassification.progression),
	"Griffin Boots":                   ItemData(2793883063, ItemClassification.progression),
	"Bell":                            ItemData(2793883078, ItemClassification.progression),
	"Crystal of Refraction":           ItemData(2793883090, ItemClassification.progression),
	"Fatal Flute":                     ItemData(2793883099, ItemClassification.progression),
	"Blue Magic":                      ItemData(2793883106, ItemClassification.progression),
	"Lightning Sword":                 ItemData(2793883111, ItemClassification.progression),
	"Enchanted Shoes":                 ItemData(2793883128, ItemClassification.progression),
	"Reflector Ring":                  ItemData(2793883136, ItemClassification.progression),
	"Winged Belt":                     ItemData(2793883144, ItemClassification.progression),
	"Purple Magic":                    ItemData(2793883160, ItemClassification.progression),
	"Citizenship Papers":              ItemData(2793883161, ItemClassification.progression),
	"Canteen":                         ItemData(2793883165, ItemClassification.progression),
	"Calendar":                        ItemData(2793883169, ItemClassification.progression),
	"200 Rupees":                      ItemData(2793883170, ItemClassification.filler),
	"Lantern":                         ItemData(2793883176, ItemClassification.progression),
	"Rope":                            ItemData(2793883177, ItemClassification.useful),
	"Fairy Dust":                      ItemData(2793883179, ItemClassification.progression),
	"Backstep":                        ItemData(2793883180, ItemClassification.useful),
	"Smart Gun":                       ItemData(2793883181, ItemClassification.progression),
	"Star Earrings":                   ItemData(2793883182, ItemClassification.progression),
	"Power Pendant":                   ItemData(2793883184, ItemClassification.progression),
	"Bomb Gauntlet":                   ItemData(2793883185, ItemClassification.progression),
	"Speedy Shoes":                    ItemData(2793883186, ItemClassification.progression),
	"Magic Cloak":                     ItemData(2793883187, ItemClassification.progression),
	"Double Wave":                     ItemData(2793883190, ItemClassification.progression)
}

rock_items = {
	"Orange Rock":                     ItemData(2793883237, ItemClassification.progression),
	"Brown Rock":                      ItemData(2793883238, ItemClassification.progression),
	"Gray Rock":                       ItemData(2793883239, ItemClassification.progression),
	"Blue Rock":                       ItemData(2793883240, ItemClassification.progression)
}

scroll_items = {
	"Faramore Bonus":                  ItemData(2793883003, ItemClassification.progression),
	"Forest Bonus":                    ItemData(2793883011, ItemClassification.progression),
	"Caves Bonus":                     ItemData(2793883028, ItemClassification.progression),
	"Desert Bonus":                    ItemData(2793883036, ItemClassification.progression),
	"Canyon Bonus":                    ItemData(2793883042, ItemClassification.progression),
	"Swamp Bonus":                     ItemData(2793883065, ItemClassification.progression),
	"Peak Bonus":                      ItemData(2793883070, ItemClassification.progression),
	"Crypts Bonus":                    ItemData(2793883079, ItemClassification.progression),
	"Volcano Bonus":                   ItemData(2793883086, ItemClassification.progression),
	"Beach Bonus":                     ItemData(2793883097, ItemClassification.progression),
	"River Bonus":                     ItemData(2793883102, ItemClassification.progression),
	"Hills Bonus":                     ItemData(2793883113, ItemClassification.progression),
	"Fort Bonus":                      ItemData(2793883138, ItemClassification.progression),
	"Castle Bonus":                    ItemData(2793883148, ItemClassification.progression),
	"Lair Bonus":                      ItemData(2793883152, ItemClassification.progression)
}

bonusreward_items = {
	"Faramore Bonus Reward":           ItemData(2793883241, ItemClassification.filler),
	"Forest Bonus Reward":             ItemData(2793883242, ItemClassification.filler),
	"Caves Bonus Reward":              ItemData(2793883243, ItemClassification.filler),
	"Desert Bonus Reward":             ItemData(2793883244, ItemClassification.filler),
	"Canyon Bonus Reward":             ItemData(2793883245, ItemClassification.filler),
	"Swamp Bonus Reward":              ItemData(2793883246, ItemClassification.filler),
	"Peak Bonus Reward":               ItemData(2793883247, ItemClassification.filler),
	"Crypts Bonus Reward":             ItemData(2793883248, ItemClassification.filler),
	"Volcano Bonus Reward":            ItemData(2793883249, ItemClassification.filler),
	"Beach Bonus Reward":              ItemData(2793883250, ItemClassification.filler),
	"River Bonus Reward":              ItemData(2793883251, ItemClassification.filler),
	"Hills Bonus Reward":              ItemData(2793883252, ItemClassification.filler),
	"Fort Bonus Reward":               ItemData(2793883253, ItemClassification.filler),
	"Castle Bonus Reward":             ItemData(2793883254, ItemClassification.filler),
	"Lair Bonus Reward":               ItemData(2793883255, ItemClassification.filler)
}

npcspawner_items = {
	"Faramore Kari Quest":             ItemData(2793883193, ItemClassification.progression),
	"Caves Ellido":                    ItemData(2793883194, ItemClassification.progression),
	"Canyon Crowdee":                  ItemData(2793883195, ItemClassification.progression),
	"Swamp Glubbert":                  ItemData(2793883196, ItemClassification.progression),
	"Faramore Barnabuss":              ItemData(2793883197, ItemClassification.progression),
	"Faramore Dewey":                  ItemData(2793883198, ItemClassification.progression),
	"Hills Milbert":                   ItemData(2793883199, ItemClassification.progression),
	"Canyon Odie":                     ItemData(2793883200, ItemClassification.progression),
	"Crypts Skelvis":                  ItemData(2793883201, ItemClassification.progression),
	"Beach Tork":                      ItemData(2793883202, ItemClassification.progression),
	"Peak Ciclena":                    ItemData(2793883203, ItemClassification.progression),
	"Forest Cypress":                  ItemData(2793883204, ItemClassification.progression),
	"River Morgh":                     ItemData(2793883205, ItemClassification.progression),
	"Desert Fairy":                    ItemData(2793883206, ItemClassification.progression),
	"Faramore Covenplate":             ItemData(2793883207, ItemClassification.progression),
	"Faramore Rudy":                   ItemData(2793883208, ItemClassification.progression),
	"Faramore Munhum":                 ItemData(2793883209, ItemClassification.progression),
	"Canyon Motte":                    ItemData(2793883210, ItemClassification.progression),
	"Faramore Cypress":                ItemData(2793883211, ItemClassification.progression),
	"River Francine":                  ItemData(2793883212, ItemClassification.progression),
	"Faramore Alven":                  ItemData(2793883213, ItemClassification.progression),
	"Faramore Frich":                  ItemData(2793883214, ItemClassification.progression),
	"Faramore Yukeen":                 ItemData(2793883215, ItemClassification.progression),
	"Lair Zazie":                      ItemData(2793883216, ItemClassification.progression),
	"Beach Fleetus":                   ItemData(2793883217, ItemClassification.progression),
	"Faramore Brinda":                 ItemData(2793883218, ItemClassification.progression),
	"Caves Munhum":                    ItemData(2793883219, ItemClassification.progression),
	"Faramore Denny":                  ItemData(2793883220, ItemClassification.progression)
}

npc_items = {
	"Faramore Boru":                   ItemData(2793883221, ItemClassification.filler),
	"Faramore Kari":                   ItemData(2793883222, ItemClassification.filler),
	"Faramore Univor":                 ItemData(2793883223, ItemClassification.filler),
	"Faramore Salvik":                 ItemData(2793883224, ItemClassification.filler),
	"Faramore Maki":                   ItemData(2793883225, ItemClassification.filler),
	"Faramore Payop":                  ItemData(2793883226, ItemClassification.filler),
	"Volcano Joe":                     ItemData(2793883227, ItemClassification.filler),
	"River Barnabuss":                 ItemData(2793883228, ItemClassification.filler),
	"Faramore Mortar":                 ItemData(2793883229, ItemClassification.progression),
	"Swamp Frich":                     ItemData(2793883230, ItemClassification.progression),
	"Forest Rudy (Start)":             ItemData(2793883231, ItemClassification.progression),
	"Forest Rudy (End)":               ItemData(2793883232, ItemClassification.progression),
	"Peak Rudy (Start)":               ItemData(2793883233, ItemClassification.progression),
	"Peak Rudy (End)":                 ItemData(2793883234, ItemClassification.progression),
	"Hills Rudy (Start)":              ItemData(2793883235, ItemClassification.progression),
	"Hills Rudy (End)":                ItemData(2793883236, ItemClassification.progression)
}

beacon_items = {
	"Forest Beacon":                   ItemData(2793883019, ItemClassification.progression),
	"Desert Beacon":                   ItemData(2793883041, ItemClassification.progression),
	"Swamp Beacon":                    ItemData(2793883066, ItemClassification.progression),
	"Beach Beacon":                    ItemData(2793883100, ItemClassification.progression),
	"Hills Beacon":                    ItemData(2793883119, ItemClassification.progression)
}

levelunlock_items = {
	"Default 1":                       ItemData(2793883256, ItemClassification.progression),
	"Default 2":                       ItemData(2793883257, ItemClassification.progression),
	"Forest Beacon 1":                 ItemData(2793883258, ItemClassification.progression),
	"Forest Beacon 2":                 ItemData(2793883259, ItemClassification.progression),
	"Forest Beacon 3":                 ItemData(2793883260, ItemClassification.progression),
	"Desert Beacon 1":                 ItemData(2793883261, ItemClassification.progression),
	"Desert Beacon 2":                 ItemData(2793883262, ItemClassification.progression),
	"Desert Beacon 3":                 ItemData(2793883263, ItemClassification.progression),
	"Swamp Beacon 1":                  ItemData(2793883264, ItemClassification.progression),
	"Swamp Beacon 2":                  ItemData(2793883265, ItemClassification.progression),
	"Swamp Beacon 3":                  ItemData(2793883266, ItemClassification.progression),
	"Beach Beacon 1":                  ItemData(2793883267, ItemClassification.progression),
	"Beach Beacon 2":                  ItemData(2793883268, ItemClassification.progression),
	"Hills Beacon 1":                  ItemData(2793883269, ItemClassification.progression),
	"Hills Beacon 2":                  ItemData(2793883270, ItemClassification.progression)
}

other_items = {
	"Daimur":                          ItemData(2793883159, ItemClassification.progression)
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