import csv
file_path = "../data/"
class DailyNDemand:
    def __init__(self, date, demand_dict):
        """
        date: string representing the date
        demand_dict: dictionary {farm_id: n_demand_kg (float)}
        """
        self.date = date
        self.n_demand = demand_dict

    def get_demand(self, farm_id):
        """Return nitrogen demand for a given farm_id"""
        return self.n_demand.get(farm_id, None)

    def total_demand(self):
        """Return total nitrogen demand across all farms for this date"""
        return sum(self.n_demand.values())

    def __repr__(self):
        return f"DailyNDemand(date={self.date}, farms={len(self.n_demand)})"


def load_daily_n_demand(filename):
    """
    Reads the CSV and returns a dictionary of {date: DailyNDemand}
    Assumes CSV has columns: date, F_1000, F_1001, ...
    """
    daily_records = {}
    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = row["date"]
            # Build dictionary of farm_id -> float demand
            demand_dict = {farm_id: float(value) for farm_id, value in row.items() if farm_id != "date"}
            daily_records[date] = DailyNDemand(date, demand_dict)
    return daily_records


# Example usage:
daily_data = load_daily_n_demand(file_path+"daily_n_demand.csv")

"""
# Access a specific date
day = daily_data["2025-01-15"]   # example date
print(day)                       # DailyNDemand(date=2026-01-15, farms=...)
print(day.get_demand("F_1000"))  # nitrogen demand for farm F_1000
print(day.total_demand())        # total demand across all farms
print(day.n_demand)              # full dictionary of farm_id -> n_demand_kg
"""