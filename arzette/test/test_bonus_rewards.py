from ..items import bonusreward_items
from ..options import ShuffleBonusScrollRewards
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

LOCKED_BONUS_REWARDS = {
    "Faramore Bonus Reward",
    "Volcano Bonus Reward",
    "Castle Bonus Reward",
}

class TestShuffledBonusRewards(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_bonus_rewards": ShuffleBonusScrollRewards.option_true,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in bonusreward_items:
            if item_name in LOCKED_BONUS_REWARDS:
                assert item_name not in item_pool_names
            else:
                assert item_name in item_pool_names

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        for item_name in bonusreward_items:
            loc_name = self.world.item_to_loc[item_name]
            assert loc_name in world_location_names
            location = self.world.get_location(loc_name)
            if item_name in LOCKED_BONUS_REWARDS:
                assert location.is_event
            else:
                assert not location.is_event

class TestVanillaBonusRewards(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "shuffle_bonus_rewards": ShuffleBonusScrollRewards.option_false,
    }

    def test_item_pool(self) -> None:
        item_pool_names = {item.name for item in self.multiworld.itempool}
        for item_name in bonusreward_items:
            assert item_name not in item_pool_names

    def test_prefills(self) -> None:
        for item_name in bonusreward_items:
            location = self.world.get_location(self.world.item_to_loc[item_name])
            assert location.is_event
            assert location.item is not None
            assert location.item.is_event
            assert location.item.name == item_name

class TestShuffledBonusRewardsCasual(TestShuffledBonusRewards, CasualLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **CasualLogic.options,
    }

class TestShuffledBonusRewardsTrickyJumps(TestShuffledBonusRewards, TrickyJumpsLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledBonusRewardsNoLantern(TestShuffledBonusRewards, NoLanternLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **NoLanternLogic.options,
    }

class TestShuffledBonusRewardsDamageBoost(TestShuffledBonusRewards, DamageBoostLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **DamageBoostLogic.options,
    }

class TestShuffledBonusRewardsTrickyJumpsNoLantern(TestShuffledBonusRewards, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledBonusRewardsTrickyJumpsDamageBoost(TestShuffledBonusRewards, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledBonusRewardsNoLanternDamageBoost(TestShuffledBonusRewards, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledBonusRewardsTrickyJumpsNoLanternDamageBoost(TestShuffledBonusRewards, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledBonusRewards.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaBonusRewardsCasual(TestVanillaBonusRewards, CasualLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **CasualLogic.options,
    }

class TestVanillaBonusRewardsTrickyJumps(TestVanillaBonusRewards, TrickyJumpsLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaBonusRewardsNoLantern(TestVanillaBonusRewards, NoLanternLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **NoLanternLogic.options,
    }

class TestVanillaBonusRewardsDamageBoost(TestVanillaBonusRewards, DamageBoostLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **DamageBoostLogic.options,
    }

class TestVanillaBonusRewardsTrickyJumpsNoLantern(TestVanillaBonusRewards, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaBonusRewardsTrickyJumpsDamageBoost(TestVanillaBonusRewards, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaBonusRewardsNoLanternDamageBoost(TestVanillaBonusRewards, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaBonusRewardsTrickyJumpsNoLanternDamageBoost(TestVanillaBonusRewards, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaBonusRewards.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

