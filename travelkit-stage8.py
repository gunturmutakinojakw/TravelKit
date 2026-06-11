# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: TravelKit
class FilterMixin:
    def filter_items(self, items=None, status=None, category=None, owner=None, tag=None):
        if items is None:
            items = self.items
        filtered = list(items)
        if status is not None:
            filtered = [i for i in filtered if getattr(i, 'status', None) == status]
        if category is not None:
            filtered = [i for i in filtered if getattr(i, 'category', None) == category]
        if owner is not None:
            filtered = [i for i in filtered if getattr(i, 'owner', None) == owner]
        if tag is not None:
            filtered = [i for i in filtered if getattr(i, 'tags', []) and tag in i.tags]
        return filtered

    def get_by_status(self, status):
        return self.filter_items(status=status)

    def get_by_category(self, category):
        return self.filter_items(category=category)

    def get_by_owner(self, owner):
        return self.filter_items(owner=owner)

    def get_by_tag(self, tag):
        return self.filter_items(tag=tag)
