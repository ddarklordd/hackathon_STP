import csv
file_path = "../data/"
from collections import defaultdict

class PlantingSchedule:
    def __init__(self):
        # farm_id -> { crop: {"plant_date": ..., "harvest_date": ...} }
        self.schedule = defaultdict(dict)

    def add_entry(self, farm_id, crop, plant_date, harvest_date):
        self.schedule[farm_id][crop] = {
            "plant_date": plant_date,
            "harvest_date": harvest_date
        }

    def get_farm_schedule(self, farm_id):
        """Return all crops and their dates for a farm_id"""
        return self.schedule.get(farm_id, {})

    def get_crop_schedule(self, farm_id, crop):
        """Return plant/harvest dates for a specific crop in a farm"""
        return self.schedule.get(farm_id, {}).get(crop, None)

    def __repr__(self):
        return f"PlantingSchedule(farms={len(self.schedule)})"


def load_planting_schedule(filename):
    ps = PlantingSchedule()
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ps.add_entry(row["farm_id"], row["crop"], row["plant_date"], row["harvest_date"])
    return ps


# Example usage:
schedule = load_planting_schedule(file_path+"planting_schedule_2025.csv")

# Get full schedule for a farm
print(schedule.get_farm_schedule("F_1035"))
# Example output:
# {
#   "Paddy": {"plant_date": "2025-01-17", "harvest_date": "2025-05-07"},
#   "Paddy": {"plant_date": "2025-05-22", "harvest_date": "2025-09-09"}
# }

# Get specific crop schedule
print(schedule.get_crop_schedule("F_1030", "Tapioca"))
# {"plant_date": "2025-06-06", "harvest_date": "2025-12-03"}
