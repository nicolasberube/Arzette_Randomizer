from ..items import plant_items
from ..options import ShufflePlants
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledPlants(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_plants": ShufflePlants.option_true,


    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in plant_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in plant_items:
            assert item_name in world_location_names
            location = self.world.get_location(item_name)
            assert not location.is_event

class TestVanillaPlants(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_plants": ShufflePlants.option_false,


    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in plant_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        vanilla_locations = [
            location for location in self.world.get_locations()
            if location.name in plant_items
        ]
        for location in vanilla_locations:
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == location.name

class TestShuffledPlantsCasual(TestShuffledPlants, CasualLogic):
    options = {
        **TestShuffledPlants.options,
        **CasualLogic.options,
    }

class TestShuffledPlantsTrickyJumps(TestShuffledPlants, TrickyJumpsLogic):
    options = {
        **TestShuffledPlants.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledPlantsNoLantern(TestShuffledPlants, NoLanternLogic):
    options = {
        **TestShuffledPlants.options,
        **NoLanternLogic.options,
    }

class TestShuffledPlantsDamageBoost(TestShuffledPlants, DamageBoostLogic):
    options = {
        **TestShuffledPlants.options,
        **DamageBoostLogic.options,
    }

class TestShuffledPlantsTrickyJumpsNoLantern(TestShuffledPlants, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledPlants.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledPlantsTrickyJumpsDamageBoost(TestShuffledPlants, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledPlants.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledPlantsNoLanternDamageBoost(TestShuffledPlants, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledPlants.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledPlantsTrickyJumpsNoLanternDamageBoost(TestShuffledPlants, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledPlants.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaPlantsCasual(TestVanillaPlants, CasualLogic):
    options = {
        **TestVanillaPlants.options,
        **CasualLogic.options,
    }

class TestVanillaPlantsTrickyJumps(TestVanillaPlants, TrickyJumpsLogic):
    options = {
        **TestVanillaPlants.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaPlantsNoLantern(TestVanillaPlants, NoLanternLogic):
    options = {
        **TestVanillaPlants.options,
        **NoLanternLogic.options,
    }

class TestVanillaPlantsDamageBoost(TestVanillaPlants, DamageBoostLogic):
    options = {
        **TestVanillaPlants.options,
        **DamageBoostLogic.options,
    }

class TestVanillaPlantsTrickyJumpsNoLantern(TestVanillaPlants, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaPlants.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaPlantsTrickyJumpsDamageBoost(TestVanillaPlants, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaPlants.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaPlantsNoLanternDamageBoost(TestVanillaPlants, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaPlants.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaPlantsTrickyJumpsNoLanternDamageBoost(TestVanillaPlants, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaPlants.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

