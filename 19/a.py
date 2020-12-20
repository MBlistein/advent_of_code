#!/usr/bin/env python3

"""Build a trie of valid words"""


import fileinput
from typing import Dict, List, Union


def parse_rules(lines: List[str]) -> Dict[int, str]:
    rules = {}
    for line in lines:
        if line and line[0].isdigit():
            num, rule = line.split(': ')
            rules[int(num)] = rule
    return rules


def parse_messages(lines: List[str]) -> List[str]:
    messages = []
    for line in lines:
        if line and line[0].isalpha():
            messages.append(line)
    return messages


def build_rule_graph(rules: Dict[int, str]) -> Dict[int, Union[str, List[List[str]]]]:
    graph = {}
    for num, rule in rules.items():
        if rule == '"a"':
            graph[num] = 'a'
        elif rule == '"b"':
            graph[num] = 'b'
        else:
            graph[num] = []
            for r in rule.split(' | '):
                graph[num].append(list(map(int, r.split())))
    return graph


def get_valid_words(graph, u) -> List[str]:
    """DFS on rule graph. Returns all valis strings generated by rule 'u'"""
    if graph[u] in ['a', 'b']:
        return graph[u]

    strings = []
    for ruleset in graph[u]:
        set_strings = ['']
        for rule in ruleset:
            rstrings = get_valid_words(graph, rule)
            new_set_strings = []
            for s in set_strings:
                for rs in rstrings:
                    new_set_strings.append(s + rs)
            set_strings = new_set_strings
        strings += set_strings

    return strings


class Trie:
    def __init__(self):
        self.trie = {}
        self.match = 'end'

    def eat(self, words):
        for word in words:
            self.add(word)

    def add(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie['end'] = True

    def contains(self, word):
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return trie.get(self.match, False)


def is_valid(message: str, t31: Trie, t42: Trie, segment_length: int):
    i = 0
    n = len(message)
    while i < n and t42.contains(message[i: i + segment_length]):
        i += segment_length

    j = i
    while j < n and t31.contains(message[j: j + segment_length]):
        j += segment_length

    n42 = i // segment_length
    n31 = (j - i) // segment_length
    return j == n and 0 < n31 < n42


def solve_a(graph, messages):
    words = get_valid_words(graph, 0)
    trie = Trie()
    trie.eat(words)
    count = 0
    for m in messages:
        if trie.contains(m):
            count += 1
    print('part A:', count)


def solve_b(graph, messages):
    words_31 = get_valid_words(graph, 31)
    trie_31 = Trie()
    trie_31.eat(words_31)

    words_42 = get_valid_words(graph, 42)
    trie_42 = Trie()
    trie_42.eat(words_42)

    wordlen = len(words_42[0])

    count = 0
    for m in messages:
        count += is_valid(m, trie_31, trie_42, wordlen)
    print('part B:', count)


def sol(lines):
    rules = parse_rules(lines)
    messages = parse_messages(lines)
    graph = build_rule_graph(rules)
    solve_a(graph, messages)
    solve_b(graph, messages)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)