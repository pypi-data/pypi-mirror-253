

'''
	from operator import itemgetter
	import fortunes.clouds.Coinbase.API.products.candles as Coinbase_API_product_candles
	candles = Coinbase_API_product_candles.proposal (
		key_name = ellipsis ["name"],
		key_secret = ellipsis ["privateKey"],
		
		product_id = "",
		granularity = "FIFTEEN_MINUTE",
		start = "",
		end = ""
	)
'''

'''
	from datetime import datetime, timezone, timedelta
	now = int (datetime.utcnow ().replace (tzinfo = timezone.utc).timestamp ())
	
	4_days_ago = int ((datetime.utcnow().replace(tzinfo=timezone.utc) - timedelta (days=4)).timestamp ())
	
	UTC_0_timestamp = datetime.fromisoformat ("2024-01-04T12:34:56.789Z").timestamp ()
'''

import fortunes.clouds.Coinbase.API as Coinbase_API

from operator import itemgetter
from datetime import datetime, timezone, timedelta

import pandas


'''
	import time
	int (time.time ())

	start = "1704405346"
	
	product_id = "FET-USD"	
'''
def proposal (
	key_name = "",
	key_secret = "",
	
	product_id = "",
	granularity = "FIFTEEN_MINUTE",
	start = "",
	end = "",
	
	return_DF = True
):
	'''
		
	'''
	request_query_params = "?" + "&".join ([
		f"granularity={ granularity }",
		f"start={ start }",
		f"end={ end }",
	])

	print ("request_query_params:", request_query_params)

	import fortunes.clouds.Coinbase.API as Coinbase_API
	proceeds = Coinbase_API.proposal (
		key_name = key_name,
		key_secret = key_secret,
		
		request_path = f"/api/v3/brokerage/products/{product_id}/candles",
		request_query_params = request_query_params
	)

	if ("candles" not in proceeds):
		print (proceeds)
		raise Exception ("'candles' were not found in the proceeds.")

	#print (proceeds)

	candles = proceeds ['candles']

	#rich.print_json (data = proceeds)
	
	if (not return_DF):
		return candles;
		
	
	OHLCV_DF = pandas.DataFrame (candles)
	OHLCV_DF = OHLCV_DF.astype ({
		"low": float, 
		"high": float,
		
		"open": float, 
		"close": float,
		
		"volume": float
	})

	for s in OHLCV_DF.index:
		#print ("s:", s, OHLCV_DF ['start'].values [s])

		datetime.utcfromtimestamp (int (OHLCV_DF ['start'].values [s])).isoformat ()

		OHLCV_DF.at [ s, 'UTC date string'] = datetime.utcfromtimestamp (
			int (OHLCV_DF ['start'].values [s])
		).isoformat ()
		
	return OHLCV_DF