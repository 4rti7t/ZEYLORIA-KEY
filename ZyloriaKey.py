import json
import random
from tqdm import tqdm  # For the loading bar

def load_common_words(country):
    try:
        print("📂 Loading passwords.json file...")
        with open("passwords.json", "r") as file:
            data = json.load(file)
        print("✅ File loaded successfully!")
        return data.get(country, [])
    except FileNotFoundError:
        print("❌ Error: passwords.json file not found.")
        return []

def generate_passwords(common_words, num_passwords, length):
    print("⚙️ Generating passwords...")
    passwords = [
        "".join(random.choices(common_words, k=length))  # Fixed length for each password
        for _ in tqdm(range(num_passwords), desc="🔑 Generating")
    ]
    return passwords

# Start of the script
print("🚀 Welcome to the Modern Password Generator!")

# Ask user for input
try:
    country_name = input("🌍 Enter country name: ").strip()
    print(f"🌟 Selected country: {country_name}")

    num_passwords = int(input("🔢 How many passwords do you want to generate? "))
    password_length = int(input("🔑 Enter the length of each password (e.g., 5): "))

    # Input validation
    if password_length < 4 or password_length > 16:
        raise ValueError("Password length should be between 4 and 16!")
except ValueError as e:
    print(f"⚠️ Input error: {e}")
    print("💡 Using default values: 5 passwords, length 8.")
    num_passwords = 5
    password_length = 8

# Fetch common words and generate passwords
common_words = load_common_words(country_name)
if not common_words:
    print(f"❌ No common words found for {country_name}. Please update passwords.json.")
else:
    print(f"📋 Common words loaded: {common_words}")
    generated_passwords = generate_passwords(common_words, num_passwords, password_length)

    # Save passwords to a file, each on a new line
    with open("generated_passwords.txt", "w") as file:
        for password in generated_passwords:
            file.write(f"{password}\n")
    
    print(f"\n🎉 Generated passwords saved to 'generated_passwords.txt'.")
    print("🎊 Congratulations! Your passwords have been successfully generated and saved! 🎉")

