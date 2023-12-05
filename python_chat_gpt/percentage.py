def calculate_percentage(part, whole):
    """
    Calculate the percentage of a part with respect to the whole.
    """
    percentage = (part / whole) * 100
    return percentage

# Example usage:
total_marks = 500
obtained_marks = 375

percentage_obtained = calculate_percentage(obtained_marks, total_marks)
print(f"Percentage obtained: {percentage_obtained:.2f}%")
