raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

unique_users = set(raw_logs)

is_id05_present = "ID05" in unique_users

print("Unique users:", unique_users)
print(f"Original count: {len(raw_logs)}")
print(f"Unique count:   {len(unique_users)}")
print(f"Is 'ID05' present? {is_id05_present}")
