import re
from datetime import datetime

def verify(context: list) -> dict:
    if not context:
        return {"is_valid": False, "is_fresh": False}

    current_year = datetime.now().year
    years_found = []

    for chunk in context:
        years = re.findall(r"\b(19\d{2}|20\d{2})\b", chunk)
        years_found.extend([int(y) for y in years])

    if years_found:
        latest_year = max(years_found)
        is_fresh = (current_year - latest_year) <= 5
    else:
        is_fresh = True  # no year info → assume okay

    return {
        "is_valid": True,
        "is_fresh": is_fresh,
        "years_detected": years_found
    }
