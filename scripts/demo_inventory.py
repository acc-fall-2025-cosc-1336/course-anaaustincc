"""Non-interactive demo for inventory helpers.

This script demonstrates `add_inventory` and `remove_inventory_widget`
without requiring interactive input, so it's easier to run in CI or
restricted environments.
"""

import os
import sys

# Ensure repo root is on sys.path when executed from project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget


def demo():
    inv = {}
    print('Initial inventory:', inv)

    add_inventory(inv, 'WidgetA', 10)
    print('After adding WidgetA 10 ->', inv)

    add_inventory(inv, 'WidgetA', -3)
    print('After decrementing WidgetA by 3 ->', inv)

    add_inventory(inv, 'WidgetB', 5)
    print('After adding WidgetB 5 ->', inv)

    res = remove_inventory_widget(inv, 'WidgetA')
    print('Remove WidgetA ->', res)
    print('Final inventory:', inv)


if __name__ == '__main__':
    demo()
