from mfrc522 import MFRC522
import RPi.GPIO as GPIO

# Initialize the reader
reader = MFRC522()

# List of known/default keys to test (common keys used in MIFARE cards)
known_keys = [
    [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF],  # Default key
    [0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5],  # Common key A
    [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5],  # Common key B
    [0xD3, 0xF7, 0xD3, 0xF7, 0xD3, 0xF7],  # Known key
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00]   # All zeros
]

try:
    print("Place the card near the reader...")
    while True:
        (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
        if status == reader.MI_OK:
            (status, uid) = reader.MFRC522_Anticoll()
            if status == reader.MI_OK:
                print(f"Card UID: {uid}")
                for sector in range(16):
                    block = sector * 4 + 3  # Last block of the sector (sector trailer)
                    found_key = False
                    for key in known_keys:
                        status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, block, key, uid)
                        if status == reader.MI_OK:
                            print(f"Sector {sector} trailer read successfully with key: {key}")
                            found_key = True
                            reader.MFRC522_StopCrypto1()
                            break
                    if not found_key:
                        print(f"Failed to read sector {sector} trailer with known keys.")
                break
finally:
    GPIO.cleanup()
