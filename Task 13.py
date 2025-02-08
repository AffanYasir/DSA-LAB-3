def find_longest_streak(streaks):
    max_streak = 0
    user_with_max_streak = 0
    for user, streak in enumerate(streaks):
        current_max = max(streak)
        if current_max > max_streak:
            max_streak = current_max
            user_with_max_streak = user + 1
    return user_with_max_streak, max_streak


streaks = [[5, 3, 7], [2, 6, 4], [8, 1, 9]]
user, streak = find_longest_streak(streaks)
print(f"User {user} has the longest streak of {streak} days.")