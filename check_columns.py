import matplotlib.pyplot as plt

# -------------------------
# Karnataka Districts
# -------------------------
north_districts = [
    "Belagavi", "Bagalkot", "Bidar", "Kalaburagi", "Raichur", "Yadgir",
    "Ballari", "Koppal", "Vijayapura", "Dharwad", "Gadag", "Haveri",
    "Uttara Kannada"
]

south_districts = [
    "Tumkur", "Mandya", "Mysuru", "Hassan", "Chikkamagaluru", "Bengaluru Urban",
    "Bengaluru Rural", "Ramanagara", "Kolar", "Chikkaballapur", "Chamarajanagar",
    "Kodagu", "Dakshina Kannada", "Udupi", "Shivamogga", "Davangere"
]

# -------------------------
# Crop yield patterns
# -------------------------
crop_yield_patterns = {
    "North Karnataka": {
        "Jowar": {"Kharif":3,"Rabi":2,"Summer":1},
        "Bajra": {"Kharif":3,"Rabi":1,"Summer":1},
        "Maize": {"Kharif":3,"Rabi":2,"Summer":1},
        "Cotton": {"Kharif":2,"Rabi":1,"Summer":1},
        "Groundnut": {"Kharif":3,"Rabi":2,"Summer":1},
        "Wheat": {"Kharif":2,"Rabi":2,"Summer":1},
        "Sugarcane": {"Kharif":3,"Rabi":2,"Summer":2}
    },
    "South Karnataka": {
        "Paddy": {"Kharif":2,"Rabi":3,"Summer":2},
        "Ragi": {"Kharif":2,"Rabi":3,"Summer":2},
        "Turmeric": {"Kharif":3,"Rabi":3,"Summer":2},
        "Coconut": {"Kharif":3,"Rabi":3,"Summer":2},
        "Arecanut": {"Kharif":3,"Rabi":3,"Summer":2},
        "Banana": {"Kharif":3,"Rabi":3,"Summer":2},
        "Sugarcane": {"Kharif":3,"Rabi":3,"Summer":2},
        "Tobacco": {"Kharif":2,"Rabi":2,"Summer":1}
    }
}

season_reason = {
    "Kharif": "Good rainfall supports maximum growth, leading to high yield.",
    "Rabi": "Cool climate with limited water leads to moderate yield.",
    "Summer": "High temperature and low soil moisture lead to low yield."
}

# -------------------------
# 1. Ask District
# -------------------------
district = input("Enter District Name: ").title()
if district in north_districts:
    region = "North Karnataka"
elif district in south_districts:
    region = "South Karnataka"
else:
    print("District not found in Karnataka dataset.")
    exit()
print(f"\nDetected Region: {region}")

# -------------------------
# 2. Ask Season
# -------------------------
season = input("Enter Season (Kharif / Rabi / Summer): ").title()
if season not in ["Kharif","Rabi","Summer"]:
    print("Invalid season.")
    exit()

# -------------------------
# 3. Show crops suitable for this season
# -------------------------
available_crops = []
for crop, yields in crop_yield_patterns[region].items():
    if yields[season] >= 2:
        available_crops.append(crop)
if not available_crops:
    print(f"No suitable crops for {season} in {region}.")
    exit()
print(f"\nCrops suitable for {season} in {region}: {', '.join(available_crops)}")

# -------------------------
# 4. Ask crop
# -------------------------
crop = input("Select a crop from the list above: ").title()
if crop not in available_crops:
    print("Invalid crop selection.")
    exit()

# -------------------------
# 5. Show expected yield & reason
# -------------------------
yield_level = crop_yield_patterns[region][crop][season]
yield_text = {1:"LOW",2:"MODERATE",3:"HIGH"}
print(f"\n🌾 Expected Yield for {crop} in {district} during {season}: {yield_text[yield_level]}")
print("Reason:", season_reason[season])

# 7. Plot scatter + bar chart side by side
# -------------------------
seasons = ["Kharif","Rabi","Summer"]
fig, axes = plt.subplots(1, 2, figsize=(14,6))

# --- Scatter plot for selected crop ---
values = [crop_yield_patterns[region][crop][s] for s in seasons]
axes[0].scatter(seasons, values, s=150, c='green')
axes[0].set_title(f"{crop} Yield Levels ({district})")
axes[0].set_xlabel("Season")
axes[0].set_ylabel("Yield Level (1-Low, 2-Moderate, 3-High)")
axes[0].set_ylim(0, 4)
axes[0].grid(True)

# --- Bar chart for all crops with 3 colors for seasons ---
x = range(len(crop_yield_patterns[region]))
bar_width = 0.25

# Assign a color for each season
season_colors = {"Kharif":"green", "Rabi":"orange", "Summer":"blue"}

for i, s in enumerate(seasons):
    heights = [crop_yield_patterns[region][c][s] for c in crop_yield_patterns[region]]
    axes[1].bar([p + i*bar_width for p in x], heights, width=bar_width, color=season_colors[s], label=s)

axes[1].set_xticks([p + bar_width for p in x])
axes[1].set_xticklabels(list(crop_yield_patterns[region].keys()), rotation=45, ha='right')
axes[1].set_ylim(0, 4)
axes[1].set_title(f"All Crops Yield Comparison ({region})")
axes[1].set_ylabel("Yield Level")
axes[1].legend()
axes[1].grid(axis='y')

plt.tight_layout()
plt.show()

print("\nGraphs displayed successfully!")
