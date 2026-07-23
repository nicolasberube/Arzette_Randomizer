from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Item, CollectionState
import warnings
from typing import List, Dict, Any
from worlds.generic.Rules import add_rule

from .locations import ArzetteLocation, all_locations, levelunlock_locations
from .items import ArzetteItem, all_item_table, all_group_table, \
    candle_items, coin_items, jewel_items, plant_items, race_items, rock_items, bag_items, \
    key_items, upgrade_items, lifeup_items, bonusreward_items, \
    npcspawner_items, npc_items, scroll_items, beacon_items, trading_items, quest_items
from .options import ArzetteOptions, LevelOrder, TradingSequence
from .rules import set_location_rules, level_to_locations

class ArzetteWebWorld(WebWorld):
    pass  # todo

class ArzetteWorld(World):
    game: str = "Arzette: The Jewel of Faramore"
    # web = ArzetteWebWorld()
    topology_present = True

    item_name_groups = {
        "magic": {"Sword Wave", "Smart Gun"},
        "bombs": {"Bombs", "Bomb Gauntlet"},
        "blue": {"Blue Magic", "Purple Magic"},
        "candles": set(candle_items),
        "coins": set(coin_items),
        "jewels": set(jewel_items),
        "plants": set(plant_items),
        "races": set(race_items),
        "rocks": set(rock_items),
        "bags": set(bag_items),
    }

    item_name_to_id = {name: data.arzid for name, data in all_item_table.items()}
    location_name_to_id = {name: data.arzid for name, data in all_locations.items()}

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
        self.unreachables = []

        super(ArzetteWorld, self).__init__(world, player)

    def generate_early(self) -> None:
        self.choose_barrier()
        self.choose_level_unlock()
        self.assign_trading()
        self.assign_locked()
        self.assign_spawner()
        self.assign_local()
        self.assign_beacon()

    def choose_barrier(self) -> None:
        # The way the barrier randomization works is by creating the dictionnary
        # self.barrier_type where the key is the default barrier type and
        # the value is the new barrier type.
        # Every time a rule is called that involves a barrier, it is called through this dictionnary.
        # The reason we do not generate the appropriate rules of the new barrier
        # in rules.py:has_color() is because colored enemies are nos randomized.

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

        if self.barrier_types["Flute"] != "Flute":
            self.unreachables.append("Crypts Coin")

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

        #if self.options.level_order.value in {LevelOrder.option_randomize, LevelOrder.option_faramore}:
        if self.options.level_order.value in {LevelOrder.option_faramore}:
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
            if self.options.shuffle_beacons.value:
                beacons = list(default_level_order)
            while len(beacons):
                beacon = beacons.pop(0)
                if not self.options.shuffle_beacons.value:
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
                            not self.options.shuffle_beacons.value):
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
            self.early_lock["Forest Bonus Reward"] = "Soul Upgrade"
            self.unreachables.append("Soul Upgrade")
        if trading_type != TradingSequence.option_included:
            # Locks the first item of the trading sequence in the last location
            # of the sequence that should not be accessible
            if start_position != 0:
                self.early_lock[trading_sequence[0]] = trading_sequence[start_position]
            for location in trading_sequence[1:start_position]:
                self.early_lock[location] = location
            self.unreachables += trading_sequence[1:start_position+1]

    def assign_locked(self) -> None:
        # Those are all locations that need to be locked as vanilla for now
        # due to the randomizer mod's limitation.

        for location, locdata in all_locations.items():
            if not locdata.locked:
                continue
            self.early_lock[location] = location

    def assign_spawner(self) -> None:
        # The way the attribution of spawners (npc and scroll) work
        # is by looking at the attribute self.early_lock
        # where the key is spawner item name and value is its location name
        # It is used when creating rules.

        # Assigning spawner items
        spawner_list = []
        if self.options.shuffle_npcs.value:
            spawner_list += [name for name in npcspawner_items if name not in self.early_lock]
        else:
            for name in list(npcspawner_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if self.options.shuffle_bonus_scrolls.value:
            spawner_list += [name for name in scroll_items if name not in self.early_lock]
        else:
            for name in list(scroll_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if len(spawner_list) > 0:
            chosen_locs = self.get_all_chosen_items()
            available_locs = [
                location for location, locdata in all_locations.items()
                if (locdata.can_spawner and (location not in self.early_lock.values()) and
                    (location in chosen_locs))]

            self.random.shuffle(available_locs)
            available_locs = available_locs[:len(spawner_list)]

            for name, location in zip(spawner_list, available_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location

    def assign_local(self) -> None:
        # Assigning other local items that are not spawners
        local_list = []
        if self.options.shuffle_npcs.value:
            local_list += [name for name in npc_items if name not in self.early_lock]
        else:
            for name in list(npc_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        if len(local_list) > 0:
            chosen_locs = self.get_all_chosen_items()
            available_locs = [
                location for location in all_locations
                if ((location not in self.early_lock.values()) and
                    (location in chosen_locs))]

            self.random.shuffle(available_locs)
            available_locs = available_locs[:len(local_list)]

            for name, location in zip(local_list, available_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location

    def assign_beacon(self) -> None:
        beacon_list = []
        if self.options.shuffle_beacons.value:
            beacon_list += [name for name in beacon_items if name not in self.early_lock]
        else:
            for name in list(beacon_items):
                if name not in self.early_lock:
                    self.early_lock[name] = name

        self.random.shuffle(beacon_list)
        available_levels = self.level_order["Default Beacon"][:]
        for beacon in beacon_list:
            chosen_locs = self.get_all_chosen_items()
            available_locs = [
                location for level in available_levels
                for location in level_to_locations[level]
                if ((location not in self.early_lock.values()) and
                    (location in chosen_locs))]
            self.random.shuffle(available_locs)
            location = available_locs[0]
            if location in self.early_lock.values():
                raise Exception(f"Location {location} already filled.")
            self.early_lock[beacon] = location
            available_levels += self.level_order[beacon]

    def get_all_chosen_items(self) -> List[str]:
        """Return all item names chosen by the options."""
        all_chosen_items = list(quest_items)
        if self.options.shuffle_npcs.value:
            all_chosen_items += list(npcspawner_items)+list(npc_items)
        if self.options.shuffle_bags.value:
            all_chosen_items += list(bag_items)
        if self.options.shuffle_keys.value:
            all_chosen_items += [name for name in key_items if name != 'Hills Key']
        if self.options.shuffle_hills_key.value:
            all_chosen_items += ['Hills Key']
        if self.options.shuffle_candles.value:
            all_chosen_items += list(candle_items)
        if self.options.shuffle_coins.value:
            all_chosen_items += list(coin_items)
        if self.options.shuffle_upgrades.value:
            all_chosen_items += list(upgrade_items)
        if self.options.shuffle_rocks.value:
            all_chosen_items += list(rock_items)
        if self.options.shuffle_plants.value:
            all_chosen_items += list(plant_items)
        if self.options.shuffle_life_ups.value:
            all_chosen_items += list(lifeup_items)
        if self.options.shuffle_bonus_scrolls.value:
            all_chosen_items += list(scroll_items)
        if self.options.shuffle_bonus_rewards.value:
            all_chosen_items += list(bonusreward_items)
        if self.options.shuffle_race_rewards.value:
            all_chosen_items += list(race_items)
        if self.options.shuffle_jewels.value:
            all_chosen_items += list(jewel_items)
        if self.options.shuffle_beacons.value:
            all_chosen_items += list(beacon_items)
        if self.options.trading_sequence.value != TradingSequence.option_vanilla:
            all_chosen_items += list(trading_items)

        return all_chosen_items

    def create_regions(self) -> None:
        active_locations = [name for name in self.get_all_chosen_items()
                            if name not in self.early_lock.values()]
        print('EARLY LOCK')
        print(self.early_lock)
        print('UNREACHABLES')
        print(self.unreachables)
        self.loc_to_id = {name: all_locations[name].arzid
                          if name in active_locations else None
                          for name in all_locations}
        ret = Region("Menu", self.player, self.multiworld)
        ret.add_locations(self.loc_to_id, ArzetteLocation)

        self.multiworld.regions.append(ret)

    def create_item(self, name:str, event:bool=False) -> Item:
        arzette_item = all_item_table.get(name)
        if not arzette_item:
            raise ValueError(f"{name} is not a valid item name for Arzette")

        arzid = arzette_item.arzid if not event else None
        created_item = ArzetteItem(name, arzette_item.type, arzid, self.player)
        return created_item

    def create_items(self) -> None:
        active_items = [name for name in self.get_all_chosen_items()
                        if name not in self.early_lock]
        itempool = []
        for name in all_item_table:
            if name not in active_items:
                add_item = self.create_item(name, event=True)
                if name in self.early_lock:
                    self.get_location(self.early_lock[name]).place_locked_item(add_item)
                else:
                    self.get_location(name).place_locked_item(add_item)
                #itempool.append(add_item)
            else:
                itempool.append(self.create_item(name, event=False))

        # Add Filler items until all locations are filled
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        if len(itempool) > total_locations:
            warnings.warn(
                "Number of total available items exceeds the number of locations, "
                "likely there is a bug in the generation."
            )

        itempool += [self.create_filler() for _ in range(total_locations - len(itempool))]
        self.multiworld.itempool.extend(itempool)

    def set_rules(self) -> None:
        set_location_rules(self)
        for location in self.unreachables:
            add_rule(self.get_location(location), lambda state: True, combine="or")

    def fill_slot_data(self) -> Dict[str, Any]:
        barrier_codes = {
            "Red": "b_red_block",
            "Blue": "b_blue_block",
            "Purple": "b_purple_block",
            "Flute": "b_flute_block",
            "Gauntlet": "b_grey_block"
        }
        barrier_info = {
            key+'_Barrier': barrier_codes[value]
            for key, value in self.barrier_types.items()
        }

        unpingable_locations = {
            all_locations[location].arzid: {
                "item": all_item_table[name].arzid,
                "flags": all_item_table[name].type.as_flag()}
            for name, location in self.early_lock.items()}

        pingable_locations = []
        for location, arzid  in self.loc_to_id.items():
            if all_locations[location].arzid in unpingable_locations:
                continue
            if arzid is None:
                unpingable_locations[all_locations[location].arzid] = {
                    "item": all_item_table[location].arzid,
                    "flags": all_item_table[location].type.as_flag()}
            else:
                pingable_locations.append(arzid)

        slot_data = {
            "barrier_info": barrier_info,
            "unpingable_locations": unpingable_locations,
            "pingable_locations": pingable_locations
        }
        return slot_data
