import logging

# ===== 1. CONFIGURING THE LOGGER
# We set up exactly how the logs should look and where they should go.

path = "./11_production/log/"  # to create file in this folder

logging.basicConfig(
    # filename=path + "server.log",  # Where to save the logs
    filename="server.log",  # Where to save the logs
    level=logging.DEBUG,  # The minimum severity level to record
    format="%(asctime)s - %(levelname)s - %(message)s",  # The standard enterprise format"
)

# ===== 2. THE 5 LEVELS OF SEVERITY
# You choose the method based on how bad the situation is.

# Level 1: DEBUG (Detailed information, typically of interest only when diagnosing problems)

logging.debug("System memory at 45%.")

# Level 2: INFO (Confirmation that things are working as expected)
logging.info("Database connection established.")

# Level 3: WARNING (An indication that something unexpected happened, but the software is still working)
logging.warning("Disk space running low (85% full).")

# Level 4: ERROR (Due to a more serious problem, the software has not been able to perform some function)
logging.error("Failed to process payment for User #1052.")

# Level 5: CRITICAL (A serious error, indicating that the program itself may be unable to continue running)
logging.critical("MAIN DATABASE CORRUPTED. INITIATING SHUTDOWN.")

# ===== 3. LOGGING EXCEPTIONS
# If you catch an error, use logging.exception(). It automatically captures
# the full technical traceback and writes it to the log file!
try:
    x = 10 / 0
except ZeroDivisionError:
    logging.exception("A mathematical failure occurred in the billing engine.")
