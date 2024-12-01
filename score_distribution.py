import team
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def get_mean(grades, numbers):
    length = len(grades)
    mean = sum([grades[i] * numbers[i] for i in range(length)]) / sum(numbers)

    return mean


def get_std(grades, numbers):
    length = len(grades)
    mean = get_mean(grades, numbers)
    std = (
        sum([(grades[i] - mean) ** 2 * numbers[i] for i in range(length)])
        / sum(numbers)
    ) ** 0.5

    return std


year = input("년도를 입력해 주세요 > ")
f = "20231231.csv"
data = team.get_data(f)

# Define the parameters for the normal distributions
male_mean = get_mean(data["grades"], data["male_number"])
male_std = get_std(data["grades"], data["male_number"])
female_mean = get_mean(data["grades"], data["female_number"])
female_std = get_std(data["grades"], data["female_number"])

# Generate points on the x axis
x = np.linspace(20, 160, 1000)  # Covers more range than the data

# Calculate the PDFs for both distributions
male_pdf = norm.pdf(x, male_mean, male_std)
female_pdf = norm.pdf(x, female_mean, female_std)

# Create the plot
plt.rcParams["font.family"] = "AppleGothic"
plt.figure(figsize=(10, 6))
plt.plot(x, male_pdf, label="남", color="blue")
plt.plot(x, female_pdf, label="여", color="orange")

# Add labels and title
plt.xlabel("점수")
plt.title(f"{year}학년도 수능 {data['search_subject']}과목 성적분포")
plt.legend()

# Hide y-axis numbers
plt.yticks([])

# Show the plot
plt.show()
