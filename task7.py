def check_voting_eligibility(age):
    try:
        age = float(age)
        if age < 0:
            return "Invalid input: Age cannot be negative"
        elif age >= 18:
            return "You are eligible to vote"
        else:
            years_left = 18 - int(age)
            return f"You are allowed to vote after {years_left} years"
    except ValueError:
        return "Invalid input: Please enter a valid number"

def main():
    age = input("Enter your age: ")
    result = check_voting_eligibility(age)
    print(result)

if __name__ == "__main__":
    main()
