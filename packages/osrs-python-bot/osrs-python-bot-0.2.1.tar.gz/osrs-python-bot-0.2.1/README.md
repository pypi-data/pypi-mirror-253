# OSRS Python Bot

- [How to Use OSRS Python Bot](#how-to-use-osrs-python-bot)
  - [Setup Guide](#setup-guide)
    - [System Requirements](#system-requirements)
    - [Getting Everything Ready](#getting-everything-ready)
    - [Actually Running Scripts](#actually-running-scripts)
  - [Contributing to the Project](#contributing-to-the-project)
- [Skill Categories](#skill-categories)
  - [Combat 🤺](#combat-)
    - [NMZ Prayer Flicking](#nmz-prayer-flicking)
  - [Herblore 🌿](#herblore-)
    - [Making Guthix Rest](#making-guthix-rest)
    - [Cleaning Herbs](#cleaning-herbs)
  - [Magic 🧙‍♂️](#magic-️)
    - [Casting High Alchemy](#casting-high-alchemy)

## Setup Guide

### System Requirements
- Windows PC 💻
- [RuneLite](https://runelite.net/) ⚔️
- [git](https://git-scm.com/download/win) 😺
- [python](https://www.python.org/downloads/) & [pip](https://pip.pypa.io/en/stable/installation/) 🐍
- Basic understanding of programming 🧑‍💻
- Ability to run commands from the terminal 👩‍💻

### Getting Everything Ready
======

```
pip install osrs-python-bot
```

**Download**
<a href='' download>runner.py</a>


### Actually Running Scripts
======

Each bot is programmed to click on specific pixels, therefore it requires precise instructions. These instructions may involve the character's orientation, the location of the item in the bank, and even the arrangement of the inventory. It is of utmost importance to follow each script's instructions accurately. These scripts are inteded for private servers. 

**Note:** press space bar to stop a script

*Using these scripts is solely at your own discretion and risk. Employing them may lead to a ban or loss of your old school runescape account. I cannot be held accountable for any misuse or consequences arising from the utilization of this code.*

## Contributing to the Project

Contributions are highly encouraged. I am eager to incorporate computer vision to make the scripts more dynamic. If there are any issues or interest for collaboration please open an issue.

I appreciate the donations, it keeps the coffee flowing ☕😊

## Skill Categories

<!---------------------------------------- COMBAT ----------------------------------------->
### Combat 🤺
---

#### NMZ Prayer Flicking

**Script**

[#nightmare_zone.py](https://github.com/osrs-bots/simple-python-bot/blob/main/scripts/nightmare_zone.py)

**Instructions**

- Cursor is hovering quick prayers button
- Quick prayers set to rapid heal
- Use Dhorak's with rock cake
- Fill up on absorptions
- Turn on run and auto retaliate

**Command**

```
python nightmare_zone.py
```


<!---------------------------------------- HERBLORE ----------------------------------------->
### Herblore 🌿

---
<!---------------------------------------- MAKING GUTHIX REST ----------------------------------------->
#### Making Guthix Rest

**Instructions**

- RuneLite client is as small as possible
- RuneLite client is in top left of monitor
- At castle wars bankchest
- Face directly East (right click the compass)
- The viewport is fully zoomed in
- Camera is positioned in the most top down position (hold up arrow key)
- Inventory pane is open and empty
- Bank menu opens to a tab with guthix rest supplies
- The bank menu is closed to start
- Supplies ordered according to the image
- Large inventory of supplies as depletion can break script

**Command**
```
python make_guthix_rest.py
```

**Images**

![guthix rest bank setup](https://github.com/osrs-bots/docs/blob/main/website/static/img/guthix_rest_maker_bank_setup.gif?raw=true?raw=true)

hot cup of water / guam / marrentill / harralander

---
<!---------------------------------------- CLEANING HERBS ----------------------------------------->
#### Cleaning Herbs

**Instructions**

- RuneLite client is as small as possible
- RuneLite client is in top left of monitor
- Character is at castle wars bankchest
- Character is facing directly East (right click the compass)
- The viewport is fully zoomed in (scroll)
- Camera is positioned in the most top down position (hold up arrow key)
- Inventory pane is open and empty
- Bank menu opens to a tab with supplies
- The bank menu is closed to start
- Herb in top right bank slot
- Large inventory of supplies as depletion can break script

**Command**
```
python clean_herbs.py
```
  
<!---------------------------------------- MAGIC ----------------------------------------->
### Magic 🧙‍♂️
---

#### Casting High Alchemy

**Instructions**

- Mouse is hovering high alchemy spell
- High alchemy item is in the designated spot

**Command**

```
python high_alchemy.py
```
