import copy
import random
import yaml
import csv
from itertools import combinations

starting_locations = ["Default Beacon"]
rock_locations = ["Orange Rock", "Brown Rock", "Gray Rock", "Blue Rock"]
level_locations = {
    "Faramore": [
        "Faramore Key (Well)",
        "Faramore Key (Tavern)",
        "Faramore Bonus",
        "Faramore Candle (Empty House)",
        "Faramore Candle (Cypress House)",
        "Faramore Coin"
    ],
    "Forest": [
        "Bombs",
        "Forest Bag (First Room 1)",
        "Forest Bag (First Room 2)",
        "Forest Key",
        "Forest Bonus",
        "Forest Candle (Tree)",
        "Forest Candle (Cypress)",
        "Forest Coin",
        "Forest Bag (Sword Wave)",
        "Sword Wave",
        "Golden Fly",
        "Forest Bag (Last Room)",
        "Forest Beacon",
        "Forest Jewel",
        "Magic Armor"
     ],
    "Caves": [
        "Silver Cricket",
        "Rope Ladder",
        "Caves Bag (Rope Ladder)",
        "Caves Candle (First Dark Room)",
        "Caves Coin",
        "Caves Candle (Second Dark Room)",
        "Caves Bonus",
        "Caves Bag (Last Room)",
        "Shield Ring",
    ],
    "Desert": [
        "Desert Coin",
        "Desert Bag (First Room 1)",
        "Desert Bag (First Room 2)",
        "Compass",
        "Desert Candle (Pit)",
        "Desert Bonus",
        "Desert Key",
        "Desert Candle (Last Room)",
        "Desert Life-Up",
        "Desert Bag (Last Room)",
        "Desert Beacon"
    ],
    "Canyon": [
        "Canyon Bonus",
        "Canyon Bag (Before Checkpoint)",
        "Canyon Bag (After Checkpoint 1)",
        "Canyon Bag (After Checkpoint 2)",
        "Canyon Bag (After Checkpoint 3)",
        "Canyon Bag (First Room End)",
        "Canyon Candle (First Room End)",
        "Canyon Jewel",
        "Canyon Key",
        "Canyon Bag (After Zipline 1)",
        "Canyon Bag (After Zipline 2)",
        "Canyon Bag (After Zipline 3)",
        "Canyon Coin",
        "Canyon Bag (Motte House)",
        "Canyon Candle (Motte House)"
    ],
    "Swamp": [
        "Swamp Candle (First Room)",
        "Swamp Bag (First Room)",
        "Swamp Coin",
        "Swamp Key (Frich House)",
        "Swamp Candle (Frich House)",
        "Swamp Key (Griffin Boots)",
        "Griffin Boots",
        "Swamp Plant",
        "Swamp Bonus",
        "Swamp Beacon"
    ],
    "Peak": [
        "Peak Candle (First Cave)",
        "Peak Bag (First Cave 1)",
        "Peak Bag (First Cave 2)",
        "Peak Bonus",
        "Peak Coin",
        "Peak Key",
        "Peak Candle (Ciclena Cave)",
        "Peak Bag (Before Apatu)",
        "Peak Jewel",
        "Peak Bag (After Apatu)"
    ],
    "Crypts": [
        "Crypts Life-Up",
        "Bell",
        "Crypts Bonus",
        "Crypts Key",
        "Crypts Candle (After Crypt)",
        "Crypts Coin",
        "Crypts Candle (Skelvis)",
        "Crypts Bag (Skelvis)"
    ],
    "Volcano": [
        "Volcano Bonus",
        "Volcano Candle (First Room)",
        "Volcano Coin",
        "Volcano Candle (Last Room)",
        "Crystal of Refraction"
    ],
    "Beach": [
        "Beach Bag (First Room)",
        "Beach Key (First House)",
        "Beach Coin",
        "Beach Key (Tork Cabin)",
        "Beach Candle (Tork Cabin)",
        "Beach Plant",
        "Beach Bonus",
        "Beach Candle (Cave)",
        "Fatal Flute",
        "Beach Beacon"
    ],
    "River": [
        "River Key (Francine)",
        "River Bonus",
        "River Candle (Boat)",
        "River Key (Submarine)",
        "River Coin",
        "Blue Magic",
        "River Bag (Last Room)",
        "River Candle (Last Room)",
        "River Life-Up"
    ],
    "Hills": [
        "Hills Candle (Cave)",
        "Lightning Sword",
        "Hills Coin",
        "Hills Bonus",
        "Hills Bag (Barn)",
        "Hills Key",
        "Hills Bag (Music Shrine)",
        "Hills Candle (Music Shrine)",
        "Hills Plant",
        "Hills Beacon"
    ],
    "Fort": [
        "Fort Bag (Dungeon 1)",
        "Fort Bag (Dungeon 2)",
        "Fort Bag (Dungeon 3)",
        "Fort Bag (Dungeon 4)",
        "Sacred Oil",
        "Fort Key (First Room)",
        "Fort Candle (Dark Room)",
        "Fort Bag (Dark Room)",
        "Enchanted Shoes",
        "Fort Coin",
        "Fort Key (Top Room)",
        "Fort Bag (Top Room 1)",
        "Fort Bag (Top Room 2)",
        "Fort Bag (Top Room 3)",
        "Fort Candle (Last Room)",
        "Fort Bag (Last Room)",
        "Reflector Ring",
        "Fort Jewel",
        "Fort Bonus"
    ],
    "Castle": [
        "Castle Bag (Entrance)",
        "Castle Candle (Right Room)",
        "Castle Key (Nodelki)",
        "Castle Candle (Top Room)",
        "Castle Bag (Top Room)",
        "Winged Belt",
        "Castle Coin",
        "Castle Key (Left Room)",
        "Castle Bag (Bonus)",
        "Castle Bonus",
        "Castle Jewel"
    ],
    "Lair": [
        "Lair Candle (Tree Trunk)",
        "Lair Candle (Tree Top)",
        "Lair Bonus",
        "Lair Bag (First Room)",
        "Lair Coin",
        "Lair Bag (Lava Room)",
        "Lair Bag (Final Room 1)",
        "Lair Bag (Final Room 2)",
        "Lair Bag (Final Room 3)",
        "Daimur"
    ]
}
bonus_locations = [f"{level} Bonus Reward" for level in level_locations]


default_level_order = {
    "Default": ["Faramore", "Forest"],
    "Forest": ["Caves", "Desert", "Canyon"],
    "Desert": ["Swamp", "Peak", "Crypts"],
    "Swamp": ["Volcano", "Beach", "River"],
    "Beach": ["Hills", "Fort"],
    "Hills": ["Castle", "Lair"]
}

default_npc_fool = [
    "Faramore Boru",  # blacksmith help
    "Faramore Kari",  # bell quest dude
    "Faramore Univor",  # guard
    "Faramore Salvik",  # drunk dude
    "Faramore Maki",  # baker
    "Faramore Payop",  # librarian
    "Volcano Joe",  # radical
    "River Barnabuss"  # sailor
]

