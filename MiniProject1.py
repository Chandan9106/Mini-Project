def input_friend_lists():
  
    num_users = int(input("Enter the number of users: "))
    friend_lists = {}


    for _ in range(num_users):
        user = input("Enter user name: ").strip()
        friends_input = input(f"Enter friends of {user} (comma-separated): ").strip()
        if friends_input:
            friends = set(friend.strip() for friend in friends_input.split(','))
        else:
            friends = set()
        friend_lists[user] = friends
    return friend_lists


def find_common_friends(friend_lists):
    """
    Finds common friends among all users using set intersection.

    """
    if not friend_lists:
        print("no users found.")
        return set()
    common_friends = set.intersection(*friend_lists.values())
    if not common_friends:
        print("no common friends found.")
    return common_friends


def find_all_friends(friend_lists):
    """
    Finds all unique friends across all users using set union.

    """
    if not friend_lists:
        print("no users found.")
        return set()
    all_friends = set.union(*friend_lists.values())
    if not all_friends:
        print("no friends found.")
    return all_friends


def find_mutual_friends(friend_lists, user1, user2):
    """
    Finds mutual friends between two specific users.

    """
    if user1 in friend_lists and user2 in friend_lists:
        return friend_lists[user1].intersection(friend_lists[user2])
    else:
        print(f"one or both users '{user1}' and '{user2}' not found in friend lists.")
        return set()


def main():
    friend_lists = input_friend_lists()

    print("\nMenu:")
    print("1. Find common friends among all users")
    print("2. Find all unique friends")
    print("3. Find mutual friends")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            common_friends = find_common_friends(friend_lists)
            print("Common friends among all users:", common_friends)

        elif choice == '2':
            all_friends = find_all_friends(friend_lists)
            print("All unique friends:", all_friends)

        elif choice == '3':
            user1 = input("Enter the first user name: ").strip()
            user2 = input("Enter the second user name: ").strip()
            mutual_friends = find_mutual_friends(friend_lists, user1, user2)
            print(f"Mutual friends between {user1} and {user2}:", mutual_friends)

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
