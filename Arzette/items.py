from BaseClasses import Item, ItemClassification
from typing import Dict, NamedTuple
from .Names import itemName

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ItemData(NamedTuple):
    arzid: int | None
    type: ItemClassification

# It is CRUCIAL that the IDs of the items match their vanilla location IDs
bag_items = {
	itemName.ForestBagFirstRoom1:        ItemData(367759008, ItemClassification.filler),
	itemName.ForestBagFirstRoom2:        ItemData(367759009, ItemClassification.filler),
	itemName.ForestBagSwordWave:         ItemData(367759015, ItemClassification.filler),
	itemName.ForestBagLastRoom:          ItemData(367759018, ItemClassification.filler),
	itemName.CavesBagRopeLadder:         ItemData(367759024, ItemClassification.filler),
	itemName.CavesBagLastRoom:           ItemData(367759029, ItemClassification.filler),
	itemName.DesertBagFirstRoom1:        ItemData(367759032, ItemClassification.filler),
	itemName.DesertBagFirstRoom2:        ItemData(367759033, ItemClassification.filler),
	itemName.DesertBagLastRoom:          ItemData(367759040, ItemClassification.filler),
	itemName.CanyonBagBeforeCheckpoint:  ItemData(367759043, ItemClassification.filler),
	itemName.CanyonBagAfterCheckpoint1:  ItemData(367759044, ItemClassification.filler),
	itemName.CanyonBagAfterCheckpoint2:  ItemData(367759045, ItemClassification.filler),
	itemName.CanyonBagAfterCheckpoint3:  ItemData(367759046, ItemClassification.filler),
	itemName.CanyonBagFirstRoomEnd:      ItemData(367759047, ItemClassification.filler),
	itemName.CanyonBagAfterZipline1:     ItemData(367759051, ItemClassification.filler),
	itemName.CanyonBagAfterZipline2:     ItemData(367759052, ItemClassification.filler),
	itemName.CanyonBagAfterZipline3:     ItemData(367759053, ItemClassification.filler),
	itemName.CanyonBagMotteHouse:        ItemData(367759055, ItemClassification.filler),
	itemName.SwampBagFirstRoom:          ItemData(367759058, ItemClassification.filler),
	itemName.PeakBagFirstCave1:          ItemData(367759068, ItemClassification.filler),
	itemName.PeakBagFirstCave2:          ItemData(367759069, ItemClassification.filler),
	itemName.PeakBagBeforeApatu:         ItemData(367759074, ItemClassification.filler),
	itemName.PeakBagAfterApatu:          ItemData(367759076, ItemClassification.filler),
	itemName.CryptsBagCrypt:             ItemData(367759081, ItemClassification.filler),
	itemName.CryptsBagSkelvis:           ItemData(367759085, ItemClassification.filler),
	itemName.BeachBagFirstRoom:          ItemData(367759091, ItemClassification.filler),
	itemName.RiverBagLastRoom:           ItemData(367759107, ItemClassification.filler),
	itemName.HillsBagBarn:               ItemData(367759114, ItemClassification.filler),
	itemName.HillsBagMusicShrine:        ItemData(367759116, ItemClassification.filler),
	itemName.FortBagDungeon1:            ItemData(367759120, ItemClassification.filler),
	itemName.FortBagDungeon2:            ItemData(367759121, ItemClassification.filler),
	itemName.FortBagDungeon3:            ItemData(367759122, ItemClassification.filler),
	itemName.FortBagDungeon4:            ItemData(367759123, ItemClassification.filler),
	itemName.FortBagDarkRoom:            ItemData(367759127, ItemClassification.filler),
	itemName.FortBagTopRoom1:            ItemData(367759131, ItemClassification.filler),
	itemName.FortBagTopRoom2:            ItemData(367759132, ItemClassification.filler),
	itemName.FortBagTopRoom3:            ItemData(367759133, ItemClassification.filler),
	itemName.FortBagLastRoom:            ItemData(367759135, ItemClassification.filler),
	itemName.CastleBagEntrance:          ItemData(367759139, ItemClassification.filler),
	itemName.CastleBagTopRoom:           ItemData(367759143, ItemClassification.filler),
	itemName.CastleBagBonus:             ItemData(367759147, ItemClassification.filler),
	itemName.LairBagFirstRoom:           ItemData(367759153, ItemClassification.filler),
	itemName.LairBagLavaRoom:            ItemData(367759155, ItemClassification.filler),
	itemName.LairBagFinalRoom1:          ItemData(367759156, ItemClassification.filler),
	itemName.LairBagFinalRoom2:          ItemData(367759157, ItemClassification.filler),
	itemName.LairBagFinalRoom3:          ItemData(367759158, ItemClassification.filler)
}

