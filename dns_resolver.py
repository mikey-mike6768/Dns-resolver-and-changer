from dns_client import send_dns_query
from dns_parser import parse_dns_response

def resolve_domain(domain):
    root_server = ("198.41.0.4", 53)  # One of the root DNS servers

    # Send the query to the root server
    response, query_id = send_dns_query(domain)
    
    # Parse the response
    answers = parse_dns_response(response, query_id)
    
    # If no answers, continue querying authoritative servers
    if not answers:
        print("No answers. Need to query authoritative servers.")
    else:
        print(f"IP addresses: {answers}")

if __name__ == "__main__":
    resolve_domain("dns.google.com")
