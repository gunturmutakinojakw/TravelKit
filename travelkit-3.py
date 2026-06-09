# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: TravelKit
def validate_trip_data(trip):
    if not isinstance(trip, dict):
        return False, "Trip data must be a dictionary."
    
    required_keys = ['id', 'destination', 'days']
    for key in required_keys:
        if key not in trip:
            return False, f"Missing required field: {key}"
    
    if not isinstance(trip['id'], str) or len(trip['id']) < 3:
        return False, "Trip ID must be a string of at least 3 characters."
    
    if not isinstance(trip['destination'], str) or len(trip['destination']) < 2:
        return False, "Destination must be a non-empty string (min 2 chars)."
    
    if not isinstance(trip['days'], int) or trip['days'] <= 0:
        return False, "Days must be a positive integer."
    
    if 'places' in trip and not isinstance(trip['places'], list):
        return False, "Places must be a list."
    
    if 'expenses' in trip and not isinstance(trip['expenses'], list):
        return False, "Expenses must be a list."
    
    if 'day_plans' in trip and not isinstance(trip['day_plans'], list):
        return False, "Day plans must be a list."
    
    for place in trip.get('places', []):
        if not isinstance(place, dict) or 'name' not in place:
            return False, "Each place must be a dict with a 'name' key."
        
        if not isinstance(place['name'], str) or len(place['name']) < 2:
            return False, "Place name must be a non-empty string (min 2 chars)."
    
    for expense in trip.get('expenses', []):
        if not isinstance(expense, dict) or 'amount' not in expense:
            return False, "Each expense must be a dict with an 'amount' key."
        
        if not isinstance(expense['amount'], (int, float)) or expense['amount'] < 0:
            return False, "Expense amount must be a non-negative number."
    
    for day_plan in trip.get('day_plans', []):
        if not isinstance(day_plan, dict) or 'date' not in day_plan:
            return False, "Each day plan must be a dict with a 'date' key."
        
        if not isinstance(day_plan['date'], str):
            return False, "Day plan date must be a string."
        
        if 'activities' in day_plan and not isinstance(day_plan['activities'], list):
            return False, "Activities must be a list."
            
        for activity in day_plan.get('activities', []):
            if not isinstance(activity, str) or len(activity) < 1:
                return False, "Activity description must be a non-empty string."
    
    return True, "Validation successful."
