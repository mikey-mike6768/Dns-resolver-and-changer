import struct

def parse_dns_response(response, query_id):
    # Extract the ID from the response and compare it with the query ID
    resp_id = struct.unpack(">H", response[:2])[0]
    if resp_id != query_id:
        raise Exception("Mismatched query ID")

    # Extract flags, question count, answer count, etc.
    flags, qdcount, ancount, nscount, arcount = struct.unpack(">HHHHH", response[2:12])
    
    # Check if the response bit (QR) is set
    if not (flags >> 15):
        raise Exception("Invalid response (not a response packet)")
    
    # Skip the question section (assume 1 question)
    offset = 12
    while response[offset] != 0:
        offset += 1  # Skip question name
    offset += 5  # Skip null byte, type, and class fields
    
    # Parse answers (if any)
    answers = []
    for _ in range(ancount):
        # Skip name field (it's compressed)
        offset += 2
        answer_type, answer_class, ttl, rdlength = struct.unpack(">HHIH", response[offset:offset+10])
        offset += 10
        if answer_type == 1:  # A record (IPv4 address)
            ip_bytes = response[offset:offset+rdlength]
            ip_addr = ".".join(map(str, ip_bytes))
            answers.append(ip_addr)
        offset += rdlength

    return answers
