interface Entity {
    id: number;
}

export interface Ability extends Entity {
    name: string;
    description: string;
}

export interface AbilityUse extends Entity {
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

export interface GameSession extends Entity {
  code: string;
}