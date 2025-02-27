import random
import json


def save_inventory():
    with open("inventory.json", "w") as f:
        json.dump(inventory, f)


def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


# ANSI renk kodları
COLORS = {
    "Blue": "\033[94m",  # 🔵 Blue
    "Purple": "\033[35m",  # 🟣 Purple
    "Pink": "\033[38;5;13m",  # 💖 Pink
    "Red": "\033[31m",  # 🔴 Red
    "Gold": "\033[93m",  # ⭐ GOLD! (Bıçaklar)
    "Reset": "\033[0m"  # Sıfırla
}

cases = [
    ("Negev | Ultralight", "Rare (Blue)", COLORS["Blue"]),
    ("P90 | Freight", "Rare (Blue)", COLORS["Blue"]),
    ("PP-Bizon | Runic", "Rare (Blue)", COLORS["Blue"]),
    ("SG 553 | Ol' Rusty", "Rare (Blue)", COLORS["Blue"]),
    ("P2000 | Gnarled", "Rare (Blue)", COLORS["Blue"]),
    ("P250 | Casette", "Rare (Blue)", COLORS["Blue"]),
    ("SSG 08 | Mainframe 001", "Rare (Blue)", COLORS["Blue"]),
    ("MAG-7 | Monster Call", "Mythical (Purple)", COLORS["Purple"]),
    ("MAC-10 | Allure", "Mythical (Purple)", COLORS["Purple"]),
    ("Galil AR | Connexion", "Mythical (Purple)", COLORS["Purple"]),
    ("MP5-SD | Kitbash", "Mythical (Purple)", COLORS["Purple"]),
    ("Tec-9 | Brother", "Mythical (Purple)", COLORS["Purple"]),
    ("XM1014 | Entombed", "Legendary (Pink)", COLORS["Pink"]),
    ("M4A4 | Tooth Fairy", "Legendary (Pink)", COLORS["Pink"]),
    ("Glock-18 | Vogue", "Legendary (Pink)", COLORS["Pink"]),
    ("Desert Eagle | Printstream", "Ancient (Red)", COLORS["Red"]),
    ("AK-47 | Legion of Anubis", "Ancient (Red)", COLORS["Red"]),
]

knives = [

    ("Nomad Knife | Slaughter", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Safari Mesh", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Case Hardened", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Crimson Web", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Scorched", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Blue Steel", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Vanilla", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Stained", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Forest DDPAT", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Urban Masked", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Nomad Knife | Boreal Forest", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Slaughter", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Night Stripe", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Case Hardened", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Crimson Web", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Scorched", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Blue Steel", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Vanilla", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Stained", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Forest DDPAT", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Urban Masked", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Boreal Forest", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Safari Mesh", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Paracord Knife | Fade", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Slaughter", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Night Stripe", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Case Hardened", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Crimson Web", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Scorched", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Blue Steel", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Vanilla", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Stained", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Forest DDPAT", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Urban Masked", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Boreal Forest", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Survival Knife | Safari Mesh", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Slaughter", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Fade", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Case Hardened", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Crimson Web", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Scorched", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Blue Steel", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Vanilla", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Stained", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Forest DDPAT", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Urban Masked", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Boreal Forest", "Exceedingly Rare (GOLD!)", COLORS["Gold"]),
    ("Skeleton Knife | Safari Mesh", "Exceedingly Rare (GOLD!)", COLORS["Gold"])
]


def generate_float():
    return round(random.uniform(0.00, 1.00), 6)


def generate_pattern():
    return random.randint(1, 1000)


# StatTrak çıkma olasılığı (~10%)
def is_stattrak():
    return random.random() < 0.10


# Kasa açma fonksiyonu
def open_case():
    chance = random.random()

    rarity_chances = {
        "Ancient (Red)": "0.32%",
        "Exceedingly Rare (GOLD!)": "0.26%"
    }

    float_value = generate_float()
    pattern_id = generate_pattern()
    stattrak = "StatTrak™ " if is_stattrak() else ""

    # Bıçak çıkma ihtimali (~0.26%)
    if chance < 0.0026:
        item, rarity, color = random.choice(knives)
        inventory.append(f"{color}{stattrak}{item} ({rarity}) | Float: {float_value} | Pattern: {pattern_id}")
        save_inventory()
        chance_text = f" | Chance: {rarity_chances.get(rarity, '')}" if rarity in rarity_chances else ""
        return f"{color}{stattrak}{item} ({rarity}) | Float: {float_value} | Pattern: {pattern_id}{chance_text}{COLORS['Reset']}"
    else:
        item, rarity, color = random.choices(
            cases,
            weights=[11.41, 11.41, 11.41, 11.41, 11.41, 11.41, 11.41,  # Blue
                     3.19, 3.19, 3.19, 3.19, 3.19,  # Purple
                     1.06, 1.06, 1.06,  # Pink
                     0.32, 0.32],  # Red
            k=1
        )[0]

        chance_text = f" | Chance: {rarity_chances.get(rarity, '')}" if rarity in rarity_chances else ""
        return f"{color}{stattrak}{item} ({rarity}) | Float: {float_value} | Pattern: {pattern_id} {chance_text}{COLORS['Reset']}"

inventory = load_inventory()


def main():
    while True:
        command = input(
            "Enter a number to open cases, type 'inventory' to access your inventory or type 'exit' to quit: ").strip().lower()

        if command == "exit":
            print("Exiting...")
            break

        elif command.isdigit():
            count = int(command)

            print(f"\n🎁 Opening {count} CASES... 🎁\n")
            for _ in range(count):
                item = open_case()
                print(item)

                if "Gold" in item:
                    inventory.append(item)

            print(f"\n🔹{count} CASE OPENED! 🔹\n")


        elif command == "inventory":

            print("\n🛠️ YOUR INVENTORY 🛠️")

            if inventory:

                for item in inventory:
                    print(item)

            else:

                print("Your inventory is empty.")

            print("\n")

        else:
            print("Invalid command. Try again or type 'exit' to quit.")


if __name__ == "__main__":
    main()
