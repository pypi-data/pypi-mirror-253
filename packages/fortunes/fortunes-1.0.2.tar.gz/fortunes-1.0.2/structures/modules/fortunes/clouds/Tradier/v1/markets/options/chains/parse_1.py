


'''

'''


def parse (LIST, EXPIRATION):
	PARSED = {
		"expiration": EXPIRATION,
		"calls": {
			"strikes": []
		},
		"puts": {
			"strikes": []
		}
	}
	
	for ENTRY in LIST:	
		OPTION_TYPE = ENTRY ["option_type"]
		
		DATA = {
			"strike": ENTRY ["strike"],
			
			"prices": {
				"bid": ENTRY ["bid"],
				"ask": ENTRY ["ask"],
				"last": ENTRY ["last"],
			},

			"contract size": ENTRY ["contract_size"],
			"open interest": ENTRY ["open_interest"],
		}
		
		if (OPTION_TYPE == "call"):
			PARSED ["calls"] ["strikes"].append (DATA)
		
		
		elif (OPTION_TYPE == "put"):
			PARSED ["puts"] ["strikes"].append (DATA)

	return PARSED