#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re
import json

def scrape_ssjcpl_events(url, library_name):
    """Scrape events from SSJCPL libraries - SIMPLE VERSION"""
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        events = []
        event_links = soup.select('a[href*="/events-services/events-calendar/"]')
        seen_urls = set()
        
        for link in event_links:
            event_url = link.get('href')
            full_url = f"https://www.ssjcpl.org{event_url}" if event_url.startswith('/') else event_url
            
            if full_url in seen_urls or 'id=' not in full_url:
                continue
            seen_urls.add(full_url)
            
            # Get the raw text which contains everything jumbled
            raw_text = link.get_text(strip=True)
            
            if not raw_text or raw_text in ['View Event', 'VIEW ALL EVENTS', 'Events Calendar']:
                continue
            
            # Extract title (everything before the date pattern)
            title_match = re.match(r'^(.+?)(?=(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{1,2})', raw_text)
            if title_match:
                title = title_match.group(1).strip()
            else:
                title = raw_text[:50] if len(raw_text) > 50 else raw_text
            
            # Extract date and day (pattern like "Dec25Thu" or "Jan1Fri")
            date = "TBD"
            day = ""
            date_match = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\d{1,2})(Mon|Tue|Wed|Thu|Fri|Sat|Sun)', raw_text)
            if date_match:
                month = date_match.group(1)
                day_num = date_match.group(2)
                day_abbr = date_match.group(3)
                date = f"{month} {day_num}"
                day = day_abbr
            
            # Extract time (look for "Time: HH:MM AM/PM - HH:MM AM/PM" pattern)
            time = "All day"  # Default
            time_match = re.search(r'Time:\s*(\d{1,2}:\d{2}\s*(?:AM|PM)\s*-\s*\d{1,2}:\d{2}\s*(?:AM|PM))', raw_text, re.IGNORECASE)
            if time_match:
                time = time_match.group(1).strip()
            
            # Extract category/age group (text after "View Event")
            category = "All Ages"  # Default
            if "View Event" in raw_text:
                # Get everything after "View Event"
                parts = raw_text.split("View Event")
                if len(parts) > 1:
                    after_view = parts[-1].strip()
                    # Remove any trailing characters and clean up
                    category = after_view if after_view else "All Ages"
            
            events.append({
                'date': date,
                'day': day,
                'time': time,
                'location': library_name,
                'event': title,
                'age': category,
                'link': full_url
            })
        
        return events
        
    except Exception as e:
        print(f"Error scraping {library_name}: {str(e)}")
        return []


def generate_home_depot_kids_workshops():
    """Generate Home Depot Kids Workshop events (first Saturday of each month)"""
    from datetime import datetime, timedelta
    
    events = []
    
    # Generate events for next 6 months
    current_date = datetime.now()
    
    for month_offset in range(6):
        # Calculate the target month
        target_month = current_date.month + month_offset
        target_year = current_date.year
        
        # Handle year rollover
        while target_month > 12:
            target_month -= 12
            target_year += 1
        
        # Find first Saturday of the month
        first_day = datetime(target_year, target_month, 1)
        
        # Calculate days until Saturday (5 = Saturday in weekday())
        days_until_saturday = (5 - first_day.weekday()) % 7
        if days_until_saturday == 0 and first_day.day > 1:
            days_until_saturday = 7
        
        first_saturday = first_day + timedelta(days=days_until_saturday)
        
        # Skip if this date is in the past
        if first_saturday < current_date.replace(hour=0, minute=0, second=0, microsecond=0):
            continue
        
        # Format date as "Mon DD"
        month_abbr = first_saturday.strftime("%b")
        day_num = first_saturday.strftime("%-d")  # Remove leading zero
        day_abbr = first_saturday.strftime("%a")
        
        events.append({
            'date': f"{month_abbr} {day_num}",
            'day': day_abbr,
            'time': '9:00 AM - 10:00 AM',
            'location': 'Home Depot Tracy',
            'event': 'Kids Workshop - Free DIY Project',
            'age': 'Children',
            'link': 'https://www.homedepot.com/workshops/kids-workshops'
        })
    
    return events


