rec1 = ("pasta", "Italian", "40 min", "medium")
rec2 = ("Chicken Biryani", "Indian", "1 hr", "Hard")

all_recs = (rec1, rec2)
print(rec2[-4])

print(rec1[0:3])

print(all_recs[0][0])

print("\nPasta Recipe Details")
for detail in rec1:
    print(" -", detail)

pasta_ing = {"pasta rolls", "sauce", "extra sauce", "extra extra sauce", "extra extra extra sauce", "flowers"}
biryani_ing = {"Rice", "sauce", "chicken", "extra sauce", "extra rice", "extra extra rice"}

print("\nPasta ingredients:", pasta_ing)
print("Biryani ingerdients", biryani_ing)
print("Total pasta ingredients", len(pasta_ing))

pasta_ing.add("extra extra extra extra sauce")
pasta_ing.discard("pasta rolls")
print("\nUpdated pasta ingredients:", pasta_ing)

all_ing = pasta_ing.union(biryani_ing)
common = pasta_ing.intersection(biryani_ing)
only_pasta = pasta_ing.difference(biryani_ing)
unique_to_each = pasta_ing.symmetric_difference(biryani_ing)

print("\nAll ingredients (union):", all_ing)
print("Common ingredients (intersection):", common)
print("Only in pasta (difference):", only_pasta)
print("not shared (sym). difference:", unique_to_each)