key_items = {
	itemName.FaramoreKeyWell:            ItemData(367759001, ItemClassification.progression),
	itemName.FaramoreKeyTavern:          ItemData(367759002, ItemClassification.progression),
	itemName.ForestKey:                  ItemData(367759010, ItemClassification.progression),
	itemName.DesertKey:                  ItemData(367759037, ItemClassification.progression),
	itemName.CanyonKey:                  ItemData(367759050, ItemClassification.progression),
	itemName.SwampKeyFrichHouse:         ItemData(367759060, ItemClassification.progression),
	itemName.SwampKeyGriffinBoots:       ItemData(367759062, ItemClassification.progression),
	itemName.PeakKey:                    ItemData(367759072, ItemClassification.progression),
	itemName.CryptsKey:                  ItemData(367759080, ItemClassification.progression),
	itemName.BeachKeyFirstHouse:         ItemData(367759092, ItemClassification.progression),
	itemName.BeachKeyTorkCabin:          ItemData(367759094, ItemClassification.progression),
	itemName.RiverKeyFrancine:           ItemData(367759101, ItemClassification.progression),
	itemName.RiverKeySubmarine:          ItemData(367759104, ItemClassification.progression),
	itemName.HillsKey:                   ItemData(367759115, ItemClassification.progression),
	itemName.FortKeyFirstRoom:           ItemData(367759125, ItemClassification.progression),
	itemName.FortKeyTopRoom:             ItemData(367759130, ItemClassification.progression),
	itemName.CastleKeyNodelki:           ItemData(367759141, ItemClassification.progression),
	itemName.CastleKeyLeftRoom:          ItemData(367759146, ItemClassification.progression)
}

candle_items = {
	itemName.FaramoreCandleEmptyHouse:   ItemData(367759004, ItemClassification.progression),
	itemName.FaramoreCandleCypressHouse: ItemData(367759005, ItemClassification.progression),
	itemName.ForestCandleTree:           ItemData(367759012, ItemClassification.progression),
	itemName.ForestCandleCypress:        ItemData(367759013, ItemClassification.progression),
	itemName.CavesCandleFirstDarkRoom:   ItemData(367759025, ItemClassification.progression),
	itemName.CavesCandleSecondDarkRoom:  ItemData(367759027, ItemClassification.progression),
	itemName.DesertCandlePit:            ItemData(367759035, ItemClassification.progression),
	itemName.DesertCandleLastRoom:       ItemData(367759038, ItemClassification.progression),
	itemName.CanyonCandleFirstRoomEnd:   ItemData(367759048, ItemClassification.progression),
	itemName.CanyonCandleMotteHouse:     ItemData(367759056, ItemClassification.progression),
	itemName.SwampCandleFirstRoom:       ItemData(367759057, ItemClassification.progression),
	itemName.SwampCandleFrichHouse:      ItemData(367759061, ItemClassification.progression),
	itemName.PeakCandleFirstCave:        ItemData(367759067, ItemClassification.progression),
	itemName.PeakCandleCiclenaCave:      ItemData(367759073, ItemClassification.progression),
	itemName.CryptsCandleAfterCrypt:     ItemData(367759082, ItemClassification.progression),
	itemName.CryptsCandleSkelvis:        ItemData(367759084, ItemClassification.progression),
	itemName.VolcanoCandleFirstRoom:     ItemData(367759087, ItemClassification.progression),
	itemName.VolcanoCandleLastRoom:      ItemData(367759089, ItemClassification.progression),
	itemName.BeachCandleTorkCabin:       ItemData(367759095, ItemClassification.progression),
	itemName.BeachCandleCave:            ItemData(367759098, ItemClassification.progression),
	itemName.RiverCandleBoat:            ItemData(367759103, ItemClassification.progression),
	itemName.RiverCandleLastRoom:        ItemData(367759108, ItemClassification.progression),
	itemName.HillsCandleCave:            ItemData(367759110, ItemClassification.progression),
	itemName.HillsCandleMusicShrine:     ItemData(367759117, ItemClassification.progression),
	itemName.FortCandleDarkRoom:         ItemData(367759126, ItemClassification.progression),
	itemName.FortCandleLastRoom:         ItemData(367759134, ItemClassification.progression),
	itemName.CastleCandleRightRoom:      ItemData(367759140, ItemClassification.progression),
	itemName.CastleCandleTopRoom:        ItemData(367759142, ItemClassification.progression),
	itemName.LairCandleTreeTrunk:        ItemData(367759150, ItemClassification.progression),
	itemName.LairCandleTreeTop:          ItemData(367759151, ItemClassification.progression)
}

