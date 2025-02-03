from typing import Any, Dict

from .Options import *

kh1_option_presets: Dict[str, Dict[str, Any]] = {
    # Standard playthrough where your goal is to defeat Ansem, reaching him by acquiring enough lucky emblems.
    "Final Ansem": {
        "final_rest_door_key": FinalRestDoorKey.option_lucky_emblems,
        "end_of_the_world_unlock": EndoftheWorldUnlock.option_lucky_emblems,
        "required_lucky_emblems_eotw": 7,
        "required_lucky_emblems_door": 10,
        "lucky_emblems_in_pool": 13,
        "required_postcards": 10,
        "required_puppies": 99,
        
        "super_bosses": False,
        "atlantica": False,
        "hundred_acre_wood": False,
        "cups": False,
        "jungle_slider": False,
        "randomize_emblem_pieces": False,
        "randomize_postcards": RandomizePostcards.option_all,
        
        "exp_multiplier": 48,
        "level_checks": 99,
        "slot_2_level_checks": 33,
        "force_stats_and_abilities_on_levels": 1,
        "strength_increase": 24,
        "defense_increase": 24,
        "hp_increase": 23,
        "ap_increase": 18,
        "mp_increase": 7,
        "accessory_slot_increase": 1,
        "item_slot_increase": 3,
        
        "keyblades_unlock_chests": False,
        "keyblade_stats": KeybladeStats.option_shuffle,
        "bad_starting_weapons": False,
        "keyblade_max_str": 14,
        "keyblade_min_str": 3,
        "keyblade_max_crit_rate": 200,
        "keyblade_min_crit_rate": 0,
        "keyblade_max_crit_str": 16,
        "keyblade_min_crit_str": 0,
        "keyblade_max_recoil": 90,
        "keyblade_min_recoil": 1,
        "keyblade_max_mp": 3,
        "keyblade_min_mp": -2,
        
        "randomize_puppies": True,
        "puppy_value": 3,
        "starting_worlds": 0,
        "starting_tools": True,
        "interact_in_battle": False,
        "advanced_logic": False,
        "extra_shared_abilities": False,
        "exp_zero_in_pool": False,
        "death_link": False,
        "donald_death_link": False,
        "goofy_death_link": False,
        "remote_items": True,
        "shorten_go_mode": False
    },
    # Puppies are found individually, and the goal is to return them all.
    "Puppy Hunt": {
        "final_rest_door_key": FinalRestDoorKey.option_puppies,
        "end_of_the_world_unlock": EndoftheWorldUnlock.option_item,
        "required_lucky_emblems_eotw": 13,
        "required_lucky_emblems_door": 13,
        "lucky_emblems_in_pool": 13,
        "required_postcards": 10,
        "required_puppies": 99,
        
        "super_bosses": False,
        "atlantica": False,
        "hundred_acre_wood": False,
        "cups": False,
        "jungle_slider": False,
        "randomize_emblem_pieces": False,
        "randomize_postcards": RandomizePostcards.option_all,
        
        "exp_multiplier": 48,
        "level_checks": 99,
        "slot_2_level_checks": 33,
        "force_stats_and_abilities_on_levels": 1,
        "strength_increase": 24,
        "defense_increase": 24,
        "hp_increase": 23,
        "ap_increase": 18,
        "mp_increase": 7,
        "accessory_slot_increase": 1,
        "item_slot_increase": 3,
        
        "keyblades_unlock_chests": False,
        "keyblade_stats": KeybladeStats.option_shuffle,
        "bad_starting_weapons": False,
        "keyblade_max_str": 14,
        "keyblade_min_str": 3,
        "keyblade_max_crit_rate": 200,
        "keyblade_min_crit_rate": 0,
        "keyblade_max_crit_str": 16,
        "keyblade_min_crit_str": 0,
        "keyblade_max_recoil": 90,
        "keyblade_min_recoil": 1,
        "keyblade_max_mp": 3,
        "keyblade_min_mp": -2,
        
        "randomize_puppies": True,
        "puppy_value": 1,
        "starting_worlds": 0,
        "starting_tools": True,
        "interact_in_battle": False,
        "advanced_logic": False,
        "extra_shared_abilities": False,
        "exp_zero_in_pool": False,
        "death_link": False,
        "donald_death_link": False,
        "goofy_death_link": False,
        "remote_items": True,
        "shorten_go_mode": False
    },
    # Advanced playthrough with most settings on.
    "Advanced": {
        "final_rest_door_key": FinalRestDoorKey.option_lucky_emblems,
        "end_of_the_world_unlock": EndoftheWorldUnlock.option_lucky_emblems,
        "required_lucky_emblems_eotw": 7,
        "required_lucky_emblems_door": 10,
        "lucky_emblems_in_pool": 13,
        "required_postcards": 10,
        "required_puppies": 99,
        
        "super_bosses": True,
        "atlantica": True,
        "hundred_acre_wood": True,
        "cups": True,
        "jungle_slider": True,
        "randomize_emblem_pieces": True,
        "randomize_postcards": RandomizePostcards.option_all,
        
        "exp_multiplier": 48,
        "level_checks": 99,
        "slot_2_level_checks": 33,
        "force_stats_and_abilities_on_levels": 1,
        "strength_increase": 24,
        "defense_increase": 24,
        "hp_increase": 23,
        "ap_increase": 18,
        "mp_increase": 7,
        "accessory_slot_increase": 1,
        "item_slot_increase": 3,
        
        "keyblades_unlock_chests": True,
        "keyblade_stats": KeybladeStats.option_shuffle,
        "bad_starting_weapons": True,
        "keyblade_max_str": 14,
        "keyblade_min_str": 3,
        "keyblade_max_crit_rate": 200,
        "keyblade_min_crit_rate": 0,
        "keyblade_max_crit_str": 16,
        "keyblade_min_crit_str": 0,
        "keyblade_max_recoil": 90,
        "keyblade_min_recoil": 1,
        "keyblade_max_mp": 3,
        "keyblade_min_mp": -2,
        
        "randomize_puppies": True,
        "puppy_value": 3,
        "starting_worlds": 0,
        "starting_tools": True,
        "interact_in_battle": True,
        "advanced_logic": True,
        "extra_shared_abilities": True,
        "exp_zero_in_pool": True,
        "death_link": False,
        "donald_death_link": False,
        "goofy_death_link": False,
        "remote_items": True,
        "shorten_go_mode": False
    },
    # Playthrough meant to enhance the level 1 experience.
    "Level 1": {
        "final_rest_door_key": FinalRestDoorKey.option_lucky_emblems,
        "end_of_the_world_unlock": EndoftheWorldUnlock.option_lucky_emblems,
        "required_lucky_emblems_eotw": 7,
        "required_lucky_emblems_door": 10,
        "lucky_emblems_in_pool": 13,
        "required_postcards": 10,
        "required_puppies": 99,
        
        "super_bosses": False,
        "atlantica": False,
        "hundred_acre_wood": False,
        "cups": False,
        "jungle_slider": False,
        "randomize_emblem_pieces": False,
        "randomize_postcards": RandomizePostcards.option_all,
        
        "exp_multiplier": 16,
        "level_checks": 0,
        "slot_2_level_checks": 0,
        "force_stats_and_abilities_on_levels": 101,
        "strength_increase": 0,
        "defense_increase": 0,
        "hp_increase": 0,
        "mp_increase": 0,
        "accessory_slot_increase": 6,
        "item_slot_increase": 5,
        
        "keyblades_unlock_chests": False,
        "keyblade_stats": KeybladeStats.option_shuffle,
        "bad_starting_weapons": False,
        "keyblade_max_str": 14,
        "keyblade_min_str": 3,
        "keyblade_max_crit_rate": 200,
        "keyblade_min_crit_rate": 0,
        "keyblade_max_crit_str": 16,
        "keyblade_min_crit_str": 0,
        "keyblade_max_recoil": 90,
        "keyblade_min_recoil": 1,
        "keyblade_max_mp": 3,
        "keyblade_min_mp": -2,
        
        "randomize_puppies": True,
        "puppy_value": 3,
        "starting_worlds": 0,
        "starting_tools": True,
        "interact_in_battle": False,
        "advanced_logic": False,
        "extra_shared_abilities": False,
        "exp_zero_in_pool": False,
        "death_link": False,
        "donald_death_link": False,
        "goofy_death_link": False,
        "remote_items": True,
        "shorten_go_mode": False
    }
}
