

'''
import fortunes.clouds.Tradier.v1.markets.options.chains as options_chains
options_chains.discover ({
	"symbol": "",
	"expiration": "",
	"authorization": ""
})
'''


import fortunes.clouds.Tradier.v1.markets.options.chains.parse_1 as parse_1

def discover (params):
	SYMBOL = params ["symbol"]
	EXPIRATION = params ["expiration"]
	AUTHORIZATION = params ["authorization"]
	
	PARSE_FORMAT = "1"

	import requests
	RESPONSE = requests.get (
		'https://api.tradier.com/v1/markets/options/chains',
		params = {
			'symbol': SYMBOL, 
			'expiration': EXPIRATION, 
			'greeks': 'true'
		},
		headers = {
			'Authorization': f'Bearer { AUTHORIZATION }', 
			'Accept': 'application/json'
		}
	)

	json_response = RESPONSE.json ()

	try:
		import json
		PARSED = parse_1.parse (
			json_response ["options"]["option"], 
			EXPIRATION
		)
	
	except Exception as E:
		print (RESPONSE.status_code)
		print (json_response)
		
		raise Exception (E)

	return PARSED