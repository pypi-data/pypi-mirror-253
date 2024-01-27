
'''
	import fortunes.clouds.Tradier.procedures.options.combine as combine_options  
	options_chains = combine_options.presently ({
		"symbol": symbol,
		"authorization": authorization
	})
'''


import fortunes.clouds.Tradier.v1.markets.options.expirations as options_expirations
import fortunes.clouds.Tradier.v1.markets.options.chains as options_chains


def presently (PARAMS):
	SYMBOL = PARAMS ["symbol"]
	AUTHORIZATION = PARAMS ["authorization"]

	EXPIRATIONS = options_expirations.discover ({
		"symbol": SYMBOL,
		"authorization": AUTHORIZATION
	})
		
	def RETRIEVE_OPTIONS_CHAINS (EXPIRATION):
		CHAIN =  options_chains.discover ({
			"symbol": SYMBOL,
			"expiration": EXPIRATION,
			"authorization": AUTHORIZATION
		})
				
		return CHAIN;
		
	def PARALLEL (
		FN,
		PARAMS
	):
		OUTPUT = []
	
		from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
		with ThreadPoolExecutor () as executor:
			CHAINS = executor.map (
				FN, 
				PARAMS
			)
			executor.shutdown (wait = True)

			for CHAIN in CHAINS:
				OUTPUT.append (CHAIN)
			
		return OUTPUT

	OUTPUT = PARALLEL (
		FN = RETRIEVE_OPTIONS_CHAINS,
		PARAMS = EXPIRATIONS
	)

	return OUTPUT