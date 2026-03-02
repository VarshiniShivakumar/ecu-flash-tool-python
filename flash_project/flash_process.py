import sqlite3
import os
import random
from datetime import datetime

DB_NAME = "flash_database.db"


# Generate Unique Session ID
def generate_session_id():

    return "SES_" + datetime.now().strftime("%Y%m%d%H%M%S")


# Flashing Process
def perform_flash(ecu_id,
                  binary_path,
                  old_version,
                  new_version):


    session_id = generate_session_id()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    binary_name = os.path.basename(binary_path)


    # Flashing Steps
    steps = [

        "Step 1 : Connecting to ECU",

        "Step 2 : Session Control Started",

        "Step 3 : Security Access Granted",

        "Step 4 : Erasing Old Software",

        "Step 5 : Uploading Binary File",

        "Step 6 : Verifying Data",

        "Step 7 : ECU Reset"

    ]


    # SUCCESS or FAULT
    success = random.choice([True, False])


    if success:

        status = "SUCCESS"
        error = "None"
        recovery = "No Recovery Needed"

    else:

        status = "FAULT"

        error = random.choice([

            "ECU Not Responding",
            "Binary Verification Failed",
            "Connection Lost",
            "Voltage Low"

        ])


        recovery_dict = {

            "ECU Not Responding":
            "Restart ECU and retry flashing",

            "Binary Verification Failed":
            "Reflash correct binary file",

            "Connection Lost":
            "Check Ethernet connection and retry",

            "Voltage Low":
            "Provide stable power supply"

        }

        recovery = recovery_dict[error]


    # Store in Database

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO flash_history_customer
    VALUES (?,?,?,?,?,?,?,?,?)

    """,

    (

        session_id,
        ecu_id,
        status,
        timestamp,
        binary_name,
        old_version,
        new_version,
        error,
        recovery

    ))

    conn.commit()
    conn.close()


    return session_id,steps,status,error,recovery