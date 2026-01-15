import csv
file_path = "../data/"
class DailyRainfall:
    def __init__(self, date, rainfall_dict):
        """
        date: string representing the date
        rainfall_dict: dictionary {location: rainfall_mm (float)}
        """
        self.date = date
        self.rainfall = rainfall_dict

    def get_rainfall(self, location):
        """Return rainfall in mm for a given location"""
        return self.rainfall.get(location, None)

    def total_rainfall(self):
        """Return total rainfall across all locations for this date"""
        return sum(self.rainfall.values())

    def __repr__(self):
        return f"DailyRainfall(date={self.date}, locations={len(self.rainfall)})"


def load_daily_rainfall(filename):
    """
    Reads the CSV and returns a dictionary of {date: DailyRainfall}
    Assumes CSV has columns: date, Location1, Location2, ...
    """
    daily_records = {}
    with open(file_path+filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = row["date"]
            # Build dictionary of location -> float rainfall
            rainfall_dict = {loc: float(value) for loc, value in row.items() if loc != "date"}
            daily_records[date] = DailyRainfall(date, rainfall_dict)
    return daily_records


# Example usage:
daily_data = load_daily_rainfall("daily_weather_2025.csv")

# Access a specific date
day = daily_data["2025-01-15"]   # example date
print(day)                       # DailyRainfall(date=2026-01-15, locations=...)
print(day.get_rainfall("Kuttanad"))  # rainfall in Hyderabad on that date
print(day.total_rainfall())      # total rainfall across all locations
print(day.rainfall)              # full dictionary of location -> rainfall_mm
