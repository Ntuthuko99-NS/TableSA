{
  "name": "Review",
  "type": "object",
  "properties": {
    "restaurant_id": {
      "type": "string",
      "description": "Restaurant ID"
    },
    "customer_id": {
      "type": "string",
      "description": "Customer user ID"
    },
    "customer_name": {
      "type": "string",
      "description": "Customer display name"
    },
    "rating": {
      "type": "number",
      "description": "Rating 1-5"
    },
    "comment": {
      "type": "string",
      "description": "Review text"
    },
    "is_approved": {
      "type": "boolean",
      "description": "Admin approved"
    }
  },
  "required": [
    "restaurant_id",
    "rating"
  ]
}
