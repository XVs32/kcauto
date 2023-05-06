# kcauto_custom

### ***Lastest download link: [Windows](https://github.com/XVs32/kcauto_custom/releases/tag/Windows_v1.0.0_pre-release), [Linux](https://github.com/XVs32/kcauto_custom/releases/tag/Linux_v1.0.0_pre-release)***

**[kcauto_custom](https://github.com/XVs32/kcauto_custom)** is a linux customized version of an archived project [kcauto](https://github.com/perryhuynh/kcauto) that includes additional features and functionality.  
In comparison with **kcauto**, **kcauto_custom** is less flexible while being more automatic for easy daily use.  
This tool is designed to help users automate repetitive tasks such as Expedition, Combat, PvP, Repair & Resupply, ultimately saving time and improving efficiency. 

***Warnning*** : kcauto_custom is not made for Windows(althought it could theoretically run on Windows), I might or might not fix any compatibility problems.

![Screenshot from 2023-05-05 23-42-59](https://user-images.githubusercontent.com/16824564/236490338-2930fada-2a0b-47da-958c-7d150b421c48.png)

---

> ### Disclaimer

> kcauto_custom is meant for educational purposes only. Botting is against the rules and prolonged usage of kcauto_custom may result in your account being banned. The developer of kcauto_custom takes no responsibility for repercussions related to the usage of kcauto_custom. You have been warned!

> Although unlikely, users may lose ships and equipment when using kcauto_custom to conduct combat sorties. While kcauto_custom has been painstakingly designed to reduce the chances of this happening, the developer of kcauto_custom does not take responsibility for any loss of ships and/or resources.

### Original features form kcauto

* Expedition &mdash; automate expeditions
* PvP Module &mdash; automate PvP
* Combat Module &mdash; automate combat sorties
* LBAS Module &mdash; automatic LBAS management
* Ship Switcher Module &mdash; automatic switching of ships based on specified criteria between combat sorties
* Fleet Switcher Module &mdash; automatic switching of fleet presets for PvP and combat sorties
* Quests Module &mdash; automatic quest management
* Repair & Resupply Modules &mdash; automatic resupply and repair of fleet ships
* Stats &mdash; keeps stats on various actions performed
* Click Tracking &mdash; optional tracking of clicks done by kcauto
* Scheduled and manual sleeping and pausing of individual modules or entire script
* Automatic catbomb and script recovery
* Random variations in navigation, timers, and click positions to combat bot detection
* Hot-reload config files
* Open-source codebase

### Features form kcauto_custom

* CUI(Character User Interface) for daily use cases
* Akashi repair Module &mdash; Repair ships with akashi
* Factory Module &mdash; Runs daily develop and ship building 
* More fleet presets &mdash; Unlimited fleet presets that you can define in a config file
* Sortie mdoe: Auto &mdash; Auto finish daily/weekly/monthly quest (KC3 is needed)
* Support for 7-4, events
* Bug fix(Fleet Switcher Module, interaction_mode, quest handling etc.)

## Installation

[wiki](https://github.com/XVs32/kcauto_custom/wiki/Ch1:-Setup-guide)  
For non-developer:
* Windows
    * Double click `kcauto_cui.exe` 
        * Or, run `.\kcauto_cui.exe` in Powershell for better user experience
* Linux
    * Run `./kcauto_cui`
    
---

For developer(Those who know what they are doing):
* Install Python 3.7.3
* (Unix only) Install additional pacakges `python3-tk scrot`
* Install pip if not already installed
* (Optional, but recommended) Install `pipenv` using `pip install pipenv`
* Install dependencies:
  * `pip`-mode: `pip install -r requirements.txt`
  * `pipenv`-mode: `pipenv shell`, then `pipenv install --ignore-pipfile`

## Wiki page
### [Setup guide](https://github.com/XVs32/kcauto_custom/wiki/Ch1:-Setup-guide)  
### [Beginner user guide](https://github.com/XVs32/kcauto_custom/wiki/Ch2.1:-Beginner-user-guide)  
### [Gamer user guide](https://github.com/XVs32/kcauto_custom/wiki/Ch2.2:-Gamer-user-guide)  
---
*You need a github account for the following*
### [Wishing pool](https://github.com/XVs32/kcauto_custom/discussions/categories/ideas): Wish/Idea for new functions
### [Bug report](https://github.com/XVs32/kcauto_custom/issues): Bro, something goes wrong
### [Q&A](https://github.com/XVs32/kcauto_custom/discussions/categories/q-a): How to use this/that?
