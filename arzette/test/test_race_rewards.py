from ..items import race_items
from ..options import ShuffleRaceRewards
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

class TestShuffledRaceRewards(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_race_rewards": ShuffleRaceRewards.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in race_items:
            assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in race_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            assert not location.is_event

class TestVanillaRaceRewards(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_race_rewards": ShuffleRaceRewards.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in race_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in race_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledRaceRewardsCasual(TestShuffledRaceRewards, CasualLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **CasualLogic.options,
    }

class TestShuffledRaceRewardsTrickyJumps(TestShuffledRaceRewards, TrickyJumpsLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledRaceRewardsNoLantern(TestShuffledRaceRewards, NoLanternLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **NoLanternLogic.options,
    }

class TestShuffledRaceRewardsDamageBoost(TestShuffledRaceRewards, DamageBoostLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **DamageBoostLogic.options,
    }

class TestShuffledRaceRewardsTrickyJumpsNoLantern(TestShuffledRaceRewards, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledRaceRewardsTrickyJumpsDamageBoost(TestShuffledRaceRewards, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledRaceRewardsNoLanternDamageBoost(TestShuffledRaceRewards, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledRaceRewardsTrickyJumpsNoLanternDamageBoost(TestShuffledRaceRewards, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledRaceRewards.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaRaceRewardsCasual(TestVanillaRaceRewards, CasualLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **CasualLogic.options,
    }

class TestVanillaRaceRewardsTrickyJumps(TestVanillaRaceRewards, TrickyJumpsLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaRaceRewardsNoLantern(TestVanillaRaceRewards, NoLanternLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **NoLanternLogic.options,
    }

class TestVanillaRaceRewardsDamageBoost(TestVanillaRaceRewards, DamageBoostLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **DamageBoostLogic.options,
    }

class TestVanillaRaceRewardsTrickyJumpsNoLantern(TestVanillaRaceRewards, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaRaceRewardsTrickyJumpsDamageBoost(TestVanillaRaceRewards, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaRaceRewardsNoLanternDamageBoost(TestVanillaRaceRewards, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaRaceRewardsTrickyJumpsNoLanternDamageBoost(TestVanillaRaceRewards, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaRaceRewards.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

