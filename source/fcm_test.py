# Send to single device.
from pyfcm import FCMNotification
from data_collection import countDown, recordBlinkSequence, majorityLogic, storeBlinkSequence

push_service = FCMNotification(api_key="AAAAeVSHIvE:APA91bFp0ac-A95fnu1cjzZL5AFafxPZDuLGM0_IuPjEjkek-a1c8APooQxLZ2frhv018SU3_qB5bc01KKj9WLXxMNlXgXHSvES5GbCaOKuW_d1SKfaHmRfxVIhPZQIyXlLJuPF5ur0e")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

BLINK_SEQUENCES = ["1010", "0101", "1100", "0011"]

for blink_sequence in BLINK_SEQUENCES:
    print("****************************************")
    print("Recording: " + blink_sequence)
    countDown()
    recorded_bits = recordBlinkSequence()
    detected_sequence = majorityLogic(recorded_bits)
    storeBlinkSequence(blink_sequence, recorded_bits, detected_sequence)

    registration_id = "d6j_2XWkSN-R2HI4uNRh2X:APA91bF1K1hbj0z074KzDwIJbwEXOxqu5OHfoEL2ULb9vBKWPTMLCMgvgfzy0-vm5gaVBH8tfR0_gFMFuSFzYFF2Pq-3RyDwiKlT9-apr35O3vyc7cE4z_xDGfxGwSrxRD1eWoWlLTmq"
    message_title = "Eye Blink Sequence Detected"
    message_body = detected_sequence 
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
    print(result)
