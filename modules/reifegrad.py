import json

def load_questions_from_json(json_path: str) -> dict:
    """
    Lädt Fragen aus einer JSON-Datei.
    
    Args:
        json_path (str): Pfad zur JSON-Datei.
        
    Returns:
        dict: Enthält 'topic' und 'questions'.
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
