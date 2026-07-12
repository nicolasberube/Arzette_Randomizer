from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld
from worlds.generic.Rules import add_rule

from .locations import all_locations
from .items import ItemData, all_item_table, all_group_table, beacon_table
from .options import ArzetteOptions, LevelOrder


class ArzetteWebWorld(WebWorld):
    pass  # todo

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteLocation(Location):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteWorld(World):
    game: str = "Arzette: The Jewel of Faramore"
    web = ArzetteWebWorld()

    item_name_groups = {
        "magic": {"Sword Wave", "Smart Gun"},
        "bombs": {"Bombs", "Bomb Gauntlet"},
        "blue": {"Blue Magic", "Purple Magic"},
    }
    location_name_groups = {
        "candles": {location for location in all_locations if "Candle" in location.split()},
        "coins": {location for location in all_locations if "Coin" in location.split()},
        "jewels": {location for location in all_locations if "Jewel" in location.split()},
        "plants": {location for location in all_locations if "Plant" in location.split()},
        "races": {location for location in all_locations if "Race" in location.split()},
        "rocks": {location for location in all_locations if "Rock" in location.split()},
        "bags": {location for location in all_locations if "Bag" in location.split()},
    }

    item_name_to_id = {name: data.btid for name, data in all_item_table.items()}

    location_name_to_id = {name: 2793883000+i for i, name in enumerate(all_locations)}

    options: ArzetteOptions
    options_dataclass = ArzetteOptions

    def generate_early(self) -> None:
        self.choose_barrier()
        self.choose_level_unlock()
        self.assign_npc_scroll_beacon()
        self.assign_trading()
        self.assign_locked()

    def choose_barrier(self) -> None:
        # The way the barrier randomization works is by creating the dictionnary
        # self.barrier_type where the key is the default barrier type and
        # the value is the new barrier type.
        # Every time a rule is called that involves a barrier, it is called through this dictionnary.
        # This is not ideal and due to legacy code of the standalone randomizer.
        # It could instead generate the appropriate rules of the new barrier
        # in rules.py:has_color()

        default_barrier_types = {
            typ: typ for typ in ["Red", "Blue", "Purple", "Gauntlet", "Flute"]}
        if self.options.shuffle_barrier_types.value:
            barrier_list = list(default_barrier_types)
            self.random.shuffle(barrier_list)
            barrier_types = {}
            for barrier in default_barrier_types:
                barrier_types[barrier] = barrier_list.pop(0)
            self.barrier_types = barrier_types
        else:
            self.barrier_types = default_barrier_types

    def choose_level_unlock(self) -> None:
        # This function could create some seed generation failures for a single world seed
        # when your starting level is Beach or Hills because not enough checks are available.

        # The way the level unlock randomization works is by creating the dictionnary
        # self.level_beacons where the key is the level name and the value is the
        # name of the beacon item that unlocks it.
        # It is used when creating rules.

        # self.level_order is the reverse attribute where the key is the beacon name
        # and the value is the list of level names that it unlocks.
        # It is used when assigning a local location for the beacon items.

        default_level_order = {
            "Default": ["Faramore", "Forest"],
            "Forest": ["Caves", "Desert", "Canyon"],
            "Desert": ["Swamp", "Peak", "Crypts"],
            "Swamp": ["Volcano", "Beach", "River"],
            "Beach": ["Hills", "Fort"],
            "Hills": ["Castle", "Lair"]
        }
        level_to_beacon_name = {
            data.default_location.split("_")[0]: beacon
            for beacon, data in beacon_table.items()}

        if self.options.level_order.value in {
                LevelOrder.option_randomize, LevelOrder.option_faramore}:
            level_list = [level for levels in default_level_order.values()
                          for level in levels]
            if self.options.level_order.value == LevelOrder.option_faramore:
                level_list = [
                    level for level in level_list if level != "Faramore"]
            self.random.shuffle(level_list)

            # Because beacons can only spawn in a random location in your local game,
            # this makes sure that the beacon unlock tree with not loop on itself
            # and will always even cover all level unlocks.
            level_order = {}
            # beacons is a dynamic list that contains all available beacons
            beacons = ["Default"]
            if self.options.shuffle_beacons:
                beacons = list(default_level_order)
            while len(beacons):
                beacon = beacons.pop(0)
                if not self.options.shuffle_beacons:
                    # If beacon locations are not random, it needs to unlock at least one
                    # level that has a beacon
                    for i_l, level in enumerate(level_list):
                        if level in default_level_order and level != beacon:
                            beacons.append(level)
                            break
                    level_order[beacon] = [level_list.pop(i_l)]
                else:
                    level_order[beacon] = []

                if (self.options.level_order.value == LevelOrder.option_faramore and
                        beacon == "Default"):
                    level_order[beacon].append("Faramore")

                n_unlocks = len(default_level_order[beacon])-len(level_order[beacon])
                for _ in range(n_unlocks):
                    if (level_list[0] in default_level_order and
                            not self.options.shuffle_beacons):
                        beacons.append(level_list[0])
                    level_order[beacon].append(level_list.pop(0))
        elif self.options.level_order.value == LevelOrder.option_vanilla:
            level_order = default_level_order
        else:
            raise ValueError(f"Config level_order {self.options.level_order.value} not recognised.")

        self.level_order = {
            level_to_beacon_name[beacon]: levels[:]
                for beacon, levels in level_order.items()}
        self.level_beacons = {
            level: beacon
            for beacon, levels in self.level_order.items()
            for level in levels}




    # generate_early() -> assign barrier, level unlocks, npc+scrolls, locked, trading_sequence
    # create_items() -> ignore all assigned items in generate_early()
    # create_regions() -> ignore all assigned locations in generate_early()
    # fill_slot_data() -> include all (except default_beacon?)