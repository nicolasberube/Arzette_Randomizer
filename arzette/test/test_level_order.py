import typing
from ..items import bag_items
from ..locations import all_levels
from ..options import LevelOrder, ShuffleBags, ShuffleBeacons
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestVanillaLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "level_order": LevelOrder.option_vanilla,
        "shuffle_bags": ShuffleBags.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_vanilla_order(self) -> None:
        assert self.world.level_order["Default Beacon"] == ["Faramore", "Forest"]
        assert self.world.level_beacons["Faramore"] == "Default Beacon"
        assert self.world.level_beacons["Forest"] == "Default Beacon"

    def test_local_early_items(self) -> None:
        assert not any(name in bag_items for name in self.multiworld.local_early_items[self.player])

    def test_slot_data(self) -> None:
        universal_tracker_info = self.slot_data["universal_tracker_info"]
        assert universal_tracker_info["level_order"]["Default Beacon"] == ["Faramore", "Forest"]
        assert universal_tracker_info["level_beacons"]["Faramore"] == "Default Beacon"
        assert universal_tracker_info["level_beacons"]["Forest"] == "Default Beacon"
        assert universal_tracker_info["progression_bag"] is None

class TestFaramoreStartShuffleLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "level_order": LevelOrder.option_faramore_start_shuffle,
        "shuffle_bags": ShuffleBags.option_true,
        "shuffle_beacons": ShuffleBeacons.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_faramore_starting(self) -> None:
        assert "Faramore" in self.world.level_order["Default Beacon"]
        assert self.world.level_beacons["Faramore"] == "Default Beacon"

    def test_local_early_items(self) -> None:
        assert not any(name in bag_items for name in self.multiworld.local_early_items[self.player])

    def test_slot_data(self) -> None:
        universal_tracker_info = self.slot_data["universal_tracker_info"]
        assert "Faramore" in universal_tracker_info["level_order"]["Default Beacon"]
        assert universal_tracker_info["level_beacons"]["Faramore"] == "Default Beacon"
        assert universal_tracker_info["progression_bag"] is None

class TestShuffleLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "level_order": LevelOrder.option_shuffle,
        "shuffle_bags": ShuffleBags.option_true,
        "shuffle_beacons": ShuffleBeacons.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_local_early_items(self) -> None:
        progression_bag = self.world.progression_bag
        assert progression_bag in bag_items
        assert self.multiworld.local_early_items[self.player].get(progression_bag) == 1
        assert sum(1 for name in self.multiworld.local_early_items[self.player] if name in bag_items) == 1

        prog_bags = [
            item for item in self.multiworld.itempool
            if item.name in bag_items and item.advancement
        ]
        assert len(prog_bags) == 1
        assert prog_bags[0].name == progression_bag

    def test_slot_data(self) -> None:
        universal_tracker_info = self.slot_data["universal_tracker_info"]
        level_order = universal_tracker_info["level_order"]
        level_beacons = universal_tracker_info["level_beacons"]

        unlocked_levels = [level for levels in level_order.values() for level in levels]
        assert sorted(unlocked_levels) == sorted(all_levels)
        assert level_beacons == {
            level: beacon for beacon, levels in level_order.items() for level in levels
        }
        assert universal_tracker_info["progression_bag"] == self.world.progression_bag
        assert universal_tracker_info["progression_bag"] in bag_items

class TestVanillaLevelOrderCasual(TestVanillaLevelOrder, CasualLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **CasualLogic.options,
    }

class TestVanillaLevelOrderTrickyJumps(TestVanillaLevelOrder, TrickyJumpsLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaLevelOrderNoLantern(TestVanillaLevelOrder, NoLanternLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **NoLanternLogic.options,
    }

class TestVanillaLevelOrderDamageBoost(TestVanillaLevelOrder, DamageBoostLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **DamageBoostLogic.options,
    }

class TestVanillaLevelOrderTrickyJumpsNoLantern(TestVanillaLevelOrder, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaLevelOrderTrickyJumpsDamageBoost(TestVanillaLevelOrder, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaLevelOrderNoLanternDamageBoost(TestVanillaLevelOrder, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaLevelOrderTrickyJumpsNoLanternDamageBoost(TestVanillaLevelOrder, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaLevelOrder.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderCasual(TestFaramoreStartShuffleLevelOrder, CasualLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **CasualLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderTrickyJumps(TestFaramoreStartShuffleLevelOrder, TrickyJumpsLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **TrickyJumpsLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderNoLantern(TestFaramoreStartShuffleLevelOrder, NoLanternLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **NoLanternLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderDamageBoost(TestFaramoreStartShuffleLevelOrder, DamageBoostLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **DamageBoostLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderTrickyJumpsNoLantern(TestFaramoreStartShuffleLevelOrder, TrickyJumpsNoLanternLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderTrickyJumpsDamageBoost(TestFaramoreStartShuffleLevelOrder, TrickyJumpsDamageBoostLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderNoLanternDamageBoost(TestFaramoreStartShuffleLevelOrder, NoLanternDamageBoostLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestFaramoreStartShuffleLevelOrderTrickyJumpsNoLanternDamageBoost(TestFaramoreStartShuffleLevelOrder, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestFaramoreStartShuffleLevelOrder.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestShuffleLevelOrderCasual(TestShuffleLevelOrder, CasualLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **CasualLogic.options,
    }

class TestShuffleLevelOrderTrickyJumps(TestShuffleLevelOrder, TrickyJumpsLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffleLevelOrderNoLantern(TestShuffleLevelOrder, NoLanternLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **NoLanternLogic.options,
    }

class TestShuffleLevelOrderDamageBoost(TestShuffleLevelOrder, DamageBoostLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **DamageBoostLogic.options,
    }

class TestShuffleLevelOrderTrickyJumpsNoLantern(TestShuffleLevelOrder, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffleLevelOrderTrickyJumpsDamageBoost(TestShuffleLevelOrder, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffleLevelOrderNoLanternDamageBoost(TestShuffleLevelOrder, NoLanternDamageBoostLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffleLevelOrderTrickyJumpsNoLanternDamageBoost(TestShuffleLevelOrder, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffleLevelOrder.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

