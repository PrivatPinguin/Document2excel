class product_data:
	def __init__(self):
		self.model = -1
		self.menge = -1
		self.seriennummer = ''
		self.imei = ''
		self.pc_name = ''
		self.mac_addr = ''
	
	def check(this_product_data:product_data):
		if type(this_product_data) == product_data:
			
		else:
			Print('Notwendige Daten fehlen. Bitte von Hand nachtragen.')
			# open PDF for user

class excel_line:
	def __init__(self):
		self.besteller = -1
		self.bestellnummer = -1
		self.lieferschein = -1
		self.ausgabeschein = ''
		self.eingerichtet = ''
		self.bemerkung = ''
		self.zubehoer = ''

	def insert_excel(self, bestellt_von, bestell_Nr, lieferschein_Nr, produkt:product_data, 
				ausgabeschein='', 
				eingerichtet='', 
				bemerkung='', 
				zubehoer=''):

		excel_input = excel_line.__init__()
		excel_input.besteller = bestellt_von
		excel_input.betellnummer = bestell_Nr
		excel_input.lieferschein = lieferschin_Nr

		if not type(product) == product_data: # Check if Product has product_data
			# Error :: init Product first
			product = product_data() # init without data to cause Error after checkout #TODO checkout check
		else:
			excel_input.product.model = product.model
			excel_input.product.menge = product.menge
			excel_input.product.seriennummer = product.seriennummer
			excel_input.product.imei = product.imei
			excel_input.product.pc_name = product.pc_name
			excel_input.product.mac_addr = product.mac_addr
		
		excel_input.ausgabeschein = ausgabeseschein
		excel_input.eingerichtet = eingerichtet
		excel_input.bemerkung = bemerkung
		excel_input.zubehoer 		
