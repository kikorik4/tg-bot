import requests
from tg_bot.config_data.config import url_hotel

headers = {
 "x-rapidapi-key": "c4daf61859mshf367daf96a89533p1fa519jsn407321d2c2ff",
 "x-rapidapi-host": "booking-com15.p.rapidapi.com"
}

def get_hotel_id(dest_id: str, search_type: str, checkinDate: str, checkoutDate: str):
    querystring = {"dest_id": dest_id, "search_type": search_type, "arrival_date": checkinDate, "departure_date": checkoutDate, }
    response_hotels = requests.get(url_hotel, headers=headers, params=querystring)
    return response_hotels

l = get_hotel_id('-2092174', 'CITY', '2025-01-25', '2025-01-26')
l = l.json()
print(l)



id = {
    "status": True,
    "message": "Success",
    "timestamp": 1727256591667,
    "data": {
        "pagination": {
            "nbResultsTotal": 3110
        },
        "availabilityInfo": {
            "totalAvailableNotAutoextended": 1055
        },
        "filters": [
            {
                "title": "Your previous filters",
                "field": "previous",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Hotels",
                        "genericId": "property_type::204",
                        "countNotAutoextended": 616
                    },
                    {
                        "title": "Pets allowed",
                        "genericId": "facility::4",
                        "countNotAutoextended": 196
                    },
                    {
                        "title": "Spa and wellness centre",
                        "genericId": "facility::54",
                        "countNotAutoextended": 57
                    },
                    {
                        "title": "Private bathroom",
                        "genericId": "room_facility::38",
                        "countNotAutoextended": 828
                    },
                    {
                        "title": "Very good: 8+",
                        "genericId": "reviewscorebuckets::80",
                        "countNotAutoextended": 449
                    },
                    {
                        "title": "Free cancellation",
                        "genericId": "free_cancellation::1",
                        "countNotAutoextended": 85
                    },
                    {
                        "title": "Free WiFi",
                        "genericId": "facility::107",
                        "countNotAutoextended": 997
                    },
                    {
                        "title": "Entire homes & apartments",
                        "genericId": "privacy_type::3",
                        "countNotAutoextended": 417
                    },
                    {
                        "title": "3 stars",
                        "genericId": "class::3",
                        "countNotAutoextended": 228
                    },
                    {
                        "title": "Airport shuttle",
                        "genericId": "facility::17",
                        "countNotAutoextended": 57
                    }
                ]
            },
            {
                "title": "Your budget (for 1 night)",
                "field": "price",
                "filterStyle": "SLIDER",
                "options": [],
                "min": "10",
                "max": "600",
                "minPriceStep": "10",
                "minSelected": "0",
                "histogram": [
                    0,
                    5,
                    8,
                    19,
                    39,
                    69,
                    75,
                    78,
                    99,
                    69,
                    69,
                    55,
                    60,
                    58,
                    64,
                    53,
                    59,
                    41,
                    30,
                    40,
                    37,
                    32,
                    39,
                    22,
                    31,
                    27,
                    28,
                    22,
                    21,
                    25,
                    21,
                    14,
                    13,
                    16,
                    9,
                    11,
                    9,
                    8,
                    4,
                    7,
                    12,
                    10,
                    7,
                    5,
                    10,
                    5,
                    6,
                    3,
                    5,
                    6
                ],
                "currency": "GBP"
            },
            {
                "title": "Popular filters",
                "field": "popular",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Hotels",
                        "genericId": "property_type::204",
                        "countNotAutoextended": 616
                    },
                    {
                        "title": "Very good: 8+",
                        "genericId": "reviewscorebuckets::80",
                        "countNotAutoextended": 449
                    },
                    {
                        "title": "Breakfast included",
                        "genericId": "mealplan::breakfast_included",
                        "countNotAutoextended": 381
                    },
                    {
                        "title": "Hostels",
                        "genericId": "property_type::203",
                        "countNotAutoextended": 26
                    },
                    {
                        "title": "Good: 7+",
                        "genericId": "reviewscorebuckets::70",
                        "countNotAutoextended": 760
                    },
                    {
                        "title": "Free WiFi",
                        "genericId": "facility::107",
                        "countNotAutoextended": 997
                    },
                    {
                        "title": "Apartments",
                        "genericId": "property_type::201",
                        "countNotAutoextended": 392
                    },
                    {
                        "title": "Double bed",
                        "genericId": "twin_double_bed::3",
                        "countNotAutoextended": 995
                    }
                ]
            },
            {
                "title": "Review score",
                "field": "review_score",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Passable: 5+",
                        "genericId": "reviewscorebuckets::50",
                        "countNotAutoextended": 935
                    },
                    {
                        "title": "Pleasant: 6+",
                        "genericId": "reviewscorebuckets::60",
                        "countNotAutoextended": 882
                    },
                    {
                        "title": "Good: 7+",
                        "genericId": "reviewscorebuckets::70",
                        "countNotAutoextended": 760
                    },
                    {
                        "title": "Very good: 8+",
                        "genericId": "reviewscorebuckets::80",
                        "countNotAutoextended": 449
                    },
                    {
                        "title": "Superb: 9+",
                        "genericId": "reviewscorebuckets::90",
                        "countNotAutoextended": 129
                    }
                ]
            },
            {
                "title": "Beach access",
                "field": "ht_beach",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Beachfront",
                        "genericId": "beach_access::1",
                        "countNotAutoextended": 0
                    }
                ]
            },
            {
                "title": "Property type",
                "field": "ht_id",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Entire homes & apartments",
                        "genericId": "privacy_type::3",
                        "countNotAutoextended": 417
                    },
                    {
                        "title": "Apartments",
                        "genericId": "property_type::201",
                        "countNotAutoextended": 392
                    },
                    {
                        "title": "Hotels",
                        "genericId": "property_type::204",
                        "countNotAutoextended": 616
                    },
                    {
                        "title": "Guest houses",
                        "genericId": "property_type::216",
                        "countNotAutoextended": 32
                    },
                    {
                        "title": "Homestays",
                        "genericId": "property_type::222",
                        "countNotAutoextended": 32
                    },
                    {
                        "title": "Holiday homes",
                        "genericId": "property_type::220",
                        "countNotAutoextended": 6
                    },
                    {
                        "title": "Bed and breakfasts",
                        "genericId": "property_type::208",
                        "countNotAutoextended": 9
                    },
                    {
                        "title": "Hostels",
                        "genericId": "property_type::203",
                        "countNotAutoextended": 26
                    },
                    {
                        "title": "Cabins",
                        "genericId": "property_type_ml::9999",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Villas",
                        "genericId": "property_type::213",
                        "countNotAutoextended": 1
                    },
                    {
                        "title": "Boats",
                        "genericId": "property_type::215",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Motels",
                        "genericId": "property_type::205",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Farm stays",
                        "genericId": "property_type::210",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Campsites",
                        "genericId": "property_type::214",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Luxury tents",
                        "genericId": "property_type::224",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Capsule hotels",
                        "genericId": "property_type::225",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Student accommodation",
                        "genericId": "property_type::235",
                        "countNotAutoextended": 1
                    }
                ]
            },
            {
                "title": "Chain",
                "field": "chaincode",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Autograph Collection",
                        "genericId": "chaincode::2542",
                        "countNotAutoextended": 5
                    },
                    {
                        "title": "Best Western",
                        "genericId": "chaincode::1029",
                        "countNotAutoextended": 3
                    },
                    {
                        "title": "Curio Collection by Hilton",
                        "genericId": "chaincode::4381",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Doubletree by Hilton",
                        "genericId": "chaincode::1984",
                        "countNotAutoextended": 7
                    },
                    {
                        "title": "easyHotel",
                        "genericId": "chaincode::2901",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Hampton Inn",
                        "genericId": "chaincode::1851",
                        "countNotAutoextended": 1
                    },
                    {
                        "title": "Hilton Hotels & Resorts",
                        "genericId": "chaincode::1078",
                        "countNotAutoextended": 8
                    },
                    {
                        "title": "Holiday Inn Express",
                        "genericId": "chaincode::2301",
                        "countNotAutoextended": 1
                    },
                    {
                        "title": "Holiday Inn Hotels & Resorts",
                        "genericId": "chaincode::1072",
                        "countNotAutoextended": 3
                    },
                    {
                        "title": "ibis",
                        "genericId": "chaincode::1053",
                        "countNotAutoextended": 2
                    },
                    {
                        "title": "Imperial Hotel Group",
                        "genericId": "chaincode::14335",
                        "countNotAutoextended": 5
                    },
                    {
                        "title": "Leonardo Hotels",
                        "genericId": "chaincode::1844",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Marriott Hotels & Resorts",
                        "genericId": "chaincode::1080",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Mercure",
                        "genericId": "chaincode::1051",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Millennium Hotels",
                        "genericId": "chaincode::1248",
                        "countNotAutoextended": 3
                    },
                    {
                        "title": "Montcalm Collection",
                        "genericId": "chaincode::1705",
                        "countNotAutoextended": 11
                    },
                    {
                        "title": "Novotel",
                        "genericId": "chaincode::1050",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "OYO Rooms",
                        "genericId": "chaincode::6015",
                        "countNotAutoextended": 4
                    },
                    {
                        "title": "Park Plaza Hotels & Resorts",
                        "genericId": "chaincode::1040",
                        "countNotAutoextended": 5
                    },
                    {
                        "title": "Point A Hotels",
                        "genericId": "chaincode::9857",
                        "countNotAutoextended": 6
                    },
                    {
                        "title": "Radisson Blu",
                        "genericId": "chaincode::8648",
                        "countNotAutoextended": 8
                    },
                    {
                        "title": "Sonder",
                        "genericId": "chaincode::14572",
                        "countNotAutoextended": 8
                    },
                    {
                        "title": "Thistle",
                        "genericId": "chaincode::1422",
                        "countNotAutoextended": 5
                    },
                    {
                        "title": "Young & Co.\u2019s Brewery",
                        "genericId": "chaincode::14659",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Z Hotels",
                        "genericId": "chaincode::8718",
                        "countNotAutoextended": 11
                    }
                ]
            },
            {
                "title": "Facilities",
                "field": "hotelfacility",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Free WiFi",
                        "genericId": "facility::107",
                        "countNotAutoextended": 997
                    },
                    {
                        "title": "Non-smoking rooms",
                        "genericId": "facility::16",
                        "countNotAutoextended": 823
                    },
                    {
                        "title": "Family rooms",
                        "genericId": "facility::28",
                        "countNotAutoextended": 590
                    },
                    {
                        "title": "Parking",
                        "genericId": "facility::2",
                        "countNotAutoextended": 264
                    },
                    {
                        "title": "24-hour front desk",
                        "genericId": "facility::8",
                        "countNotAutoextended": 586
                    },
                    {
                        "title": "Free parking",
                        "genericId": "facility::46",
                        "countNotAutoextended": 15
                    },
                    {
                        "title": "Restaurant",
                        "genericId": "facility::3",
                        "countNotAutoextended": 282
                    },
                    {
                        "title": "Pets allowed",
                        "genericId": "facility::4",
                        "countNotAutoextended": 196
                    },
                    {
                        "title": "Room service",
                        "genericId": "facility::5",
                        "countNotAutoextended": 275
                    },
                    {
                        "title": "Fitness centre",
                        "genericId": "facility::11",
                        "countNotAutoextended": 209
                    },
                    {
                        "title": "Wheelchair accessible",
                        "genericId": "facility::185",
                        "countNotAutoextended": 174
                    },
                    {
                        "title": "Electric vehicle charging station",
                        "genericId": "facility::182",
                        "countNotAutoextended": 43
                    },
                    {
                        "title": "Airport shuttle",
                        "genericId": "facility::17",
                        "countNotAutoextended": 57
                    },
                    {
                        "title": "Adult only",
                        "genericId": "facility::149",
                        "countNotAutoextended": 29
                    },
                    {
                        "title": "Swimming Pool",
                        "genericId": "facility::433",
                        "countNotAutoextended": 44
                    },
                    {
                        "title": "Spa and wellness centre",
                        "genericId": "facility::54",
                        "countNotAutoextended": 57
                    },
                    {
                        "title": "BBQ facilities",
                        "genericId": "facility::72",
                        "countNotAutoextended": 14
                    },
                    {
                        "title": "Airport shuttle (free)",
                        "genericId": "facility::139",
                        "countNotAutoextended": 0
                    }
                ]
            },
            {
                "title": "Landmarks",
                "field": "popular_nearby_landmarks",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Barking Station",
                        "genericId": "popular_nearby_landmarks::210628",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Brunel University",
                        "genericId": "popular_nearby_landmarks::205807",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Chessington World of Adventures",
                        "genericId": "popular_nearby_landmarks::11961",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Cockfosters",
                        "genericId": "popular_nearby_landmarks::10839",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Croydon University Hospital",
                        "genericId": "popular_nearby_landmarks::900065852",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Hampton Court Palace",
                        "genericId": "popular_nearby_landmarks::15723",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Harrow School",
                        "genericId": "popular_nearby_landmarks::900065913",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Hatton Cross",
                        "genericId": "popular_nearby_landmarks::10879",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Heathrow Terminal 4",
                        "genericId": "popular_nearby_landmarks::10881",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Heathrow Terminal 5",
                        "genericId": "popular_nearby_landmarks::17001",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Kew Gardens",
                        "genericId": "popular_nearby_landmarks::11044",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "London Eye",
                        "genericId": "popular_nearby_landmarks::1722",
                        "countNotAutoextended": 42
                    },
                    {
                        "title": "London Zoo",
                        "genericId": "popular_nearby_landmarks::1728",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Mount Vernon Hospital",
                        "genericId": "popular_nearby_landmarks::900065807",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Osterley Park",
                        "genericId": "popular_nearby_landmarks::27617",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Perivale",
                        "genericId": "popular_nearby_landmarks::10949",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Redbridge",
                        "genericId": "popular_nearby_landmarks::10960",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Richmond Station",
                        "genericId": "popular_nearby_landmarks::212044",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "South Harrow",
                        "genericId": "popular_nearby_landmarks::10977",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "South Mimms Services M25",
                        "genericId": "popular_nearby_landmarks::264319",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "The Grove",
                        "genericId": "popular_nearby_landmarks::8407",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "The Stoop",
                        "genericId": "popular_nearby_landmarks::15919",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Tower of London",
                        "genericId": "popular_nearby_landmarks::846",
                        "countNotAutoextended": 32
                    },
                    {
                        "title": "Twickenham Stadium",
                        "genericId": "popular_nearby_landmarks::12535",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Watford General Hospital",
                        "genericId": "popular_nearby_landmarks::900065358",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Watford Junction",
                        "genericId": "popular_nearby_landmarks::22043",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Watford Stadium",
                        "genericId": "popular_nearby_landmarks::22045",
                        "countNotAutoextended": 0
                    }
                ]
            },
            {
                "title": "District",
                "field": "di",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Bayswater",
                        "genericId": "district::42",
                        "countNotAutoextended": 95
                    },
                    {
                        "title": "Bloomsbury",
                        "genericId": "district::54",
                        "countNotAutoextended": 95
                    },
                    {
                        "title": "Brent",
                        "genericId": "district::1825",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Camden",
                        "genericId": "district::1543",
                        "countNotAutoextended": 160
                    },
                    {
                        "title": "Canary Wharf and Docklands",
                        "genericId": "district::48",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Central London",
                        "genericId": "district::2280",
                        "countNotAutoextended": 1055
                    },
                    {
                        "title": "Chelsea",
                        "genericId": "district::30",
                        "countNotAutoextended": 40
                    },
                    {
                        "title": "City of London",
                        "genericId": "district::47",
                        "countNotAutoextended": 52
                    },
                    {
                        "title": "Ealing",
                        "genericId": "district::74",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Earls Court",
                        "genericId": "district::75",
                        "countNotAutoextended": 38
                    },
                    {
                        "title": "East End",
                        "genericId": "district::40",
                        "countNotAutoextended": 47
                    },
                    {
                        "title": "Greenwich",
                        "genericId": "district::37",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Guests' favourite area ",
                        "genericId": "district::9009",
                        "countNotAutoextended": 827
                    },
                    {
                        "title": "Hackney",
                        "genericId": "district::84",
                        "countNotAutoextended": 36
                    },
                    {
                        "title": "Hammersmith",
                        "genericId": "district::85",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Hammersmith and Fulham",
                        "genericId": "district::1544",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Hyde Park",
                        "genericId": "district::44",
                        "countNotAutoextended": 221
                    },
                    {
                        "title": "Islington",
                        "genericId": "district::96",
                        "countNotAutoextended": 41
                    },
                    {
                        "title": "Kensington",
                        "genericId": "district::29",
                        "countNotAutoextended": 122
                    },
                    {
                        "title": "Kensington and Chelsea",
                        "genericId": "district::1545",
                        "countNotAutoextended": 185
                    },
                    {
                        "title": "Kings Cross St Pancras",
                        "genericId": "district::102",
                        "countNotAutoextended": 98
                    },
                    {
                        "title": "Lambeth",
                        "genericId": "district::103",
                        "countNotAutoextended": 29
                    },
                    {
                        "title": "Marylebone",
                        "genericId": "district::34",
                        "countNotAutoextended": 77
                    },
                    {
                        "title": "Mayfair",
                        "genericId": "district::28",
                        "countNotAutoextended": 60
                    },
                    {
                        "title": "Newham",
                        "genericId": "district::1257",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Oxford Street",
                        "genericId": "district::338",
                        "countNotAutoextended": 100
                    },
                    {
                        "title": "Paddington",
                        "genericId": "district::43",
                        "countNotAutoextended": 65
                    },
                    {
                        "title": "Pimlico",
                        "genericId": "district::336",
                        "countNotAutoextended": 44
                    },
                    {
                        "title": "Shoreditch",
                        "genericId": "district::120",
                        "countNotAutoextended": 43
                    },
                    {
                        "title": "South Kensington",
                        "genericId": "district::333",
                        "countNotAutoextended": 104
                    },
                    {
                        "title": "Southwark",
                        "genericId": "district::122",
                        "countNotAutoextended": 46
                    },
                    {
                        "title": "St James",
                        "genericId": "district::33",
                        "countNotAutoextended": 74
                    },
                    {
                        "title": "Stratford",
                        "genericId": "district::1826",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Theatreland",
                        "genericId": "district::1127",
                        "countNotAutoextended": 82
                    },
                    {
                        "title": "Tower Hamlets",
                        "genericId": "district::1546",
                        "countNotAutoextended": 15
                    },
                    {
                        "title": "Victoria",
                        "genericId": "district::343",
                        "countNotAutoextended": 61
                    },
                    {
                        "title": "Wandsworth",
                        "genericId": "district::133",
                        "countNotAutoextended": 7
                    },
                    {
                        "title": "West End",
                        "genericId": "district::136",
                        "countNotAutoextended": 218
                    },
                    {
                        "title": "Westminster Borough",
                        "genericId": "district::32",
                        "countNotAutoextended": 482
                    },
                    {
                        "title": "Whitechapel",
                        "genericId": "district::138",
                        "countNotAutoextended": 11
                    }
                ]
            },
            {
                "title": "Property rating",
                "field": "class",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Unrated",
                        "genericId": "class::0",
                        "countNotAutoextended": 197
                    },
                    {
                        "title": "1 star",
                        "genericId": "class::1",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "2 stars",
                        "genericId": "class::2",
                        "countNotAutoextended": 73
                    },
                    {
                        "title": "3 stars",
                        "genericId": "class::3",
                        "countNotAutoextended": 228
                    },
                    {
                        "title": "4 stars",
                        "genericId": "class::4",
                        "countNotAutoextended": 404
                    },
                    {
                        "title": "5 stars",
                        "genericId": "class::5",
                        "countNotAutoextended": 153
                    }
                ]
            },
            {
                "title": "Bed preference",
                "field": "tdb",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "2 single beds",
                        "genericId": "twin_double_bed::2",
                        "countNotAutoextended": 325
                    },
                    {
                        "title": "Double bed",
                        "genericId": "twin_double_bed::3",
                        "countNotAutoextended": 995
                    }
                ]
            },
            {
                "title": "Room facilities",
                "field": "roomfacility",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Coffee machine",
                        "genericId": "room_facility::120",
                        "countNotAutoextended": 315
                    },
                    {
                        "title": "Electric kettle",
                        "genericId": "room_facility::86",
                        "countNotAutoextended": 690
                    },
                    {
                        "title": "View",
                        "genericId": "room_facility::81",
                        "countNotAutoextended": 348
                    },
                    {
                        "title": "Washing machine",
                        "genericId": "room_facility::34",
                        "countNotAutoextended": 330
                    },
                    {
                        "title": "Flat-screen TV",
                        "genericId": "room_facility::75",
                        "countNotAutoextended": 829
                    },
                    {
                        "title": "Bath",
                        "genericId": "room_facility::5",
                        "countNotAutoextended": 330
                    },
                    {
                        "title": "Desk",
                        "genericId": "room_facility::23",
                        "countNotAutoextended": 602
                    },
                    {
                        "title": "Air conditioning",
                        "genericId": "room_facility::11",
                        "countNotAutoextended": 519
                    },
                    {
                        "title": "Kitchenette",
                        "genericId": "room_facility::16",
                        "countNotAutoextended": 208
                    },
                    {
                        "title": "Private bathroom",
                        "genericId": "room_facility::38",
                        "countNotAutoextended": 828
                    }
                ]
            },
            {
                "title": "Free cancellation ",
                "field": "fc",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Free cancellation",
                        "genericId": "free_cancellation::1",
                        "countNotAutoextended": 85
                    }
                ]
            },
            {
                "title": "Online payment",
                "field": "pmt",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Accepts online payments",
                        "genericId": "pmt::101",
                        "countNotAutoextended": 862
                    }
                ]
            },
            {
                "title": "Number of bedrooms",
                "field": "entire_place_bedroom_count",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "1+ bedrooms",
                        "genericId": "entire_place_bedroom_count::1",
                        "countNotAutoextended": 417
                    },
                    {
                        "title": "2+ bedrooms",
                        "genericId": "entire_place_bedroom_count::2",
                        "countNotAutoextended": 200
                    },
                    {
                        "title": "3+ bedrooms",
                        "genericId": "entire_place_bedroom_count::3",
                        "countNotAutoextended": 60
                    },
                    {
                        "title": "4+ bedrooms",
                        "genericId": "entire_place_bedroom_count::4",
                        "countNotAutoextended": 9
                    }
                ]
            },
            {
                "title": "Meals",
                "field": "mealplan",
                "filterStyle": "CHECKBOX",
                "options": [
                    {
                        "title": "Breakfast included",
                        "genericId": "mealplan::breakfast_included",
                        "countNotAutoextended": 381
                    },
                    {
                        "title": "Breakfast & lunch included",
                        "genericId": "mealplan::breakfast_and_lunch",
                        "countNotAutoextended": 0
                    },
                    {
                        "title": "Breakfast & dinner included",
                        "genericId": "mealplan::breakfast_and_dinner",
                        "countNotAutoextended": 12
                    },
                    {
                        "title": "Self catering",
                        "genericId": "mealplan::999",
                        "countNotAutoextended": 443
                    }
                ]
            }
        ]
    }
}

print(id['data']['filters'][6]['options'])
for i in id['data']['filters'][6]['options']:
    print(i['title'])
