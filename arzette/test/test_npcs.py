import typing
from ..items import all_item_table, npc_items, npcspawner_items
from ..locations import all_locations
from ..options import ShuffleBags, ShuffleNPCs
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

NPC_NAMES = list(npcspawner_items) + list(npc_items)

class TestShuffledNPCs(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_npcs": ShuffleNPCs.option_true,
        "shuffle_bags": ShuffleBags.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in NPC_NAMES:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in NPC_NAMES:
            assert item_name in self.world.early_lock
            host = self.world.early_lock[item_name]
            assert self.world.get_location(host).item.name == item_name
            if item_name in npcspawner_items:
                assert all_locations[host].can_spawner

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in NPC_NAMES:
            assert item_name in world_location_names

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in NPC_NAMES:
            host_id = all_locations[self.world.early_lock[item_name]].arzid
            assert unpingable_locations[host_id]["item"] == all_item_table[item_name].arzid

class TestVanillaNPCs(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in NPC_NAMES:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in NPC_NAMES:
            assert self.world.early_lock[item_name] == item_name
            assert self.world.get_location(item_name).item.name == item_name

    def test_prefills(self) -> None:
        for item_name in NPC_NAMES:
            location = self.world.get_location(item_name)
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in NPC_NAMES:
            vanilla_id = all_locations[item_name].arzid
            assert unpingable_locations[vanilla_id]["item"] == all_item_table[item_name].arzid

class TestShuffledNPCsCasual(TestShuffledNPCs, CasualLogic):
    options = {
        **TestShuffledNPCs.options,
        **CasualLogic.options,
    }

class TestShuffledNPCsTrickyJumps(TestShuffledNPCs, TrickyJumpsLogic):
    options = {
        **TestShuffledNPCs.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledNPCsNoLantern(TestShuffledNPCs, NoLanternLogic):
    options = {
        **TestShuffledNPCs.options,
        **NoLanternLogic.options,
    }

class TestShuffledNPCsDamageBoost(TestShuffledNPCs, DamageBoostLogic):
    options = {
        **TestShuffledNPCs.options,
        **DamageBoostLogic.options,
    }

class TestShuffledNPCsTrickyJumpsNoLantern(TestShuffledNPCs, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledNPCs.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledNPCsTrickyJumpsDamageBoost(TestShuffledNPCs, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledNPCs.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledNPCsNoLanternDamageBoost(TestShuffledNPCs, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledNPCs.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledNPCsTrickyJumpsNoLanternDamageBoost(TestShuffledNPCs, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledNPCs.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaNPCsCasual(TestVanillaNPCs, CasualLogic):
    options = {
        **TestVanillaNPCs.options,
        **CasualLogic.options,
    }

class TestVanillaNPCsTrickyJumps(TestVanillaNPCs, TrickyJumpsLogic):
    options = {
        **TestVanillaNPCs.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaNPCsNoLantern(TestVanillaNPCs, NoLanternLogic):
    options = {
        **TestVanillaNPCs.options,
        **NoLanternLogic.options,
    }

class TestVanillaNPCsDamageBoost(TestVanillaNPCs, DamageBoostLogic):
    options = {
        **TestVanillaNPCs.options,
        **DamageBoostLogic.options,
    }

class TestVanillaNPCsTrickyJumpsNoLantern(TestVanillaNPCs, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaNPCs.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaNPCsTrickyJumpsDamageBoost(TestVanillaNPCs, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaNPCs.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaNPCsNoLanternDamageBoost(TestVanillaNPCs, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaNPCs.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaNPCsTrickyJumpsNoLanternDamageBoost(TestVanillaNPCs, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaNPCs.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

