from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld
from worlds.generic.Rules import add_rule

from .locations import all_locations, trading_locations, default_npc_locked, non_spawner_locations
from .items import ItemData, all_item_table, all_group_table, beacon_table, scroll_table, npc_table, beacon_table
from .options import ArzetteOptions, LevelOrder, TradingSequence


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

    def __init__(self, world, player):
        # Items (key) and Locations (value) that have been attributed
        # during generate_early to take out of the pool
        # when running self.create_items() and self.create_regions()
        self.early_lock = {}
        self.spawner_locations = {}

        self.barrier_types = {}
        self.level_order = {}
        self.level_beacons = {}

        super(ArzetteWorld, self).__init__(world, player)

    def generate_early(self) -> None:
        self.choose_barrier()
        self.choose_level_unlock()
        self.assign_trading()
        self.assign_locked()
        self.assign_npc_scroll_beacon()

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

    def assign_trading(self) -> None:
        # (item, location) tuple of the vanilla trading sequence
        trading_sequence = []
        for location in trading_locations:
            location = location.replace(" ", "_")
            associated_item = [
                item_name for item_name, data in all_item_table.items()
                if data.default_location == location]
            if len(associated_item) != 1:
                raise Exception(f"Cannot find associated item for location {location}. "
                                "Something went wrong.")
            trading_sequence.append((associated_item[0], location))

        trading_type = self.options.trading_sequence.value
        if trading_type not in {
                TradingSequence.option_vanilla,
                TradingSequence.option_included,
                TradingSequence.option_excluded}:
            raise Exception(f"config file trading_type {trading_type} not recognised.")

        if trading_type == TradingSequence.option_vanilla:
            # TODO: possible future option
            # Assuming you want to start later in the sequence
            # start_position = self.random.randint(0, len(trading_locations)-2)
            # But we need to treat Zazie's Soul Upgrade location accordingly
            start_position = 0
        elif trading_type == TradingSequence.option_excluded:
            start_position = len(trading_sequence)-2
            # With this option, the Soul Upgrade location is unreachable
            self.early_lock["obj_quest_rubie_bag_25_1"] = "Soul_Upgrade"
        if trading_type != TradingSequence.option_included:
            # Locks the first item of the trading sequence in the last location
            # of the sequence that should not be accessible
            if start_position != 0:
                self.early_lock[trading_sequence[0][0]] = trading_sequence[start_position][1]

            for (item, location) in trading_sequence[1:start_position]:
                self.early_lock[item] = location

    def assign_locked(self) -> None:
        # Those are all locations that need to be locked as vanilla for now
        # due to the randomizer mod's limitation.

        # TODO:
        # Obviously those lists should identify the locked items, not the locked locations
        # and reverse search the attributed item to it.
        # This is horrible and is due to legacy code from the standalone randomizer.
        location_locked = ["Default Beacon", "Daimur"]
        location_locked += ["Faramore Bonus Reward",
                            "Volcano Bonus Reward",
                            "Castle Bonus Reward"]
        location_locked += default_npc_locked

        for location in location_locked:
            location = location.replace(" ", "_")
            if location.endswith(" Rudy (Start)"):
                associated_item = ["npc_rudy_start"]
            elif location.endswith(" Rudy (End)"):
                associated_item = ["npc_rudy_goal"]
            else:
                associated_item = [
                    item_name for item_name, data in all_item_table.items()
                    if data.default_location == location]
            if len(associated_item) != 1:
                raise Exception(f"Cannot find associated item for location {location}. "
                                "Something went wrong.")
            self.early_lock[associated_item[0]] = location
            if location in default_npc_locked:
                self.spawner_locations[associated_item[0]] = location

    def assign_npc_scroll_beacon(self) -> None:
        # The way the attribution of spawners (npc and scroll) work
        # is by building the attribute self.spawner_locations
        # where the key is spawner item name and value is its location
        # It is used when creating rules.
        spawner_list = []
        if self.options.shuffle_npcs:
            spawner_list += list(npc_table)
        else:
            for name in list(npc_table):
                self.early_lock[name] = all_item_table[name].default_location
                self.spawner_locations[name] = all_item_table[name].default_location

        if self.options.shuffle_bonus_scrolls:
            spawner_list += list(scroll_table)
        else:
            for name in list(scroll_table):
                self.early_lock[name] = all_item_table[name].default_location
                self.spawner_locations[name] = all_item_table[name].default_location

        if len(spawner_list) > 0:
            spawner_locs = [
                location for location in self.location_name_to_id
                if location not in non_spawner_locations
                and location not in self.early_lock.values()]

            self.random.shuffle(spawner_locs)
            spawner_locs = spawner_locs[:len(spawner_list)]

            for name, location in zip(spawner_list, spawner_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location
                self.spawner_locations[name] = location

        beacon_list = [name for name in beacon_table if name != "beacon_default"]
        if not self.options.shuffle_beacons:
            for name in list(beacon_list):
                self.early_lock[name] = all_item_table[name].default_location
                self.spawner_locations[name] = all_item_table[name].default_location
            beacon_list = []

        if len(beacon_list) > 0:
            available_locs = [
                location for location in self.location_name_to_id
                if location not in self.early_lock.values()]

            self.random.shuffle(available_locs)
            available_locs = available_locs[:len(beacon_list)]

            for name, location in zip(beacon_list, available_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location
                self.spawner_locations[name] = location

    # generate_early() -> assign barrier, level unlocks, npc+scrolls, locked, trading_sequence
    # create_items() -> ignore all assigned items in generate_early()
    # create_regions() -> ignore all assigned locations in generate_early()
    # fill_slot_data() -> include all (except default_beacon?)