def analyze_result(status, physics):
    if status == "CRASH":
        return {
            "title": "MISSION FAILED",
            "msg": "VEHICLE DESTROYED ON IMPACT.",
            "type": "error"
        }
    elif status == "LANDED":
        return {
            "title": "MISSION ACCOMPLISHED",
            "msg": "SUCCESSFUL SOFT LANDING CONFIRMED.",
            "type": "success"
        }
    return None