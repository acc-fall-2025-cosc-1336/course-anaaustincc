"""Simple inventory helpers for dictionary exercises.

Functions:
- add_inventory(widgets, widget_name, quantity): add or update quantity in-place
- remove_inventory_widget(widgets, widget_name): remove key and return status string
"""

from typing import Dict


def add_inventory(widgets: Dict[str, int], widget_name: str, quantity: int) -> None:
	"""Add quantity for widget_name into widgets dict (in-place).

	If widget_name does not exist, it is created with the provided quantity.
	If it exists, the stored quantity is increased by quantity.

	Raises ValueError for invalid inputs (non-dict, non-string name, or
	non-integer quantity).
	"""
	if not isinstance(widgets, dict):
		raise TypeError("widgets must be a dict")
	if not isinstance(widget_name, str):
		raise TypeError("widget_name must be a string")
	if not isinstance(quantity, int):
		raise TypeError("quantity must be an int")

	current = widgets.get(widget_name, 0)
	widgets[widget_name] = current + quantity


def remove_inventory_widget(widgets: Dict[str, int], widget_name: str) -> str:
	"""Remove widget_name from widgets dict if present.

	Returns 'Record deleted' when a record was removed, otherwise
	returns 'Item not found'. Modifies widgets in-place.
	"""
	if not isinstance(widgets, dict):
		raise TypeError("widgets must be a dict")
	if not isinstance(widget_name, str):
		raise TypeError("widget_name must be a string")

	if widget_name in widgets:
		del widgets[widget_name]
		return 'Record deleted'
	else:
		return 'Item not found'
