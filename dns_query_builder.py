import random
import struct

# Helper to encode the domain name
def encode_domain(domain):
    parts = domain.split('.')
    encoded = b''.join(bytes([len(part)]) + part.encode() for part in parts)
    return encoded + b'\x00'  # end of the domain name

# Build the DNS query
def build_query(domain):
    # Generate random ID
    query_id = random.randint(0, 65535)
    
    # Flags: standard query with recursion desired
    flags = 0x0100
    
    # Header fields
    qdcount = 1  # number of questions
    ancount = 0  # no answer
    nscount = 0  # no authority
    arcount = 0  # no additional
    
    # Create the header (12 bytes)
    header = struct.pack(">HHHHHH", query_id, flags, qdcount, ancount, nscount, arcount)
    
    # Question section
    qname = encode_domain(domain)
    qtype = 1  # A record (IPv4)
    qclass = 1  # Internet class
    question = qname + struct.pack(">HH", qtype, qclass)
    
    return header + question, query_id