def generate_ksb_skate_dojo_events():
    """Generate KSB Skate Dojo events - 4 specific Sundays in January 2026"""
    events = []
    
    # Only these 4 specific dates in January 2026
    january_dates = [
        datetime(2026, 1, 4),   # Jan 4 (Sun)
        datetime(2026, 1, 11),  # Jan 11 (Sun)
        datetime(2026, 1, 18),  # Jan 18 (Sun)
        datetime(2026, 1, 25),  # Jan 25 (Sun)
    ]
    
    current_date = datetime.now()
    
    for event_date in january_dates:
        # Skip if this date is in the past
        if event_date < current_date.replace(hour=0, minute=0, second=0, microsecond=0):
            continue
        
        month_abbr = event_date.strftime("%b")
        day_num = event_date.strftime("%-d")
        day_abbr = event_date.strftime("%a")
        
        events.append({
            'date': f"{month_abbr} {day_num}",
            'day': day_abbr,
            'time': '3:00 PM - 4:00 PM',
            'location': 'Tracy Veterans Park',
            'event': 'aariv Sawhney - KSB Skate Session',
            'age': 'Children',
            'link': 'https://www.ksbskatedojo.com/'
        })
    
    return events


def generate_omca_first_sunday():
    """Generate Oakland Museum of California (OMCA) First Sunday Free Admission events for next 6 months"""
    events = []
    current_date = datetime.now()
    
    # Generate for next 6 months
    for month_offset in range(6):
        # Calculate the target month
        target_month = current_date.month + month_offset
        target_year = current_date.year
        
        # Handle year rollover
        while target_month > 12:
            target_month -= 12
            target_year += 1
        
        # Get first day of the month
        first_day = datetime(target_year, target_month, 1)
        
        # Calculate first Sunday (0 = Monday, 6 = Sunday)
        days_until_sunday = (6 - first_day.weekday()) % 7
        if days_until_sunday == 0 and first_day.day != 1:
            days_until_sunday = 7
        first_sunday = first_day + timedelta(days=days_until_sunday)
        
        # Skip if this date is in the past
        if first_sunday < current_date.replace(hour=0, minute=0, second=0, microsecond=0):
            continue
        
        # Format date as "Mon DD"
        month_abbr = first_sunday.strftime("%b")
        day_num = first_sunday.strftime("%-d")  # Remove leading zero
        day_abbr = first_sunday.strftime("%a")
        
        events.append({
            'date': f"{month_abbr} {day_num}",
            'day': day_abbr,
            'time': '10:00 AM - 5:00 PM',
            'location': 'Oakland Museum of CA',
            'event': 'First Sunday Free Admission',
            'age': 'All Ages',
            'link': 'https://museumca.org/visit'
        })
    
    return events


