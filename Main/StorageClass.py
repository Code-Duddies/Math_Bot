from dataclasses import dataclass

#Class to store various information in
@dataclass(frozen=True)
class DataStorage:
	string_dict ={
		'lama3_url' : 'https://llama.meta.com/llama3/',
		'exerience_lama_button' : '/html/body/div[1]/div/div/div/div[1]/div[1]/main/div/div[1]/div[2]/div/div/div/div/div/div[3]/div[2]/a',
		'text_area' : '//*[@id=":r5:"]',
	}
