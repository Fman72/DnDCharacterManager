export interface Ability {
    name: string;
    description: string;
}

export interface AbilityUse {
    character: {
        name: string;
    }
    ability: {
        name: string;
    }
    caster: SpellCasterTarget;
    target: SpellCasterTarget;
}

export interface SpellCasterTarget {
    name: string;
}