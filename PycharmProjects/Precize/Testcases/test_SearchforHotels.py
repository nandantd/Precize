import requests
import json
import os


class test_SearchforHotels:
    """
    A class to find, process, and store top restaurant information from Google Places API

    Attributes:
        api_key (str): Google Cloud API key for Places API
        city (str): Target city name from user input
        base_url (str): Google Places API endpoint
    """

    def __init__(self):
        """
        Initialize RestaurantFinder with API key from environment variables
        Raises ValueError if API key is not found
        """
        self.api_key = os.getenv('GOOGLE_API_KEY')  # Get the API key from environment variables
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")

        self.city = None
        self.base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        self.restaurants = []

    def get_city_input(self):
        """Get and validate city name from user input"""
        self.city = input("Enter the name of a city: ").strip()
        if not self.city:
            raise ValueError("City name cannot be empty")

    def fetch_restaurants(self):
        """
        Fetch restaurants from Google Places API
        Handles API errors and network exceptions
        """
        params = {
            'query': f'restaurants in {self.city}',
            'key': self.api_key,
            'type': 'restaurant',
            'region': 'us'
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()

            # Check if the API response status is 'OK'
            if data['status'] != 'OK':
                raise Exception(f"API Error: {data.get('error_message', 'Unknown error')}")

            # Debugging: print the raw data received from the API
            print(f"Received data: {json.dumps(data, indent=2)}")

            self._process_raw_data(data.get('results', []))

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {str(e)}")

    def _process_raw_data(self, raw_data):
        """
        Process raw API response data
        Args:
            raw_data (list): List of restaurant entries from API
        """
        if not raw_data:
            print("No restaurants found in the API response.")

        for item in raw_data:
            self.restaurants.append({
                'name': item.get('name', 'Unknown'),
                'rating': item.get('rating', 0),
                'reviews': item.get('user_ratings_total', 0),
                'address': item.get('formatted_address', ''),
                'price_level': item.get('price_level', 'N/A')
            })

        # Debugging: print the processed restaurant data
        print(f"Processed {len(self.restaurants)} restaurants.")

    def _sort_restaurants(self):
        """Sort restaurants by rating (descending) and reviews (descending)"""
        self.restaurants.sort(key=lambda x: (-x['rating'], -x['reviews']))
        self.restaurants = self.restaurants[:10]  # Get top 10

    def save_to_json(self):
        """Save sorted restaurants to JSON file with city name in filename"""
        if not self.restaurants:
            raise Exception("No restaurant data to save")

        # Ensure that the filename is unique or overwrite is acceptable
        filename = f"restaurants_{self.city.lower().replace(' ', '_')}.json"
        restaurant_dict = {item['name']: item for item in self.restaurants}

        try:
            with open(filename, 'w') as f:
                json.dump(restaurant_dict, f, indent=2)
            print(f"Successfully saved {len(self.restaurants)} restaurants to {filename}")
        except IOError as e:
            print(f"Error writing to file: {e}")

    def run(self):
        """Main execution flow controller"""
        try:
            self.get_city_input()
            self.fetch_restaurants()
            self._sort_restaurants()  # Call _sort_restaurants to sort before saving
            self.save_to_json()
        except Exception as e:
            print(f"Error occurred: {str(e)}")




if __name__ == "__main__":
    try:
        finder = test_SearchforHotels()
        finder.run()
    except ValueError as e:
        print(f"Configuration error: {str(e)}")
