def calculate(ratings):
    if not ratings:
        return 0.0
    positive_ratings = sum(1 for r in ratings if r >= 4)
    return (positive_ratings / len(ratings)) * 100

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
res = calculate(ratings)

print(f"Positive Feedback: {res :.2f}%")
