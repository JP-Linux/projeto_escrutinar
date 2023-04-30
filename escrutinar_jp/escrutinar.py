import socket
import requests

def sondar_ip(ip=None, mostrar_flag=False):
    """
    Retorna informações de um endereço IP utilizando o serviço https://ipwho.is/.
    
    Args:
        ip (str): Endereço IP a ser consultado. Se for `None`, o endereço IP público da máquina local será usado.
        mostrar_flag (bool): Se for `True`, inclui a chave 'flag' na resposta. Caso contrário, essa chave é removida.
        
    Returns:
        dict: Um dicionário contendo informações sobre o endereço IP consultado.
    """
    whois = "https://ipwho.is/"
    
    if ip is None:
        requisicao = requests.get(whois).json()
    else:
        ip = ip.strip()
        requisicao = requests.get(f"{whois}{ip}").json()
    
    if not mostrar_flag:
        requisicao.pop('flag', None)
    
    return requisicao

def pedir_ip_site(host):
    """
    Retorna o endereço IP de um site.
    
    Args:
        host (str): Endereço de um site.
        
    Returns:
        str: O endereço IP do site.
    """
    host = host.strip()
    host = host.replace('https://www.', '')
    host = host.replace('http://www.', '')
    host = host.replace('www.', '')
    
    ip = socket.gethostbyname(host)
    
    return ip
