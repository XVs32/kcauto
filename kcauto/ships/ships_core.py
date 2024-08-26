from ships.ship import Ship
from util.json_data import JsonData
from util.logger import Log
from util.wctf import WhoCallsTheFleetData


class ShipsCore(object):
    max_ship_count = 0
    ship_pool = []
    local_ships_by_production_id = {}
    ship_library = []
    name_db = {}

    def __init__(self):
        Log.log_debug("Initializing Ship core.")
        self.load_wctf_names()

    def update_ship_pool(self, data):
        # from this api call, api_id = local_api_id, and api_ship_id = api_id
        Log.log_debug("Updating ship data from API.")
        self.ship_pool = {}
        for ship in data:
            ship_instance = self.create_ship(
                self.get_ship_static_data(ship["api_sortno"]), ship)
            self.ship_pool[ship['api_id']] = ship_instance
            

    def update_ship_library(self, data):
        Log.log_debug("Updating ship library data.")
        self.ship_library = data
        
    def get_ship_static_data(self,api_sortno):
        for ship in self.ship_library:
            if ship['api_sortno'] == api_sortno:
                return ship

    def load_wctf_names(self, force_update=False):
        if force_update:
            WhoCallsTheFleetData.get_and_save_wgtf_data()

        try:
            temp_db = JsonData.load_json('data|temp|wctf.json')
        except FileNotFoundError:
            WhoCallsTheFleetData.get_and_save_wgtf_data()
            temp_db = JsonData.load_json('data|temp|wctf.json')

        self.name_db = {}
        for key in temp_db:
            self.name_db[int(key)] = temp_db[key]

    @property
    def ship_count(self):
        return len(self.ship_pool)

    def get_ship_from_production_id(self, ship_id):
        
        return self.ship_pool[ship_id]

    def create_ship(self, static_data, local_data = Ship.EMPTY_LOCAL_DATA):
        return Ship(static_data, local_data)
    

ships = ShipsCore()
