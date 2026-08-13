import typing
from ..items import all_item_table, beacon_items
from ..locations import all_locations
from ..options import ShuffleBags, ShuffleBeacons
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledBeacons(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_beacons": ShuffleBeacons.option_true,
        "shuffle_bags": ShuffleBags.option_true,
    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in beacon_items:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in beacon_items:
            assert item_name in self.world.early_lock
            host = self.world.early_lock[item_name]
            location = self.world.get_location(host)
            assert location.item.name == item_name
            assert not location.is_event
            assert not location.item.is_event

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in beacon_items:
            assert item_name in world_location_names

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in beacon_items:
            host_id = all_locations[self.world.early_lock[item_name]].arzid
            assert unpingable_locations[host_id]["item"] == all_item_table[item_name].arzid

class TestVanillaBeacons(ArzetteTestBase):
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
        for item_name in beacon_items:
            assert item_name not in item_pool_names

    def test_early_lock(self) -> None:
        for item_name in beacon_items:
            assert self.world.early_lock[item_name] == item_name
            assert self.world.get_location(item_name).item.name == item_name

    def test_prefills(self) -> None:
        for item_name in beacon_items:
            location = self.world.get_location(item_name)
            assert not location.is_event
            assert location.item is not None
            assert not location.item.is_event
            assert location.item.name == item_name

    def test_slot_data(self) -> None:
        unpingable_locations = self.slot_data["unpingable_locations"]
        for item_name in beacon_items:
            vanilla_id = all_locations[item_name].arzid
            assert unpingable_locations[vanilla_id]["item"] == all_item_table[item_name].arzid

class TestShuffledBeaconsCasual(TestShuffledBeacons, CasualLogic):
    options = {
        **TestShuffledBeacons.options,
        **CasualLogic.options,
    }

class TestShuffledBeaconsTrickyJumps(TestShuffledBeacons, TrickyJumpsLogic):
    options = {
        **TestShuffledBeacons.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledBeaconsNoLantern(TestShuffledBeacons, NoLanternLogic):
    options = {
        **TestShuffledBeacons.options,
        **NoLanternLogic.options,
    }

class TestShuffledBeaconsDamageBoost(TestShuffledBeacons, DamageBoostLogic):
    options = {
        **TestShuffledBeacons.options,
        **DamageBoostLogic.options,
    }

class TestShuffledBeaconsTrickyJumpsNoLantern(TestShuffledBeacons, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledBeacons.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledBeaconsTrickyJumpsDamageBoost(TestShuffledBeacons, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledBeacons.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledBeaconsNoLanternDamageBoost(TestShuffledBeacons, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledBeacons.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledBeaconsTrickyJumpsNoLanternDamageBoost(TestShuffledBeacons, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledBeacons.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaBeaconsCasual(TestVanillaBeacons, CasualLogic):
    options = {
        **TestVanillaBeacons.options,
        **CasualLogic.options,
    }

class TestVanillaBeaconsTrickyJumps(TestVanillaBeacons, TrickyJumpsLogic):
    options = {
        **TestVanillaBeacons.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaBeaconsNoLantern(TestVanillaBeacons, NoLanternLogic):
    options = {
        **TestVanillaBeacons.options,
        **NoLanternLogic.options,
    }

class TestVanillaBeaconsDamageBoost(TestVanillaBeacons, DamageBoostLogic):
    options = {
        **TestVanillaBeacons.options,
        **DamageBoostLogic.options,
    }

class TestVanillaBeaconsTrickyJumpsNoLantern(TestVanillaBeacons, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaBeacons.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaBeaconsTrickyJumpsDamageBoost(TestVanillaBeacons, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaBeacons.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaBeaconsNoLanternDamageBoost(TestVanillaBeacons, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaBeacons.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaBeaconsTrickyJumpsNoLanternDamageBoost(TestVanillaBeacons, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaBeacons.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

