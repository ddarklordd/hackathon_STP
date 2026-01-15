import csv
import math
from getStp import STP
file_path = "../data/"
# Define a class to hold Farm data
class Farm:
    def __init__(self, farm_id, zone, area_ha, lat, lon):
        self.farm_id = farm_id
        self.zone = zone
        self.area_ha = float(area_ha)
        self.lat = float(lat)
        self.lon = float(lon)

    def __repr__(self):
        return (f"Farm({self.farm_id}, zone={self.zone}, "
                f"area_ha={self.area_ha}, lat={self.lat}, lon={self.lon})")

    # Method to calculate distance to another farm using Haversine formula
    def distance_to(self, other_farm):
        # Convert degrees to radians
        lat1, lon1 = math.radians(self.lat), math.radians(self.lon)
        lat2, lon2 = math.radians(other_farm.lat), math.radians(other_farm.lon)

        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        # Earth radius in kilometers
        R = 6371.0
        return R * c

# Read CSV into a dictionary keyed by farm_id
farm_registry = {}
with open(file_path+"farm_locations.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        farm = Farm(
            row["farm_id"],
            row["zone"],
            row["area_ha"],
            row["lat"],
            row["lon"]
        )
        farm_registry[farm.farm_id] = farm

# Function to get Farm object by id
def get_farm(farm_id):
    return farm_registry.get(farm_id)

# Function to get total number of farms
def total_farms():
    return len(farm_registry)

# Function to get all farm_ids in a particular zone
def farms_in_zone(zone_name):
    return [farm.farm_id for farm in farm_registry.values() if farm.zone == zone_name]

# Function to get the farm_id with maximum area
def farm_with_max_area():
    max_farm = max(farm_registry.values(), key=lambda f: f.area_ha)
    return max_farm.farm_id


"""
# Example usage:
print("Total farms:", total_farms())
print("Farms in Kuttanad:", farms_in_zone("Kuttanad"))
print("Farm with maximum area:", farm_with_max_area())

farm1 = get_farm("F_1000")
farm2 = get_farm("F_1001")
print(f"Distance between {farm1.farm_id} and {farm2.farm_id}: {farm1.distance_to(farm2):.2f} km")
"""
