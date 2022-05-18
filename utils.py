import json


def get_json():
    """
    Импорт JSON списка
    """
    with open('candidates.json', "r", encoding="UTF-8") as file:
        candidates_json = json.load(file)
        return candidates_json


candidates_list = get_json()


def get_candidates():
    """
    Получение списка имен
    """
    name = []
    for s in candidates_list:
        name.append(s["name"])
    return name


def get_candidate_name(name):
    """
    Получение кандидата по имени
    """
    for candidate in candidates_list:
        if name.title().strip() == candidate["name"]:
            return candidate


def candidate_page_id(pk):
    """
    Получение кандидата по id
    """
    for candidate in candidates_list:
        if pk.title().strip() == candidate["id"]:
            return candidate
    return "Такого кандидата нет в базе"


def find_candidate_name(name):
    """
    Поиск кандидата по имени
    """
    count = 0
    candidates = []
    for candidate in candidates_list:
        if name.lower().strip() in candidate["name"].lower():
            count += 1
            candidates.append(candidate["name"])
    return candidates, count


def find_candidates_skill(skills):
    """
    Поиск кандидата по навыкам
    """
    count = 0
    candidates = []
    for candidate in candidates_list:
        if skills.lower().strip() in candidate["skills"].lower().split(", "):
            count += 1
            candidates.append(candidate["name"])
    return candidates, count