default_npc_locations = {
    "Purple Magic": "Faramore Yukeen",
    "Citizenship Papers": "Faramore Covenplate",
    "Power Stone Upgrade": "Faramore Kari Quest",
    "Dungeon Key": "Faramore Alven",
    "Chainsword": "Faramore Alven",
    "Canteen": "Faramore Brinda",
    "Wallet Upgrade": "Faramore Frich",
    "Infinite Soulfire": "Faramore Rudy",
    "Bomb Upgrade": "Faramore Barnabuss",
    "Calendar": "Faramore Denny",
    "200 Rupees": "Faramore Dewey",
    "Lamp Oil Upgrade": "Faramore Cypress",
    "Rope Upgrade": "Faramore Munhum",
    "Forest Race 100 Rupees": "Faramore Rudy",
    "Peak Race 100 Rupees": "Faramore Rudy",
    "Hills Race 100 Rupees": "Faramore Rudy",
    "Lantern": "Forest Cypress",
    "Rope": "Caves Munhum",
    "Snail Salt": "Caves Ellido",
    "Fairy Dust": "Desert Fairy",
    "Backstep": "Canyon Crowdee",
    "Smart Gun": "Canyon Motte",
    "Star Earrings": "Canyon Odie",
    "Ogre Hair": "Swamp Glubbert",
    "Power Pendant": "Peak Ciclena",
    "Bomb Gauntlet": "Crypts Skelvis",
    "Speedy Shoes": "Beach Fleetus",
    "Magic Cloak": "Beach Tork",
    "Cleaver Shovel": "River Francine",
    "Oil and Chains": "River Morgh",
    "Double Wave": "Hills Milbert",
    "Funky Fungus": "Lair Zazie",
    "Soul Upgrade": "Lair Zazie"
}
default_npc_locked = [
    "Faramore Mortar", "Swamp Frich", "Forest Rudy (Start)", "Forest Rudy (End)",
    "Peak Rudy (Start)", "Peak Rudy (End)", "Hills Rudy (Start)", "Hills Rudy (End)"]
trading_locations = [
    "Sacred Oil", "Funky Fungus", "Snail Salt",
    "Cleaver Shovel", "Ogre Hair", "Oil and Chains", "Chainsword"]

default_barrier_types = {typ: typ for typ in ["Red", "Blue", "Purple", "Gauntlet", "Flute"]}

all_locations = starting_locations + [
    location for locations in level_locations.values() for location in locations] + \
    [location for location in (
        list(default_npc_locations) + rock_locations + bonus_locations)]
all_npcs = (list(set(default_npc_locations.values())) + default_npc_locked + default_npc_fool)

level_names = {
    "Faramore": "Faramore Town",
    "Forest": "Durridin Forest",
    "Caves": "Cogwyn Caves",
    "Desert": "Anju Desert",
    "Canyon": "Creece Canyon",
    "Swamp": "Norin Swamp",
    "Peak": "Chillinax Peaks",
    "Crypts": "Boanjale Crypts",
    "Volcano": "Sprigum Volcano",
    "Beach": "Badonc Beach",
    "River": "Ryha River",
    "Hills": "Lichen Hills",
    "Fort": "Fort Findula",
    "Castle": "Dennys Castle",
    "Lair": "Daimurs Lair"
}

def add_rule(spot, rule, combine="and"):
    old_rule = spot.access_rule
    if combine == "and":
        spot.access_rule = lambda state: rule(state) and old_rule(state)
    else:
        spot.access_rule = lambda state: rule(state) or old_rule(state)

class ArzetteLocation():
    access_rule = staticmethod(lambda state: True)
    item = None

    def can_reach(self, state) -> bool:
        return self.access_rule(state)

