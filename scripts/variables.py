class SchemaDefinition():
	schema = {
	    "type": "object",
	    "properties": {
	        "id": { "$ref": "#/definitions/non-empty-string" },
	        "anonymous_id": { "$ref": "#/definitions/non-empty-string" },
	        "context_device_manufacturer": { "$ref": "#/definitions/non-empty-string" },
	        "context_device_model": { "$ref": "#/definitions/non-empty-string" },
	        "context_device_type": { "$ref": "#/definitions/non-empty-string" },
	        "context_library_name": { "$ref": "#/definitions/non-empty-string" },
	        "context_library_version": { "$ref": "#/definitions/non-empty-string" },
	        "context_locale": { "$ref": "#/definitions/non-empty-string" },
	        "context_os_name": { "$ref": "#/definitions/non-empty-string" },
	        "event": { "$ref": "#/definitions/non-empty-string" },
	        "event_text": { "$ref": "#/definitions/non-empty-string" },
	        "context_network_carrier": { "$ref": "#/definitions/non-empty-string" },
	        "context_traits_taxfix_language": { "$ref": "#/definitions/non-empty-string" },
	        "context_os_name": { "$ref": "#/definitions/non-empty-string" },
	        "context_app_version": { "$ref": "#/definitions/non-empty-string" },
	        "context_device_ad_tracking_enabled": { "type": 'boolean' },
	        "context_timezone": { "$ref": "#/definitions/non-empty-string" },
	        "user_id": { "$ref": "#/definitions/non-empty-string" },
	        "context_device_token": { "$ref": "#/definitions/non-empty-string" },
	        "received_at": {"type": "string",
	            "format": "date"},
	        "original_timestamp": {"type": "string",
	            "format": "date"},
	        "sent_at": {"type": "string",
	            "format": "date"},
	        "timestamp": {"type": "string",
	            "format": "date"},
	        "context_network_wifi" : {"type": 'boolean'}
	    },
	    "definitions": {
	        "non-empty-string": {
	            "type": "string",
	            "minLength": 1
	        },
	    }
	}

	output_json_log_folder_path = '/output_json_log/'
	csv_generated_report_folder_path = '/csv_generated_report/'