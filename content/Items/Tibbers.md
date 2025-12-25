---
tags:
  - type/wondrous-item
  - rarity/very-rare
  - attunement/required
  - attunement/spellcaster
aliases: [ "Tibbers Beast Form" ]
---

# Tibbers

> [!info] Item Stats
> * **Type:** Wondrous Item
> * **Rarity:** Very Rare
> * **Attunement:** Requires Attunement by a Spellcaster
> * **Charges:** 6 (Regains 1d4 at the beginning of every day)

## Capabilities

### Beast Form
As an Action, you can speak the command word and throw the bear to a point on the ground within 30 feet of you. It expends **3 charges** and becomes a living creature taking its **Beast Form** (stat block below).
* If the space is occupied or there isn't enough space, it does not become a creature.
* The creature is friendly to you and your companions.
* It understands your languages and obeys your spoken commands.
* **Duration:** 1 minute, until it drops to 0 Hit Points, or by command word.

### Toy Form
While holding Tibbers in its Toy Form, you can spend charges to cast spells using your Spell Save DC:
* **2 Charges:** Cast **Burning Hands** at 1st Level. You can increase the spell slot level by one for every two extra charges you expend.
* **3 Charges:** Cast **Shield**.

---

```statblock
name: Tibbers Beast Form
size: Large
type: Beast
alignment: Lawful Neutral
ac: 11
hp: 35
speed: 40 ft.
stats: [18, 10, 15, 10, 10, 8]
vulnerabilities: Cold Damage
resistances: Poison Damage
damage_immunities: 
condition_immunities: Poisoned
senses: Darkvision 60 ft., Passive Perception 16
languages: Understands commands
traits:
  - name: Illumination
    desc: "In its beast form, Tibbers sheds Bright Light in a 5-foot radius and Dim Light in an additional 15 feet."
  - name: Fire Aura
    desc: "Each creature that starts its turn within 5 feet of Tibbers must make a DC 15 Dexterity Saving Throw. On a failure, they take 1d8 Fire Damage. On a success, they take half damage."
  - name: Broken Stitches
    desc: "When dropping to 0 Hit Points, roll 1d20. On a 1–5, Tibbers cannot take its beast form again until it is sewn again, which requires 72 hours of work."
actions:
  - name: Multiattack
    desc: "The bear makes two attacks: one with its bite and one with its claws."
  - name: Bite
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d6 + 4 Piercing Damage."
  - name: Claws
    desc: "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 1d6 + 4 Slashing Damage."
