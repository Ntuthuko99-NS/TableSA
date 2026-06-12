{
  "name": "Reservation",
  "type": "object",
  "properties": {
    "restaurant_id": {
      "type": "string",
      "description": "Restaurant ID"
    },
    "restaurant_name": {
      "type": "string",
      "description": "Restaurant name for display"
    },
    "customer_id": {
      "type": "string",
      "description": "Customer user ID"
    },
    "customer_name": {
      "type": "string",
      "description": "Customer name"
    },
    "customer_email": {
      "type": "string",
      "description": "Customer email"
    },
    "customer_phone": {
      "type": "string",
      "description": "Customer phone"
    },
    "table_id": {
      "type": "string",
      "description": "Assigned table ID"
    },
    "reservation_date": {
      "type": "string",
      "format": "date",
      "description": "Date of reservation"
    },
    "reservation_time": {
      "type": "string",
      "description": "Time of reservation"
    },
    "guest_count": {
      "type": "number",
      "description": "Number of guests"
    },
    "status": {
      "type": "string",
      "enum": [
        "pending",
        "confirmed",
        "cancelled",
        "no_show",
        "completed"
      ],
      "default": "pending"
    },
    "special_requests": {
      "type": "string",
      "description": "Special requests or notes"
    }
  },
  "required": [
    "restaurant_id",
    "reservation_date",
    "reservation_time",
    "guest_count"
  ]
}
