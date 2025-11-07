#!/usr/bin/env python3
import json

# Read the current JSON
with open('links.json', 'r') as f:
    data = json.load(f)

# Mapping of melacha names to image filenames
name_to_filename = {
    "Choresh": "choresh.png",
    "Zoreah": "zoreah.png",
    "Kotzair": "kotzair.png",
    "Ma'amir": "maamir.png",
    "Dush": "dush.png",
    "Zoreh": "zoreh.png",
    "Ma'avir": "maavir.png",
    "Mechabeh": "mechabeh.png",
    "Borer": "borer.png",
    "Tochain": "tochain.png",
    "Miraked": "miraked.png",
    "Lush": "lush.png",
    "Ofeh": "ofeh.png",
    "Kotaiv": "kotaiv.png",
    "Mechait": "mechait.png",
    "Goez": "goez.png",
    "Melabain": "melabain.png",
    "Menafetz": "menafetz.png",
    "Tzovayah": "tzovayah.png",
    "Toveh": "toveh.png",
    "Maisach": "maisach.png",
    "Oseh Bei Batel Neirin": "oseh_bei_batel_neirin.png",
    "Boneh": "boneh.png",
    "Oraig": "oraig.png",
    "Potzi'ah": "potziah.png",
    "Koshair": "koshair.png",
    "Matir": "matir.png",
    "Memacheik": "memacheik.png",
    "Tofair": "tofair.png",
    "Ko'reah": "koreah.png",
    "Soiser": "soiser.png",
    "Tzud": "tzud.png",
    "Shochet": "shochet.png",
    "Mafshit": "mafshit.png",
    "Ma'aboid": "maaboid.png",
    "Mechateich": "mechateich.png",
    "Meshartois": "meshartois.png",
    "Hatza'ah": "hatzaah.png",
    "Makeh b'Potash": "makeh_bpotash.png",
}

# Update each melacha with its image path
for melacha_name, filename in name_to_filename.items():
    if melacha_name in data:
        data[melacha_name]["image"] = f"images/{filename}"
        print(f"Updated {melacha_name} with image path")

# Write the updated JSON back
with open('links.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nJSON file updated successfully!")
