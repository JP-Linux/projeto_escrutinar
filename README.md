# Biblioteca `projeto_escrutinar`

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Uma biblioteca Python para análise de informações de IP e resolução de domínios com foco em resiliência e precisão.

## 📦 Recursos Principais

- **Consulta detalhada de informações de IP** usando a API [ipwho.is](https://ipwho.is/)
- **Resolução confiável de domínios** para IPv4 e IPv6
- **Normalização inteligente de URLs** com validação rigorosa
- **Mecanismos de retry e tratamento de erros** robustos
- **Logging completo** com saída para arquivo e console

## ⚙️ Instalação

```bash
pip install projeto-escrutinar
```

## 🚀 Como Usar

### 1. Consulta de informações de IP

```python
from projeto_escrutinar import fetch_ip_info

# Consulta IP público da máquina
info = fetch_ip_info()
print(info)

# Consulta IP específico com informações de bandeira
info_google = fetch_ip_info("8.8.8.8", show_flag=True)
print(info_google)
```

### 2. Resolução de domínios

```python
from projeto_escrutinar import resolve_domain, normalize_domain

# Normalizar domínio
dominio = normalize_domain("https://www.google.com/")
print(f"Domínio normalizado: {dominio}")

# Resolver IPs com tempo de resposta
ips, tempo = resolve_domain("google.com")
print(f"IPs: {ips} | Tempo: {tempo}ms")
```

## 🧪 Exemplos de Saída

### Saída da função `fetch_ip_info`
```json
{
  "ip": "8.8.8.8",
  "success": true,
  "type": "IPv4",
  "continent": "North America",
  "country": "United States",
  "region": "California",
  "city": "Mountain View",
  "latitude": 37.3860517,
  "longitude": -122.0838511,
  "connection": {
    "asn": 15169,
    "org": "Google LLC",
    "isp": "Google LLC",
    "domain": "google.com"
  },
  "timezone": {
    "id": "America/Los_Angeles",
    "abbr": "PDT",
    "is_dst": true,
    "offset": -25200,
    "utc": "-07:00",
    "current_time": "2025-06-09T23:08:47-07:00"
  },
  "flag": {
    "img": "https://cdn.ipwhois.io/flags/us.svg", 
    "emoji": "🇺🇸",
    "emoji_unicode": "U+1F1FA U+1F1F8"
  },
  "flag_emoji": null
}
```

### Saída da função `resolve_domain`
```
Domínio normalizado: google.com
IPs: ['142.250.218.14', '2800:3f0:4001:82d::200e'] | Tempo: 15.32ms
```

## ⚙️ Configurações Personalizáveis

### Constantes globais
```python
API_URL = "https://ipwho.is/"  # Endpoint alternativo
DEFAULT_TIMEOUT = 5            # Timeout padrão em segundos
MAX_RETRIES = 2                # Tentativas de reconexão
```

### Parâmetros das funções
```python
# Consulta IP com timeout personalizado
fetch_ip_info("8.8.4.4", timeout=10)

# Resolução de domínio sem IPv6
resolve_domain("example.com", ipv6=False)
```

## 🛠 Tratamento de Erros

A biblioteca implementa tratamento robusto de erros com:

- Validação rigorosa de entradas
- Mecanismo de retry automático
- Exceções específicas para diferentes cenários
- Logging detalhado de todos os erros

### Exemplo de tratamento:
```python
try:
    ips, _ = resolve_domain("dominio-invalido.com")
except (ValueError, socket.gaierror) as e:
    print(f"Erro na resolução: {str(e)}")
```

## 📝 Logging

Todas as operações são registradas em `ip_debug.log` com formato:

```
2023-10-15 14:23:45,678 - INFO - Consulta IP: 200.150.100.50
2023-10-15 14:24:01,123 - WARNING - Timeout na tentativa 1/2
2023-10-15 14:24:02,456 - ERROR - Erro DNS para google.br: [Errno -2] Name or service not known
```

## ⚠️ Casos Especiais

1. **IPs inválidos**:
   ```python
   fetch_ip_info("300.400.500.600")
   # Retorna: {'error': 'Endereço IP inválido: 300.400.500.600'}
   ```

2. **Domínios malformados**:
   ```python
   normalize_domain("http:///sem-dominio")
   # ValueError: Formato de domínio inválido: 
   ```

3. **Falhas de conexão**:
   ```python
   fetch_ip_info(timeout=0.001)
   # Retorna: {'error': 'Erro de conexão: HTTPSConnectionPool...'}
   ```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga os passos:

1. Faça um fork do projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob licença MIT. Veja o arquivo `LICENSE` para mais informações.

## ✉️ Contato

Desenvolvedor: [Jorge Paulo Santos]  
Email: jorgepsan7@gmail.com  
Projeto: https://github.com/JP-Linux/projeto_escrutinar

---

**Obtendo informações de rede com precisão e resiliência** 🌐🔍
