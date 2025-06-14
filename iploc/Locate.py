import requests
import socket


if __name__ == '__main__':
    ip = '17.253.0.0'
    apiKey = '228e6205ec5d357ead4c6740a3f57d29'
    url = f'https://iplocate.io/api/lookup/{ip}&apikey={apiKey}'
    response = requests.get(url)
    print(response.json())

def getip():
    # Replace 'example.com' with the domain you want to resolve
    domain_name = "example.com"
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"The IP address of {domain_name} is: {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(f"Error resolving {domain_name}: {e}")
        return None