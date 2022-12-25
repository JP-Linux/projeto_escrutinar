# escrutinar_jp

### Descrição. 

* O pacote escrutinar é usado para:
	

	 * Pegar o endereço de IP de um site requisitado
	 * Pega vários dados referênte a um IP, como citado nos exemplos abaixo
	 * Obs: esse pacote usa uma API do site "https://ipwho.is/" para   obter os dados de um determinado IP
	
-
		exemplo 1
```python
from escrutinar_jp import escrutinar
print(escrutinar.pediripsite("github.com"))
```			
	Para saber os dados de um IP, usa-se
	sondarip('' -> str, mostrar_flag=False -> bool)
	que irá gerar um API no formato json,
	se não colocar nada no parâmetro será retornado seu própio ip.

		exemplo 2
```python
from escrutinar_jp import escrutinar
print(escrutinar.sondarip("8.8.8.8"))
```
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
-

		exemplo 3
```python		
from escrutinar_jp import escrutinar
print(escrutinar.sondarip("8.8.8.8", mostrar_flag=True))
```
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
					
= 
		exemplo 4

```python		
from escrutinar_jp import escrutinar

ipsite = escrutinar.pediripsite("pip.pypa.io")
print(escrutinar.sondarip(ipsite))
```

			


## Instalação

Use o gerenciador de pacote [pip](https://pip.pypa.io/en/stable/) para instalar escrutinar-jp

```bash
pip install escrutinar-jp
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