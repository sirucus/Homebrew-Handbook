---
tags:
  - type/spell
  - level/3
  - school/conjuration
  - class/druid
  - class/warlock
  - class/wizard
aliases: [ "Skeletal Hound" ]
---

# Summon Skeletal Hound

> [!info] Spell Stats
> * **Level:** 3rd Level Conjuration
> * **Casting Time:** 1 Action
> * **Range:** 60 feet
> * **Components:** V, S, M (the charred skull of a hound)
> * **Duration:** Concentration, up to 10 minutes
> * **Classes:** Druid, Warlock, Wizard

## Description
You call forth a hellish spirit from its remnants. The spirit manifests physically in an unoccupied space that you can see within range. This corporeal form uses the **Skeletal Hound** stat block below. The creature disappears when it drops to 0 Hit Points or when the spell ends.

The creature is friendly to you and your companions for the spell's duration. In combat, the creature shares your initiative count, but it takes its turn immediately after yours. It obeys verbal commands that you issue to it (no action required by you). If you don't issue any, it defends itself but otherwise takes no action.

**At Higher Levels.** When you cast this spell using a spell slot of 4th level or higher, the hound assumes the higher level for that casting wherever it uses the spell's level in its stat block.

---

```statblock
name: Skeletal Hound
size: Medium
type: Undead
alignment: Same alignment as the caster
ac: 11 + the level of the spell (natural armor)
hp: "Constitution modifier + your spellcasting ability modifier + ten times the spell's level"
speed: 50 ft.
stats: [17, 12, 14, 6, 13, 6]
damage_immunities: Fire, Poison
condition_immunities: Exhaustion, Frightened, Poisoned
senses: Darkvision 60 ft., Passive Perception 15
languages: Understands the languages you speak and Infernal but can't speak it
traits:
  - name: Keen Hearing and Smell
    desc: "The hound has advantage on Wisdom (Perception) checks that rely on hearing or smell."
  - name: Pack Tactics
    desc: "The hound has advantage on an attack roll against a creature if at least one of the hound's allies is within 5 ft. of the creature and the ally isn't incapacitated."
actions:
  - name: Multiattack
    desc: "The hound makes a number of attacks equal to half this spell's level (rounded down)."
  - name: Bite
    desc: "Melee Weapon Attack: +3 + the spell's level to hit, reach 5 ft., one target. Hit: 1d10 + 3 + the spell's level piercing damage."
  - name: Fire Breath (Once per casting)
    desc: "The hound exhales fire in a 15-foot cone. Each creature in that area must succeed a Dexterity saving throw against your spell save DC, taking 3d6 + twice the spell's level fire damage on a failed save, or half as much damage on a successful one."