from ..options import DamageBoost, NoLantern, TrickyJumps


class CasualLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_false,
        "no_lantern": NoLantern.option_false,
        "damage_boost": DamageBoost.option_false,
    }


class TrickyJumpsLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_true,
        "no_lantern": NoLantern.option_false,
        "damage_boost": DamageBoost.option_false,
    }


class NoLanternLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_false,
        "no_lantern": NoLantern.option_true,
        "damage_boost": DamageBoost.option_false,
    }


class DamageBoostLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_false,
        "no_lantern": NoLantern.option_false,
        "damage_boost": DamageBoost.option_true,
    }


class TrickyJumpsNoLanternLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_true,
        "no_lantern": NoLantern.option_true,
        "damage_boost": DamageBoost.option_false,
    }


class TrickyJumpsDamageBoostLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_true,
        "no_lantern": NoLantern.option_false,
        "damage_boost": DamageBoost.option_true,
    }


class NoLanternDamageBoostLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_false,
        "no_lantern": NoLantern.option_true,
        "damage_boost": DamageBoost.option_true,
    }


class TrickyJumpsNoLanternDamageBoostLogic:
    options = {
        "tricky_jumps": TrickyJumps.option_true,
        "no_lantern": NoLantern.option_true,
        "damage_boost": DamageBoost.option_true,
    }
