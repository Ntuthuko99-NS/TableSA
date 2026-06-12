{
  "name": "Restaurant",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Restaurant name"
    },
    "description": {
      "type": "string",
      "description": "Restaurant description"
    },
    "cuisine_type": {
      "type": "string",
      "enum": [
        "south_african",
        "indian",
        "italian",
        "chinese",
        "japanese",
        "mexican",
        "mediterranean",
        "american",
        "french",
        "thai",
        "portuguese",
        "ethiopian",
        "fusion",
        "seafood",
        "steakhouse",
        "vegetarian",
        "fast_food",
        "other"
      ],
      "description": "Type of cuisine"
    },
    "city": {
      "type": "string",
      "description": "City location"
    },
    "address": {
      "type": "string",
      "description": "Full address"
    },
    "province": {
      "type": "string",
      "enum": [
        "gauteng",
        "western_cape",
        "kwazulu_natal",
        "eastern_cape",
        "free_state",
        "limpopo",
        "mpumalanga",
        "north_west",
        "northern_cape"
      ],
      "description": "Province"
    },
    "opening_hours": {
      "type": "string",
      "description": "Opening hours description"
    },
    "price_range": {
      "type": "string",
      "enum": [
        "budget",
        "moderate",
        "upscale",
        "fine_dining"
      ],
      "description": "Price range"
    },
    "rating": {
      "type": "number",
      "description": "Average rating"
    },
    "review_count": {
      "type": "number",
      "description": "Number of reviews"
    },
    "image_url": {
      "type": "string",
      "description": "Main restaurant image"
    },
    "logo_url": {
      "type": "string",
      "description": "Restaurant logo"
    },
    "gallery_urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Gallery images"
    },
    "phone": {
      "type": "string",
      "description": "Contact phone"
    },
    "email": {
      "type": "string",
      "description": "Contact email"
    },
    "website": {
      "type": "string",
      "description": "Website URL"
    },
    "features": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Features like wifi, parking, etc."
    },
    "is_featured": {
      "type": "boolean",
      "description": "Featured restaurant"
    },
    "is_published": {
      "type": "boolean",
      "description": "Published and visible"
    },
    "subscription_plan": {
      "type": "string",
      "enum": [
        "basic",
        "professional",
        "enterprise"
      ],
      "default": "basic"
    },
    "chain_name": {
      "type": "string",
      "description": "Chain name if part of chain"
    },
    "owner_id": {
      "type": "string",
      "description": "Owner user ID"
    }
  },
  "required": [
    "name",
    "cuisine_type",
    "city"
  ]
}
