
import csv
file_path = "../data/"
# Define a class to hold STP data
class STP:
    def __init__(self, stp_id, daily_output, storage_max, lat, lon):
        self.stp_id = stp_id
        self.daily_output = int(daily_output)
        self.storage_max = int(storage_max)
        self.lat = float(lat)
        self.lon = float(lon)

    def __repr__(self):
        return (f"STP({self.stp_id}, daily_output={self.daily_output}, "
                f"storage_max={self.storage_max}, lat={self.lat}, lon={self.lon})")

# Read CSV into a dictionary keyed by stp_id
stp_registry = {}
with open(file_path+"stp_registry.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        stp = STP(
            row["stp_id"],
            row["daily_output_tons"],
            row["storage_max_tons"],
            row["lat"],
            row["lon"]
        )
        stp_registry[stp.stp_id] = stp

# Function to get STP object by id
def get_stp(stp_id):
    return stp_registry.get(stp_id)


"""
# Example usage:
stp = get_stp("STP_TVM")
print(stp)                 # STP(STP_TVM, daily_output=30, storage_max=500, lat=8.468, lon=76.936)
print(stp.daily_output)    # 30
print(stp.storage_max)     # 500
print(stp.lat, stp.lon)    # 8.468 76.936
"""