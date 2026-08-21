import typing
from ..items import all_item_table, trading_items
from ..locations import all_locations, trading_sequence
from ..Names import itemName, locName
from ..options import TradingSequence
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase


class TestVanillaTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "trading_sequence": TradingSequence.option_vanilla,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in trading_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for loc_name in trading_sequence:
            item_name = self.world.loc_to_item[loc_name]
            location = self.world.get_location(loc_name)
            assert location.item is not None
            assert location.item.name == item_name

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        for loc_name in trading_sequence:
            assert loc_name not in unreachables

        for loc_name in trading_sequence:
            item_name = self.world.loc_to_item[loc_name]
            location_id = all_locations[loc_name].arzid
            assert unpingable_locations[location_id]["item"] == all_item_table[item_name].arzid

class TestRandomStartTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "trading_sequence": TradingSequence.option_random_start,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        assert itemName.DungeonKey in item_pool_names or itemName.DungeonKey in self.world.early_lock

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in trading_items:
            assert self.world.item_to_loc[item_name] in world_location_names

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        # The Sacred Oil is locked on the location of the item the sequence starts at.
        start_loc = self.world.early_lock.get(
            itemName.SacredOil, self.world.item_to_loc[itemName.SacredOil])
        start_index = trading_sequence.index(start_loc)

        for loc_name in trading_sequence[1:start_index + 1]:
            assert loc_name in unreachables
        for loc_name in trading_sequence[start_index + 1:]:
            assert loc_name not in unreachables

        if start_index:
            assert locName.SoulUpgrade in unreachables
            start_id = all_locations[start_loc].arzid
            assert unpingable_locations[start_id]["item"] == all_item_table[itemName.SacredOil].arzid

        for loc_name in trading_sequence[start_index + 1:]:
            item_name = self.world.loc_to_item[loc_name]
            location_id = all_locations[loc_name].arzid
            assert unpingable_locations[location_id]["item"] == all_item_table[item_name].arzid

class TestExcludedTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "trading_sequence": TradingSequence.option_excluded,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        assert itemName.SacredOil in item_pool_names or itemName.SacredOil in self.world.early_lock
        assert itemName.OilandChains in item_pool_names or itemName.OilandChains in self.world.early_lock
        assert itemName.Chainsword in item_pool_names or itemName.Chainsword in self.world.early_lock
        assert itemName.DungeonKey in item_pool_names or itemName.DungeonKey in self.world.early_lock

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        assert self.world.item_to_loc[itemName.SacredOil] in world_location_names
        assert self.world.item_to_loc[itemName.OilandChains] in world_location_names
        assert self.world.item_to_loc[itemName.Chainsword] in world_location_names
        assert self.world.item_to_loc[itemName.DungeonKey] in world_location_names

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        assert locName.SoulUpgrade in unreachables
        # Only the Sacred Oil, the Oil and Chains and the Chainsword remain in the pools.
        for loc_name in trading_sequence[1:-1]:
            assert loc_name in unreachables

        oil_and_chains_id = all_locations[locName.OilandChains].arzid
        assert unpingable_locations[oil_and_chains_id]["item"] == all_item_table[itemName.SacredOil].arzid

        for item_name in (itemName.SacredOil, itemName.Chainsword, itemName.DungeonKey):
            assert all_locations[self.world.item_to_loc[item_name]].arzid in slot_data["pingable_locations"]

class TestShuffledTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "trading_sequence": TradingSequence.option_shuffle,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in trading_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in trading_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]

        for item_name in trading_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name not in unreachables
            assert all_locations[loc_name].arzid in slot_data["pingable_locations"]

class TestVanillaTradingSequenceCasual(TestVanillaTradingSequence, CasualLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **CasualLogic.options,
    }

