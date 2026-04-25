def search_data(data, keyword):
    results = [item for item in data if keyword.lower() in str(item).lower()]

    print("\n--- Search Results ---")
    for item in results:
        print(item)

    if not results:
        print("No results found.")