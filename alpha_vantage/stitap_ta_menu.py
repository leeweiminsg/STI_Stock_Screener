import time

from stitap_ta_screens import MACDScreener, RSIScreener, StochRSIScreener

class TechnicalAnalysisMenu:
	"""Displays technical analysis menu
	"""
	def __init__(self):
		self._technical_analysis_screens = {"Moving Average Convergence / Divergence":"MACD",
											"Relative Strength Index":"RSI",
											"Stochastic Relative Strength Index":"STOCHRSI"}
		self._screen = None

	@property
	def screen(self):
		return self._screen

	@screen.setter
	def screen(self, screen):
		self._screen = screen

	def _technical_analysis_screener(self, screen):
		"""Runs the technical screen of the user's choice
		
		Keyword arguments:
			screen: type of technical indicator to be used for screening
				"MACD": Moving Average Convergence / Divergence
				"RSI": Relative Strength Index
				"STOCHRSI": Stochastic Relative Strength Index
		"""
		if screen == "MACD":
			macd = MACDScreener()
			macd.run()
			self.run()
		elif screen == "RSI":
			rsi = RSIScreener()
			rsi.run()
			self.run()
		elif screen == "STOCHRSI":
			stochrsi = StochRSIScreener()
			stochrsi.run()
			self.run()
		else:
			return

	def _start(self):
		"""Prints the menu
		"""
		print("-----Straits Times Index Technical Analysis Screener-----", end="\n"*3)
		time.sleep(0.1)
		print("Please enter your desired technical analysis screener below (the symbol to the right) in UPPERCASE:", end="\n"*3)
		time.sleep(0.1)
		print("Moving Average Convergence / Divergence - MACD",
			"Relative Strength Index - RSI",
			"Stochastic Relative Strength Index - STOCHRSI", sep="\n", end="\n"*3)

	def _input(self):
		"""Collects input from the user and runs selected technical analysis screen
		"""
		while True:
			self.screen = input()

			if self.screen in self._technical_analysis_screens.values():
				time.sleep(0.1)
				print(f"\n\n\n{self.screen} SELECTED", end="\n"*3)
				time.sleep(0.1)
				break

			else:
				print(f"\n\n\n{self.screen} is invalid input. Please try again.", end="\n"*3)

	def run(self):
		"""Runs technical analysis menu
		"""
		self._start()
		self._input()
		self._technical_analysis_screener(self.screen)