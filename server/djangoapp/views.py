def fetch_dealers(request):
    dealers = {
        "status": 200,
        "dealers": [
            {
                "id": 1,
                "full_name": "Best Cars Dealership",
                "city": "New York",
                "state": "NY",
                "address": "123 Main Street",
                "zip": "10001"
            },
            {
                "id": 2,
                "full_name": "Super Auto Sales",
                "city": "Chicago",
                "state": "IL",
                "address": "456 Market Street",
                "zip": "60601"
            }
        ]
    }
    return JsonResponse(dealers)
