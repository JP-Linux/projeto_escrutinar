# escrutinar_jp

Descrição. 

O pacote escrutinar é usado para:
	

	- Pegar o endereço de IP de um site requisitado
		--exemplo 1
			from escrutinar_jp import escrutinar
			print(escrutinar.pegaripsite("github.com"))
			
	- Saber os dados de um IP no formato json
		-sondarip('' -> str, mostrar_flag=False -> bool)
		se não colocar nada no parâmetro será retornado seu ip

		-- exemplo 2

			from escrutinar_jp import escrutinar
			print(escrutinar.sondarip("8.8.8.8"))

				saida -->> 

					{
						'ip': '8.8.8.8', 
						'success': True, 
						'type': 'IPv4', 
						'continent': 'North America', 
						'continent_code': 'NA', 
						'country': 'United States', 
						'country_code': 'US', 
						'region': 'California', 
						'region_code': 'CA', 
						'city': 'Mountain View', 
						'latitude': 37.3860517, 
						'longitude': -122.0838511, 
						'is_eu': False, 
						'postal': '94039', 
						'calling_code': '1', 
						'capital': 'Washington D.C.', 
						'borders': 'CA,MX', 
						'connection': {
							'asn': 15169, 
							'org': 'Google LLC', 
							'isp': 'Google LLC', 
							'domain': 'google.com'
						}, 
						'timezone': {
							'id': 'America/Los_Angeles', 
							'abbr': 'PST', 
							'is_dst': False, 
							'offset': -28800, 
							'utc': '-08:00', 
							'current_time': '2022-12-10T16:48:07-08:00'
						}
					}

		-- exemplo 3
		
			from escrutinar_jp import escrutinar
			print(escrutinar.sondarip("8.8.8.8", mostrar_flag=True))

				saida -->>

					{
						'ip': '8.8.8.8', 
						'success': True, 
						'type': 'IPv4', 
						'continent': 'North America', 
						'continent_code': 'NA', 
						'country': 'United States', 
						'country_code': 'US', 
						'region': 'California', 
						'region_code': 'CA', 
						'city': 'Mountain View', 
						'latitude': 37.3860517, 
						'longitude': -122.0838511, 
						'is_eu': False, 
						'postal': '94039', 
						'calling_code': '1', 
						'capital': 'Washington D.C.', 
						'borders': 'CA,MX', 
						'flag': {
							'img': 'https://cdn.ipwhois.io/flags/us.svg', 
							'emoji': '🇺🇸',
							'emoji_unicode': 'U+1F1FA U+1F1F8'
						}, 
						'connection': {
							'asn': 15169, 
							'org': 'Google LLC',
							'isp': 'Google LLC', 
							'domain': 'google.com'
						}, 
						'timezone': {
							'id': 'America/Los_Angeles', 
							'abbr': 'PST',
							'is_dst': False, 
							'offset': -28800, 
							'utc': '-08:00', 
							'current_time': '2022-12-10T16:54:32-08:00'
						}
					}


			


## Instalação

Use o gerenciador de pacote [pip](https://pip.pypa.io/en/stable/) para instalar escrutinar_jp

```bash
pip install escrutinar_jp
```

## Uso

```python
from escrutinar_jp import escrutinar

escrutinar.pediripsite()
escrutinar.sondarip()
```

## Author
Jorge Paulo

## License
[MIT](https://choosealicense.com/licenses/mit/)
