import json

# Function to read JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to extract Instagram usernames from the JSON data
def extract_usernames(data, key="relationships_following"):
    usernames = set()
    if key in data:
        for entry in data[key]:
            usernames.add(entry['string_list_data'][0]['value'])
    else:  # For the follower JSON file
        for entry in data:
            usernames.add(entry['string_list_data'][0]['value'])
    return usernames

# Function to compare following and followers
def find_non_followers(following, followers):
    return sorted(followers - following)  # Return the difference: people you follow who don't follow back, sorted alphabetically

# Main function
def main(following_file, followers_file):
    # Read the JSON files
    following_data = read_json(following_file)
    followers_data = read_json(followers_file)
    
    # Extract usernames from both files
    following_usernames = extract_usernames(following_data)
    followers_usernames = extract_usernames(followers_data, key=None)
    
    # Find the people who don't follow back
    non_followers = find_non_followers(following_usernames, followers_usernames)
    
    # Output the result
    if non_followers:
        print("People you follow who don't follow you back (sorted alphabetically):")
        for user in non_followers:
            print(user)
        print(len(non_followers), "people in total")
    else:
        print("Everyone you follow follows you back!")

# Replace with your actual file paths if necessary
following_file = 'following.json'
followers_file = 'followers_1.json'

# Run the main function
main(following_file, followers_file)
