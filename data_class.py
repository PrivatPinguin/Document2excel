class product_data:
	def __init__(self):
		self.model = -1
		self.menge = -1
		self.seriennummer = ''
		self.imei = ''
		self.pc_name = ''
		self.mac_addr = ''
	
	def check(self, this_product_data):
		if type(this_product_data) == product_data:
			return True
		else:
			print('Notwendige Daten fehlen. Bitte von Hand nachtragen.')
			# open PDF for user
			return False

class excel_line:
	def __init__(self):
		self.besteller = -1
		self.bestellnummer = -1
		self.lieferschein = -1
		self.ausgabeschein = ''
		self.eingerichtet = ''
		self.bemerkung = ''
		self.zubehoer = ''
		# creates a list of product_data
		self.product_list = []
		self.product = product_data()

	def insert_excel(self, bestellt_von, bestell_Nr, lieferschein_Nr, product:product_data, 
				ausgabeschein='', 
				eingerichtet='', 
				bemerkung='', 
				zubehoer=''):

		self.besteller = bestellt_von
		self.betellnummer = bestell_Nr
		self.lieferschein = lieferschein_Nr
		# intis product_data if not already done
		if type(product) != product_data:
			product = product_data()

			product.model = product.model
			product.menge = product.menge
			product.seriennummer = product.seriennummer
			product.imei = product.imei
			product.pc_name = product.pc_name
			product.mac_addr = product.mac_addr
		
		self.ausgabeschein = ausgabeschein
		self.eingerichtet = eingerichtet
		self.bemerkung = bemerkung
		self.zubehoer = zubehoer	
