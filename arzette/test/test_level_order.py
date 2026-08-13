import typing
from ..items import bag_items
from ..locations import all_levels
from ..options import LevelOrder, ShuffleBags
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestVanillaLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
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

class TestFaramoreLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "level_order": LevelOrder.option_faramore,
        "shuffle_bags": ShuffleBags.option_true,


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

class TestRandomizedLevelOrder(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "level_order": LevelOrder.option_randomize,
        "shuffle_bags": ShuffleBags.option_true,


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

class TestFaramoreLevelOrderCasual(TestFaramoreLevelOrder, CasualLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **CasualLogic.options,
    }

class TestFaramoreLevelOrderTrickyJumps(TestFaramoreLevelOrder, TrickyJumpsLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **TrickyJumpsLogic.options,
    }

class TestFaramoreLevelOrderNoLantern(TestFaramoreLevelOrder, NoLanternLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **NoLanternLogic.options,
    }

class TestFaramoreLevelOrderDamageBoost(TestFaramoreLevelOrder, DamageBoostLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **DamageBoostLogic.options,
    }

class TestFaramoreLevelOrderTrickyJumpsNoLantern(TestFaramoreLevelOrder, TrickyJumpsNoLanternLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestFaramoreLevelOrderTrickyJumpsDamageBoost(TestFaramoreLevelOrder, TrickyJumpsDamageBoostLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestFaramoreLevelOrderNoLanternDamageBoost(TestFaramoreLevelOrder, NoLanternDamageBoostLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestFaramoreLevelOrderTrickyJumpsNoLanternDamageBoost(TestFaramoreLevelOrder, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestFaramoreLevelOrder.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestRandomizedLevelOrderCasual(TestRandomizedLevelOrder, CasualLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **CasualLogic.options,
    }

class TestRandomizedLevelOrderTrickyJumps(TestRandomizedLevelOrder, TrickyJumpsLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **TrickyJumpsLogic.options,
    }

class TestRandomizedLevelOrderNoLantern(TestRandomizedLevelOrder, NoLanternLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **NoLanternLogic.options,
    }

class TestRandomizedLevelOrderDamageBoost(TestRandomizedLevelOrder, DamageBoostLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **DamageBoostLogic.options,
    }

class TestRandomizedLevelOrderTrickyJumpsNoLantern(TestRandomizedLevelOrder, TrickyJumpsNoLanternLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestRandomizedLevelOrderTrickyJumpsDamageBoost(TestRandomizedLevelOrder, TrickyJumpsDamageBoostLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestRandomizedLevelOrderNoLanternDamageBoost(TestRandomizedLevelOrder, NoLanternDamageBoostLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestRandomizedLevelOrderTrickyJumpsNoLanternDamageBoost(TestRandomizedLevelOrder, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestRandomizedLevelOrder.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

