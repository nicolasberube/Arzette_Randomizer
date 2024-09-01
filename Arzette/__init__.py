from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld


class ArzetteWebWorld(WebWorld):
    pass  # todo

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteLocation(Location):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteWorld(World):
    game: str = "Arzette: The Jewel of Faramore"
    web = ArzetteWebWorld()
    pass  # todo