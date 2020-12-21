#!/usr/bin/env python3

"""Allergen detection using set logic"""


import fileinput
from collections import Counter


def sol(lines):
    allergen_map = {}
    ingredient_count = Counter()
    for line in lines:
        ing_txt, all_txt = line.split(' (contains')
        ingredients = ing_txt.strip().split()
        allergens = all_txt.strip()[:-1].split(', ')

        ingredient_count.update(ingredients)
        for a in allergens:
            if a not in allergen_map:
                allergen_map[a] = set(ingredients)
            else:
                allergen_map[a] = allergen_map[a] & set(ingredients)

    # count non-allergenic ingredients
    allergenic_ingredients = set()
    for ingredients in allergen_map.values():
        allergenic_ingredients |= ingredients

    cnt = 0
    for i in ingredient_count:
        if i not in allergenic_ingredients:
            cnt += ingredient_count[i]
    print(f'part A: {cnt}')

    # deduce allergens from allergenic ingredients
    allergen_ingredient_combos = []
    while allergen_map:
        for allergen, ingredients in allergen_map.items():
            if len(ingredients) == 1:
                allergen_map.pop(allergen)
                allergenic_ingredient = ingredients.pop()
                allergen_ingredient_combos.append((allergen,
                                                   allergenic_ingredient))
                for ingredients in allergen_map.values():
                    ingredients.discard(allergenic_ingredient)
                break

    allergen_ingredient_combos.sort()
    res = ','.join([t[1] for t in allergen_ingredient_combos])
    print(f'part B: {res}')


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
