import re
text = """
Contact List & Logs:
- Alice Smith: alice.smith@example.com, +1-555-0192, 1024 Elm St. (Zip: 90210)
- Bob Jones: b_jones1984@work-place.org, 555.839.2019, 44 Oak Ave. (Zip: 10001)
- Charlie: charlie@domain.co.uk, 5550183829, 89 Pine Rd. 

Log entries on 2026-06-15:
[INFO] User login from IP 192.168.1.50
[ERROR] Failed connection attempt by 10.0.0.99 at 14:32:05
[WARNING] Low disk space on server-01 (ID: 404)
"""
# email_pattern = r"[a-zA-Z._0-9]+@[a-zA-Z-]+.[a-zA-Z.]+"
# matches = re.finditer(email_pattern, text)
# for match in matches:
#      print(f"Email: {match}")

# name_pattern = r"(?<=- )[A-Z][a-z]+(\s([A-Z][a-z])*)?"
# matches = re.finditer(name_pattern, text)
# for match in matches:
#     print(f"Name: {match}")


text_2 = """
# User Profiles and Contacts
John Doe: john.doe@example.com | Phone: +1-555-0199 | ID: 1042
Jane_Smith_99: jane.smith@work-place.net | Phone: 555.0142 | ID: 8831
bob_builder@test.co.uk | Phone: (555) 012-3456 | ID: 0012

# Server Logs and IP Addresses
2026-06-01 08:30:12 [INFO] Connection established from 192.168.1.50
2026-06-01 08:31:05 [WARNING] High memory usage on 10.0.0.99
2026-06-01 09:15:00 [ERROR] Failed login attempt from 256.300.1.1 (Invalid IP)

# Postal Codes and Prices
Item A costs $45.99 (SKU: AB-1234)
Item B costs $1,200.00 (SKU: XY-9876)
Zip Codes: 90210, 10001-1234, and 30301.

# Random text with repeating patterns
banana, bandana, band, granada, cabana
12345, 1234, 123, 12, 1
"""
