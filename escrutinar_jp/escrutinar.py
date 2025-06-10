import socket
import requests
import re
from urllib.parse import urlparse
import ipaddress
import logging
from typing import Dict, List, Optional, Tuple, Union
import time

# Configuração aprimorada de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ip_debug.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

# Constantes configuráveis
API_URL = "https://ipwho.is/"
DEFAULT_TIMEOUT = 5
MAX_RETRIES = 2
DOMAIN_REGEX = re.compile(
    r"^([a-z0-9\-]+\.)+[a-z]{2,}$",
    re.IGNORECASE
)

def is_valid_ip(ip: str) -> bool:
    """Verifica se uma string é um endereço IP válido (IPv4 ou IPv6)."""
    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False

def fetch_ip_info(
    ip: Optional[str] = None,
    show_flag: bool = False,
    timeout: int = DEFAULT_TIMEOUT
) -> Dict:
    """
    Retorna informações de um endereço IP utilizando o serviço https://ipwho.is/.

    Args:
        ip: Endereço IP a ser consultado. Se None, usa o IP público da máquina.
        show_flag: Se True, inclui a chave 'flag' na resposta.
        timeout: Timeout em segundos para a requisição.

    Returns:
        Dicionário com informações do IP ou mensagem de erro.
    """
    # Preparar URL da API
    url = API_URL.rstrip('/') + '/'
    params = {'lang': 'pt'}

    if ip:
        ip = ip.strip()
        if not is_valid_ip(ip):
            return {'error': f'Endereço IP inválido: {ip}'}
        url += ip

    try:
        # Tentativa com retry
        for attempt in range(MAX_RETRIES + 1):
            try:
                response = requests.get(
                    url,
                    params=params,
                    timeout=timeout,
                    headers={'User-Agent': 'IPInfoClient/1.0'}
                )
                response.raise_for_status()
                data = response.json()
                break
            except requests.exceptions.Timeout:
                if attempt < MAX_RETRIES:
                    logging.warning(f"Timeout na tentativa {attempt+1}/{MAX_RETRIES}")
                    time.sleep(1)  # Backoff simples
                    continue
                raise

        # Verificar resposta da API
        if not data.get('success', True):
            error_msg = data.get('message', 'Erro desconhecido na API')
            return {'error': f'Erro na API: {error_msg}'}

        # Filtrar dados e remover flag se necessário
        relevant_fields = {
            'ip', 'success', 'type', 'continent', 'country', 'region', 'city',
            'latitude', 'longitude', 'org', 'isp', 'timezone', 'connection'
        }

        result = {k: v for k, v in data.items() if k in relevant_fields}

        if show_flag:
            result.update({
                'flag': data.get('flag'),
                'flag_emoji': data.get('flag_emoji')
            })

        return result

    except requests.exceptions.RequestException as e:
        error_type = type(e).__name__
        logging.error(f"Erro de requisição ({error_type}): {str(e)}")
        return {'error': f'Erro de conexão: {str(e)}'}
    except ValueError as e:
        logging.error(f"Erro ao decodificar JSON: {str(e)}")
        return {'error': 'Resposta inválida da API'}
    except Exception as e:
        logging.exception("Erro inesperado na consulta de IP:")
        return {'error': f'Erro inesperado: {str(e)}'}

def normalize_domain(host: str) -> str:
    """
    Normaliza um domínio removendo protocolos, paths e subdomínios www.

    Args:
        host: URL ou domínio a ser normalizado

    Returns:
        Domínio normalizado

    Raises:
        ValueError: Se o host for inválido
    """
    if not host or not isinstance(host, str):
        raise ValueError("Host inválido ou vazio")

    host = host.strip().lower()

    # Remover prefixos comuns
    for prefix in ('http://', 'https://', 'ftp://', '//'):
        if host.startswith(prefix):
            host = host[len(prefix):]

    # Extrair domínio principal
    domain = host.split('/', 1)[0]

    # Remover subdomínios 'www' e portas
    domain = domain.replace('www.', '').split(':', 1)[0]

    # Validar formato básico
    if not DOMAIN_REGEX.match(domain):
        raise ValueError(f"Formato de domínio inválido: {domain}")

    return domain

def resolve_domain(
    host: str,
    timeout: int = DEFAULT_TIMEOUT,
    ipv6: bool = True
) -> Tuple[List[str], float]:
    """
    Retorna o(s) endereço(s) IP de um site e o tempo de resposta.

    Args:
        host: URL ou domínio do site
        timeout: Timeout em segundos para resolução DNS
        ipv6: Incluir endereços IPv6 na resposta

    Returns:
        Tupla com (lista de IPs, tempo de resolução em ms)

    Raises:
        ValueError: Se o host for inválido
        socket.gaierror: Se falhar a resolução DNS
    """
    domain = normalize_domain(host)

    # Configurar famílias de endereços
    families = [socket.AF_INET]
    if ipv6:
        families.append(socket.AF_INET6)

    try:
        ips = []
        resolution_time = 0

        for family in families:
            # Medir tempo de resolução
            start_time = time.perf_counter()
            addr_info = socket.getaddrinfo(
                domain,
                None,
                family=family,
                proto=socket.IPPROTO_TCP,
                type=socket.SOCK_STREAM
            )
            end_time = time.perf_counter()

            # Coletar IPs únicos
            new_ips = {info[4][0] for info in addr_info}
            ips.extend(new_ips)

            # Atualizar tempo de resolução
            resolution_time = max(resolution_time, (end_time - start_time) * 1000)

        # Ordenar IPv4 primeiro
        ips.sort(key=lambda ip: ':' not in ip, reverse=True)

        return ips, round(resolution_time, 2)

    except socket.gaierror as e:
        logging.error(f"Erro DNS para {domain}: {str(e)}")
        raise
    except socket.timeout:
        logging.error(f"Timeout ao resolver {domain}")
        raise socket.gaierror(f"Timeout ao resolver {domain}")
    except Exception as e:
        logging.exception(f"Erro inesperado na resolução de {domain}:")
        raise

# Função principal para exemplo de uso
'''def main():
    """Exemplos de uso das funções principais"""
    print("Exemplo 1 - Consulta IP com flag:")
    print(fetch_ip_info("8.8.8.8", show_flag=True))

    print("\nExemplo 2 - IP público local:")
    print(fetch_ip_info())

    print("\nExemplo 3 - Resolução DNS com tempo:")
    try:
        ips, rtime = resolve_domain("https://www.google.com")
        print(f"Endereços IP encontrados ({rtime}ms): {', '.join(ips)}")
    except Exception as e:
        print(f"Erro: {str(e)}")

    print("\nExemplo 4 - Domínio inválido:")
    try:
        print(resolve_domain("invalid-domain..com"))
    except Exception as e:
        print(f"Erro esperado: {str(e)}")

if __name__ == "__main__":
    main()'''