def scrape_eventbrite_organizer(organizer_url):
    """Scrape events from an Eventbrite organizer page."""
    events = []
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(organizer_url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Method 1: Look for JSON-LD structured data
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        
        for script in json_ld_scripts:
            try:
                data = json.loads(script.string)
                
                # Handle both single events and event lists
                event_list = []
                if isinstance(data, list):
                    event_list = data
                elif isinstance(data, dict):
                    if data.get('@type') == 'Event':
                        event_list = [data]
                    elif 'event' in data:
                        event_list = data['event'] if isinstance(data['event'], list) else [data['event']]
                
                for event in event_list:
                    if isinstance(event, dict) and event.get('@type') == 'Event':
                        parsed_event = parse_event_from_json_ld(event)
                        if parsed_event:
                            events.append(parsed_event)
                            
            except (json.JSONDecodeError, KeyError, TypeError):
                continue
        
        # Method 2: Look for event data in JavaScript variables
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and 'window.__SERVER_DATA__' in script.string:
                try:
                    match = re.search(r'window\.__SERVER_DATA__\s*=\s*({.+?});', script.string, re.DOTALL)
                    if match:
                        server_data = json.loads(match.group(1))
                        extracted_events = extract_events_from_server_data(server_data)
                        events.extend(extracted_events)
                except:
                    continue
        
        print(f"Found {len(events)} Eventbrite events")
        
    except Exception as e:
        print(f"Error scraping Eventbrite: {e}")
    
    return events


def parse_event_from_json_ld(event_data):
    """Parse event from JSON-LD structured data."""
    try:
        name = event_data.get('name', '')
        start_date_str = event_data.get('startDate', '')
        if not start_date_str:
            return None
            
        start_date = datetime.fromisoformat(start_date_str.replace('Z', '+00:00'))
        
        end_date_str = event_data.get('endDate', '')
        end_date = None
        if end_date_str:
            end_date = datetime.fromisoformat(end_date_str.replace('Z', '+00:00'))
        
        location_data = event_data.get('location', {})
        if isinstance(location_data, dict):
            location_name = location_data.get('name', 'Thrive City')
        else:
            location_name = 'Thrive City'
        
        url = event_data.get('url', '')
        
        formatted_event = {
            'date': start_date.strftime('%b %-d'),
            'day': start_date.strftime('%a'),
            'time': format_time_range(start_date, end_date),
            'location': location_name,
            'event': name,
            'age': 'All Ages',
            'link': url
        }
        
        return formatted_event
        
    except Exception as e:
        print(f"Error parsing event: {e}")
        return None


def extract_events_from_server_data(data, events=None):
    """Recursively search for event data in server data structure."""
    if events is None:
        events = []
    
    if isinstance(data, dict):
        if 'name' in data and 'start' in data and 'url' in data:
            try:
                parsed = parse_event_from_server_data(data)
                if parsed:
                    events.append(parsed)
            except:
                pass
        
        for value in data.values():
            extract_events_from_server_data(value, events)
            
    elif isinstance(data, list):
        for item in data:
            extract_events_from_server_data(item, events)
    
    return events


def parse_event_from_server_data(event_data):
    """Parse event from server data structure."""
    try:
        name = event_data.get('name', {})
        if isinstance(name, dict):
            name = name.get('text', '')
        
        start_data = event_data.get('start', {})
        start_str = start_data.get('utc', '') or start_data.get('local', '')
        if not start_str:
            return None
            
        start_date = datetime.fromisoformat(start_str.replace('Z', '+00:00'))
        
        end_data = event_data.get('end', {})
        end_str = end_data.get('utc', '') or end_data.get('local', '')
        end_date = None
        if end_str:
            end_date = datetime.fromisoformat(end_str.replace('Z', '+00:00'))
        
        url = event_data.get('url', '')
        
        formatted_event = {
            'date': start_date.strftime('%b %-d'),
            'day': start_date.strftime('%a'),
            'time': format_time_range(start_date, end_date),
            'location': 'Thrive City',
            'event': name,
            'age': 'All Ages',
            'link': url
        }
        
        return formatted_event
        
    except Exception:
        return None


def format_time_range(start_date, end_date):
    """Format time range for display."""
    start_time = start_date.strftime('%-I:%M %p').replace(':00', '')
    
    if end_date:
        end_time = end_date.strftime('%-I:%M %p').replace(':00', '')
        return f"{start_time} - {end_time}"
    else:
        return start_time


def scrape_thrive_city_events():
    """Scrape Thrive City events from Eventbrite."""
    url = "https://www.eventbrite.com/o/thrive-city-36308481623"
    events = scrape_eventbrite_organizer(url)
    
    # Filter to only future events within 3 months
    now = datetime.now()
    three_months_from_now = now + timedelta(days=90)  # Approximately 3 months
    
    future_events = []
    for event in events:
        try:
            # Reconstruct the datetime for filtering
            date_str = event['date']
            month_map = {
                'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
            }
            parts = date_str.split()
            if len(parts) == 2:
                month = month_map.get(parts[0], 12)
                day = int(parts[1])
                year = 2025 if month == 12 else 2026
                event_date = datetime(year, month, day)
                
                # Only include events that are:
                # 1. In the future (>= now)
                # 2. Within 3 months from now (<= three_months_from_now)
                if now <= event_date <= three_months_from_now:
                    future_events.append(event)
        except:
            # If we can't parse the date, skip the event
            pass
    
    return future_events


def parse_date(date_str):
    """Parse date string - SIMPLIFIED"""
    return {
        'parsed_date': datetime.now(),  # Fallback
        'date_display': "TBD",
        'day_display': "",
        'time_display': "See event page",
        'is_weekend': False
    }


def sort_events(events):
    """Sort events by date (asc), time (asc), then location priority"""
    from datetime import datetime
    
    # Location priority mapping
    location_priority = {
        'Tracy Branch Library': 1,
        'Mountain House Branch Library': 2,
        'Manteca Branch Library': 3,
        'Lathrop Branch Library': 4,
        'Home Depot Tracy': 5,
        'Tracy Veterans Park': 6,
        'Oakland Museum of CA': 7,
        'Thrive City': 8
    }
    
    def parse_sort_key(event):
        # Parse date (Dec 25 -> 2025-12-25)
        date_str = event.get('date', 'TBD')
        parsed_date = datetime(2099, 12, 31)  # Default far future for TBD
        
        if date_str != 'TBD':
            try:
                # Map month abbreviations
                month_map = {
                    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
                }
                parts = date_str.split()
                if len(parts) == 2:
                    month_abbr = parts[0]
                    day = int(parts[1])
                    month = month_map.get(month_abbr, 12)
                    
                    # Smart year assignment
                    # We're currently in Dec 2025, so:
                    # - Dec events -> 2025
                    # - Jan-Nov events -> 2026 (future)
                    if month == 12:
                        year = 2025
                    else:
                        year = 2026
                    
                    parsed_date = datetime(year, month, day)
            except:
                pass
        
        # Parse time (11:00 AM -> sortable)
        time_str = event.get('time', 'All day')
        time_sort = 9999  # Default for "All day"
        
        if time_str != 'All day':
            try:
                # Extract first time (start time) from "11:00 AM - 12:00 PM"
                time_parts = time_str.split('-')[0].strip()
                time_obj = datetime.strptime(time_parts, '%I:%M %p')
                time_sort = time_obj.hour * 60 + time_obj.minute
            except:
                pass
        
        # Get location priority
        location = event.get('location', '')
        loc_priority = location_priority.get(location, 999)
        
        return (parsed_date, time_sort, loc_priority)
    
    return sorted(events, key=parse_sort_key)


def scrape_all_events():
    """Scrape all library events"""
    print("Starting library event scraping...")
    all_events = []
    
    # Only SSJCPL libraries (San Joaquin County)
    libraries = {
        'Tracy Branch Library': ('ssjcpl', 'https://www.ssjcpl.org/your-library/locations/tracy'),
        'Mountain House Branch Library': ('ssjcpl', 'https://www.ssjcpl.org/your-library/locations/mountain-house'),
        'Manteca Branch Library': ('ssjcpl', 'https://www.ssjcpl.org/your-library/locations/manteca'),
        'Lathrop Branch Library': ('ssjcpl', 'https://www.ssjcpl.org/your-library/locations/lathrop'),
    }
    
    for library_name, (lib_type, url) in libraries.items():
        print(f"Scraping {library_name}...")
        
        if lib_type == 'ssjcpl':
            events = scrape_ssjcpl_events(url, library_name)
        else:
            events = []
        
        all_events.extend(events)
        print(f"  Found {len(events)} events")
    
    # Add Home Depot Kids Workshops (first Saturday of each month)
    print("Generating Home Depot Kids Workshop events...")
    home_depot_events = generate_home_depot_kids_workshops()
    all_events.extend(home_depot_events)
    print(f"  Generated {len(home_depot_events)} Home Depot events")
    
    # Add KSB Skate Dojo Sunday events
    print("Generating KSB Skate Dojo events...")
    ksb_events = generate_ksb_skate_dojo_events()
    all_events.extend(ksb_events)
    print(f"  Generated {len(ksb_events)} KSB Skate events")
    
    # Add Oakland Museum of California First Sunday Free Admission
    print("Generating OMCA First Sunday events...")
    omca_events = generate_omca_first_sunday()
    all_events.extend(omca_events)
    print(f"  Generated {len(omca_events)} OMCA events")
    
    # Add Thrive City events from Eventbrite
    print("Scraping Thrive City events from Eventbrite...")
    try:
        thrive_city_events = scrape_thrive_city_events()
        all_events.extend(thrive_city_events)
        print(f"  Found {len(thrive_city_events)} Thrive City events")
    except Exception as e:
        print(f"  Error scraping Thrive City: {e}")
    
    # Sort events by date, time, and location
    all_events = sort_events(all_events)
    print(f"\n✅ Total events: {len(all_events)} (sorted by date, time, location)")
    
    return all_events


def generate_html(events):
    """Generate HTML website"""
    
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p PST")
    
    total_events = len(events)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 Local Family Events - Tracy Area</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{ font-size: 2.5em; margin-bottom: 10px; }}
        .header p {{ opacity: 0.9; font-size: 1.1em; }}
        .stats {{
            display: flex;
            justify-content: space-around;
            padding: 20px;
            background: #f8f9fa;
            flex-wrap: wrap;
        }}
        .stat-card {{
            text-align: center;
            padding: 15px;
            min-width: 150px;
        }}
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
            margin-top: 5px;
        }}
        .content {{
            padding: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 30px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        th {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #e0e0e0;
        }}
        tr:hover {{ background-color: #f8f9fa; }}
        .event-link {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
        }}
        .event-link:hover {{
            text-decoration: underline;
        }}
        .age-badge {{
            display: inline-block;
            padding: 4px 12px;
            background: #e3f2fd;
            color: #1976d2;
            border-radius: 12px;
            font-size: 0.85em;
        }}
        .footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            background: #f8f9fa;
            border-top: 1px solid #e0e0e0;
        }}
        h2 {{
            color: #333;
            margin: 30px 0 20px 0;
            font-size: 1.8em;
            border-left: 4px solid #667eea;
            padding-left: 15px;
        }}
        .filter-container {{
            padding: 20px 30px;
            background: #f8f9fa;
            border-bottom: 2px solid #e0e0e0;
            display: flex;
            align-items: center;
            gap: 15px;
            flex-wrap: wrap;
        }}
        .filter-label {{
            font-weight: 600;
            color: #333;
            font-size: 1.1em;
        }}
        .filter-select {{
            padding: 10px 20px;
            font-size: 1em;
            border: 2px solid #667eea;
            border-radius: 8px;
            background: white;
            color: #333;
            cursor: pointer;
            min-width: 250px;
            transition: all 0.3s;
        }}
        .filter-select:hover {{
            border-color: #764ba2;
            box-shadow: 0 2px 8px rgba(102, 126, 234, 0.2);
        }}
        .filter-select:focus {{
            outline: none;
            border-color: #764ba2;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }}
        @media (max-width: 768px) {{
            .header h1 {{ font-size: 1.8em; }}
            table {{ font-size: 0.9em; }}
            th, td {{ padding: 10px 8px; }}
            .filter-select {{ min-width: 100%; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 Local Family Events</h1>
            <p>Libraries • Home Depot • KSB Skate • OMCA • Thrive City | Tracy • San Jose • Oakland • SF</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">{total_events}</div>
                <div class="stat-label">Total Events</div>
            </div>
        </div>
        
        <div class="filter-container">
            <label class="filter-label" for="locationFilter">📍 Filter by Location:</label>
            <select id="locationFilter" class="filter-select" onchange="filterEvents()">
                <option value="all">All Locations</option>
                <option value="Tracy Branch Library">Tracy Branch Library</option>
                <option value="Mountain House Branch Library">Mountain House Branch Library</option>
                <option value="Manteca Branch Library">Manteca Branch Library</option>
                <option value="Lathrop Branch Library">Lathrop Branch Library</option>
                <option value="Home Depot Tracy">Home Depot Tracy</option>
                <option value="Tracy Veterans Park">Tracy Veterans Park</option>
                <option value="Oakland Museum of CA">Oakland Museum of CA</option>
                <option value="Thrive City">Thrive City (SF)</option>
            </select>
            
            <label class="filter-label" for="dateFilter" style="margin-left: 20px;">📅 Filter by Date:</label>
            <select id="dateFilter" class="filter-select" onchange="filterEvents()">
                <option value="all">All Dates</option>
                <option value="today">Today</option>
                <option value="tomorrow">Tomorrow</option>
                <option value="this-week">This Week</option>
                <option value="next-week">Next Week</option>
                <option value="this-month">This Month</option>
                <option value="next-month">Next Month</option>
            </select>
        </div>
        
        <div class="content">
            <h2>📅 All Events</h2>
            <table>
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Day</th>
                        <th>Time</th>
                        <th>Location</th>
                        <th>Event</th>
                        <th>Category</th>
                    </tr>
                </thead>
                <tbody>
"""
    
    for event in events:
        html += f"""
                    <tr data-location="{event['location']}" data-date="{event['date']}">
                        <td>{event['date']}</td>
                        <td>{event['day']}</td>
                        <td>{event['time']}</td>
                        <td>{event['location']}</td>
                        <td><a href="{event['link']}" target="_blank" class="event-link">{event['event']}</a></td>
                        <td><span class="age-badge">{event['age']}</span></td>
                    </tr>
"""
    
    html += f"""
                </tbody>
            </table>
        </div>
        
        <div class="footer">
            <p>Last updated: {current_time}</p>
            <p>Auto-updates daily • Data from library websites</p>
        </div>
    </div>
    
    <script>
        function filterEvents() {{
            const locationFilter = document.getElementById('locationFilter').value;
            const dateFilter = document.getElementById('dateFilter').value;
            const rows = document.querySelectorAll('tbody tr');
            
            // Get current date info for date filtering
            const now = new Date();
            const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
            const tomorrow = new Date(today);
            tomorrow.setDate(tomorrow.getDate() + 1);
            
            // Calculate week boundaries
            const thisWeekStart = new Date(today);
            const dayOfWeek = today.getDay(); // 0 = Sunday, 6 = Saturday
            thisWeekStart.setDate(today.getDate() - dayOfWeek); // Start of this week (Sunday)
            const thisWeekEnd = new Date(thisWeekStart);
            thisWeekEnd.setDate(thisWeekStart.getDate() + 6); // End of this week (Saturday)
            
            const nextWeekStart = new Date(thisWeekEnd);
            nextWeekStart.setDate(thisWeekEnd.getDate() + 1);
            const nextWeekEnd = new Date(nextWeekStart);
            nextWeekEnd.setDate(nextWeekStart.getDate() + 6);
            
            // Calculate month boundaries
            const thisMonthStart = new Date(now.getFullYear(), now.getMonth(), 1);
            const thisMonthEnd = new Date(now.getFullYear(), now.getMonth() + 1, 0);
            
            const nextMonthStart = new Date(now.getFullYear(), now.getMonth() + 1, 1);
            const nextMonthEnd = new Date(now.getFullYear(), now.getMonth() + 2, 0);
            
            let visibleCount = 0;
            rows.forEach(row => {{
                const location = row.getAttribute('data-location');
                const dateStr = row.getAttribute('data-date');
                
                // Location filter
                const locationMatch = locationFilter === 'all' || location === locationFilter;
                
                // Date filter
                let dateMatch = true;
                if (dateFilter !== 'all' && dateStr) {{
                    const eventDate = parseDateString(dateStr);
                    
                    if (eventDate) {{
                        switch(dateFilter) {{
                            case 'today':
                                dateMatch = eventDate.getTime() === today.getTime();
                                break;
                            case 'tomorrow':
                                dateMatch = eventDate.getTime() === tomorrow.getTime();
                                break;
                            case 'this-week':
                                dateMatch = eventDate >= thisWeekStart && eventDate <= thisWeekEnd;
                                break;
                            case 'next-week':
                                dateMatch = eventDate >= nextWeekStart && eventDate <= nextWeekEnd;
                                break;
                            case 'this-month':
                                dateMatch = eventDate >= thisMonthStart && eventDate <= thisMonthEnd;
                                break;
                            case 'next-month':
                                dateMatch = eventDate >= nextMonthStart && eventDate <= nextMonthEnd;
                                break;
                        }}
                    }}
                }}
                
                // Show row if both filters match
                if (locationMatch && dateMatch) {{
                    row.style.display = '';
                    visibleCount++;
                }} else {{
                    row.style.display = 'none';
                }}
            }});
            
            console.log(`Showing ${{visibleCount}} events`);
        }}
        
        function parseDateString(dateStr) {{
            // Parse "Dec 25" format to Date object
            const months = {{
                'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5,
                'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11
            }};
            
            const parts = dateStr.split(' ');
            if (parts.length !== 2) return null;
            
            const month = months[parts[0]];
            const day = parseInt(parts[1]);
            
            if (month === undefined || isNaN(day)) return null;
            
            // Determine year (Dec 2025, Jan-Nov 2026)
            const now = new Date();
            const currentYear = now.getFullYear();
            
            let year;
            if (month === 11) {{ // December
                year = currentYear; // December 2025
            }} else {{ // Jan-Nov
                year = currentYear + 1; // 2026
            }}
            
            return new Date(year, month, day);
        }}
    </script>
</body>
</html>
"""
    
    return html


if __name__ == "__main__":
    events = scrape_all_events()
    html = generate_html(events)
    
    # Write to current directory (works on GitHub Actions)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"\n✅ Generated website with {len(events)} events")
    print(f"📄 File: index.html")
