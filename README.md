
# DNS Resolver and Changer

This is a comprehensive Python-based DNS Resolver and Changer application. The project enables users to resolve domain names, change the system's DNS server settings, and also provides backup and restore functionality for DNS configurations. The project includes multiple scripts to handle DNS queries, change DNS settings, and back up existing DNS configurations.

## Features

- **DNS Resolution**: Resolves domain names to their IP addresses using a customizable DNS query builder.
- **DNS Changer**: Changes the system's DNS settings to predefined or user-specified DNS servers.
- **Backup & Restore**: Backs up the current DNS settings before applying changes, with the ability to restore previous configurations.
- **Interactive App**: Provides an interactive interface using Streamlit for a user-friendly DNS resolver and changer.

## File Overview

- `.gitignore`: Specifies intentionally untracked files to ignore.
- `LICENSE`: The MIT License governing the usage of this project.
- `README.md`: Project documentation file.
- `requirements.txt`: Lists the necessary dependencies to run the project.
- `backup_dns.py`: Script to back up the system's current DNS settings.
- `dns_backup.txt`: A text file used to store the backed-up DNS settings.
- `dns_changer.py`: Script to change the system's DNS settings.
- `dns_client.py`: Implements a simple DNS client to interact with DNS servers.
- `dns_parser.py`: Script for parsing DNS responses.
- `dns_query_builder.py`: Builds DNS queries from domain names for resolution.
- `dns_resolver.py`: Main DNS resolver script to resolve domain names to IP addresses.
- `streamlit_app.py`: Provides an interactive web-based user interface using Streamlit.

## Requirements

The project requires Python 3.x and a few additional libraries, which are listed in the `requirements.txt` file. You can install the dependencies by running:

```bash
pip install -r requirements.txt
```

The main dependencies include:
- `streamlit`: For the web-based interactive interface.
- `dnspython`: For handling DNS queries.
- Other standard Python libraries such as `socket` and `os`.

## Usage

### DNS Resolver

To resolve a domain name, you can use the `dns_resolver.py` script. For example:

```bash
python dns_resolver.py <domain_name>
```

This will send a DNS query for the specified domain and return its IP address.

### DNS Changer

The `dns_changer.py` script allows you to change your system's DNS settings to a new DNS server. You can specify the DNS server's IP as an argument:

```bash
python dns_changer.py <dns_server>
```

To change to Google DNS, for example, run:

```bash
python dns_changer.py 8.8.8.8
```

### Backup and Restore DNS Settings

Before making any changes to DNS settings, it's important to back up the current configuration. The `backup_dns.py` script handles this:

```bash
python backup_dns.py
```

This script will store the current DNS configuration in the `dns_backup.txt` file. To restore the previous DNS settings, you can refer to this file or run a similar restore script if implemented.

### Interactive Web Interface

The project includes a web-based interface built with Streamlit. To launch the interface, run:

```bash
streamlit run streamlit_app.py
```

This will open a web-based tool where you can easily resolve domains and change DNS settings without using the command line.

## DNS Client and Query Builder

The DNS resolution functionality is built using the following modules:
- `dns_client.py`: Implements a DNS client that interacts with DNS servers.
- `dns_query_builder.py`: Constructs valid DNS queries based on the domain names provided by the user.
- `dns_parser.py`: Parses the responses from the DNS server and extracts useful information such as IP addresses.

These components work together to form a complete DNS resolution pipeline.

## Contributing

We welcome contributions to this project. If you would like to add a feature or report a bug, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
