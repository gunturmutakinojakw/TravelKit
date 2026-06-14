# === Stage 18: Add an activity log with timestamps and action names ===
# Project: TravelKit
class ActivityLogger:
    def __init__(self, log_file="travelkit.log"):
        self.log_file = log_file
        from datetime import datetime
        self._now = datetime.now()

    def _format(self, action):
        return f"[{self._now.strftime('%Y-%m-%d %H:%M:%S')}] {action}"

    def log_action(self, user, action_name, details=""):
        entry = f"{self._format(f'{user}: {action_name}')}{f' | {details}' if details else ''}\n"
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(entry)

    def log_entry_created(self, user):
        self.log_action(user, "ENTRY_CREATED")

    def log_place_added(self, user, place_name):
        self.log_action(user, "PLACE_ADDED", details=place_name)

    def log_expense_recorded(self, user, amount, category):
        self.log_action(
            user,
            "EXPENSE_RECORDED",
            details=f"amount={amount},category={category}"
        )

    def log_day_plan_updated(self, user, day_num):
        self.log_action(user, "DAY_PLAN_UPDATED", details=f"day={day_num}")
