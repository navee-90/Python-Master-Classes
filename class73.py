# import logging
# import logging in Python is used to bring in the built-in logging module, which helps you record messages from your program while it runs.
# You can control the level of importance (info, warning, error, etc.)
# Easily write logs to a file
# Turn logging on/off or set levels without changing your code logic
# Cleaner and more professional for production-level projects

import logging
logging.basicConfig(filename='app.log',level=logging.INFO)
logging.debug("this debug msg")
logging.info("this information msg")
logging.warning("this is warning msg")
logging.error("this eroor msg")
logging.critical("this is critical msg")