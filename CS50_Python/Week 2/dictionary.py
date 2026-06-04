distances= {
        "Voyager 1": 163,
        "Voyager 2": 136,
        "Pioneer 10": 80,
        "New Horizons": 58,
        "Pioneer 11": 44
}

def main():
    spacecraft = {"name": "Voyager 1", "distance": 163}
    print(create_report(spacecraft))

    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")


def create_report(spacecraft):
    return f"""
    ============ REPORT ============
    NAME: {spacecraft["name"]}
    DISTANCE: {spacecraft["distance"]} AU
    ================================
    """

main()