def find_all_missing(arr):
    if not arr:
        return "Array is empty"

    full_range = set(range(min(arr), max(arr) + 1))
    given_set = set(arr)
    missing = sorted(full_range - given_set)

    return missing if missing else "No numbers are missing"


arr = list(map(int, input("Enter array elements: ").split()))


print("Missing numbers:", find_all_missing(arr))