class TestVanillaTradingSequenceTrickyJumps(TestVanillaTradingSequence, TrickyJumpsLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaTradingSequenceNoLantern(TestVanillaTradingSequence, NoLanternLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **NoLanternLogic.options,
    }

class TestVanillaTradingSequenceDamageBoost(TestVanillaTradingSequence, DamageBoostLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **DamageBoostLogic.options,
    }

class TestVanillaTradingSequenceTrickyJumpsNoLantern(TestVanillaTradingSequence, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaTradingSequenceTrickyJumpsDamageBoost(TestVanillaTradingSequence, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaTradingSequenceNoLanternDamageBoost(TestVanillaTradingSequence, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaTradingSequenceTrickyJumpsNoLanternDamageBoost(TestVanillaTradingSequence, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaTradingSequence.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestRandomStartTradingSequenceCasual(TestRandomStartTradingSequence, CasualLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **CasualLogic.options,
    }

class TestRandomStartTradingSequenceTrickyJumps(TestRandomStartTradingSequence, TrickyJumpsLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **TrickyJumpsLogic.options,
    }

class TestRandomStartTradingSequenceNoLantern(TestRandomStartTradingSequence, NoLanternLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **NoLanternLogic.options,
    }

class TestRandomStartTradingSequenceDamageBoost(TestRandomStartTradingSequence, DamageBoostLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **DamageBoostLogic.options,
    }

class TestRandomStartTradingSequenceTrickyJumpsNoLantern(TestRandomStartTradingSequence, TrickyJumpsNoLanternLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestRandomStartTradingSequenceTrickyJumpsDamageBoost(TestRandomStartTradingSequence, TrickyJumpsDamageBoostLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestRandomStartTradingSequenceNoLanternDamageBoost(TestRandomStartTradingSequence, NoLanternDamageBoostLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestRandomStartTradingSequenceTrickyJumpsNoLanternDamageBoost(TestRandomStartTradingSequence, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestRandomStartTradingSequence.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestExcludedTradingSequenceCasual(TestExcludedTradingSequence, CasualLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **CasualLogic.options,
    }

class TestExcludedTradingSequenceTrickyJumps(TestExcludedTradingSequence, TrickyJumpsLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **TrickyJumpsLogic.options,
    }

class TestExcludedTradingSequenceNoLantern(TestExcludedTradingSequence, NoLanternLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **NoLanternLogic.options,
    }

class TestExcludedTradingSequenceDamageBoost(TestExcludedTradingSequence, DamageBoostLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **DamageBoostLogic.options,
    }

class TestExcludedTradingSequenceTrickyJumpsNoLantern(TestExcludedTradingSequence, TrickyJumpsNoLanternLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestExcludedTradingSequenceTrickyJumpsDamageBoost(TestExcludedTradingSequence, TrickyJumpsDamageBoostLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestExcludedTradingSequenceNoLanternDamageBoost(TestExcludedTradingSequence, NoLanternDamageBoostLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestExcludedTradingSequenceTrickyJumpsNoLanternDamageBoost(TestExcludedTradingSequence, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestExcludedTradingSequence.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestShuffledTradingSequenceCasual(TestShuffledTradingSequence, CasualLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **CasualLogic.options,
    }

class TestShuffledTradingSequenceTrickyJumps(TestShuffledTradingSequence, TrickyJumpsLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledTradingSequenceNoLantern(TestShuffledTradingSequence, NoLanternLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **NoLanternLogic.options,
    }

class TestShuffledTradingSequenceDamageBoost(TestShuffledTradingSequence, DamageBoostLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **DamageBoostLogic.options,
    }

class TestShuffledTradingSequenceTrickyJumpsNoLantern(TestShuffledTradingSequence, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledTradingSequenceTrickyJumpsDamageBoost(TestShuffledTradingSequence, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledTradingSequenceNoLanternDamageBoost(TestShuffledTradingSequence, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledTradingSequenceTrickyJumpsNoLanternDamageBoost(TestShuffledTradingSequence, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledTradingSequence.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

