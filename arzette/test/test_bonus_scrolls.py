import typing
from ..items import all_item_table, scroll_items
from ..locations import all_locations
from ..options import ShuffleBags, ShuffleBonusScrolls
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledBonusScrolls(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_bonus_scrolls": ShuffleBonusScrolls.option_true,
        "shuffle_bags": ShuffleBags.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in scroll_items:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in scroll_items:
            assert item_name in self.world.early_lock
            host = self.world.early_lock[item_name]
            assert self.world.get_location(host).item.name == item_name
            assert all_locations[host].can_spawner

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in scroll_items:
            assert self.world.item_to_loc[item_name] in world_location_names

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in scroll_items:
            host_id = all_locations[self.world.early_lock[item_name]].arzid
            assert unpingable_locations[host_id]["item"] == all_item_table[item_name].arzid

class TestVanillaBonusScrolls(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in scroll_items:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in scroll_items:
            vanilla_loc = self.world.item_to_loc[item_name]
            assert self.world.early_lock[item_name] == vanilla_loc
            assert self.world.get_location(vanilla_loc).item.name == item_name

    def test_prefills(self) -> None:
        for item_name in scroll_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in scroll_items:
            vanilla_id = all_locations[self.world.item_to_loc[item_name]].arzid
            assert unpingable_locations[vanilla_id]["item"] == all_item_table[item_name].arzid

class TestShuffledBonusScrollsCasual(TestShuffledBonusScrolls, CasualLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **CasualLogic.options,
    }

class TestShuffledBonusScrollsTrickyJumps(TestShuffledBonusScrolls, TrickyJumpsLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledBonusScrollsNoLantern(TestShuffledBonusScrolls, NoLanternLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **NoLanternLogic.options,
    }

class TestShuffledBonusScrollsDamageBoost(TestShuffledBonusScrolls, DamageBoostLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **DamageBoostLogic.options,
    }

class TestShuffledBonusScrollsTrickyJumpsNoLantern(TestShuffledBonusScrolls, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledBonusScrollsTrickyJumpsDamageBoost(TestShuffledBonusScrolls, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledBonusScrollsNoLanternDamageBoost(TestShuffledBonusScrolls, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledBonusScrollsTrickyJumpsNoLanternDamageBoost(TestShuffledBonusScrolls, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledBonusScrolls.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaBonusScrollsCasual(TestVanillaBonusScrolls, CasualLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **CasualLogic.options,
    }

class TestVanillaBonusScrollsTrickyJumps(TestVanillaBonusScrolls, TrickyJumpsLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaBonusScrollsNoLantern(TestVanillaBonusScrolls, NoLanternLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **NoLanternLogic.options,
    }

class TestVanillaBonusScrollsDamageBoost(TestVanillaBonusScrolls, DamageBoostLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **DamageBoostLogic.options,
    }

class TestVanillaBonusScrollsTrickyJumpsNoLantern(TestVanillaBonusScrolls, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaBonusScrollsTrickyJumpsDamageBoost(TestVanillaBonusScrolls, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaBonusScrollsNoLanternDamageBoost(TestVanillaBonusScrolls, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaBonusScrollsTrickyJumpsNoLanternDamageBoost(TestVanillaBonusScrolls, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaBonusScrolls.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

