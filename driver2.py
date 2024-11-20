from mfrc522 import MFRC522
import RPi.GPIO as GPIO

# Initialize the reader
reader = MFRC522()

try:
    print("Place the original card near the reader...")

    # Read data from the original card
    original_data = []
    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

        if status == reader.MI_OK:
            print("Original card detected")

            (status, uid) = reader.MFRC522_Anticoll()

            if status == reader.MI_OK:
                print(f"Original Card UID: {uid}")
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                for sector in range(16):  # MIFARE Classic 1K
                    sector_data = []
                    for block in range(sector * 4, (sector * 4) + 4):
                        status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, block, key, uid)
                        if status == reader.MI_OK:
                            data = reader.MFRC522_Read(block)
                            sector_data.append(data)
                        else:
                            sector_data.append(None)  # Block could not be read
                    original_data.append(sector_data)
                    reader.MFRC522_StopCrypto1()

                break

    # Print the original card data for verification (optional)
    for i, sector in enumerate(original_data):
        for j, block_data in enumerate(sector):
            if block_data:
                print(f"Sector {i}, Block {i * 4 + j}: {block_data}")

    input("Place the blank card near the reader and press Enter to write...")

    # Write data to a blank card
    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

        if status == reader.MI_OK:
            print("Blank card detected")

            (status, uid) = reader.MFRC522_Anticoll()

            if status == reader.MI_OK:
                print(f"Blank Card UID: {uid}")
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                for i, sector in enumerate(original_data):
                    for j, block_data in enumerate(sector):
                        block = i * 4 + j
                        if block_data and status == reader.MFRC522_Auth(reader.PICC_AUTHENT1A, block, key, uid):
                            reader.MFRC522_Write(block, block_data)
                        else:
                            print(f"Failed to write to Sector {i}, Block {block}")

                    reader.MFRC522_StopCrypto1()

                print("Data written to the blank card successfully.")
                break

finally:
    GPIO.cleanup()