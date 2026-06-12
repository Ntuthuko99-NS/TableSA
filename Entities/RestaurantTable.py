{
  "name": "RestaurantTable",
  "type": "object",
  "properties": {
    "restaurant_id": {
      "type": "string",
      "description": "Restaurant ID"
    },
    "table_number": {
      "type": "number",
      "description": "Table number"
    },
    "capacity": {
      "type": "number",
      "description": "Seating capacity"
    },
    "is_indoor": {
      "type": "boolean",
      "description": "Indoor table"
    },
    "is_smoking": {
      "type": "boolean",
      "description": "Smoking allowed"
    },
    "is_available": {
      "type": "boolean",
      "description": "Currently available"
    },
    "description": {
      "type": "string",
      "description": "Table description"
    }
  },
  "required": [
    "restaurant_id",
    "table_number",
    "capacity"
  ]
}
