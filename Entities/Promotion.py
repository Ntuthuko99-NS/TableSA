{
  "name": "Promotion",
  "type": "object",
  "properties": {
    "restaurant_id": {
      "type": "string",
      "description": "Restaurant ID"
    },
    "title": {
      "type": "string",
      "description": "Promotion title"
    },
    "description": {
      "type": "string",
      "description": "Promotion description"
    },
    "start_date": {
      "type": "string",
      "format": "date",
      "description": "Start date"
    },
    "end_date": {
      "type": "string",
      "format": "date",
      "description": "End date"
    },
    "is_active": {
      "type": "boolean",
      "description": "Currently active"
    },
    "discount_type": {
      "type": "string",
      "enum": [
        "percentage",
        "fixed",
        "bogo",
        "special"
      ],
      "description": "Type of discount"
    },
    "discount_value": {
      "type": "number",
      "description": "Discount amount"
    }
  },
  "required": [
    "restaurant_id",
    "title",
    "start_date",
    "end_date"
  ]
}
