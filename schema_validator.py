# Import required modules
import json
import simplejson
import datetime
from jsonschema import validate, ValidationError, FormatChecker


# Define schema
schema = {
	"$schema": "https://example.com/json-schema-validator/draft-01/schema",
	"title": "Event",
	"description": "an event is created by a user's interaction with the application on web or mobile",
	"type": "object",
	"properties": {
		"id": {
			"description": "unique id for each triggered event type",
			"type": "string"
		},
		"received_at": {
			"description": "timestamp when event trigger request was recieved",
			"type": "string"
		},
		"anonymous_id": {
			"description": "id of the user triggering the event",
			"type": "string"
		},
		"context_app_version": {
			"description": "version number of the app",
			"type": "string"
		},
		"context_device_ad_tracking_enabled": {
			"description": "if device ad tracking is enabled",
			"type": "boolean"
		},
		"context_device_manufacturer": {
			"description": "device manufacturer name",
			"type": "string"
		},
		"context_device_model": {
			"description": "model of the device",
			"type": "string"
		},
		"context_device_type": {
			"description": "os of the device",
			"type": "string"
		},
		"context_library_name": {
			"type": "string"
		},
		"context_library_version": {
			"type": "string"
		},
		"context_locale": {
			"description": "device location",
			"type": "string"
		},
		"context_network_wifi": {
			"type": "boolean"
		},
		"context_os_name": {
			"type": "string"
		},
		"context_timezone": {
			"type": "string"
		},
		"event": {
			"description": "type of event",
			"type": "string"
		},
		"event_text": {
			"type": "string"
		},
		"original_timestamp": {
			"type": "string"
		},
		"sent_at": {
			"type": "string"
		},
		"timestamp": {
			"type": "string"
		},
		"user_id": {
			"type": "string"
		},
		"context_network_carrier": {
			"type": "string"
		},
		"context_device_token": {
			"type": ["string","null"]
		},
		"context_traits_taxfix_language": {
			"type": "string"
		}
	},
	"required": ["id","received_at","anonymous_id","context_device_manufacturer","context_device_type","context_locale","context_network_wifi","context_os_name","event","event_text","original_timestamp","sent_at","timestamp","context_network_carrier","context_traits_taxfix_language"]
}
	
# Define functions	
def validate_json(json_data):
        #results = []
        
        if not bool(json_data)==True:
            results = f'FATAL: Cannot validate empty json object'
            return False, results
        try:
            validate(instance=json_data,schema=schema,format_checker=FormatChecker())
        except ValidationError as err:
            results = f'ERROR: {err}'
            return False, results
        r = 'Given JSON object is valid'
        return True,r

def extract_json(file):
    json_list=[]
    json_dict={}
    validation_results=[]
    filename= f'log_{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}.txt' 
    with open(file,'r') as f:
        for json_obj in f:
            json_dict=simplejson.loads(json_obj)   # reading each json string in the file
            is_valid, msg = validate_json(json_dict)
            f = open(f'./{filename}','a')
            f.write(msg+'\n')
    f.close()
    print("Schema validation complete")


# Run schema validate
extract_json('input.json')	
	