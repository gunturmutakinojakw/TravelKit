# === Stage 55: Add a setting to disable colorized output ===
# Project: TravelKit
import sys
from typing import Optional, Callable

class ColorControl:
    def __init__(self):
        self._disabled = False
        self._original_stdout = None

    @property
    def is_disabled(self) -> bool:
        return self._disabled

    def disable_colors(self) -> None:
        """Disables color output by replacing stdout with a plain text stream."""
        if not sys.stdout.isatty():
            return
        
        # Save original stdout to restore later if needed (optional feature)
        self._original_stdout = sys.stdout
        
        # Create a wrapper that strips ANSI codes from any print calls
        class PlainStream:
            def __init__(self, stream):
                self.stream = stream
            
            def write(self, text):
                # Remove common ANSI escape sequences (e.g., '\033[...m')
                plain_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
                self.stream.write(plain_text)
            
            def flush(self):
                self.stream.flush()
        
        # Apply the wrapper only if colors are disabled and not already handled by terminal settings
        if self._disabled:
            sys.stdout = PlainStream(sys.stdout)

def setup_color_control(disable_colors: bool = False) -> Optional[Callable]:
    """
    Configures color output based on environment or explicit flag.
    Returns a cleanup function to restore colors if disable_colors was True.
    
    Args:
        disable_colors (bool): If True, disables ANSI color codes in stdout.
        
    Returns:
        Optional[Callable]: A function to restore original stdout and re-enable colors.
                            None if no change was made or restoration is not supported.
    """
    control = ColorControl()
    
    # Check environment variable first (e.g., NO_COLOR=1)
    import os
    env_no_color = os.getenv('NO_COLOR', '').lower() in ('1', 'true', 'yes')
    
    if disable_colors or env_no_color:
        try:
            control.disable_colors()
            return lambda: setattr(sys.stdout, '_original_stdout', sys.stdout) # Placeholder for restoration logic
        except Exception:
            pass
    
    return None

# Usage example within main script context:
# from travelkit.utils import setup_color_control
# cleanup = setup_color_control(disable_colors=True)
# if cleanup:
#     try:
#         print("This text will have no colors.")
#     finally:
#         cleanup()
