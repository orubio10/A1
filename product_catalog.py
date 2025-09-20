from product_data import products

def get_preferences():
    prefs = []
    while True:
        pref = input("Input a preference: ").strip().lower()
        if pref == "n":
            break
        if pref:
            prefs.append(pref)
        again = input("Do you want to add another preference? (Y/N): ").strip().lower()
        if again != "y":
            break
    return prefs

def recommend_products(products, prefs):
    pref_set = set(prefs)
    recs = []
    for p in products:
        tags = set(t.lower() for t in p["tags"])
        matches = len(tags & pref_set)
        if matches > 0:
            recs.append((p["name"], matches))
    recs.sort(key=lambda x: (-x[1], x[0]))
    return recs

def main():
    for p in products[:3]:
        print(f"- {p['name']}: {p['tags']}")
    prefs = get_preferences()
    recs = recommend_products(products, prefs)
    print("\nRecommended Products:\n")
    if not recs:
        print("No matches found.")
    else:
        for name, m in recs:
            print(f"- {name} ({m} match{'es' if m > 1 else ''})")

if __name__ == "__main__":
    main()