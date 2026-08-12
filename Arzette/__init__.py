from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Item, ItemClassification, Tutorial, CollectionState
import warnings
from Options import OptionError
from typing import List, Dict, Any
from worlds.generic.Rules import add_rule
import logging

from .Names import itemName, locName
from .locations import ArzetteLocation, all_locations, levelunlock_locations
from .items import ArzetteItem, all_item_table, \
    candle_items, coin_items, jewel_items, plant_items, race_items, rock_items, bag_items, \
    key_items, upgrade_items, lifeup_items, bonusreward_items, \
    npcspawner_items, npc_items, scroll_items, beacon_items, trading_items, quest_items
from .options import ArzetteOptions, LevelOrder, TradingSequence, arzette_option_groups
from .rules import set_location_rules, level_to_locations

class ArzetteWebWorld(WebWorld):
    setup_en = Tutorial(
        "Setup Arzette: The Jewel of Faramore",
        """A guide to setting up Archipelago Arzette on your computer.""",
        "English",
        "setup_en.md",
        "setup/en",
        ["Lightmopp"])

    tutorials = [setup_en]
    option_groups = arzette_option_groups

class ArzetteWorld(World):
    game: str = "Arzette: The Jewel of Faramore"
    web = ArzetteWebWorld()
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

    ut_can_gen_without_yaml = True

    def __init__(self, world, player):
        # Item name (key) and Locations name (value) that have been attributed
        # during generate_early to take out of the pool
        # when running self.create_items() and self.create_regions()
        # Also useful when creating rules for spawner items
        # I know the having the items as key instead of locations is
        # bad practice, it's legacy code and I'm tired.
        self.early_lock = {}

        self.barrier_types = {}
        self.level_order = {}
        self.level_beacons = {}
        # Unreachable locations for logic purposes. Should all be in self.early_lock
        self.unreachables = []
        self.progression_bag = None

        item_id_to_name = {arzid: name for name, arzid in self.item_name_to_id.items()}
        self.loc_to_item = {
            location: item_id_to_name[arzid]
            for location, arzid in self.location_name_to_id.items()
        }
        self.item_to_loc = {
            name: location
            for location, name in self.loc_to_item.items()
        }

        super(ArzetteWorld, self).__init__(world, player)

    def generate_early(self) -> None:
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Universal Tracker trickery
            slot_data = self.multiworld.re_gen_passthrough[self.game]

            slot_options: dict[str, Any] = slot_data["universal_tracker_info"].get("options", {})
            for key, value in slot_options.items():
                opt = getattr(self.options, key, None)
                if opt is not None:
                    setattr(self.options, key, opt.from_any(value))

            self.barrier_types = slot_data["universal_tracker_info"]["barrier_types"]
            self.early_lock = slot_data["universal_tracker_info"]["early_lock"]
            self.unreachables = slot_data["universal_tracker_info"]["unreachables"]
            self.level_order = slot_data["universal_tracker_info"]["level_order"]
            self.level_beacons = slot_data["universal_tracker_info"]["level_beacons"]
            self.progression_bag = slot_data["universal_tracker_info"].get("progression_bag")
        else:
            # Normal generation
            self.validate_yaml_options()
            self.choose_barrier()
            self.choose_level_unlock()
            self.assign_trading()
            self.assign_locked()
            self.assign_spawner()
            self.assign_local()
            self.assign_beacon()

    def validate_yaml_options(self) -> None:
        if self.options.shuffle_barrier_types.value and not self.options.shuffle_coins.value:
            raise OptionError(
                "Shuffle Coins must be enabled to randomize barriers."
            )
        if self.options.shuffle_beacons.value and not (
                self.options.shuffle_npcs.value or
                self.options.shuffle_bags.value or
                self.options.shuffle_candles.value or
                self.options.shuffle_keys.value or
                self.options.shuffle_coins.value or
                self.options.shuffle_upgrades.value):
            raise OptionError(
                "Shuffle for a least one common items (npcs, bags, candles, keys, coins or upgrades) "
                "must be enabled to randomize beacons."
            )

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
            self.early_lock[itemName.CavesBonusReward] = locName.CryptsCoin
            self.unreachables.append(locName.CryptsCoin)

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
        all_levels = [level for levels in default_level_order.values()
                      for level in levels]
        start_levels = ["Faramore", "Forest", "Desert", "Canyon"]
        if self.options.level_order.value != LevelOrder.option_shuffle:
            start_levels = all_levels

        if self.options.level_order.value in {LevelOrder.option_faramore_start_shuffle, LevelOrder.option_shuffle}:
            if (self.options.level_order.value == LevelOrder.option_shuffle and
                    self.options.shuffle_bags.value):
                self.progression_bag = self.random.choice(list(bag_items))
                self.multiworld.local_early_items[self.player][self.progression_bag] = 1
            level_list = all_levels[:]
            if self.options.level_order.value == LevelOrder.option_faramore_start_shuffle:
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

                if (self.options.level_order.value == LevelOrder.option_faramore_start_shuffle and
                        beacon == "Default"):
                    level_order[beacon].append("Faramore")

                n_unlocks = len(default_level_order[beacon])-len(level_order[beacon])
                for i_u in range(n_unlocks):
                    i_l = 0
                    while (level_list[i_l] not in start_levels) and (beacon == "Default") and (i_u == 0):
                        i_l += 1
                    if (level_list[i_l] in default_level_order and
                            not self.options.shuffle_beacons.value):
                        beacons.append(level_list[i_l])
                    level_order[beacon].append(level_list.pop(i_l))
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

        level_to_id = {}
        for level in all_levels:
            # Reading from the item_code is terrible and I'm sorry for it
            possible_locs = [location for location, locdata in levelunlock_locations.items()
                             if level.lower() in locdata.item_code]
            if len(possible_locs) != 1:
                raise Exception(f'Level unlock location not found for level {level}')
            level_to_id[level] = self.loc_to_item[possible_locs[0]]

        code_to_loc = {
            data.location_code: location
            for location, data in all_locations.items()
        }
        for beacon, levels in self.level_order.items():
            if beacon == 'Default Beacon':
                beacon = 'Default'
            for i_l, level in enumerate(levels, 1):
                self.early_lock[level_to_id[level]] = code_to_loc[f'{beacon} {i_l}']

    def assign_trading(self) -> None:
        # (item, location) tuple of the vanilla trading sequence
        trading_sequence = [
            locName.SacredOil,
            locName.FunkyFungus,
            locName.SnailSalt,
            locName.CleaverShovel,
            locName.OgreHair,
            locName.OilandChains,
            locName.Chainsword]

        trading_type = self.options.trading_sequence.value
        if trading_type not in {
                TradingSequence.option_vanilla,
                TradingSequence.option_random_start,
                TradingSequence.option_shuffle,
                TradingSequence.option_excluded}:
            raise Exception(f"config file trading_type {trading_type} not recognised.")

        start_position = 0
        lock_position = -1
        if trading_type == TradingSequence.option_random_start:
            start_position = self.random.randint(0, len(trading_sequence)-2)
        elif trading_type == TradingSequence.option_excluded:
            start_position = len(trading_sequence)-2
        if trading_type in {TradingSequence.option_random_start, TradingSequence.option_vanilla}:
            lock_position = start_position+1
        # With this option, the Soul Upgrade location is unreachable
        if start_position != 0:
            if self.options.shuffle_upgrades.value:
                self.early_lock[itemName.ForestBonusReward] = locName.SoulUpgrade
            self.unreachables.append(locName.SoulUpgrade)
        if trading_type != TradingSequence.option_shuffle:
            # Locks the first item of the trading sequence in the last location
            # of the sequence that should not be accessible
            if start_position != 0:
                self.early_lock[self.loc_to_item[trading_sequence[0]]] = \
                    trading_sequence[start_position]
            for location in trading_sequence[1:start_position]:
                self.early_lock[self.loc_to_item[location]] = location
            self.unreachables += trading_sequence[1:start_position+1]
            if lock_position > 0:
                for location in trading_sequence[lock_position:]:
                    self.early_lock[self.loc_to_item[location]] = location

    def assign_locked(self) -> None:
        # Those are all locations that need to be locked as vanilla for now
        # due to the randomizer mod's limitation.

        for location, locdata in all_locations.items():
            if not locdata.locked:
                continue
            self.early_lock[self.loc_to_item[location]] = location

    def assign_spawner(self) -> None:
        # The way the attribution of spawners (npc and scroll) work
        # is by looking at the attribute self.early_lock
        # where the key is spawner item name and value is its location name
        # It is used when creating rules.

        logging.info('ASSIGN SPAWNER')
        logging.info('EARLY LOCK')
        logging.info(self.early_lock)

        # Assigning spawner items
        spawner_list = []
        if self.options.shuffle_npcs.value:
            spawner_list += [name for name in npcspawner_items if name not in self.early_lock]
        else:
            for name in list(npcspawner_items):
                if name not in self.early_lock:
                    self.early_lock[name] = self.item_to_loc[name]

        if self.options.shuffle_bonus_scrolls.value:
            spawner_list += [name for name in scroll_items if name not in self.early_lock]
        else:
            for name in list(scroll_items):
                if name not in self.early_lock:
                    self.early_lock[name] = self.item_to_loc[name]

        if len(spawner_list) > 0:
            chosen_locs = self.get_all_chosen_locations()
            available_locs = [
                location for location, locdata in all_locations.items()
                if (locdata.can_spawner and (location not in self.early_lock.values()) and
                    (location in chosen_locs))]

            self.random.shuffle(available_locs)
            if len(available_locs) < len(spawner_list):
                raise Exception('Not enough available locations for all spawners')
            available_locs = available_locs[:len(spawner_list)]

            for name, location in zip(spawner_list, available_locs):
                if location in self.early_lock.values():
                    raise Exception(f"Location {location} already filled.")
                self.early_lock[name] = location

        logging.info('SPAWNER LIST')
        logging.info(spawner_list)
        logging.info('AVAILABLE LOCS')
        logging.info(available_locs)
        logging.info('EARLY LOCK')
        logging.info(self.early_lock)

    def assign_local(self) -> None:
        # Assigning other local items that are not spawners
        local_list = []
        if self.options.shuffle_npcs.value:
            local_list += [name for name in npc_items if name not in self.early_lock]
        else:
            for name in list(npc_items):
                if name not in self.early_lock:
                    self.early_lock[name] = self.item_to_loc[name]

        if len(local_list) > 0:
            chosen_locs = self.get_all_chosen_locations()
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
                    self.early_lock[name] = self.item_to_loc[name]

        self.random.shuffle(beacon_list)
        available_levels = self.level_order["Default Beacon"][:]
        for beacon in beacon_list:
            chosen_locs = self.get_all_chosen_locations()
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
            all_chosen_items += [name for name in key_items if name != itemName.HillsKey]
        if self.options.shuffle_hills_key.value:
            all_chosen_items += [itemName.HillsKey]
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

    def get_all_chosen_locations(self):
        return [self.item_to_loc[name] for name in self.get_all_chosen_items()]

    def create_regions(self) -> None:
        active_locations = [name for name in self.get_all_chosen_locations()
                            if (name not in self.early_lock.values())]
        active_locations += [self.early_lock[name] for name in beacon_items]

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
        classification = arzette_item.type
        if event and name in bag_items:
            classification = ItemClassification.progression
        created_item = ArzetteItem(name, classification, arzid, self.player)
        return created_item

    def get_filler_item_name(self) -> str:
        # I don't think this will work right
        filler_items = list(bag_items) + list(race_items) + list(bonusreward_items)
        return self.random.choice(filler_items)

    def create_items(self) -> None:
        # Debug
        if True:
            logging.info('EARLY LOCK')
            logging.info(self.early_lock)
            logging.info('UNREACHABLES')
            logging.info(self.unreachables)
            logging.info('LEVEL ORDER')
            logging.info(self.level_order)
            logging.info('OPTIONS')
            logging.info(self.options)

        active_items = [name for name in self.get_all_chosen_items()
                        if name not in self.early_lock]

        # Not all candles/coins are needed for logic. Picks the bare minimum randomly and sets them as progression;
        # the rest are useful for the fill step and changes back to progression in post_fill.
        # This lowers the progression density to help the fill step.
        fill_useful = set()
        candle_pool = [name for name in active_items if name in candle_items]
        self.random.shuffle(candle_pool)
        fill_useful.update(candle_pool[21:])
        coin_pool = [name for name in active_items if name in coin_items]
        self.random.shuffle(coin_pool)
        fill_useful.update(coin_pool[11:])

        itempool = []
        for name in all_item_table:
            if name not in active_items:
                is_event_item = name not in beacon_items
                add_item = self.create_item(name, event=is_event_item)
                if name in self.early_lock:
                    # DEBUG
                    # try:
                        self.get_location(self.early_lock[name]).place_locked_item(add_item)
                    # except:
                    #     logging.info('name'+name)
                    #     logging.info('location'+self.early_lock[name])
                    #     logging.info('lockeditem'+self.get_location(self.early_lock[name]).item.name)
                    #     raise Exception()
                else:
                    self.get_location(self.item_to_loc[name]).place_locked_item(add_item)
            else:
                pool_item = self.create_item(name, event=False)
                if name in fill_useful:
                    pool_item.classification = ItemClassification.useful
                elif name == self.progression_bag:
                    pool_item.classification = ItemClassification.progression
                if name == itemName.Lantern and self.options.no_lantern.value:
                    pool_item.classification = ItemClassification.useful
                if name in {itemName.MagicCloak, itemName.ReflectorRing} and self.options.damage_boost.value:
                    pool_item.classification = ItemClassification.useful
                if name == itemName.Backstep and not self.options.tricky_jumps.value:
                    pool_item.classification = ItemClassification.useful
                if name == itemName.SoulUpgrade and not (
                        locName.SoulUpgrade in self.unreachables and
                        not self.options.shuffle_upgrades.value):
                    pool_item.classification = ItemClassification.useful
                itempool.append(pool_item)

        # Add Filler items until all locations are filled
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        if len(itempool) > total_locations:
            warnings.warn(
                "Number of total available items exceeds the number of locations, "
                "likely there is a bug in the generation."
            )

        itempool += [self.create_filler() for _ in range(total_locations - len(itempool))]
        self.multiworld.itempool.extend(itempool)

    @classmethod
    def stage_fill_hook(cls, multiworld, progitempool, usefulitempool, filleritempool, fill_locations):
        # Prefer progression over deprioritized or skip-balancing items when filling.
        def sort_key(item: Item) -> int:
            classification = item.classification
            if classification == ItemClassification.progression_deprioritized_skip_balancing:
                return 1
            if classification == ItemClassification.progression_deprioritized:
                return 2
            if classification == ItemClassification.progression_skip_balancing:
                return 3
            return 4

        arzette_players = {world.player for world in multiworld.get_game_worlds(cls.game)}
        if not arzette_players:
            return

        indices = [i for i, item in enumerate(progitempool) if item.player in arzette_players]
        arzette_items = [progitempool[i] for i in indices]
        arzette_items.sort(key=sort_key)
        for i, item in zip(indices, arzette_items):
            progitempool[i] = item

    def post_fill(self) -> None:
        # Restore progression on the extra copies that were classified as useful for the fill step.
        for location in self.multiworld.get_locations(self.player):
            item = location.item
            if item is None or item.player != self.player:
                continue
            if item.name in candle_items:
                item.classification = ItemClassification.progression
            elif item.name in coin_items:
                item.classification = ItemClassification.progression_deprioritized_skip_balancing
    def set_rules(self) -> None:
        set_location_rules(self)
        for location in self.unreachables:
            add_rule(self.get_location(location), lambda state: True, combine="or")
        # Victory condition
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(itemName.Daimur, self.player)

    # Code written by Mysteryem, to detect an early unbeatable seed.
    def generate_basic(self) -> None:
        ## By running this check *before* item plando, it is only necessary to collect the current world's items and
        ## pre-placed items in the current world, which has much better performance scaling in large multiworlds.
        test_state = CollectionState(self.multiworld)
        # Collect our progression items from the item pool.
        for item in self.multiworld.itempool:
            if item.player == self.player and item.advancement:
                test_state.collect(item, True)
        ## This is being run before the `pre_fill` step, so also collect any items that are going to be placed in the
        ## `pre_fill` step.
        # Collect our progression items that are going to be placed in the `pre_fill` step.
        for item in self.get_pre_fill_items():
            if item.advancement:
                test_state.collect(item, True)
        # Collect our reachable pre-placed progression items.
        test_state.sweep_for_advancements(self.get_locations())
        unreachable = [loc for loc in self.get_locations() if not loc.can_reach(test_state)]

        def log_unreachable(reason: str) -> None:
            if not unreachable:
                return
            body = "\n".join(str(loc) for loc in unreachable)
            logging.warning(
                "%s generate_basic — %s — %d unreachable location(s):\n%s",
                self.player_name,
                reason,
                len(unreachable),
                body,
            )

        ## If the loading zone randomization is performed after the item pool is created, e.g. in `connect_entrances`,
        ## then accessibility/beatability failures here could be used to perform a limited number of retries at loading
        ## zone randomization, in which case, this function could be changed to return True/False instead of raising
        ## exceptions.
        if not self.multiworld.has_beaten_game(test_state, self.player):
            log_unreachable("has_beaten_game is False (after granting local advancement + sweep)")
            raise OptionError(f"{self.player_name}: The game is unbeatable.")
        ## Technically, MultiWorld.fulfills_accessibility() only raises an exception with __debug__, so it would be
        ## optional to check accessibility, but note that AP's webhost runs with __debug__=True, so this would fail
        ## there.
        if __debug__:
            ## If you were to opt-in to Items accessibility in the future, that would be a separate check that all your
            ## pre-placed progression items are reachable.
            # All locations must be reachable in Full accessibility.
            if self.options.accessibility == "full" and unreachable:
                log_unreachable("full accessibility (same can_reach probe as above)")
                raise OptionError(
                    f"{self.player_name}: The Full Accessibility requirement could not be met with the rolled loading "
                    f"zone randomization. {len(unreachable)} location(s) unreachable (see log); first: {unreachable[0]}"
                )

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
        for location, arzid in self.loc_to_id.items():
            if all_locations[location].arzid in unpingable_locations:
                continue
            if arzid is None:
                unpingable_locations[all_locations[location].arzid] = {
                    "item": all_item_table[self.loc_to_item[location]].arzid,
                    "flags": all_item_table[self.loc_to_item[location]].type.as_flag()}
            else:
                pingable_locations.append(arzid)

        arzoptions = {option_name: option.value for option_name, option in self.options.__dict__.items()}
        # plando_items not serialisable, so we can't include it in slot_data.
        arzoptions.pop("plando_items")

        universal_tracker_info = {
            "barrier_types": self.barrier_types,
            "early_lock": self.early_lock,
            "unreachables": self.unreachables,
            "level_order": self.level_order,
            "level_beacons": self.level_beacons,
            "progression_bag": self.progression_bag,
            "options": arzoptions
        }
        slot_data = {
            "barrier_info": barrier_info,
            "unpingable_locations": unpingable_locations,
            "pingable_locations": pingable_locations,
            "universal_tracker_info": universal_tracker_info
        }
        return slot_data
