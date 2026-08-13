from BaseClasses import ItemClassification
from ..Names import itemName
from ..options import DamageBoost, NoLantern, ShuffleUpgrades, TrickyJumps
from . import ArzetteTestBase


def _pool_item(multiworld, name: str):
    for item in multiworld.itempool:
        if item.name == name:
            return item
    raise AssertionError(f"{name} not found in item pool")


class TestLogicItemClassificationsCasual(ArzetteTestBase):
    """Default logic options demote Backstep; keep lantern/cloak/ring as progression."""

    options = {
        **ArzetteTestBase.base_options,
        "tricky_jumps": TrickyJumps.option_false,
        "no_lantern": NoLantern.option_false,
        "damage_boost": DamageBoost.option_false,
        "shuffle_upgrades": ShuffleUpgrades.option_true,
    }

    def test_classifications(self) -> None:
        assert _pool_item(self.multiworld, itemName.Backstep).classification == ItemClassification.useful
        assert _pool_item(self.multiworld, itemName.Lantern).advancement
        assert _pool_item(self.multiworld, itemName.MagicCloak).advancement
        assert _pool_item(self.multiworld, itemName.ReflectorRing).advancement
        assert _pool_item(self.multiworld, itemName.SoulUpgrade).classification == ItemClassification.useful


class TestLogicItemClassificationsNoLantern(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "no_lantern": NoLantern.option_true,
    }

    def test_lantern_is_useful(self) -> None:
        assert _pool_item(self.multiworld, itemName.Lantern).classification == ItemClassification.useful


class TestLogicItemClassificationsDamageBoost(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "damage_boost": DamageBoost.option_true,
    }

    def test_damage_items_are_useful(self) -> None:
        assert _pool_item(self.multiworld, itemName.MagicCloak).classification == ItemClassification.useful
        assert _pool_item(self.multiworld, itemName.ReflectorRing).classification == ItemClassification.useful


class TestLogicItemClassificationsTrickyJumps(ArzetteTestBase):
    options = {
        **ArzetteTestBase.base_options,
        "tricky_jumps": TrickyJumps.option_true,
    }

    def test_backstep_stays_progression(self) -> None:
        assert _pool_item(self.multiworld, itemName.Backstep).advancement
