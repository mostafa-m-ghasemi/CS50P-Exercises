
def main():
    spacecraft = {
        "name": "James Webb Space Telescope"
    }
    # Adding to dict
    #spacecraft["distance"] = 0.01

    # Update dict
    # spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(creat_report(spacecraft))


def creat_report(spacecraft):
    # Missing value as unknown with .get method
    return f"""

    ========== Report ==========
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    ============================
"""






main()