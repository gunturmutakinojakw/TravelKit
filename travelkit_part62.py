# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: TravelKit
class TripScorer:
    def __init__(self, places):
        self.places = {name: data for name, data in places.items()}
    
    def calculate_priority(self, place_name, day_plan=None):
        if place_name not in self.places:
            return 0.0
        base_score = self.places[place_name].get('interest_level', 3) * 10
        distance_penalty = max(0, (self.places[place_name].get('distance_km', 0) - 5)) / 2
        weather_bonus = self.places[place_name].get('weather_factor', 1.0)
        if day_plan and place_name in day_plan:
            base_score *= 1.2
        return round((base_score - distance_penalty) * weather_bonus, 2)

    def get_top_recommendations(self, n=3):
        scored = [(name, self.calculate_priority(name)) for name in self.places]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [self.places[name] for name, _ in scored[:n]]
