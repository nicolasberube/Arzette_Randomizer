import typing
from ..items import all_item_table, trading_items
from ..locations import all_locations
from ..options import TradingSequence
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

TRADING_SEQUENCE = [
    "Sacred Oil",
    "Funky Fungus",
    "Snail Salt",
    "Cleaver Shovel",
    "Ogre Hair",
    "Oil and Chains",
    "Chainsword",
]

class TestVanillaTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
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
        for item_name in TRADING_SEQUENCE:
            if item_name == "Sacred Oil":
                continue
            location = self.world.get_location(item_name)
            assert location.item is not None
            assert location.item.name == item_name

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        for item_name in TRADING_SEQUENCE:
            assert item_name not in unreachables

        for item_name in TRADING_SEQUENCE[1:]:
            location_id = all_locations[item_name].arzid
            assert unpingable_locations[location_id]["item"] == all_item_table[item_name].arzid

class TestRandomStartTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "trading_sequence": TradingSequence.option_random_start,

    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        assert "Dungeon Key" in item_pool_names or "Dungeon Key" in self.world.early_lock

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in trading_items:
            assert item_name in world_location_names

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        # The Sacred Oil is locked on the location of the item the sequence starts at.
        start = self.world.early_lock.get("Sacred Oil", "Sacred Oil")
        start_index = TRADING_SEQUENCE.index(start)

        for item_name in TRADING_SEQUENCE[1:start_index + 1]:
            assert item_name in unreachables
        for item_name in TRADING_SEQUENCE[start_index + 1:]:
            assert item_name not in unreachables

        if start_index:
            assert "Soul Upgrade" in unreachables
            start_id = all_locations[start].arzid
            assert unpingable_locations[start_id]["item"] == all_item_table["Sacred Oil"].arzid

        for item_name in TRADING_SEQUENCE[start_index + 1:]:
            location_id = all_locations[item_name].arzid
            assert unpingable_locations[location_id]["item"] == all_item_table[item_name].arzid

class TestExcludedTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "trading_sequence": TradingSequence.option_excluded,

    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in ("Sacred Oil", "Oil and Chains", "Chainsword", "Dungeon Key"):
            assert item_name in item_pool_names or item_name in self.world.early_lock

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in ("Sacred Oil", "Oil and Chains", "Chainsword", "Dungeon Key"):
            assert item_name in world_location_names

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]
        unpingable_locations = slot_data["unpingable_locations"]

        assert "Soul Upgrade" in unreachables
        # Only the Sacred Oil, the Oil and Chains and the Chainsword remain in the pools.
        for item_name in TRADING_SEQUENCE[1:-1]:
            assert item_name in unreachables

        oil_and_chains_id = all_locations["Oil and Chains"].arzid
        assert unpingable_locations[oil_and_chains_id]["item"] == all_item_table["Sacred Oil"].arzid

        for item_name in ("Sacred Oil", "Chainsword", "Dungeon Key"):
            assert all_locations[item_name].arzid in slot_data["pingable_locations"]

class TestShuffledTradingSequence(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
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
            assert item_name in world_location_names
            location = self.world.get_location(item_name)
            assert not location.is_event

    def test_slot_data(self) -> None:
        slot_data = self.slot_data
        unreachables = slot_data["universal_tracker_info"]["unreachables"]

        for item_name in trading_items:
            assert item_name not in unreachables
            assert all_locations[item_name].arzid in slot_data["pingable_locations"]

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

