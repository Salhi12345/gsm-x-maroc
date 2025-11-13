#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate promotional images for UnlockTool MA Facebook Marketplace listings"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create output directory
os.makedirs('marketplace_images', exist_ok=True)

# Image configurations for 10 different designs
designs = [
    {
        'title': 'UnlockTool MA Pro',
        'subtitle': 'أداة احترافية للصيانة',
        'bg_color': '#1a73e8',
        'text_color': '#ffffff',
        'accent': '#ff6b35'
    },
    {
        'title': 'UnlockTool GSM',
        'subtitle': 'برنامج تقني متطور',
        'bg_color': '#34a853',
        'text_color': '#ffffff',
        'accent': '#fbbc04'
    },
    {
        'title': 'UnlockTool Pro',
        'subtitle': 'حل شامل للتقنيين',
        'bg_color': '#ea4335',
        'text_color': '#ffffff',
        'accent': '#34a853'
    },
    {
        'title': 'UnlockTool MA',
        'subtitle': 'للصيانة الاحترافية',
        'bg_color': '#5f6368',
        'text_color': '#ffffff',
        'accent': '#1a73e8'
    },
    {
        'title': 'GSM UnlockTool',
        'subtitle': 'أداة موثوقة وسريعة',
        'bg_color': '#0f9d58',
        'text_color': '#ffffff',
        'accent': '#f4b400'
    },
    {
        'title': 'UnlockTool Expert',
        'subtitle': 'تقنية متقدمة للهواتف',
        'bg_color': '#9334e6',
        'text_color': '#ffffff',
        'accent': '#ff6b6b'
    },
    {
        'title': 'UnlockTool Maroc',
        'subtitle': 'أفضل أداة صيانة',
        'bg_color': '#d93025',
        'text_color': '#ffffff',
        'accent': '#188038'
    },
    {
        'title': 'UnlockTool Plus',
        'subtitle': 'حل سريع وآمن',
        'bg_color': '#1967d2',
        'text_color': '#ffffff',
        'accent': '#fa7b17'
    },
    {
        'title': 'UnlockTool Master',
        'subtitle': 'برنامج متخصص للجوال',
        'bg_color': '#137333',
        'text_color': '#ffffff',
        'accent': '#e37400'
    },
    {
        'title': 'UnlockTool Premium',
        'subtitle': 'دعم فني ممتاز',
        'bg_color': '#8e24aa',
        'text_color': '#ffffff',
        'accent': '#ff9800'
    }
]

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_promo_image(design, index):
    """Create a promotional image for the listing"""
    # Image dimensions (Facebook Marketplace recommended: 1200x1200)
    width, height = 1200, 1200

    # Create image with gradient-like background
    img = Image.new('RGB', (width, height), hex_to_rgb(design['bg_color']))
    draw = ImageDraw.Draw(img)

    # Add decorative rectangles
    accent_color = hex_to_rgb(design['accent'])
    draw.rectangle([50, 50, 1150, 250], fill=accent_color)
    draw.rectangle([100, 950, 1100, 1150], outline=accent_color, width=8)

    # Try to use a default font, fallback to basic
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf", 80)
        subtitle_font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 50)
        feature_font = ImageFont.truetype("/usr/share/fonts/dejavu/DejaVuSans.ttf", 35)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        feature_font = ImageFont.load_default()

    text_color = hex_to_rgb(design['text_color'])

    # Draw title (centered in top accent bar)
    title = design['title']
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text(((width - title_width) // 2, 120), title, fill=text_color, font=title_font)

    # Draw subtitle (Arabic text)
    subtitle = design['subtitle']
    subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text(((width - subtitle_width) // 2, 350), subtitle, fill=text_color, font=subtitle_font)

    # Add features in the middle
    features = [
        '✓ Support Multiple Brands',
        '✓ Fast & Reliable',
        '✓ Regular Updates',
        '✓ Professional Tool',
        '✓ Technical Support'
    ]

    y_position = 500
    for feature in features:
        draw.text((150, y_position), feature, fill=text_color, font=feature_font)
        y_position += 70

    # Add "Made in Morocco" badge at bottom
    morocco_text = "🇲🇦 Made for Morocco GSM"
    morocco_bbox = draw.textbbox((0, 0), morocco_text, font=feature_font)
    morocco_width = morocco_bbox[2] - morocco_bbox[0]
    draw.text(((width - morocco_width) // 2, 1020), morocco_text, fill=text_color, font=feature_font)

    # Save image
    filename = f'marketplace_images/unlocktool_listing_{index+1}.png'
    img.save(filename, quality=95)
    print(f"Created: {filename}")

# Generate all images
for i, design in enumerate(designs):
    create_promo_image(design, i)

print(f"\n✅ Generated {len(designs)} promotional images in 'marketplace_images/' directory")
