import csv


def get_subjects(file):
    subjects = set()
    with open(file, newline="", encoding="cp949") as f:
        reader = csv.DictReader(f)
        for row in reader:
            subjects.add(row["유형"])

    return subjects


def get_search_subject(file):
    subjects = list(get_subjects(file))
    print("-", "\n- ".join(subjects))
    search_subject = input("- 유형을 선택하세요: ")
    while True:
        if search_subject in subjects:
            break
        else:
            search_subject = input("없는 유형입니다. 다시 입력해 주세요 > ")

    return search_subject


def get_data(file):
    data = {}
    search_subject = get_search_subject(file)
    data["search_subject"] = search_subject
    data["grades"] = []
    data["male_number"] = []
    data["female_number"] = []

    with open("20231231.csv", newline="", encoding="cp949") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["유형"] == search_subject:
                data["grades"].append(int(row["표준점수"]))
                data["male_number"].append(int(row["남자"]))
                data["female_number"].append(int(row["여자"]))

    return data
