import re
import whois


def extract_email(text):
    """Extracts an email address from the given text using regex."""
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    match = re.search(pattern, text)
    return match.group() if match else None


def get_domain_age(domain):
    """Fetches the creation date of a domain using WHOIS."""
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date

        # Handle cases where creation_date is a list or None
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        elif creation_date is None:
            return "Creation date not available"

        return creation_date
    except Exception as e:
        return f"Error fetching domain age: {e}"


def main():
    print("Welcome to the Domain Age Checker and Email Extractor!")
    print("------------------------------------------------------")

    while True:
        print("\nWhat would you like to do?")
        print("1. Check the age of a domain")
        print("2. Extract an email from text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            # Domain Age Checker
            domain = input("\nEnter a domain (e.g., example.com): ").strip()
            if not domain:
                print("Please enter a valid domain.")
                continue

            result = get_domain_age(domain)
            print(f"\nDomain: {domain}")
            print(f"Creation Date: {result}")

        elif choice == '2':
            # Email Extractor
            text = input(
                "\nEnter some text to extract an email (or type 'skip' to go back): "
            ).strip()
            if text.lower() == 'skip':
                continue

            email = extract_email(text)
            if email:
                print(f"\nEmail found: {email}")
            else:
                print("\nNo email found in the provided text.")

        elif choice == '3':
            # Exit
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
