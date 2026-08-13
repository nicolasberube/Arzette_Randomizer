import typing
from ..options import ShuffleBarrierTypes, ShuffleCoins
from .test_logic import CasualLogic, TrickyJumpsLogic, NoLanternLogic, DamageBoostLogic, \
    TrickyJumpsNoLanternLogic, TrickyJumpsDamageBoostLogic, NoLanternDamageBoostLogic, \
    TrickyJumpsNoLanternDamageBoostLogic
from . import ArzetteTestBase

BARRIER_CODES = {
    "Red": "b_red_block",
    "Blue": "b_blue_block",
    "Purple": "b_purple_block",
    "Gauntlet": "b_grey_block",
    "Flute": "b_flute_block",
}

class TestShuffledBarrierTypes(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_true,
        "shuffle_coins": ShuffleCoins.option_true,


    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_barrier_types(self) -> None:
        assert set(self.world.barrier_types.keys()) == {"Red", "Blue", "Purple", "Gauntlet", "Flute"}
        assert set(self.world.barrier_types.values()) == {"Red", "Blue", "Purple", "Gauntlet", "Flute"}

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        assert "Crypts Coin" in world_location_names

    def test_slot_data(self) -> None:
        barrier_info = self.slot_data["barrier_info"]
        assert set(barrier_info) == {f"{barrier}_Barrier" for barrier in BARRIER_CODES}
        assert set(barrier_info.values()) == set(BARRIER_CODES.values())
        assert barrier_info == {
            f"{barrier}_Barrier": BARRIER_CODES[replacement]
            for barrier, replacement in self.world.barrier_types.items()
        }

class TestVanillaBarrierTypes(ArzetteTestBase):
    options = {
        **ArzetteTestBase.no_early_lock_options,
        "shuffle_barrier_types": ShuffleBarrierTypes.option_false,
        "shuffle_coins": ShuffleCoins.option_true,


    }

    def world_setup(self, seed: typing.Optional[int] = None) -> None:
        super().world_setup(seed)
        if not hasattr(self, "multiworld"):
            return
        self.slot_data = self.world.fill_slot_data()


    def test_barrier_types(self) -> None:
        assert self.world.barrier_types == {
            "Red": "Red",
            "Blue": "Blue",
            "Purple": "Purple",
            "Gauntlet": "Gauntlet",
            "Flute": "Flute",
        }

    def test_locations(self) -> None:
        world_location_names = {location.name for location in self.world.get_locations()}
        assert "Crypts Coin" in world_location_names

    def test_slot_data(self) -> None:
        barrier_info = self.slot_data["barrier_info"]
        assert barrier_info == {
            f"{barrier}_Barrier": code for barrier, code in BARRIER_CODES.items()
        }

class TestShuffledBarrierTypesCasual(TestShuffledBarrierTypes, CasualLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **CasualLogic.options,
    }

class TestShuffledBarrierTypesTrickyJumps(TestShuffledBarrierTypes, TrickyJumpsLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **TrickyJumpsLogic.options,
    }

class TestShuffledBarrierTypesNoLantern(TestShuffledBarrierTypes, NoLanternLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **NoLanternLogic.options,
    }

class TestShuffledBarrierTypesDamageBoost(TestShuffledBarrierTypes, DamageBoostLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **DamageBoostLogic.options,
    }

class TestShuffledBarrierTypesTrickyJumpsNoLantern(TestShuffledBarrierTypes, TrickyJumpsNoLanternLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestShuffledBarrierTypesTrickyJumpsDamageBoost(TestShuffledBarrierTypes, TrickyJumpsDamageBoostLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestShuffledBarrierTypesNoLanternDamageBoost(TestShuffledBarrierTypes, NoLanternDamageBoostLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestShuffledBarrierTypesTrickyJumpsNoLanternDamageBoost(TestShuffledBarrierTypes, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestShuffledBarrierTypes.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

class TestVanillaBarrierTypesCasual(TestVanillaBarrierTypes, CasualLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **CasualLogic.options,
    }

class TestVanillaBarrierTypesTrickyJumps(TestVanillaBarrierTypes, TrickyJumpsLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **TrickyJumpsLogic.options,
    }

class TestVanillaBarrierTypesNoLantern(TestVanillaBarrierTypes, NoLanternLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **NoLanternLogic.options,
    }

class TestVanillaBarrierTypesDamageBoost(TestVanillaBarrierTypes, DamageBoostLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **DamageBoostLogic.options,
    }

class TestVanillaBarrierTypesTrickyJumpsNoLantern(TestVanillaBarrierTypes, TrickyJumpsNoLanternLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **TrickyJumpsNoLanternLogic.options,
    }

class TestVanillaBarrierTypesTrickyJumpsDamageBoost(TestVanillaBarrierTypes, TrickyJumpsDamageBoostLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **TrickyJumpsDamageBoostLogic.options,
    }

class TestVanillaBarrierTypesNoLanternDamageBoost(TestVanillaBarrierTypes, NoLanternDamageBoostLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **NoLanternDamageBoostLogic.options,
    }

class TestVanillaBarrierTypesTrickyJumpsNoLanternDamageBoost(TestVanillaBarrierTypes, TrickyJumpsNoLanternDamageBoostLogic):
    options = {
        **TestVanillaBarrierTypes.options,
        **TrickyJumpsNoLanternDamageBoostLogic.options,
    }

