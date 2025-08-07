from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.utilities.types import Image

import pyautogui
import pyscreeze
import io
import sys

# Create server
mcp = FastMCP("Screenshot Demo")

@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture the current screen and return the image. Use this tool whenever the user requests a screenshot of their activity.
    """
    try:
        # Check if pyscreeze is available
        
        print("pyscreeze imported successfully", file=sys.stderr)
        
        buffer = io.BytesIO()

        # if the file exceeds ~1MB, it will be rejected by Claude
        screenshot = pyautogui.screenshot()
        print(f"Screenshot captured: {screenshot.size}", file=sys.stderr)
        
        screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
        print(f"Image saved to buffer, size: {len(buffer.getvalue())} bytes", file=sys.stderr)
        
        return Image(data=buffer.getvalue(), format="jpeg")
    
    except ImportError as e:
        print(f"Import error: {e}", file=sys.stderr)
        raise Exception(f"Required dependencies not available: {e}")
    except Exception as e:
        print(f"Screenshot error: {e}", file=sys.stderr)
        raise Exception(f"Failed to capture screenshot: {e}")

if __name__ == "__main__":
    mcp.run()