# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAeVSHIvE:APA91bFp0ac-A95fnu1cjzZL5AFafxPZDuLGM0_IuPjEjkek-a1c8APooQxLZ2frhv018SU3_qB5bc01KKj9WLXxMNlXgXHSvES5GbCaOKuW_d1SKfaHmRfxVIhPZQIyXlLJuPF5ur0e")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "d6j_2XWkSN-R2HI4uNRh2X:APA91bF1K1hbj0z074KzDwIJbwEXOxqu5OHfoEL2ULb9vBKWPTMLCMgvgfzy0-vm5gaVBH8tfR0_gFMFuSFzYFF2Pq-3RyDwiKlT9-apr35O3vyc7cE4z_xDGfxGwSrxRD1eWoWlLTmq"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
print(result)
