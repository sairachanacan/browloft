#!/usr/bin/env python3
"""
Script to convert remaining service sections to the new design pattern
"""

# This script will help convert the remaining sections
# Each section needs: section heading, services list with data, and mobile/desktop layouts

sections_to_convert = {
    "Gentlemen's Bar": {
        "heading": "GENTLEMEN'S BAR",
        "image": "image18.png",
        "services": [
            {
                "id": "mens-unibrow",
                "name": "Men's Unibrow",
                "duration": "10 min",
                "description": "Threading and clean-up between the brows for a polished look."
            },
            {
                "id": "mens-luxe-brows",
                "name": "Men's Luxe Brows",
                "duration": "20 min",
                "description": "A comprehensive brow service for men, including trimming, shaping, threading, a soothing brow massage, and a personalized consultation."
            },
            {
                "id": "mens-cheeks-forehead",
                "name": "Men's Cheeks + Forehead or Ears",
                "duration": "15 min",
                "description": "Threading and clean-up for both cheeks, plus your choice of either the forehead or the area around the ears."
            }
        ]
    }
}

print("Section conversion data prepared")
print("Use this data to manually create the sections following the Eye-Brow Threading pattern")
