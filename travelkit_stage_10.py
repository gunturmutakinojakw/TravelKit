# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: TravelKit
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query, fields=None):
        if not query:
            return list(self.data)
        
        q_lower = query.lower()
        results = []
        
        for item in self.data:
            match = False
            
            # Check all specified fields or default to keys containing 'name', 'place', 'item'
            check_fields = fields if fields else [k for k in item.keys() if any(x in k.lower() for x in ['name', 'place', 'item'])]
            
            for field_name in check_fields:
                # Handle nested dictionaries safely
                value = self._get_nested_value(item, field_name)
                
                if isinstance(value, str):
                    if q_lower in value.lower():
                        match = True
                        break
                
                # Check list items inside the field (e.g., tags or categories)
                elif isinstance(value, list):
                    for v in value:
                        if isinstance(v, str) and q_lower in v.lower():
                            match = True
                            break
            
            if match:
                results.append(item)
        
        return results
    
    def _get_nested_value(self, obj, key):
        parts = key.split('.')
        current = obj
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return ""
        return current
