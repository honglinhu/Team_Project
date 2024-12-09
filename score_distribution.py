import team
import numpy as np
import matplotlib.pyplot as plt


year = input("- 연도 선택(2020, 2021, 2022, 2023): ")
f = year + "1231.csv"
data = team.get_data(f)

search_subject = data["search_subject"]
grades = data["grades"]
male_number = data["male_number"]
female_number = data["female_number"]

male_scores = []
female_scores = []

for i in range(len(grades)):
    grade = grades[i]
    for _ in range(male_number[i]):
        male_scores.append(grade)
    for _ in range(female_number[i]):
        female_scores.append(grade)

plt.rcParams["font.family"] = "AppleGothic"
plt.figure(figsize=(10, 6))
plt.boxplot([male_scores, female_scores], labels=["남성", "여성"])
plt.title(f"{year}학년도 수능 {search_subject}과목 성적분포")
plt.ylabel("성적")

plt.show()