class ArzetteWorld():
    level_locations = level_locations
    all_locations = all_locations
    n_tries = 0
    item_name_groups = {
        "magic": {"Sword Wave", "Smart Gun"},
        "bombs": {"Bombs", "Bomb Gauntlet"},
        "candles": {location for location in all_locations if "Candle" in location.split()},
        "coins": {location for location in all_locations if "Coin" in location.split()},
        "jewels": {location for location in all_locations if "Jewel" in location.split()},
        "plants": {location for location in all_locations if "Plant" in location.split()},
        "races": {location for location in all_locations if "Race" in location.split()},
        "rocks": {location for location in all_locations if "Rock" in location.split()},
        "bags": {location for location in all_locations if "Bag" in location.split()},
    }

    def __init__(self, config_path="config.yml"):
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def fill(self, seed=None):
        if seed == "vanilla":
            self.level_order = default_level_order
            self.level_beacons = {
                level: f"{beacon} Beacon" for beacon, levels in self.level_order.items()
                for level in levels}

            self.barrier_cache = {name: ArzetteLocation() for name in default_barrier_types}
            self.set_rules_barrier()
            self.barrier_types = default_barrier_types

            self.npc_cache = {name: ArzetteLocation() for name in all_npcs}
            self.set_rules_npc()
            for name in self.npc_cache:
                self.npc_cache[name].item = name
            self.npc_locations = default_npc_locations

            self.location_cache = {name: ArzetteLocation() for name in all_locations}
            self.set_rules()
            for name in self.location_cache:
                self.location_cache[name].item = name
            return

        if seed is None:
            self.seed = random.randint(0, 4294967295)
        else:
            self.seed = seed
        random.seed(seed)

        # Level order randomisation
        # This function causes some seed generation failures when your
        # starting level is Beach or Hills.
        if self.config["level_order"]:
            level_list = [level for levels in default_level_order.values()
                          for level in levels]
            random.shuffle(level_list)
            level_order = {}
            beacons = ["Default"]
            while len(beacons):
                beacon = beacons.pop(0)
                for i_l, level in enumerate(level_list):
                    if level in default_level_order and level != beacon:
                        beacons.append(level)
                        break
                level_order[beacon] = [level_list.pop(i_l)]
                for _ in range(len(default_level_order[beacon])-1):
                    if level_list[0] in default_level_order:
                        beacons.append(level_list[0])
                    level_order[beacon].append(level_list.pop(0))
            self.level_order = level_order
        else:
            self.level_order = default_level_order
        self.level_beacons = {
            level: f"{beacon} Beacon" for beacon, levels in self.level_order.items()
            for level in levels}

        # Barrier types randomisation
        self.barrier_cache = {name: ArzetteLocation() for name in default_barrier_types}
        self.set_rules_barrier()
        if self.config["barrier_types"]:
            barrier_list = list(default_barrier_types)
            random.shuffle(barrier_list)
            barrier_types = {}
            for barrier in default_barrier_types:
                barrier_types[barrier] = barrier_list.pop(0)
            self.barrier_types = barrier_types
        else:
            self.barrier_types = default_barrier_types

        # Bonus scrolls randomisation
        self.location_cache = {name: ArzetteLocation() for name in all_locations}
        item_locked = []
        scroll_locations = [item for item in all_locations if "Bonus" in item.split()
                            and "Reward" not in item.split()]
        if self.config["item_pool"]["bonus_scrolls"]:
            for item in scroll_locations:
                level = item.split()[0]
                possible_locations = [
                    location for location in level_locations[level]
                    if not any(word in location for word in {"Jewel", "Beacon"}) and
                    location != "Hills Key"]
                location = random.choice(possible_locations)
                self.get_location(location).item = item
        else:
            item_locked += scroll_locations

        # NPC randomisation
        if self.config["npc"]["randomize"]:
            npc_cache = {name: ArzetteLocation() for name in all_npcs}            
            if self.config["npc"]["include_foolish"]:
                npc_list = list(set(default_npc_locations.values())) + default_npc_fool
                npc_locked = default_npc_locked
            else:
                npc_list = list(set(default_npc_locations.values()))
                npc_locked = default_npc_locked + default_npc_fool
            for npc in npc_locked:
                npc_cache[npc].item = npc
            random.shuffle(npc_list)
            for npc in npc_cache:
                if npc_cache[npc].item is not None:
                    continue
                npc_cache[npc].item = npc_list.pop(0)

            npc_locations = {}
            npc_to_location = {npc_cache[name].item: name for name in npc_cache}
            for item, npc in default_npc_locations.items():
                npc_locations[item] = npc_to_location[default_npc_locations[item]]
            self.npc_cache = npc_cache
            self.npc_locations = npc_locations
        else:
            self.npc_cache = {name: ArzetteLocation() for name in all_npcs}
            for name in self.npc_cache:
                self.npc_cache[name].item = name
            self.npc_locations = default_npc_locations
        self.set_rules_npc()

        # Item randomisation

        # Set-up item pool based on settings
        self.set_rules()

        item_locked += ["Daimur"]
        #item_locked += [item for item in all_locations if "Rock" in item.split()]
        item_locked += [item for item in all_locations if "Beacon" in item.split()]
        # item_locked += [item for item in all_locations if "Jewel" in item.split()]
        item_locked += ["Faramore Bonus Reward",
                        "Volcano Bonus Reward",
                        "Castle Bonus Reward"]

        item_list = []
        sub_item_lists = {
            "bags": [item for item in all_locations if "Bag" in item.split()],
            "keys": [item for item in all_locations if "Key" in item.split()
                     and item not in {"Dungeon Key", "Hills Key"}],
            "hills_key": ["Hills Key"],
            "candles": [item for item in all_locations if "Candle" in item.split()],
            "coins": [item for item in all_locations if "Coin" in item.split()],
            "plants": [item for item in all_locations if "Plant" in item.split()],
            "rocks": [item for item in all_locations if "Rock" in item.split()],
            "upgrades": ([item for item in all_locations if "Upgrade" in item.split()] +
                        ["Infinite Soulfire"]),
            "life_ups": [item for item in all_locations if "Life-Up" in item.split()],
            "bonus_rewards": [item for item in all_locations if "Bonus" in item.split() and
                "Reward" in item.split() and
                not any(level in item for level in ["Faramore", "Volcano", "Castle"])],
            "race_rewards": [item for item in all_locations if "Race" in item.split()],
            "jewels": [item for item in all_locations if "Jewel" in item.split()],
        }
        for option, sub_item_list in sub_item_lists.items():
            if self.config["item_pool"][option]:
                item_list += sub_item_list
            else:
                item_locked += sub_item_list

        trading_type = self.config["item_pool"]["trading_sequence"].lower()
        if trading_type not in {"included", "excluded", "vanilla"}:
            raise Exception(f"config file trading_type {trading_type} not recognised.")
        if trading_type == "included":
            item_list += trading_locations

        # Locking items in location before trading_sequence
        for item in item_locked:
            self.location_cache[item].item = item

        if trading_type == "vanilla":
            # Assuming you want to start later in the sequence
            # start_position = random.randint(0, len(trading_locations)-2)
            start_position = 0
        elif trading_type == "excluded":
            start_position = len(trading_locations)-2
        if trading_type != "included":
            if start_position != 0:
                item_locked.append(trading_locations[0])
                self.location_cache[trading_locations[start_position]].item = \
                    trading_locations[0]
            for i_s, item in enumerate(trading_locations):
                if i_s in {0, start_position}:
                    continue
                item_locked.append(item)
                self.location_cache[item].item = item
            item_list.append(trading_locations[start_position])

        core_items = [name for name in all_locations
                      if name not in item_list+item_locked+scroll_locations]
        item_list += core_items

        location_list = [name for name, location in self.location_cache.items()
                        if location.item is None]
        if len(item_list) != len(location_list):
            raise Exception("Something went wrong.")

        # Randomise item pool
        # This function is not based on the Archipelago Fill.py functions. It is a homemade algorithm, but it works.
        random.shuffle(item_list)
        random.shuffle(location_list)

        # For debugging
        all_spheres = []
        all_expanders = []
        n_spheres = -1
        while True:
            state = self.sweep()
            if "Daimur" in state.prog_items:
                n_spheres = len(all_spheres)
            current_sphere = [location for location in location_list
                            if self.get_location(location).can_reach(state)]
            all_spheres.append(current_sphere[:])
            current_expanders = {}
            for n_items in range(1, 3):
                for test_items in combinations(item_list, n_items):
                    test_state = self.sweep(extra_items=test_items)
                    test_sphere = [location for location in location_list
                                if self.get_location(location).can_reach(test_state)]
                    delta = len(test_sphere) - len(current_sphere)
                    if delta > 0:
                        if delta not in current_expanders:
                            current_expanders[delta] = []
                        current_expanders[delta].append(list(test_items))
                if len([delta for delta in current_expanders if delta > 1]):
                    break
            if n_items > len(current_sphere) or len(current_expanders) == 0:
                if state.prog_items["Daimur"]:
                    break
                if seed is None:
                    self.n_tries += 1
                    if self.n_tries < 10:
                        print(f"Seed generation failed {self.n_tries} time(s). Trying again")
                        self.fill()
                        return
                print(self.level_order)
                print(all_spheres)
                print(all_expanders)
                raise Exception("Seed generation failed.")

            expand_value = random.choice(list(current_expanders))
            all_expanders.append((expand_value, current_expanders))
            current_expander = current_expanders[expand_value][0][:]

            while len(current_sphere):
                location = current_sphere.pop(0)
                location = location_list.pop(location_list.index(location))
                if len(current_expander):
                    item = current_expander.pop(0)
                    item = item_list.pop(item_list.index(item))
                else:
                    item = item_list.pop(0)
                self.get_location(location).item = item
            if len(item_list) == 0:
                break

        print(f"{len(item_list)} unplaced items, but game is beatable.")
        print("Locations:\n\t" + "\n\t".join(location_list))
        print("Items:\n\t" + "\n\t".join(item_list))
        while len(item_list):
            item = item_list.pop(0)
            location = location_list.pop(0)
            self.get_location(location).item = item
        print("All items and locations have been filled. "
              f"Game is beatable in {n_spheres} spheres.")

    def get_location(self, location_name):
        return self.location_cache[location_name]

    def get_npc(self, location_name):
        return self.npc_cache[location_name]

    def get_barrier(self, location_name):
        return self.barrier_cache[location_name]

    def set_rules_barrier(self):
        add_rule(self.get_barrier("Red"), lambda state:
            state.has_group("magic"))

        add_rule(self.get_barrier("Blue"), lambda state:
            state.has_group("magic") and (state.has("Blue Magic") or state.has("Purple Magic")))

        add_rule(self.get_barrier("Purple"), lambda state:
            state.has_group("magic") and state.has("Purple Magic"))

        add_rule(self.get_barrier("Gauntlet"), lambda state:
            state.has("Bomb Gauntlet") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_barrier("Flute"), lambda state:
            state.has("Fatal Flute") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

    def set_rules_npc(self):
        # Level Access Rules
        for npc in self.npc_cache:
            level = npc.split()[0]
            add_rule(self.get_npc(npc), lambda state, level=level:
                state.has(self.level_beacons[level]))
            if level in ["Crypts", "Fort", "Castle", "Lair"]:
                add_rule(self.get_npc(npc), lambda state:
                    state.has("Power Pendant"))

        # Faramore Rules
        for npc in ["Faramore Kari Quest", "Faramore Barnabuss"]:
            add_rule(self.get_npc(npc), lambda state:
                 state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)") or
                 (state.has("Griffin Boots") and
                  (self.get_barrier(self.barrier_types["Red"]).access_rule(state) or
                   self.get_barrier(self.barrier_types["Blue"]).access_rule(state))))

        add_rule(self.get_npc("Faramore Maki"), lambda state:
            ((state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)")) and
             self.get_barrier(self.barrier_types["Blue"]).access_rule(state)) or
            state.has("Griffin Boots"))

        for npc in ["Faramore Payop", "Faramore Dewey"]:
            add_rule(self.get_npc(npc), lambda state:
                ((state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)")) and
                 self.get_barrier(self.barrier_types["Red"]).access_rule(state)) or
                state.has("Griffin Boots"))
        #add_rule(self.get_npc("Faramore Dewey"), lambda state:
        #    self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        for npc in ["Faramore Denny", "Faramore Cypress"]:
            add_rule(self.get_npc(npc), lambda state: state.has("Griffin Boots"))

        add_rule(self.get_npc("Faramore Rudy"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        # Forest Rules
        add_rule(self.get_npc("Forest Cypress"), lambda state:
            state.has("Forest Key") or state.has("Griffin Boots"))
        
        add_rule(self.get_npc("Forest Rudy (End)"), lambda state:
            state.has("Forest Key"))

        # Caves Rules
        add_rule(self.get_npc("Caves Ellido"), lambda state:
            state.has("Bombs") and state.has("Lantern") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        # Desert Rules
        add_rule(self.get_npc("Desert Fairy"), lambda state:
            state.has("Desert Key"))

        # Canyon Rules
        add_rule(self.get_npc("Canyon Crowdee"), lambda state:
            state.has_group("candles", 20) and state.has_group("magic"))

        for npc in ["Canyon Motte", "Canyon Odie"]:
            add_rule(self.get_npc(npc), lambda state:
                state.has_group("bombs") and state.has("Canyon Key") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))
        add_rule(self.get_npc("Canyon Odie"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) or
            state.has("Griffin Boots"))

        # Swamp Rules
        add_rule(self.get_npc("Swamp Frich"), lambda state: state.has_group("magic"))

        add_rule(self.get_npc("Swamp Glubbert"), lambda state:
            state.has_group("magic") and state.has("Swamp Key (Frich House)") and
            state.has("Golden Fly"))  # This is only because Frich is locked for now

        # Peak Rules
        add_rule(self.get_npc("Peak Ciclena"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            state.has_group("magic") and state.has("Peak Key"))

        add_rule(self.get_npc("Peak Rudy (End)"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            state.has_group("magic"))

        # Crypts Rules
        add_rule(self.get_npc("Crypts Skelvis"), lambda state:
            state.has_group("magic") and state.has("Crypts Key") and
            state.has("Lantern") and state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        # Beach Rules
        add_rule(self.get_npc("Beach Fleetus"), lambda state:
            state.has("Beach Key (First House)") and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
            state.has_group("magic") and state.has("Blue Magic"))

        add_rule(self.get_npc("Beach Tork"), lambda state:
            state.has("Beach Key (First House)") and
            state.has("Beach Key (Tork Cabin)") and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
            state.has_group("magic") and state.has("Blue Magic"))

        # River Rules
        add_rule(self.get_npc("River Francine"), lambda state:
            state.has("River Key (Francine)"))

        add_rule(self.get_npc("River Barnabuss"), lambda state:
            state.has_group("magic"))
        
        add_rule(self.get_npc("River Morgh"), lambda state:
            state.has_group("magic") and state.has("Lantern") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            (state.has("Blue Magic") or state.has("Shield Ring")) and
            state.has("River Key (Submarine)"))

        # Hills Rules
        for npc in ["Hills Rudy (End)", "Hills Milbert"]:
            add_rule(self.get_npc(npc), lambda state:
                state.has("Blue Magic") and state.has_group("magic") and
                    (state.has("Griffin Boots") or state.has("Winged Belt")))

        add_rule(self.get_npc("Hills Milbert"), lambda state:
            state.has("Hills Key") and state.has("Fatal Flute"))

    def set_rules(self):
        # Level Access Rules
        for level, locations in self.level_locations.items():
            for item in locations:
                add_rule(self.get_location(item), lambda state, level=level:
                    state.has(self.level_beacons[level]))
                if level in ["Crypts", "Fort", "Castle", "Lair"]:
                    add_rule(self.get_location(item), lambda state:
                        state.has("Power Pendant"))

        # Rocks Rules
        for item in rock_locations:
            add_rule(self.get_location(item), lambda state:
                self.get_npc(self.npc_locations["Rope Upgrade"]).access_rule(state) and
                self.get_npc(self.npc_locations["Rope"]).access_rule(state))

        add_rule(self.get_location("Orange Rock"), lambda state:
            state.has(self.level_beacons["Caves"]) and
            state.has("Bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Brown Rock"), lambda state:
            state.has(self.level_beacons["Canyon"]) or
            (state.has(self.level_beacons["Lair"]) and
             state.has("Power Pendant") and state.has_group("magic") and
             state.has("Blue Magic") and state.has("Lantern") and
             (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
             self.get_barrier(self.barrier_types["Purple"]).access_rule(state)))

        add_rule(self.get_location("Gray Rock"), lambda state:
            (state.has(self.level_beacons["Peak"]) and
             self.get_barrier(self.barrier_types["Red"]).access_rule(state)) or
            (state.has(self.level_beacons["Fort"]) and
             state.has("Power Pendant")))

        add_rule(self.get_location("Blue Rock"), lambda state:
            state.has("Beach Key (First House)") and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
            state.has_group("magic") and state.has("Blue Magic"))

        # Bonus Rewards Rules
        for item in [location for location in self.location_cache
                if "Bonus" in location.split() and "Reward" in location.split()]:
            level = item.split()[0]
            parent = f"{level} Bonus"
            add_rule(self.get_location(item), lambda state, parent=parent:
                state.has(parent))
            if level in ["Desert", "Swamp", "Fort"]:
                add_rule(self.get_location(item), lambda state:
                    state.has("Lantern") and
                    (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))
            if level in ["Hills"]:
                add_rule(self.get_location(item), lambda state:
                    state.has("Griffin Boots"))  # Not 100% required but hard without it

        # Faramore Rules
        add_rule(self.get_location("Rope Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Rope Upgrade"]).access_rule(state) and
            state.has_group("rocks", 4) and
            state.has("Rope") and state.has(self.level_beacons["Swamp"]))

        add_rule(self.get_location("Purple Magic"), lambda state:
            self.get_npc(self.npc_locations["Purple Magic"]).access_rule(state) and
            state.has_group("jewels", 5))

        add_rule(self.get_location("Citizenship Papers"), lambda state:
            self.get_npc(self.npc_locations["Citizenship Papers"]).access_rule(state) and
            self.get_npc(self.npc_locations["Lantern"]).access_rule(state))

        add_rule(self.get_location("Faramore Key (Well)"), lambda state:
            state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)") or
            state.has("Griffin Boots"))

        add_rule(self.get_location("Power Stone Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Power Stone Upgrade"]).access_rule(state) and
            state.has("Bell") and state.has(self.level_beacons["Castle"]) and
            state.has("Bomb Gauntlet"))

        add_rule(self.get_location("Dungeon Key"), lambda state:
            self.get_npc(self.npc_locations["Dungeon Key"]).access_rule(state))

        add_rule(self.get_location("Chainsword"), lambda state:
            self.get_npc(self.npc_locations["Chainsword"]).access_rule(state) and
            state.has("Oil and Chains"))

        add_rule(self.get_location("Canteen"), lambda state:
            self.get_npc(self.npc_locations["Canteen"]).access_rule(state) and
            state.has("Star Earrings"))

        add_rule(self.get_location("Wallet Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Wallet Upgrade"]).access_rule(state) and
            self.get_npc("Swamp Frich").access_rule(state) and
            state.has("Golden Fly") and
            state.has("Silver Cricket") and state.has(self.level_beacons["Volcano"]))

        add_rule(self.get_location("Infinite Soulfire"), lambda state:
            self.get_npc(self.npc_locations["Infinite Soulfire"]).access_rule(state) and
            state.has_group("races", 3))

        for item in ["Faramore Bonus", "Faramore Candle (Empty House)"]:
            add_rule(self.get_location(item), lambda state:
                ((state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)")) and
                 self.get_barrier(self.barrier_types["Blue"]).access_rule(state)) or
                state.has("Griffin Boots"))

        add_rule(self.get_location("Bomb Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Bomb Upgrade"]).access_rule(state) and
            state.has("Griffin Boots") and state.has(self.level_beacons["Hills"]) and
            state.has("Compass"))

        add_rule(self.get_location("200 Rupees"), lambda state:
            self.get_npc(self.npc_locations["200 Rupees"]).access_rule(state) and
            state.has("Rope Ladder"))

        add_rule(self.get_location("Lamp Oil Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Lamp Oil Upgrade"]).access_rule(state) and
            state.has("Lantern") and state.has_group("plants", 3) and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            state.has(self.level_beacons["Swamp"]) and
            self.get_npc(self.npc_locations["Lantern"]).access_rule(state) and
            state.has("Citizenship Papers"))

        add_rule(self.get_location("Faramore Coin"), lambda state:
            ((state.has("Faramore Key (Well)") or state.has("Faramore Key (Tavern)")) and
             self.get_barrier(self.barrier_types["Red"]).access_rule(state)) or
            state.has("Griffin Boots"))
        add_rule(self.get_location("Faramore Coin"), lambda state:
            (state.has("Griffin Boots") and state.has("Winged Belt")) or
            self.get_barrier(self.barrier_types["Purple"]).access_rule(state))
    
        add_rule(self.get_location("Calendar"), lambda state:
            self.get_npc(self.npc_locations["Calendar"]).access_rule(state) and
            state.has("Castle Jewel"))

        add_rule(self.get_location("Faramore Candle (Cypress House)"), lambda state:
            state.has("Griffin Boots") and
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        # Forest Rules
        for item in ["Forest Coin", "Forest Bag (Sword Wave)", "Golden Fly", "Sword Wave",
                "Forest Bag (Last Room)", "Forest Beacon", "Forest Jewel", "Magic Armor"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Forest Key") or state.has("Griffin Boots"))
        add_rule(self.get_location("Golden Fly"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Red"]).access_rule(state))
        add_rule(self.get_location("Forest Jewel"), lambda state:
            state.has_group("candles", 17))
        add_rule(self.get_location("Magic Armor"), lambda state:
            state.has_group("candles", 20) and
            self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))
        add_rule(self.get_location("Sword Wave", "Forest Bag (Sword Wave)"), lambda state:
            state.has("Lantern") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Forest Bonus"), lambda state:
            state.has("Forest Key"))

        add_rule(self.get_location("Forest Candle (Tree)"), lambda state:
            state.has("Forest Key") and
            self.get_barrier(self.barrier_types["Red"]).access_rule(state))

        add_rule(self.get_location("Forest Candle (Cypress)"), lambda state:
            state.has("Griffin Boots"))

        add_rule(self.get_location("Lantern"), lambda state:
            self.get_npc(self.npc_locations["Lantern"]).access_rule(state) and
            state.has("Citizenship Papers"))

        add_rule(self.get_location("Forest Race 100 Rupees"), lambda state:
            self.get_npc(self.npc_locations["Forest Race 100 Rupees"]).access_rule(state) and
            state.has_group("coins", 1) and
            self.get_npc("Forest Rudy (Start)").access_rule(state) and
            self.get_npc("Forest Rudy (End)").access_rule(state))

        # Caves Rules
        add_rule(self.get_location("Rope"), lambda state:
            self.get_npc(self.npc_locations["Rope"]).access_rule(state))

        for item in ["Silver Cricket", "Rope Ladder", "Caves Bag (Rope Ladder)",
                "Caves Candle (First Dark Room)", "Caves Coin",
                "Caves Candle (Second Dark Room)", "Caves Bonus", "Shield Ring",
                "Caves Bag (Last Room)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Bombs") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Caves Candle (First Dark Room)", "Caves Coin",
                "Caves Candle (Second Dark Room)", "Caves Bonus", "Shield Ring",
                "Caves Bag (Last Room)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))
        
        for item in ["Silver Cricket", "Rope Ladder", "Caves Bag (Rope Ladder)"]:
            add_rule(self.get_location(item), lambda state:
                     self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        for item in ["Rope Ladder", "Caves Bag (Rope Ladder)"]:
            add_rule(self.get_location(item), lambda state:
                     self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        add_rule(self.get_location("Caves Candle (First Dark Room)"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state))

        add_rule(self.get_location("Caves Coin"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        add_rule(self.get_location("Snail Salt"), lambda state:
            self.get_npc(self.npc_locations["Snail Salt"]).access_rule(state) and
            state.has("Funky Fungus"))

        # Desert Rules
        add_rule(self.get_location("Desert Key"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Desert Key", "Desert Candle (Last Room)", "Desert Life-Up",
                "Desert Bag (Last Room)", "Desert Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Desert Candle (Last Room)", "Desert Life-Up",
                "Desert Bag (Last Room)", "Desert Beacon"]:
            add_rule(self.get_location(item), lambda state: state.has("Desert Key"))

        add_rule(self.get_location("Fairy Dust"), lambda state:
            self.get_npc(self.npc_locations["Fairy Dust"]).access_rule(state))

        add_rule(self.get_location("Desert Candle (Last Room)"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        add_rule(self.get_location("Desert Life-Up"), lambda state:
            state.has_group("candles", 20))

        add_rule(self.get_location("Desert Beacon"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) or
            state.has("Griffin Boots"))

        # Canyon Rules
        add_rule(self.get_location("Canyon Bonus"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state))

        add_rule(self.get_location("Canyon Candle (First Room End)"), lambda state:
            (state.has("Speedy Shoes") and state.has("Winged Belt")) or
            state.has("Griffin Boots"))

        add_rule(self.get_location("Canyon Jewel"), lambda state:
            state.has_group("candles", 20) and state.has_group("magic"))

        add_rule(self.get_location("Backstep"), lambda state:
            self.get_npc(self.npc_locations["Backstep"]).access_rule(state) and
            state.has("Canyon Jewel"))

        for item in ["Canyon Key", "Canyon Bag (After Zipline 1)",
                "Canyon Bag (After Zipline 2)", "Canyon Bag (After Zipline 3)",
                "Canyon Coin", "Canyon Bag (Motte House)", "Canyon Candle (Motte House)"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("bombs") and state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))
        
        add_rule(self.get_location("Canyon Candle (Motte House)"), lambda state:
            state.has("Canyon Key") and
            (self.get_barrier(self.barrier_types["Red"]).access_rule(state) or
             state.has("Griffin Boots")) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        add_rule(self.get_location("Star Earrings"), lambda state:
            self.get_npc(self.npc_locations["Star Earrings"]).access_rule(state))

        add_rule(self.get_location("Smart Gun"), lambda state:
            self.get_npc(self.npc_locations["Smart Gun"]).access_rule(state) and
            state.has("Fairy Dust"))

        # Swamp Rules
        for item in ["Swamp Candle (First Room)", "Swamp Bag (First Room)", "Swamp Coin",
                "Swamp Key (Frich House)", "Swamp Candle (Frich House)",
                "Swamp Key (Griffin Boots)", "Griffin Boots", "Swamp Plant",
                "Swamp Bonus", "Swamp Beacon"]:
            add_rule(self.get_location(item), lambda state: state.has_group("magic"))

        for item in ["Swamp Candle (First Room)", "Swamp Bag (First Room)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Griffin Boots"))

        for item in ["Swamp Coin", "Swamp Key (Frich House)", "Swamp Candle (Frich House)",
                "Swamp Key (Griffin Boots)", "Griffin Boots", "Swamp Plant",
                "Swamp Bonus", "Swamp Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Golden Fly"))  # This is only because Frich is locked for now

        for item in ["Swamp Candle (Frich House)", "Swamp Key (Griffin Boots)",
                "Griffin Boots", "Swamp Plant", "Swamp Bonus", "Swamp Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Swamp Key (Frich House)"))

        add_rule(self.get_location("Swamp Key (Griffin Boots)"), lambda state:
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        for item in ["Griffin Boots", "Swamp Plant", "Swamp Bonus"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Swamp Key (Griffin Boots)") or
                self.get_barrier(self.barrier_types["Red"]).access_rule(state))

        add_rule(self.get_location("Swamp Beacon"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Ogre Hair"), lambda state:
            self.get_npc(self.npc_locations["Ogre Hair"]).access_rule(state) and
            state.has("Cleaver Shovel"))

        # Peak Rules
        for item in ["Peak Candle (First Cave)", "Peak Bag (First Cave 1)",
                "Peak Bag (First Cave 2)", "Peak Bonus", "Peak Coin", "Peak Key",
                "Peak Candle (Ciclena Cave)", "Peak Bag (Before Apatu)",
                "Peak Jewel", "Peak Bag (After Apatu)"]:
            add_rule(self.get_location(item), lambda state:
                self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
                state.has_group("magic"))
        
        add_rule(self.get_location("Peak Candle (First Cave)"), lambda state:
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        add_rule(self.get_location("Peak Coin"), lambda state:
            self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        add_rule(self.get_location("Peak Candle (Ciclena Cave)"), lambda state:
            state.has("Peak Key") and state.has("Griffin Boots"))

        for item in ["Peak Jewel", "Peak Bag (After Apatu)"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("candles", 20))

        add_rule(self.get_location("Peak Bag (After Apatu)"), lambda state:
            state.has("Peak Jewel"))

        add_rule(self.get_location("Power Pendant"), lambda state:
            self.get_npc(self.npc_locations["Power Pendant"]).access_rule(state) and
            state.has("Crystal of Refraction"))

        add_rule(self.get_location("Peak Race 100 Rupees"), lambda state:
            self.get_npc(self.npc_locations["Peak Race 100 Rupees"]).access_rule(state) and
            state.has_group("coins", 5) and
            state.has(self.level_beacons["Peak"]) and
            self.get_npc("Peak Rudy (Start)").access_rule(state) and
            self.get_npc("Peak Rudy (End)").access_rule(state) and
            state.has(self.level_beacons["Forest"]) and
            self.get_npc("Forest Rudy (Start)").access_rule(state) and
            self.get_npc("Forest Rudy (End)").access_rule(state))

        # Crypts Rules
        for item in ["Crypts Life-Up", "Bell", "Crypts Bonus", "Crypts Key",
                "Crypts Candle (After Crypt)", "Crypts Coin",
                "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("magic"))

        add_rule(self.get_location("Crypts Life-Up"), lambda state:
            state.has_group("bombs") and state.has_group("candles", 20) and
            state.has("Griffin Boots") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Bell"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
            (state.has_group("candles", 20) and state.has("Griffin Boots")))

        for item in ["Crypts Bonus", "Crypts Key",
                "Crypts Candle (After Crypt)", "Crypts Coin",
                "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Crypts Candle (After Crypt)", "Crypts Coin",
                "Crypts Candle (Skelvis)", "Crypts Bag (Skelvis)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Crypts Key"))
        
        add_rule(self.get_location("Crypts Candle (After Crypt)"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        add_rule(self.get_location("Crypts Coin"), lambda state:
            self.get_barrier(self.barrier_types["Flute"]).access_rule(state) and
            self.barrier_types["Flute"] == "Flute")

        add_rule(self.get_location("Crypts Candle (Skelvis)"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        add_rule(self.get_location("Crypts Bag (Skelvis)"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
            self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))

        add_rule(self.get_location("Bomb Gauntlet"), lambda state:
            self.get_npc(self.npc_locations["Bomb Gauntlet"]).access_rule(state))

        # Volcano Rules
        add_rule(self.get_location("Volcano Bonus"), lambda state:
            self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))

        for item in ["Volcano Candle (First Room)", "Volcano Coin",
                "Volcano Candle (Last Room)", "Crystal of Refraction"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("magic"))

        add_rule(self.get_location("Volcano Coin"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        # Beach Rules
        for item in ["Beach Coin", "Beach Key (First House)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Griffin Boots") or state.has("Winged Belt"))
        add_rule(self.get_location("Beach Coin"), lambda state:
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        for item in ["Beach Key (Tork Cabin)", "Beach Candle (Tork Cabin)", "Beach Plant",
                "Beach Bonus", "Beach Candle (Cave)", "Fatal Flute", "Beach Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Beach Key (First House)") and
                self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
                state.has_group("magic") and state.has("Blue Magic"))

        add_rule(self.get_location("Beach Key (Tork Cabin)"), lambda state:
            state.has("Griffin Boots") or
            ((state.has("Smart Gun") or state.has("Sword Wave") or
              (state.has("Bombs") and
               (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))) and
             (state.has("Winged Belt") or state.has("Speedy Shoes"))))

        add_rule(self.get_location("Speedy Shoes"), lambda state:
            self.get_npc(self.npc_locations["Speedy Shoes"]).access_rule(state))

        add_rule(self.get_location("Beach Candle (Tork Cabin)"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        for item in ["Beach Plant", "Beach Bonus"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Beach Key (Tork Cabin)"))

        add_rule(self.get_location("Beach Candle (Cave)"), lambda state:
            self.get_barrier(self.barrier_types["Flute"]).access_rule(state))

        add_rule(self.get_location("Fatal Flute"), lambda state:
            state.has_group("bombs") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Beach Beacon"), lambda state:
            state.has("Griffin Boots") or state.has("Smart Gun") or
            state.has("Sword Wave") or state.has("Winged Belt"))

        add_rule(self.get_location("Magic Cloak"), lambda state:
            self.get_npc(self.npc_locations["Magic Cloak"]).access_rule(state) and
            state.has("Calendar"))

        # River Rules
        add_rule(self.get_location("River Bonus"), lambda state:
            state.has("River Key (Francine)"))

        add_rule(self.get_location("River Key (Francine)"), lambda state:
            state.has_group("magic"))

        add_rule(self.get_location("Cleaver Shovel"), lambda state:
            self.get_npc(self.npc_locations["Cleaver Shovel"]).access_rule(state) and
            state.has("Snail Salt"))

        add_rule(self.get_location("River Candle (Boat)"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        for item in ["River Candle (Boat)", "River Key (Submarine)", "River Coin",
                "Blue Magic", "River Bag (Last Room)", "River Candle (Last Room)",
                "River Life-Up"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("magic"))
        add_rule(self.get_location("River Key (Submarine)"), lambda state:
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))
        add_rule(self.get_location("River Coin"), lambda state:
            self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        for item in ["River Key (Submarine)", "River Coin",
                "Blue Magic", "River Bag (Last Room)", "River Candle (Last Room)",
                "River Life-Up"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Blue Magic", "River Bag (Last Room)",
                     "River Candle (Last Room)", "River Life-Up"]:
            add_rule(self.get_location(item), lambda state:
                self.get_barrier(self.barrier_types["Red"]).access_rule(state))

        for item in ["River Bag (Last Room)",
                     "River Candle (Last Room)", "River Life-Up"]:
            add_rule(self.get_location(item), lambda state:
                (state.has("Blue Magic") or state.has("Shield Ring")) and
                state.has("River Key (Submarine)"))
        add_rule(self.get_location("River Candle (Last Room)"), lambda state:
            state.has("Griffin Boots"))
        add_rule(self.get_location("River Life-Up"), lambda state:
            state.has_group("candles", 20))

        add_rule(self.get_location("Oil and Chains"), lambda state:
            self.get_npc(self.npc_locations["Oil and Chains"]).access_rule(state) and
            state.has("Ogre Hair"))

        # Hills Rules
        for item in ["Hills Candle (Cave)", "Lightning Sword"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("bombs") and state.has("Lantern") and
                state.has_group("magic") and
                (state.has("Blue Magic") or state.has("Griffin Boots") or
                 state.has("Winged Belt")) and
                 (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))
        add_rule(self.get_location("Lightning Sword"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))
        
        for item in ["Hills Coin", "Hills Bonus", "Hills Bag (Barn)", "Hills Key",
                "Hills Bag (Music Shrine)", "Hills Candle (Music Shrine)", "Hills Plant",
                "Hills Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Blue Magic") and state.has_group("magic") and
                (state.has("Griffin Boots") or state.has("Winged Belt")))

        add_rule(self.get_location("Hills Coin"), lambda state:
            self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        for item in ["Hills Bag (Barn)", "Hills Key", "Hills Bag (Music Shrine)",
                "Hills Candle (Music Shrine)"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("bombs") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Hills Plant", "Hills Beacon"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Hills Key") and state.has("Fatal Flute"))

        add_rule(self.get_location("Double Wave"), lambda state:
            self.get_npc(self.npc_locations["Double Wave"]).access_rule(state) and
            state.has("Sword Wave"))

        add_rule(self.get_location("Hills Race 100 Rupees"), lambda state:
            self.get_npc(self.npc_locations["Hills Race 100 Rupees"]).access_rule(state) and
            state.has_group("coins", 10) and
            state.has(self.level_beacons["Hills"]) and
            self.get_npc("Hills Rudy (Start)").access_rule(state) and
            self.get_npc("Hills Rudy (End)").access_rule(state) and
            state.has(self.level_beacons["Peak"]) and
            self.get_npc("Peak Rudy (Start)").access_rule(state) and
            self.get_npc("Peak Rudy (End)").access_rule(state) and
            state.has(self.level_beacons["Forest"]) and
            self.get_npc("Forest Rudy (Start)").access_rule(state) and
            self.get_npc("Forest Rudy (End)").access_rule(state))

        # Fort Rules
        for item in ["Fort Bag (Dungeon 1)", "Fort Bag (Dungeon 2)", "Fort Bag (Dungeon 3)",
                "Fort Bag (Dungeon 4)", "Sacred Oil"]:
            add_rule(self.get_location(item), lambda state: state.has("Dungeon Key"))

        for item in ["Fort Bag (Dungeon 1)", "Fort Bag (Dungeon 2)", "Fort Bag (Dungeon 3)",
                "Fort Bag (Dungeon 4)", "Sacred Oil", "Fort Candle (Dark Room)",
                "Fort Bag (Dark Room)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        for item in ["Fort Key (First Room)", "Enchanted Shoes", "Fort Coin", "Fort Key (Top Room)",
                "Fort Bag (Top Room 1)", "Fort Bag (Top Room 2)", "Fort Bag (Top Room 3)",
                "Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
                "Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state: state.has_group("magic"))

        add_rule(self.get_location("Enchanted Shoes"), lambda state:
            self.get_barrier(self.barrier_types["Flute"]).access_rule(state))

        for item in ["Enchanted Shoes", "Fort Coin", "Fort Key (Top Room)"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Blue Magic"))

        for item in ["Enchanted Shoes", "Fort Coin", "Fort Key (Top Room)",
                "Fort Bag (Top Room 1)", "Fort Bag (Top Room 2)", "Fort Bag (Top Room 3)",
                "Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
                "Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Griffin Boots"))

        for item in ["Fort Bag (Top Room 1)", "Fort Bag (Top Room 2)", "Fort Bag (Top Room 3)",
                "Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
                "Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Blue Magic") or state.has("Shield Ring"))

        for item in ["Fort Candle (Last Room)", "Fort Bag (Last Room)", "Reflector Ring",
                "Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Fort Key (Top Room)") and
                self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        for item in ["Fort Bag (Last Room)", "Reflector Ring",
                "Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state:
                self.get_barrier(self.barrier_types["Red"]).access_rule(state))
        add_rule(self.get_location("Reflector Ring"), lambda state:
            self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))

        for item in ["Fort Jewel", "Fort Bonus"]:
            add_rule(self.get_location(item), lambda state:
                 state.has_group("candles", 20))

        add_rule(self.get_location("Fort Bonus"), lambda state:
            state.has("Fort Jewel"))

        # Castle Rules
        add_rule(self.get_location("Castle Bag (Entrance)"), lambda state:
            state.has("Griffin Boots"))

        for item in ["Castle Candle (Right Room)",
                "Castle Key (Nodelki)", "Castle Candle (Top Room)", "Castle Bag (Top Room)",
                "Winged Belt", "Castle Coin", "Castle Key (Left Room)", "Castle Bag (Bonus)",
                "Castle Bonus", "Castle Jewel"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("magic") and state.has("Blue Magic") and
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Castle Candle (Right Room)"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
            self.get_barrier(self.barrier_types["Blue"]).access_rule(state))

        add_rule(self.get_location("Castle Key (Nodelki)"), lambda state:
            (self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
             (state.has("Griffin Boots") or (
                self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
                state.has_group("bombs") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])) and
                self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state)))
            ) or
            (self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
             state.has("Griffin Boots") and
             self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state)))

        add_rule(self.get_location("Castle Candle (Top Room)"), lambda state:
            self.get_barrier(self.barrier_types["Red"]).access_rule(state) or
            (self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
             self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state)))

        for item in ["Castle Bag (Top Room)", "Castle Jewel"]:
            add_rule(self.get_location(item), lambda state:
                (self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
                (state.has("Griffin Boots") or
                self.get_barrier(self.barrier_types["Blue"]).access_rule(state)) and
                ((state.has_group("bombs") and
                  (state.has_group("bags") or state.has(self.level_beacons["Faramore"]))) or
                 self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))
                ) or
                (self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
                state.has("Griffin Boots")))

        for item in ["Winged Belt", "Castle Coin", "Castle Key (Left Room)",
                "Castle Bag (Bonus)", "Castle Bonus"]:
            add_rule(self.get_location(item), lambda state:
                self.get_barrier(self.barrier_types["Blue"]).access_rule(state) and
                ((self.get_barrier(self.barrier_types["Red"]).access_rule(state) and
                  ((state.has_group("bombs") and
                    (state.has_group("bags") or state.has(self.level_beacons["Faramore"]))) or
                   self.get_barrier(self.barrier_types["Gauntlet"]).access_rule(state))) or
                state.has("Griffin Boots")))
        add_rule(self.get_location("Winged Belt"), lambda state:
            (state.has("Griffin Boots") or state.has("Winged Belt")) and
            state.has_group("candles", 20) and
            self.get_barrier(self.barrier_types["Flute"]).access_rule(state))

        add_rule(self.get_location("Castle Jewel"), lambda state:
            state.has_group("candles", 20) and
            state.has("Castle Key (Nodelki)"))

        add_rule(self.get_location("Castle Bonus"), lambda state:
            (state.has("Griffin Boots") or state.has("Winged Belt")) and
            self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        # Lair Rules
        add_rule(self.get_location("Funky Fungus"), lambda state:
            self.get_npc(self.npc_locations["Funky Fungus"]).access_rule(state) and
            state.has("Sacred Oil"))
        add_rule(self.get_location("Soul Upgrade"), lambda state:
            self.get_npc(self.npc_locations["Soul Upgrade"]).access_rule(state) and
            state.has("Sacred Oil") and state.has("Smart Gun"))

        for item in ["Lair Candle (Tree Trunk)", "Lair Candle (Tree Top)"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("bombs") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Lair Candle (Tree Top)"), lambda state:
            state.has("Griffin Boots") and
            (self.get_barrier(self.barrier_types["Flute"]).access_rule(state) or
             (self.get_barrier(self.barrier_types["Purple"]).access_rule(state) and
              state.has("Speedy Shoes"))))

        for item in ["Lair Bonus",
                "Lair Bag (First Room)", "Lair Coin", "Lair Bag (Lava Room)",
                "Lair Bag (Final Room 1)", "Lair Bag (Final Room 2)",
                "Lair Bag (Final Room 3)", "Daimur"]:
            add_rule(self.get_location(item), lambda state:
                state.has_group("magic") and state.has("Blue Magic") and
                self.get_barrier(self.barrier_types["Purple"]).access_rule(state))

        for item in ["Lair Bonus", "Lair Coin"]:
            add_rule(self.get_location(item), lambda state:
                state.has("Griffin Boots"))
        add_rule(self.get_location("Lair Coin"), lambda state:
            state.has("Lantern") and
            (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        add_rule(self.get_location("Lair Bag (First Room)"), lambda state:
            state.has("Griffin Boots") or state.has("Winged Belt"))

        for item in ["Lair Bag (Lava Room)",
                "Lair Bag (Final Room 1)", "Lair Bag (Final Room 2)",
                "Lair Bag (Final Room 3)", "Daimur"]:
            add_rule(self.get_location(item), lambda state:
                (state.has("Griffin Boots") or state.has("Winged Belt")) and
                state.has("Lantern") and
                (state.has_group("bags") or state.has(self.level_beacons["Faramore"])))

        # The jewels rule is not in vanilla game and should be added
        add_rule(self.get_location("Daimur"), lambda state:
            state.has("Purple Magic") and state.has_group("jewels", 5))

    def sweep(self, extra_items=None):
        if extra_items is None:
            extra_items = []
        state = ArzetteCollectionState(self)
        for item in extra_items:
            state.collect(item)
        collection_flag = True
        collected_items = []
        while collection_flag:
            collection_flag = False
            for name in all_locations:
                location = self.get_location(name)
                if (location.can_reach(state) and location.item is not None and
                        location.item not in collected_items):
                    state.collect(location.item)
                    collected_items.append(location.item)
                    collection_flag = True
        return state

    def print(self, save_path="randomizer.csv", sphere_path=None):
        with open("vanilla.csv", "r") as csvfile:
            vanilla_output = [row for row in csv.reader(csvfile, delimiter=",")]

        variable_dictionary = {}
        for i_r, row in enumerate(vanilla_output):
            if (i_r == 0 or row[0] == "" or row[0].startswith("[") or
                    (row[1].startswith("world_") and row[1].endswith("_unlocked"))):
                continue
            if row[0] in variable_dictionary:
                raise Exception("Cannot import vanilla.csv")
            variable_dictionary[row[0]] = row[1].split("//")[0]

        level_unlocks = {}
        for beacon, levels in self.level_order.items():
            if beacon != "Default":
                beacon = f"{beacon}_Beacon"
            for i_u, level in enumerate(levels):
                level = level_names[level].lower().replace(" ", "_")
                level_unlocks[f"{beacon}_{i_u+1}"] = f"world_{level}_unlocked"

        location_dict = {}
        for name, barrier in self.barrier_types.items():
            key = f"{name}_Barrier"
            if key in location_dict:
                raise Exception(f"Multiple key {key}")
            value = variable_dictionary[f"{barrier}_Barrier"]
            location_dict[key] = value
        for name in all_npcs:
            key = name.replace(" ", "_")
            npc = self.get_npc(name).item
            if npc is None:
                raise Exception(f"NPC {name} not assigned")
            value = variable_dictionary[npc.replace(" ", "_")]
            if key in location_dict:
                raise Exception(f"Multiple key {key}")
            location_dict[key] = value
        for location in all_locations:
            key = location.replace(" ", "_")
            item = self.get_location(location).item
            if item is None:
                raise Exception(f"Location {location} not assigned")
            value = variable_dictionary[item.replace(" ", "_")]
            location_dict[key] = value

        output = []
        for i_r, row in enumerate(vanilla_output):
            if (i_r == 0 or row[0] == "" or row[0].startswith("[")):
                output.append(row)
                if row[0].startswith("[WORLD UNLOCKS]"):
                    for key, value in level_unlocks.items():
                        output.append([key, value])
                continue
            if (row[1].startswith("world_") and row[1].endswith("_unlocked")):
                continue
            value = location_dict[row[0]]
            output.append([row[0], value])

        with open(save_path, "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            for row in output:
                writer.writerow(row)

        # Prints a collection document for testing
        if not sphere_path:
            return

        state = ArzetteCollectionState(self)
        for item in starting_locations:
            state.collect(item)

        all_spheres = [[{"item": self.get_location(name).item,
                         "location": name, "expander": True}
                        for name in starting_locations]]

        while True:
            collected_items = [collect["item"] for sphere in all_spheres for collect in sphere]
            current_sphere = []
            for name in all_locations:
                location = self.get_location(name)
                if (location.can_reach(state) and location.item not in collected_items):
                    current_sphere.append(
                        {"item": location.item, "location": name, "expander": False})

            for collect in current_sphere:
                test_state = state.copy()
                test_state.collect(collect["item"])
                test_sphere = [name for name in all_locations
                               if (self.get_location(name).can_reach(test_state) and
                                   self.get_location(name).item not in collected_items)]
                if len(test_sphere) > len(current_sphere):
                    collect["expander"] = True

            all_spheres.append(current_sphere)
            for collect in current_sphere:
                state.collect(collect["item"])
            if "Daimur" in [collect["item"] for collect in current_sphere]:
                break
            if len(current_sphere) == 0:
                raise Exception("Something went wrong")

        output = [f"seed: {self.seed}"]
        for i_s, sphere in enumerate(all_spheres):
            output.append(" "*28+f"[SPHERE {i_s}]")
            for collect in sphere:
                if collect["expander"]:
                    output.append(f"*{collect['item']:31s} in  {collect['location']}")
                else:
                    output.append(f"{collect['item']:32s} in  {collect['location']}")
        output = "\n".join(output)
        print(output)

        with open(sphere_path, "w") as file:
            file.write(output)


class ArzetteCollectionState():
    def __init__(self, parent: ArzetteWorld):
        self.prog_items = {item: 0 for item in parent.location_cache}
        self.multiworld = parent

    def has(self, item: str) -> bool:
        return self.prog_items[item] >= 1

    def has_group(self, item_name_group: str, count: int = 1) -> bool:
        found = 0
        player_prog_items = self.prog_items
        for item_name in self.multiworld.item_name_groups[item_name_group]:
            found += player_prog_items[item_name]
            if found >= count:
                return True
        return False

    def collect(self, item):
        self.prog_items[item] += 1

    def copy(self):
        ret = ArzetteCollectionState(self.multiworld)
        ret.prog_items = copy.deepcopy(self.prog_items)
        return ret

if __name__ == "__main__":
    world = ArzetteWorld()
    world.fill()
    world.print(sphere_path="spheres.txt")
