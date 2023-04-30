# escrutinar_jp

## Informações sobre endereços IP

* Este projeto contém duas funções úteis para obtenção de informações sobre endereços IP:
	

	 * sondar_ip: consulta o serviço https://ipwho.is/ e retorna informações sobre o endereço IP informado;
	 * pedir_ip_site: dado um endereço de site, retorna o endereço IP associado a esse site.

## Como usar

### sondar_ip

A função sondar_ip pode ser usada para obter informações sobre um endereço IP específico ou, se nenhum endereço for informado, sobre o endereço IP público da máquina local. É possível escolher se a chave "flag" deve ou não ser incluída na resposta.

Para utilizar a função sondar_ip, faça:

```python
from escrutinar_jp.escrutinar import sondar_ip

# Obter informações sobre o endereço IP 8.8.8.8
resultado = sondar_ip("8.8.8.8")
print(resultado)

# Obter informações sobre o endereço IP público da máquina local sem incluir a chave "flag" na resposta
resultado = sondar_ip(mostrar_flag=False)
print(resultado)
```
A função retorna um dicionário contendo informações sobre o endereço IP. Exemplo de resposta:
```python
{
	"ip": "8.8.8.8",
	"success": "True",
	"type": "IPv4",
  	"continent": "North America",
	"continent_code": "NA",
  	"country": "United States",
  	"country_code": "US",
  	"region": "California",
  	"region_code": "CA",
  	"city": "Mountain View",
  	"latitude": "37.3860517",
  	"longitude": "-122.0838511",
  	"postal": "94039",
  	"calling_code": "1",
	"capital": "Washington D.C.",
  	"borders": "CA,MX",
  	"connection": {
		"asn": "15169",
		"org": "Google LLC",
		"isp": "Google LLC",
		"domain": "google.com"
	},
  	"timezone": {
		"id": "America/Los_Angeles",
		"abbr": "PDT",
		"is_dst": "True",
		"offset": "-25200",
		"utc": "-07:00",
		"current_time": "2023-04-29T18:44:31-07:00"
	}
}
```

### pedir_ip_site

A função pedir_ip_site recebe um endereço de site e retorna o endereço IP associado a esse site.

Para utilizar a função pedir_ip_site, faça:

```python
from escrutinar_jp.escrutinar import pedir_ip_site

# Obter o endereço IP do site google.com
resultado = pedir_ip_site("google.com")
print(resultado)
```

A função retorna uma string contendo o endereço IP do site. Exemplo de resposta:

```python
"172.217.29.206"
```

## Instalação

Use o gerenciador de pacote [pip](https://pip.pypa.io/en/stable/) para instalar escrutinar_jp

```sh-session
pip3 install escrutinar_jp
```

## Author
Jorge Paulo

## License
[MIT](https://choosealicense.com/licenses/mit/)
