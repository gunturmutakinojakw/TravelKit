# === Stage 19: Add undo support for the last simple mutation ===
# Project: TravelKit
import json
from datetime import datetime, timedelta

class TravelKit:
    def __init__(self):
        self.history = []
    
    def _save_state(self):
        state = {
            "packing_list": self.packing_list.copy(),
            "places": [p.copy() for p in self.places],
            "expenses": [e.copy() for e in self.expenses],
            "day_plans": [d.copy() for d in self.day_plans]
        }
        self.history.append(state)
    
    def add_item(self, item):
        if len(self.history) >= 10:
            del self.history[0]
        self.packing_list.append(item)
        self._save_state()
    
    def remove_item(self, index):
        if not self.packing_list or index < 0 or index >= len(self.packing_list):
            return False
        item = self.packing_list.pop(index)
        if len(self.history) >= 10:
            del self.history[0]
        else:
            state = {
                "packing_list": self.packing_list.copy(),
                "places": [p.copy() for p in self.places],
                "expenses": [e.copy() for e in self.expenses],
                "day_plans": [d.copy() for d in self.day_plans]
            }
            self.history.append(state)
        return True
    
    def undo(self):
        if not self.history:
            return False
        state = self.history.pop()
        self.packing_list[:] = state["packing_list"]
        self.places[:] = state["places"]
        self.expenses[:] = state["expenses"]
        self.day_plans[:] = state["day_plans"]
        return True

# Example usage:
if __name__ == "__main__":
    kit = TravelKit()
    kit.add_item("Passport")
    kit.add_item("Sunscreen")
    kit.remove_item(1)  # Remove Sunscreen
    print(f"Current list: {kit.packing_list}")
    kit.undo()
    print(f"After undo: {kit.packing_list}")
