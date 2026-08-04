import datetime
import requests
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("QuickStart-Server")

@mcp.tool()
def get_weather(city: str) -> str:
    """Fetch the current weather for a given city."""
    # Using a free, no-auth weather API for testing
    url = f"https://wttr.in{city}?format=3"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        return f"Could not find weather data for {city}."
    except Exception as e:
        return f"Error fetching weather: {str(e)}"

@mcp.tool()
def get_local_time(timezone_offset: int = 0) -> str:
    """Get the current local time adjusted by a UTC offset hours."""
    now = datetime.datetime.now(datetime.timezone.utc)
    adjusted_time = now + datetime.timedelta(hours=timezone_offset)
    return f"The current time is: {adjusted_time.strftime('%Y-%m-%d %H:%M:%S')} (UTC {timezone_offset:+})"

if __name__ == "__main__":
    # Run the server using Stdio transport (standard for local AI IDEs)
    mcp.run(transport="stdio")
