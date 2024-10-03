import socket
from dns_query_builder import build_query

def send_dns_query(domain):
    # Build the query message
    query, query_id = build_query(domain)
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # DNS server address (Google's public DNS server)
    dns_server = ("8.8.8.8", 53)
    
    try:
        # Send the DNS query to the server
        sock.sendto(query, dns_server)
        
        # Receive the response
        data, _ = sock.recvfrom(512)  # DNS responses are typically under 512 bytes
        
        return data, query_id
    finally:
        sock.close()

# Test query
if __name__ == "__main__":
    domain = "dns.google.com"
    response, query_id = send_dns_query(domain)
    print(f"Received response: {response.hex()}")
