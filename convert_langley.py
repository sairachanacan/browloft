#!/usr/bin/env python3
"""
Script to convert langley-location.html to the new service booking design
This will read the burnaby structure and adapt it for Langley services
"""

# Read the header part (up to service-details section)
with open('/Users/sairachanamaguluri/Desktop/Brow-loft/langley-location.html', 'r') as f:
    content = f.read()

# Find where service-details starts
service_start = content.find('        <!-- service-details -->')
header_part = content[:service_start]

# Find where footer starts  
footer_start = content.find('        <!-- main-footer -->')
footer_part = content[footer_start:]

# The service sections from burnaby (lines 220-1780 approximately)
# We'll read from burnaby and adapt for Langley's 8 sections

print("Header lines:", len(header_part.split('\n')))
print("Footer lines:", len(footer_part.split('\n')))
print("Service start position:", service_start)
print("Footer start position:", footer_start)
