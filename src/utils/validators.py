def validate_classification_output(data: dict):
    """Ensure classifier agent returns correct JSON structure."""
    required_keys = {
        "experience_level": str,
        "learning_style": str,
        "goal": str,
        "recommended_track": str,
        "confidence": (float, int),
    }

    for key, expected_type in required_keys.items():
        if key not in data:
            raise ValueError(f"Missing key: {key}")
        if not isinstance(data[key], expected_type):
            raise TypeError(f"Invalid type for {key}: expected {expected_type}, got {type(data[key])}")

    if data["recommended_track"] not in ["practical", "academic", "comprehensive"]:
        raise ValueError(f"Invalid recommended_track: {data['recommended_track']}")

    if not 0 <= float(data["confidence"]) <= 1:
        raise ValueError(f"Confidence must be between 0 and 1")
