#!/usr/bin/env python3

"""Template for AOC python scripts"""


import fileinput
from typing import List


def parse_ticket(line):
    return list(map(int, line.split(',')))


def parse_input(txt):
    rules, my_tickt, nearby_tickets = [], [], []
    section = 0
    for line in txt:
        if line == '':
            section += 1
        elif section == 0:
            _, valid_ranges = line.split(': ')
            rule = []
            for valid_range in valid_ranges.split(' or '):
                rule += list(map(int, valid_range.split('-')))
            rules.append(rule)
        elif section == 1 and line[0].isdigit():
            my_ticket = parse_ticket(line)
        elif section == 2 and line[0].isdigit():
            nearby_tickets.append(parse_ticket(line))

    return rules, my_ticket, nearby_tickets


def fits_rule(val: int, rule: List[int]):
    return rule[0] <= val <= rule[1] or rule[2] <= val <= rule[3]


def get_invalid_values(ticket: List[int], rules: List[List[int]]) -> List[int]:
    invalid_values = []
    for val in ticket:
        if not any([fits_rule(val, rule) for rule in rules]):
            invalid_values.append(val)
    return invalid_values


def check_tickets(tickets, rules):
    valid_tickets = []
    invalid_values = []
    for ticket in tickets:
        invalid_fields = get_invalid_values(ticket, rules)
        if len(invalid_fields) == 0:
            valid_tickets.append(ticket)
        else:
            invalid_values += invalid_fields
    return valid_tickets, invalid_values


def sol(lines):
    rules, my_ticket, nearby_tickets = parse_input(lines)

    valid_tickets, invalid_values = check_tickets(nearby_tickets, rules)
    print(f'partA: {sum(invalid_values)}')

    return

    # if i find a num that matches only a single rule, that num position points to a fixed rule idx.
    # Later, I only want my nums at the positions pointing at rule indexes 1 - 6
    field_ptrs = {}
    fields = set(range(20))
    # for _ in range(2):
    while fields:
        for field in fields:
            print('\n', fields)
            matched_rules = []
            for ridx, rule in enumerate(rules):
                valid = True
                for nums in valid_nums:
                    if not (rule[0][0] <= nums[field] <= rule[0][1] or rule[1][0] <= nums[field] <= rule[1][1]):
                        valid=False
                        break
                if valid:
                    matched_rules.append(ridx)

            print(f"field {field} matched_rules {matched_rules}")
            if len(matched_rules) == 1:
                print(f"field {field} matched_rules {matched_rules}")
                field_ptrs[field] = matched_rules[0]
                fields.remove(field)
                rules[matched_rules[0]] = [(-1, -1), (-1, -1)]
                break


    print(field_ptrs)

    res = 1
    for field in field_ptrs:
        if field_ptrs[field] < 6:
            res *= MINE[field]

    print(res)




if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)

