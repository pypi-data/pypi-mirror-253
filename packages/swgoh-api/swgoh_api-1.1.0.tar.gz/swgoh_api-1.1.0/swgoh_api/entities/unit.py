class Unit(object):
    UNIT = 0
    SHEEP = 1

    def __init__(self, data):
        self.id = data["base_id"]
        self.name = data["name"]
        self.galactic_power = data["power"]
        self.stars = data["rarity"]
        self.kind = Unit.UNIT if data["combat_type"] == 1 else Unit.SHEEP
        if self.kind == Unit.UNIT:
            self.gear_level = data["gear_level"]
            self.relic = data["relic_tier"] - 2

    def check_requirement(self, req):
        for key in req.require:
            if hasattr(self, key):
                val = self.__getattribute__(key)
                if val < req.require[key]:
                    return False
        return True
