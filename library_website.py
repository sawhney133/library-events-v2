import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

def get_tracy_library_events():
    """Scrape Tracy Branch Library events"""
    events = []
    try:
        url = "https://www.ssjcpl.org/events-services/events-calendar/tracy"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for event_div in soup.find_all('div', class_='spl-component-event-list-item'):
            try:
                title_elem = event_div.find('h2')
                if not title_elem:
                    continue
                    
                title = title_elem.get_text(strip=True)
                link_elem = title_elem.find('a')
                link = 'https://www.ssjcpl.org' + link_elem['href'] if link_elem and 'href' in link_elem.attrs else url
                
                date_elem = event_div.find('div', class_='date')
                time_elem = event_div.find('div', class_='time')
                category_elem = event_div.find('div', class_='category')
                
                date_str = date_elem.get_text(strip=True) if date_elem else 'TBD'
                time_str = time_elem.get_text(strip=True) if time_elem else 'All day'
                category = category_elem.get_text(strip=True) if category_elem else 'All Ages'
                
                events.append({
                    'date': date_str,
                    'time': time_str,
                    'location': 'Tracy Branch Library',
                    'title': title,
                    'link': link,
                    'category': category,
                    'source': 'Library'
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Error fetching Tracy Library events: {e}")
    
    return events

def get_manteca_library_events():
    """Scrape Manteca Branch Library events"""
    events = []
    try:
        url = "https://www.ssjcpl.org/events-services/events-calendar/manteca-branch"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for event_div in soup.find_all('div', class_='spl-component-event-list-item'):
            try:
                title_elem = event_div.find('h2')
                if not title_elem:
                    continue
                    
                title = title_elem.get_text(strip=True)
                link_elem = title_elem.find('a')
                link = 'https://www.ssjcpl.org' + link_elem['href'] if link_elem and 'href' in link_elem.attrs else url
                
                date_elem = event_div.find('div', class_='date')
                time_elem = event_div.find('div', class_='time')
                category_elem = event_div.find('div', class_='category')
                
                date_str = date_elem.get_text(strip=True) if date_elem else 'TBD'
                time_str = time_elem.get_text(strip=True) if time_elem else 'All day'
                category = category_elem.get_text(strip=True) if category_elem else 'All Ages'
                
                events.append({
                    'date': date_str,
                    'time': time_str,
                    'location': 'Manteca Branch Library',
                    'title': title,
                    'link': link,
                    'category': category,
                    'source': 'Library'
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Error fetching Manteca Library events: {e}")
    
    return events

def get_mountain_house_library_events():
    """Scrape Mountain House Branch Library events"""
    events = []
    try:
        url = "https://www.ssjcpl.org/events-services/events-calendar/mountain-house"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for event_div in soup.find_all('div', class_='spl-component-event-list-item'):
            try:
                title_elem = event_div.find('h2')
                if not title_elem:
                    continue
                    
                title = title_elem.get_text(strip=True)
                link_elem = title_elem.find('a')
                link = 'https://www.ssjcpl.org' + link_elem['href'] if link_elem and 'href' in link_elem.attrs else url
                
                date_elem = event_div.find('div', class_='date')
                time_elem = event_div.find('div', class_='time')
                category_elem = event_div.find('div', class_='category')
                
                date_str = date_elem.get_text(strip=True) if date_elem else 'TBD'
                time_str = time_elem.get_text(strip=True) if time_elem else 'All day'
                category = category_elem.get_text(strip=True) if category_elem else 'All Ages'
                
                events.append({
                    'date': date_str,
                    'time': time_str,
                    'location': 'Mountain House Branch Library',
                    'title': title,
                    'link': link,
                    'category': category,
                    'source': 'Library'
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Error fetching Mountain House Library events: {e}")
    
    return events

def get_lathrop_library_events():
    """Scrape Lathrop Branch Library events"""
    events = []
    try:
        url = "https://www.ssjcpl.org/events-services/events-calendar/lathrop"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for event_div in soup.find_all('div', class_='spl-component-event-list-item'):
            try:
                title_elem = event_div.find('h2')
                if not title_elem:
                    continue
                    
                title = title_elem.get_text(strip=True)
                link_elem = title_elem.find('a')
                link = 'https://www.ssjcpl.org' + link_elem['href'] if link_elem and 'href' in link_elem.attrs else url
                
                date_elem = event_div.find('div', class_='date')
                time_elem = event_div.find('div', class_='time')
                category_elem = event_div.find('div', class_='category')
                
                date_str = date_elem.get_text(strip=True) if date_elem else 'TBD'
                time_str = time_elem.get_text(strip=True) if time_elem else 'All day'
                category = category_elem.get_text(strip=True) if category_elem else 'All Ages'
                
                events.append({
                    'date': date_str,
                    'time': time_str,
                    'location': 'Lathrop Branch Library',
                    'title': title,
                    'link': link,
                    'category': category,
                    'source': 'Library'
                })
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Error fetching Lathrop Library events: {e}")
    
    return events

def get_home_depot_events():
    """Generate Home Depot Kids Workshop events"""
    events = []
    # First Saturday of each month at 9 AM
    base_date = datetime(2026, 2, 7)  # Feb 7, 2026
    months = [2, 3, 4, 5, 6]  # Feb through Jun
    
    for month in months:
        # First Saturday of each month
        first_day = datetime(2026, month, 1)
        # Find first Saturday
        days_until_saturday = (5 - first_day.weekday()) % 7
        if days_until_saturday == 0 and first_day.weekday() != 5:
            days_until_saturday = 7
        event_date = first_day + timedelta(days=days_until_saturday)
        
        events.append({
            'date': event_date.strftime('%b %d'),
            'time': '9:00 AM - 10:00 AM',
            'location': 'Home Depot Tracy',
            'title': 'Kids Workshop - Free DIY Project',
            'link': 'https://www.homedepot.com/workshops/kids-workshops',
            'category': 'Children',
            'source': 'Home Depot'
        })
    
    return events

def get_ksb_skate_events():
    """Generate KSB Skate events at Tracy Veterans Park"""
    events = []
    # Sunday afternoons in January 2026
    january_sundays = [
        datetime(2026, 1, 4),
        datetime(2026, 1, 11),
        datetime(2026, 1, 18),
        datetime(2026, 1, 25)
    ]
    
    for sunday in january_sundays:
        events.append({
            'date': sunday.strftime('%b %d').replace(' 0', ' '),
            'time': '3:00 PM - 4:00 PM',
            'location': 'Tracy Veterans Park',
            'title': 'aariv Sawhney - KSB Skate Session',
            'link': 'https://www.ksbskatedojo.com/',
            'category': 'Children',
            'source': 'KSB Skate'
        })
    
    return events

def get_omca_events():
    """Generate Oakland Museum of California First Sunday events"""
    events = []
    # First Sunday of each month
    months = [1, 2, 3, 4, 5, 6]
    
    for month in months:
        first_sunday = datetime(2026, month, 1)
        # Find first Sunday
        days_until_sunday = (6 - first_sunday.weekday()) % 7
        if days_until_sunday == 0 and first_sunday.weekday() != 6:
            days_until_sunday = 7
        event_date = first_sunday + timedelta(days=days_until_sunday)
        
        events.append({
            'date': event_date.strftime('%b %d').replace(' 0', ' '),
            'time': '10:00 AM - 5:00 PM',
            'location': 'Oakland Museum of CA',
            'title': 'First Sunday Free Admission',
            'link': 'https://museumca.org/visit',
            'category': 'All Ages',
            'source': 'OMCA'
        })
    
    return events

def get_eventbrite_sf_events():
    """Scrape Eventbrite for SF area family events"""
    events = []
    try:
        # Search for "san francisco bay area family events"
        url = "https://www.eventbrite.com/d/ca--san-francisco/family--events/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find event cards
        for event_card in soup.find_all('div', class_='discover-search-desktop-card')[:5]:
            try:
                title_elem = event_card.find('h2')
                if not title_elem:
                    continue
                
                title = title_elem.get_text(strip=True)
                
                # Get link
                link_elem = event_card.find('a', href=True)
                link = link_elem['href'] if link_elem else url
                
                # Get date and location
                date_elem = event_card.find('p', string=re.compile(r'(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'))
                location_elem = event_card.find('p', string=re.compile(r'(San Francisco|SF|Bay Area)'))
                
                date_str = date_elem.get_text(strip=True) if date_elem else 'TBD'
                location_str = location_elem.get_text(strip=True) if location_elem else 'Thrive City (SF)'
                
                events.append({
                    'date': date_str,
                    'time': 'TBD',
                    'location': location_str,
                    'title': title,
                    'link': link,
                    'category': 'All Ages',
                    'source': 'Eventbrite'
                })
            except Exception:
                continue
                
    except Exception as e:
        print(f"Error fetching Eventbrite events: {e}")
        # Add a placeholder event
        events.append({
            'date': 'Mar 22',
            'time': '10 PM - 12 AM',
            'location': 'Thrive City',
            'title': 'Lucha Libre Wrestling Night',
            'link': 'https://www.eventbrite.com/e/lucha-libre-wrestling-night-tickets-1975640975340',
            'category': 'All Ages',
            'source': 'Eventbrite'
        })
    
    return events

def parse_date_for_sorting(date_str):
    """Parse date string and return sortable datetime object"""
    try:
        # Handle "Jan 04" or "Jan 4" format
        current_year = datetime.now().year
        date_str_clean = date_str.strip()
        
        # Parse the date
        parsed_date = datetime.strptime(date_str_clean, '%b %d')
        parsed_date = parsed_date.replace(year=current_year)
        
        # If date has already passed this year, assume it's next year
        if parsed_date < datetime.now():
            parsed_date = parsed_date.replace(year=current_year + 1)
        
        return parsed_date
    except:
        return datetime(2099, 12, 31)  # Far future for unparseable dates

def generate_html(events):
    """Generate HTML website with proper date attributes for filtering"""
    
    # Sort events by date
    events.sort(key=lambda x: parse_date_for_sorting(x['date']))
    
    # Get unique locations for filter
    locations = sorted(set(event['location'] for event in events))
    sources = sorted(set(event['source'] for event in events))
    
    # Get current timestamp
    now = datetime.now().strftime('%B %d, %Y at %I:%M %p PST')
    
    # Build HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚 Local Family Events</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        .subtitle {{
            opacity: 0.95;
            font-size: 1.1em;
        }}
        
        .stats {{
            background: rgba(255,255,255,0.2);
            display: inline-block;
            padding: 15px 30px;
            border-radius: 50px;
            margin-top: 20px;
            backdrop-filter: blur(10px);
        }}
        
        .stats-number {{
            font-size: 2.5em;
            font-weight: bold;
            display: block;
        }}
        
        .filters {{
            padding: 30px 40px;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
            display: flex;
            gap: 20px;
            flex-wrap: wrap;
            align-items: center;
        }}
        
        .filter-group {{
            display: flex;
            flex-direction: column;
            gap: 8px;
            flex: 1;
            min-width: 200px;
        }}
        
        .filter-group label {{
            font-weight: 600;
            color: #495057;
            font-size: 0.9em;
        }}
        
        select {{
            padding: 12px 16px;
            border: 2px solid #dee2e6;
            border-radius: 10px;
            font-size: 1em;
            background: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        select:hover {{
            border-color: #667eea;
        }}
        
        select:focus {{
            outline: none;
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }}
        
        .content {{
            padding: 40px;
        }}
        
        table {{
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            margin-top: 20px;
        }}
        
        thead {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            position: sticky;
            top: 0;
            z-index: 10;
        }}
        
        th {{
            padding: 16px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.5px;
        }}
        
        tbody tr {{
            background: white;
            transition: all 0.3s ease;
            border-bottom: 1px solid #e9ecef;
        }}
        
        tbody tr:hover {{
            background: #f8f9fa;
            transform: translateX(5px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        
        td {{
            padding: 16px;
        }}
        
        td:first-child {{
            font-weight: 600;
            color: #667eea;
        }}
        
        .day-badge {{
            display: inline-block;
            padding: 4px 12px;
            background: #e7f3ff;
            color: #0066cc;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: 600;
        }}
        
        .category-badge {{
            display: inline-block;
            padding: 4px 12px;
            background: #f0f0f0;
            border-radius: 20px;
            font-size: 0.85em;
            margin-right: 4px;
        }}
        
        a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }}
        
        a:hover {{
            color: #764ba2;
            text-decoration: underline;
        }}
        
        footer {{
            text-align: center;
            padding: 30px;
            background: #f8f9fa;
            color: #6c757d;
            font-size: 0.9em;
        }}
        
        .location-cell {{
            color: #6c757d;
            font-size: 0.95em;
        }}
        
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            
            .container {{
                border-radius: 10px;
            }}
            
            header {{
                padding: 20px;
            }}
            
            h1 {{
                font-size: 1.8em;
            }}
            
            .filters {{
                padding: 20px;
                flex-direction: column;
            }}
            
            .content {{
                padding: 20px;
                overflow-x: auto;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            th, td {{
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📚 Local Family Events</h1>
            <p class="subtitle">Libraries • Home Depot • KSB Skate • OMCA • Thrive City | Tracy • San Jose • Oakland • SF</p>
            <div class="stats">
                <span class="stats-number">{len(events)}</span>
                Total Events
            </div>
        </header>
        
        <div class="filters">
            <div class="filter-group">
                <label for="locationFilter">📍 Filter by Location:</label>
                <select id="locationFilter">
                    <option value="all">All Locations</option>
'''
    
    for location in locations:
        html += f'                    <option value="{location}">{location}</option>\n'
    
    html += '''                </select>
            </div>
            
            <div class="filter-group">
                <label for="dateFilter">📅 Filter by Date:</label>
                <select id="dateFilter">
                    <option value="all">All Dates</option>
                    <option value="today">Today</option>
                    <option value="tomorrow">Tomorrow</option>
                    <option value="week">This Week</option>
                    <option value="nextweek">Next Week</option>
                    <option value="month">This Month</option>
                    <option value="nextmonth">Next Month</option>
                </select>
            </div>
        </div>
        
        <div class="content">
            <h2>📅 All Events</h2>
            <table id="eventsTable">
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
'''
    
    # Add events to table with proper data attributes
    for event in events:
        # Parse date for data attribute (YYYY-MM-DD format)
        try:
            event_datetime = parse_date_for_sorting(event['date'])
            iso_date = event_datetime.strftime('%Y-%m-%d')
            day_name = event_datetime.strftime('%a')
        except:
            iso_date = '2099-12-31'
            day_name = 'TBD'
        
        html += f'''                    <tr data-location="{event['location']}" data-source="{event['source']}" data-date="{iso_date}">
                        <td>{event['date']}</td>
                        <td><span class="day-badge">{day_name}</span></td>
                        <td>{event['time']}</td>
                        <td class="location-cell">{event['location']}</td>
                        <td><a href="{event['link']}" target="_blank">{event['title']}</a></td>
                        <td><span class="category-badge">{event['category']}</span></td>
                    </tr>
'''
    
    html += f'''                </tbody>
            </table>
        </div>
        
        <footer>
            <p>Last updated: {now}</p>
            <p>Auto-updates daily • Data from library websites</p>
        </footer>
    </div>
    
    <script>
        function applyFilters() {{
            const selectedDate = document.getElementById('dateFilter').value;
            const selectedLocation = document.getElementById('locationFilter').value;
            const rows = document.querySelectorAll('#eventsTable tbody tr');
            
            // Get today's date at midnight
            const now = new Date();
            const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
            
            // Calculate date ranges
            const tomorrow = new Date(today);
            tomorrow.setDate(tomorrow.getDate() + 1);
            
            const endOfWeek = new Date(today);
            endOfWeek.setDate(today.getDate() + (7 - today.getDay()));
            
            const startOfNextWeek = new Date(endOfWeek);
            startOfNextWeek.setDate(startOfNextWeek.getDate() + 1);
            const endOfNextWeek = new Date(startOfNextWeek);
            endOfNextWeek.setDate(endOfNextWeek.getDate() + 6);
            
            const endOfMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0);
            
            const startOfNextMonth = new Date(today.getFullYear(), today.getMonth() + 1, 1);
            const endOfNextMonth = new Date(today.getFullYear(), today.getMonth() + 2, 0);
            
            rows.forEach(row => {{
                const location = row.getAttribute('data-location');
                const dateStr = row.getAttribute('data-date'); // YYYY-MM-DD format
                
                // Parse event date
                const eventDate = new Date(dateStr);
                
                // Date filter logic
                let dateMatch = true;
                if (selectedDate === 'today') {{
                    dateMatch = eventDate.toDateString() === today.toDateString();
                }} else if (selectedDate === 'tomorrow') {{
                    dateMatch = eventDate.toDateString() === tomorrow.toDateString();
                }} else if (selectedDate === 'week') {{
                    dateMatch = eventDate >= today && eventDate <= endOfWeek;
                }} else if (selectedDate === 'nextweek') {{
                    dateMatch = eventDate >= startOfNextWeek && eventDate <= endOfNextWeek;
                }} else if (selectedDate === 'month') {{
                    dateMatch = eventDate >= today && eventDate <= endOfMonth;
                }} else if (selectedDate === 'nextmonth') {{
                    dateMatch = eventDate >= startOfNextMonth && eventDate <= endOfNextMonth;
                }}
                
                // Location filter
                const locationMatch = selectedLocation === 'all' || location === selectedLocation;
                
                // Show/hide row
                if (dateMatch && locationMatch) {{
                    row.style.display = '';
                }} else {{
                    row.style.display = 'none';
                }}
            }});
        }}
        
        // Attach event listeners
        document.getElementById('dateFilter').addEventListener('change', applyFilters);
        document.getElementById('locationFilter').addEventListener('change', applyFilters);
    </script>
</body>
</html>'''
    
    return html

def main():
    """Main function to generate the website"""
    print("Fetching events from all sources...")
    
    all_events = []
    
    # Get events from all sources
    print("- Tracy Library...")
    all_events.extend(get_tracy_library_events())
    
    print("- Manteca Library...")
    all_events.extend(get_manteca_library_events())
    
    print("- Mountain House Library...")
    all_events.extend(get_mountain_house_library_events())
    
    print("- Lathrop Library...")
    all_events.extend(get_lathrop_library_events())
    
    print("- Home Depot...")
    all_events.extend(get_home_depot_events())
    
    print("- KSB Skate...")
    all_events.extend(get_ksb_skate_events())
    
    print("- OMCA...")
    all_events.extend(get_omca_events())
    
    print("- Eventbrite...")
    all_events.extend(get_eventbrite_sf_events())
    
    print(f"\nTotal events found: {len(all_events)}")
    
    # Generate HTML
    print("Generating HTML...")
    html = generate_html(all_events)
    
    # Write to file
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("✅ Website generated successfully: index.html")
    print(f"📊 Total events: {len(all_events)}")

if __name__ == "__main__":
    main()
