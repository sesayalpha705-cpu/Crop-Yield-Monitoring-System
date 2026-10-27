class CropRecord:
    def __init__(self, crop_name, farm_area, harvest_kg):
        self.crop_name = crop_name
        self.farm_area = farm_area
        self.harvest_kg = harvest_kg

    def calculate_yield(self):
        return self.harvest_kg / self.farm_area

    def display_record(self):
        print("Crop:", self.crop_name)
        print("Farm Area:", self.farm_area, "hectares")
        print("Harvest:", self.harvest_kg, "kg")
        print("Yield:", self.calculate_yield(), "kg/hectare")


class CropMonitoringSystem:
    def __init__(self):
        self.system_name = "Crop Yield Monitoring System"
        self.crop_records = []

    def add_crop(self, crop):
        self.crop_records.append(crop)
        print(crop.crop_name, "added successfully!")

    def display_all_crops(self):
        if not self.crop_records:
            print("No crop records available.")
            return

        print("\n--- All Crop Records ---")
        for crop in self.crop_records:
            crop.display_record()


# Create the monitoring system
system = CropMonitoringSystem()

# Create three crop objects
maize = CropRecord("Maize", 2, 3000)
rice = CropRecord("Rice", 3, 4500)
cassava = CropRecord("Cassava", 1.5, 2250)

# Add objects to the list
system.add_crop(maize)
system.add_crop(rice)
system.add_crop(cassava)

# Display all stored records
system.display_all_crops()