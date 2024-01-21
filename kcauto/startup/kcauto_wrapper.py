import traceback
from pyvisauto import FindFailed
from time import sleep

import startup.kcauto as _
import args.args_core as arg
from constants import LOOP_BREAK_SECONDS
from util.exceptions import (
    ApiException, Catbomb201Exception, ChromeCrashException)
from util.logger import Log
from util.recovery import Recovery
import ships.equipment_core as equ 


def kcauto_main():
    """Primary method that contains kcauto and various recovery logic.
    """
    active_loop = True
    kca_loop = True
    while active_loop:
        try:
            # startup methods
            _.kcauto.find_browser()
            _.kcauto.start_kancolle()
            _.kcauto.find_kancolle()

            
            if arg.args.parsed_args.save_equipment:
                equ.equipment.save_loaded_equipment()
                #kcauto should end here

            while kca_loop:
                # primary logic
                _.kcauto.hook_health_check()
                _.kcauto.check_config()
                if _.kcauto.scheduler_kca_active:
                    #if first_loop == True:

                    Log.log_debug("New kca_loop started")

                    _.kcauto.initialization_check()
                    _.kcauto.run_expedition_logic()
                    _.kcauto.run_factory_logic()
                    _.kcauto.run_pvp_logic()
                    _.kcauto.run_combat_logic()

                    _.kcauto.run_repair_logic()
                    _.kcauto.run_shipswitch_logic()
                    _.kcauto.check_end_loop_at_port()
                    _.kcauto.print_stats()
                _.kcauto.run_scheduler()
                sleep(LOOP_BREAK_SECONDS)
        except FindFailed:
            Log.log_error("FindFailed stacktrace:")
            print(traceback.format_exc())
            Log.log_error("End stacktrace.")
            if not Recovery.attempt_recovery():
                Log.log_error("Recovery failed. Shutting down kcauto.")
                active_loop = False
        except ApiException:
            Log.log_error("ApiException stacktrace:")
            print(traceback.format_exc())
            Log.log_error("End stacktrace.")
            if not Recovery.recovery_from_catbomb():
                Log.log_error("Recovery failed. Shutting down kcauto.")
                active_loop = False
        except Catbomb201Exception:
            Log.log_error("Catbomb201Exception stacktrace:")
            print(traceback.format_exc())
            Log.log_error("End stacktrace.")
            if not Recovery.recovery_from_catbomb(catbomb_201=True):
                Log.log_error("Recovery failed. Shutting down kcauto.")
                active_loop = False
        except ChromeCrashException:
            Log.log_error("ChromeCrashException stacktrace:")
            print(traceback.format_exc())
            Log.log_error("End stacktrace.")
            if not Recovery.recovery_from_chrome_crash(crash_type=2):
                Log.log_error("Recovery failed. Shutting down kcauto.")
                active_loop = False