coin_items = {
	itemName.FaramoreCoin:               ItemData(367759006, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.ForestCoin:                 ItemData(367759014, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.CavesCoin:                  ItemData(367759026, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.DesertCoin:                 ItemData(367759031, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.CanyonCoin:                 ItemData(367759054, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.SwampCoin:                  ItemData(367759059, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.PeakCoin:                   ItemData(367759071, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.CryptsCoin:                 ItemData(367759083, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.VolcanoCoin:                ItemData(367759088, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.BeachCoin:                  ItemData(367759093, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.RiverCoin:                  ItemData(367759105, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.HillsCoin:                  ItemData(367759112, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.FortCoin:                   ItemData(367759129, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.CastleCoin:                 ItemData(367759145, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.LairCoin:                   ItemData(367759154, ItemClassification.progression_deprioritized_skip_balancing)
}

plant_items = {
	itemName.SwampPlant:                 ItemData(367759064, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.BeachPlant:                 ItemData(367759096, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.HillsPlant:                 ItemData(367759118, ItemClassification.progression_deprioritized_skip_balancing)
}

upgrade_items = {
	itemName.PowerStoneUpgrade:          ItemData(367759162, ItemClassification.useful),
	itemName.WalletUpgrade:              ItemData(367759166, ItemClassification.useful),
	itemName.InfiniteSoulfire:           ItemData(367759167, ItemClassification.progression_deprioritized_skip_balancing),
	itemName.BombUpgrade:                ItemData(367759168, ItemClassification.useful),
	itemName.LampOilUpgrade:             ItemData(367759171, ItemClassification.useful),
	itemName.RopeUpgrade:                ItemData(367759172, ItemClassification.useful),
	itemName.SoulUpgrade:                ItemData(367759192, ItemClassification.filler)
}

lifeup_items = {
	itemName.DesertLifeUp:               ItemData(367759039, ItemClassification.useful),
	itemName.CryptsLifeUp:               ItemData(367759077, ItemClassification.useful),
	itemName.RiverLifeUp:                ItemData(367759109, ItemClassification.useful)
}

race_items = {
	itemName.ForestRace100Rupees:        ItemData(367759173, ItemClassification.filler),
	itemName.PeakRace100Rupees:          ItemData(367759174, ItemClassification.filler),
	itemName.HillsRace100Rupees:         ItemData(367759175, ItemClassification.filler)
}

trading_items = {
	itemName.SacredOil:                  ItemData(367759124, ItemClassification.progression_deprioritized),
	itemName.DungeonKey:                 ItemData(367759163, ItemClassification.progression_deprioritized),
	itemName.Chainsword:                 ItemData(367759164, ItemClassification.progression_deprioritized),
	itemName.SnailSalt:                  ItemData(367759178, ItemClassification.progression_deprioritized),
	itemName.OgreHair:                   ItemData(367759183, ItemClassification.progression_deprioritized),
	itemName.CleaverShovel:              ItemData(367759188, ItemClassification.progression_deprioritized),
	itemName.OilandChains:               ItemData(367759189, ItemClassification.progression_deprioritized),
	itemName.FunkyFungus:                ItemData(367759191, ItemClassification.progression_deprioritized)
}

jewel_items = {
	itemName.ForestJewel:                ItemData(367759020, ItemClassification.progression_skip_balancing),
	itemName.CanyonJewel:                ItemData(367759049, ItemClassification.progression_skip_balancing),
	itemName.PeakJewel:                  ItemData(367759075, ItemClassification.progression_skip_balancing),
	itemName.FortJewel:                  ItemData(367759137, ItemClassification.progression_skip_balancing),
	itemName.CastleJewel:                ItemData(367759149, ItemClassification.progression_skip_balancing)
}

quest_items = {
	itemName.Bombs:                      ItemData(367759007, ItemClassification.progression),
	itemName.SwordWave:                  ItemData(367759016, ItemClassification.progression),
	itemName.GoldenFly:                  ItemData(367759017, ItemClassification.progression),
	itemName.MagicArmor:                 ItemData(367759021, ItemClassification.useful),
	itemName.SilverCricket:              ItemData(367759022, ItemClassification.progression_deprioritized),
	itemName.RopeLadder:                 ItemData(367759023, ItemClassification.progression_deprioritized),
	itemName.ShieldRing:                 ItemData(367759030, ItemClassification.useful),
	itemName.Compass:                    ItemData(367759034, ItemClassification.progression_deprioritized),
	itemName.GriffinBoots:               ItemData(367759063, ItemClassification.progression),
	itemName.Bell:                       ItemData(367759078, ItemClassification.progression_deprioritized),
	itemName.CrystalofRefraction:        ItemData(367759090, ItemClassification.progression_deprioritized),
	itemName.FatalFlute:                 ItemData(367759099, ItemClassification.progression),
	itemName.BlueMagic:                  ItemData(367759106, ItemClassification.progression),
	itemName.LightningSword:             ItemData(367759111, ItemClassification.useful),
	itemName.EnchantedShoes:             ItemData(367759128, ItemClassification.progression_deprioritized),
	itemName.ReflectorRing:              ItemData(367759136, ItemClassification.progression),
	itemName.WingedBelt:                 ItemData(367759144, ItemClassification.progression),
	itemName.PurpleMagic:                ItemData(367759160, ItemClassification.progression),
	itemName.CitizenshipPapers:          ItemData(367759161, ItemClassification.progression_deprioritized),
	itemName.Canteen:                    ItemData(367759165, ItemClassification.useful),
	itemName.Calendar:                   ItemData(367759169, ItemClassification.progression_deprioritized),
	itemName.Rupees200:                  ItemData(367759170, ItemClassification.filler),
	itemName.Lantern:                    ItemData(367759176, ItemClassification.progression),
	itemName.Rope:                       ItemData(367759177, ItemClassification.filler),
	itemName.FairyDust:                  ItemData(367759179, ItemClassification.progression_deprioritized),
	itemName.Backstep:                   ItemData(367759180, ItemClassification.progression_deprioritized),
	itemName.SmartGun:                   ItemData(367759181, ItemClassification.progression),
	itemName.StarEarrings:               ItemData(367759182, ItemClassification.progression_deprioritized),
	itemName.PowerPendant:               ItemData(367759184, ItemClassification.progression),
	itemName.BombGauntlet:               ItemData(367759185, ItemClassification.progression),
	itemName.SpeedyShoes:                ItemData(367759186, ItemClassification.progression),
	itemName.MagicCloak:                 ItemData(367759187, ItemClassification.progression),
	itemName.DoubleWave:                 ItemData(367759190, ItemClassification.useful)
}

rock_items = {
	itemName.OrangeRock:                 ItemData(367759237, ItemClassification.progression),
	itemName.BrownRock:                  ItemData(367759238, ItemClassification.progression),
	itemName.GrayRock:                   ItemData(367759239, ItemClassification.progression),
	itemName.BlueRock:                   ItemData(367759240, ItemClassification.progression)
}

scroll_items = {
	itemName.FaramoreBonus:              ItemData(367759003, ItemClassification.progression_deprioritized),  # Collect rubies
	itemName.ForestBonus:                ItemData(367759011, ItemClassification.progression_deprioritized),  # Close all of the doors
	itemName.CavesBonus:                 ItemData(367759028, ItemClassification.progression_deprioritized),  # Break the targets
	itemName.DesertBonus:                ItemData(367759036, ItemClassification.progression_deprioritized),  # Find the exit
	itemName.CanyonBonus:                ItemData(367759042, ItemClassification.progression_deprioritized),  # Close all of the doors
	itemName.SwampBonus:                 ItemData(367759065, ItemClassification.progression_deprioritized),  # Find the exit
	itemName.PeakBonus:                  ItemData(367759070, ItemClassification.progression_deprioritized),  # Break the targets
	itemName.CryptsBonus:                ItemData(367759079, ItemClassification.progression_deprioritized),  # Close all of the doors
	itemName.VolcanoBonus:               ItemData(367759086, ItemClassification.progression_deprioritized),  # Collect rubies
	itemName.BeachBonus:                 ItemData(367759097, ItemClassification.progression_deprioritized),  # Break the targets
	itemName.RiverBonus:                 ItemData(367759102, ItemClassification.progression_deprioritized),  # Close all of the doors
	itemName.HillsBonus:                 ItemData(367759113, ItemClassification.progression_deprioritized),  # Break the targets
	itemName.FortBonus:                  ItemData(367759138, ItemClassification.progression_deprioritized),  # Find the exit
	itemName.CastleBonus:                ItemData(367759148, ItemClassification.progression_deprioritized),  # Collect rubies
	itemName.LairBonus:                  ItemData(367759152, ItemClassification.progression_deprioritized)   # Close all of the doors 
}

bonusreward_items = {
	itemName.FaramoreBonusReward:        ItemData(367759241, ItemClassification.filler),
	itemName.ForestBonusReward:          ItemData(367759242, ItemClassification.filler),
	itemName.CavesBonusReward:           ItemData(367759243, ItemClassification.filler),
	itemName.DesertBonusReward:          ItemData(367759244, ItemClassification.filler),
	itemName.CanyonBonusReward:          ItemData(367759245, ItemClassification.filler),
	itemName.SwampBonusReward:           ItemData(367759246, ItemClassification.filler),
	itemName.PeakBonusReward:            ItemData(367759247, ItemClassification.filler),
	itemName.CryptsBonusReward:          ItemData(367759248, ItemClassification.filler),
	itemName.VolcanoBonusReward:         ItemData(367759249, ItemClassification.filler),
	itemName.BeachBonusReward:           ItemData(367759250, ItemClassification.filler),
	itemName.RiverBonusReward:           ItemData(367759251, ItemClassification.filler),
	itemName.HillsBonusReward:           ItemData(367759252, ItemClassification.filler),
	itemName.FortBonusReward:            ItemData(367759253, ItemClassification.filler),
	itemName.CastleBonusReward:          ItemData(367759254, ItemClassification.filler),
	itemName.LairBonusReward:            ItemData(367759255, ItemClassification.filler)
}

npcspawner_items = {
	itemName.FaramoreCovenplate:         ItemData(367759193, ItemClassification.progression),
	itemName.CanyonCrowdee:              ItemData(367759194, ItemClassification.progression),
	itemName.PeakCiclena:                ItemData(367759195, ItemClassification.progression),
	itemName.BeachFleetus:               ItemData(367759196, ItemClassification.progression),
	itemName.ForestCypress:              ItemData(367759197, ItemClassification.progression),
	itemName.FaramoreYukeen:             ItemData(367759198, ItemClassification.progression),
	itemName.FaramoreRudy:               ItemData(367759199, ItemClassification.progression),
	itemName.DesertFairy:                ItemData(367759200, ItemClassification.progression),
	itemName.BeachTork:                  ItemData(367759201, ItemClassification.progression),
	itemName.FaramoreAlven:              ItemData(367759202, ItemClassification.progression),
	itemName.CavesEllido:                ItemData(367759203, ItemClassification.progression),
	itemName.CanyonMotte:                ItemData(367759204, ItemClassification.progression),
	itemName.FaramoreBarnabuss:          ItemData(367759205, ItemClassification.progression),
	itemName.FaramoreDenny:              ItemData(367759206, ItemClassification.progression),
	itemName.FaramoreDewey:              ItemData(367759207, ItemClassification.progression),
	itemName.CryptsSkelvis:              ItemData(367759208, ItemClassification.progression),
	itemName.FaramoreFrich:              ItemData(367759209, ItemClassification.progression),
	itemName.LairZazie:                  ItemData(367759210, ItemClassification.progression),
	itemName.CavesMunhum:                ItemData(367759211, ItemClassification.progression),
	itemName.FaramoreBrinda:             ItemData(367759212, ItemClassification.progression),
	itemName.SwampGlubbert:              ItemData(367759213, ItemClassification.progression),
	itemName.HillsMilbert:               ItemData(367759214, ItemClassification.progression),
	itemName.FaramoreCypress:            ItemData(367759215, ItemClassification.progression),
	itemName.CanyonOdie:                 ItemData(367759216, ItemClassification.progression),
	itemName.FaramoreKariQuest:          ItemData(367759217, ItemClassification.progression),
	itemName.RiverMorgh:                 ItemData(367759218, ItemClassification.progression),
	itemName.RiverFrancine:              ItemData(367759219, ItemClassification.progression),
	itemName.FaramoreMunhum:             ItemData(367759220, ItemClassification.progression)
}

npc_items = {
	itemName.FaramoreBoru:               ItemData(367759221, ItemClassification.filler),
	itemName.FaramoreKari:               ItemData(367759222, ItemClassification.filler),
	itemName.FaramoreUnivor:             ItemData(367759223, ItemClassification.filler),
	itemName.FaramoreSalvik:             ItemData(367759224, ItemClassification.filler),
	itemName.FaramoreMaki:               ItemData(367759225, ItemClassification.filler),
	itemName.FaramorePayop:              ItemData(367759226, ItemClassification.filler),
	itemName.VolcanoJoe:                 ItemData(367759227, ItemClassification.filler),
	itemName.RiverBarnabuss:             ItemData(367759228, ItemClassification.filler),
	itemName.FaramoreMortar:             ItemData(367759229, ItemClassification.progression),
	itemName.SwampFrich:                 ItemData(367759230, ItemClassification.progression),
	itemName.ForestRudyStart:            ItemData(367759231, ItemClassification.progression),
	itemName.ForestRudyEnd:              ItemData(367759232, ItemClassification.progression),
	itemName.PeakRudyStart:              ItemData(367759233, ItemClassification.progression),
	itemName.PeakRudyEnd:                ItemData(367759234, ItemClassification.progression),
	itemName.HillsRudyStart:             ItemData(367759235, ItemClassification.progression),
	itemName.HillsRudyEnd:               ItemData(367759236, ItemClassification.progression)
}

beacon_items = {
	itemName.ForestBeacon:               ItemData(367759019, ItemClassification.progression),
	itemName.DesertBeacon:               ItemData(367759041, ItemClassification.progression),
	itemName.SwampBeacon:                ItemData(367759066, ItemClassification.progression),
	itemName.BeachBeacon:                ItemData(367759100, ItemClassification.progression),
	itemName.HillsBeacon:                ItemData(367759119, ItemClassification.progression)
}

levelunlock_items = {
	itemName.Default1:                   ItemData(367759256, ItemClassification.progression),
	itemName.Default2:                   ItemData(367759257, ItemClassification.progression),
	itemName.ForestBeacon1:              ItemData(367759258, ItemClassification.progression),
	itemName.ForestBeacon2:              ItemData(367759259, ItemClassification.progression),
	itemName.ForestBeacon3:              ItemData(367759260, ItemClassification.progression),
	itemName.DesertBeacon1:              ItemData(367759261, ItemClassification.progression),
	itemName.DesertBeacon2:              ItemData(367759262, ItemClassification.progression),
	itemName.DesertBeacon3:              ItemData(367759263, ItemClassification.progression),
	itemName.SwampBeacon1:               ItemData(367759264, ItemClassification.progression),
	itemName.SwampBeacon2:               ItemData(367759265, ItemClassification.progression),
	itemName.SwampBeacon3:               ItemData(367759266, ItemClassification.progression),
	itemName.BeachBeacon1:               ItemData(367759267, ItemClassification.progression),
	itemName.BeachBeacon2:               ItemData(367759268, ItemClassification.progression),
	itemName.HillsBeacon1:               ItemData(367759269, ItemClassification.progression),
	itemName.HillsBeacon2:               ItemData(367759270, ItemClassification.progression)
}

other_items = {
	itemName.Daimur:                     ItemData(367759159, ItemClassification.progression)
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
