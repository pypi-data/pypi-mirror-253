

import fortunes.clouds.Tradier.procedures.options.combine as combine_options  
import fortunes.climate as climate
import fortunes.treasures.options.shapes.shape_1 as shares_shape_1 

def check_1 ():
	Tradier = climate.find ("Tradier")

	options_chains = combine_options.presently ({
		"symbol": "RUN",
		"authorization": Tradier ["authorization"]
	})	
	
	shares_shape_1.assertions (options_chains)
	
	
	#print ("options_chains:", options_chains)

	return;
	
	
checks = {
	'check 1': check_1
}