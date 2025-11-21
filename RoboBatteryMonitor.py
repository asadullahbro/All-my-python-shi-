def analyze_battery(robot_name, level):
    if level == 0:
        return"Offline"
    elif level > 95:
        return"Overcharged"
    elif level < 20:
        return"Low Battery"
    return "Stable"

def process_battery_levels(levels):
    battery_score = lambda score: "⚡ Power Surge" if score > 40 else ""
    for l in levels:
        if l == 0:
            print("Level 0: skipping")
            continue
        elif l > 95:
            print("Overcharged. Stopping checks..")
            break
        if l < 20:
            category = "LOW"
        elif 20 <= l <= 60:
            category = "NORMAL"
        else:
            category = "HIGH"
        if l % 2 == 0:
            score = l / 2
        else:
            score = l * 1.5
        alert = battery_score(score)
        print(f"Level {l}: Category {category}, Score {score}, {alert}")

process_battery_levels([10, 20, 70]) # Insert Readings
