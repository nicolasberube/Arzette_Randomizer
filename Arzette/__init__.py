from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld
from worlds.generic.Rules import add_rule

from .locations import all_locations
from .items import ItemData, all_item_table, all_group_table, \
    npcspawner_items, npc_items, scroll_items, beacon_items
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
        # Also useful when creating rules for spawner items
        self.early_lock = {}

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
            f'{beacon} Beacon': levels[:]
                for beacon, levels in level_order.items()}
        self.level_beacons = {
            level: beacon
            for beacon, levels in self.level_order.items()
            for level in levels}

    def assign_trading(self) -> None:
        # (item, location) tuple of the vanilla trading sequence
        trading_sequence = [
            "Sacred Oil", "Funky Fungus", "Snail Salt",
            "Cleaver Shovel", "Ogre Hair", "Oil and Chains", "Chainsword"]

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
            self.early_lock["Forest Bonus Reward"] = "Soul_Upgrade"
        if trading_type != TradingSequence.option_included:
            # Locks the first item of the trading sequence in the last location
            # of the sequence that should not be accessible
            if start_position != 0:
                self.early_lock[trading_sequence[0]] = trading_sequence[start_position]

            for location in trading_sequence[1:start_position]:
                self.early_lock[location] = location

    def assign_locked(self) -> None:
        # Those are all locations that need to be locked as vanilla for now
        # due to the randomizer mod's limitation.

        for location, locdata in all_locations.items():
            if not locdata.locked:
                continue
            self.early_lock[location] = location

    def assign_npc_scroll_beacon(self) -> None:
        # The way the attribution of spawners (npc and scroll) work
        # is by looking at the attribute self.early_lock
        # where the key is spawner item name and value is its location name
        # It is used when creating rules.

        # Assigning spawner items
        spawner_list = []
        if self.options.shuffle_npcs:
            spawner_list += [name for name in npcspawner_items if name not in self.early_lock]
        else:
            for name in list(npcspawner_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if self.options.shuffle_bonus_scrolls:
            spawner_list += [name for name in scroll_items if name not in self.early_lock]
        else:
            for name in list(scroll_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if len(spawner_list) > 0:
            spawner_locs = [
                location for location, locdata in all_locations.items()
                if locdata.can_spawner and (location not in self.early_lock.values())]

            self.random.shuffle(spawner_locs)
            spawner_locs = spawner_locs[:len(spawner_list)]

            for name, location in zip(spawner_list, spawner_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location

        # Assigning other local items that are not spawners
        local_list = []
        if self.options.shuffle_npcs:
            local_list += [name for name in npc_items if name not in self.early_lock]
        else:
            for name in list(npc_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if self.options.shuffle_beacons:
            local_list += [name for name in beacon_items if name not in self.early_lock]
        else:
            for name in list(beacon_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if len(local_list) > 0:
            available_locs = [
                location for location in all_locations
                if (location not in self.early_lock.values())]

            self.random.shuffle(available_locs)
            available_locs = available_locs[:len(local_list)]

            for name, location in zip(local_list, available_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location

        # WHY is self.level_order not used here for the beacons? Should it?

    # generate_early() -> assign barrier, level unlocks, npc+scrolls, locked, trading_sequence

    # create_items() -> ignore all assigned items in generate_early()
    # create_regions() -> ignore all assigned locations in generate_early()
    # fill_slot_data() -> include all (except default_beacon?)