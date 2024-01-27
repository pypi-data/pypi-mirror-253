import os
import getpass

## Try to import Google Colab userdata
try:
    from google.colab import userdata
    from google.colab.userdata import NotebookAccessError
except ImportError:
    colab_exists = False
else:
    colab_exists = True


def get_secret_value(key):
    """
    Check in to env
    if not found check in to google colab userdata, if available
    else asks for that key, will be presented as ****
    """
    # Check in os.environ
    if key in os.environ:
        return os.environ[key]
    
    if colab_exists:
        colab_val = None

        # Check in Google Colab's user data
        try:        
            colab_val = userdata.get(key)
            return colab_val
        except NotebookAccessError as nae:
            raise nae
        except Exception:
            pass
        
    # Ask the user for the value if not found
    return getpass.getpass(f"Enter the value for {key}: ")