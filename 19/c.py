#!/usr/bin/env python3

"""Build a trie of valid words"""


import fileinput
import re
from typing import Dict, List, Union


def parse_rules(lines: List[str]) -> Dict[int, str]:
    rules = {}
    for line in lines:
        if line and line[0].isdigit():
            name, rule = line.split(': ')
            rules[int(name)] = rule
    return rules


def parse_messages(lines: List[str]) -> List[str]:
    messages = []
    for line in lines:
        if line and line[0].isalpha():
            messages.append(line)
    return messages


def build_rule_graph(rules: Dict[int, str]) -> Dict[int, Union[str, List[List[str]]]]:
    graph = {}
    for name, rule in rules.items():
        if rule == '"a"':
            graph[name] = 'a'
        elif rule == '"b"':
            graph[name] = 'b'
        else:
            graph[name] = []
            for r in rule.split(' | '):
                graph[name].append(list(map(int, r.split())))
    return graph


def get_regexpr(graph, rule):
    if isinstance(graph[rule], str):
        return graph[rule]  # base case: found concrete substring

    regexpr = []
    for ruleset in graph[rule]:
        sub_regexpr = []
        for subrule in ruleset:
            sub_regexpr.append(get_regexpr(graph, subrule))
        regexpr.append(''.join(sub_regexpr))

    return '(' + '|'.join(regexpr) + ')'


def sol(lines):
    rules = parse_rules(lines)
    messages = parse_messages(lines)
    graph = build_rule_graph(rules)
    pattern = re.compile(get_regexpr(graph, 0))
    cnt = 0
    for m in messages:
        if pattern.fullmatch(m):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    lines = [l.strip() for l in fileinput.input()]
    sol(lines)
