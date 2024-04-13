from discord import SyncWebhook, File
import time

def send_msg():
    webhook_url = 'channel-webhook'
    message_text = 'your-message'
    image_file_path = 'photo-path'
    webhook = SyncWebhook.from_url(webhook_url)
    message = webhook.send(content='Message number 1', file=File(image_file_path), wait=True)
    counter = 2
    while True:
        new_content = f'{message_text} {counter}'
        webhook.edit_message(message_id=message.id, content=new_content)
        counter += 1
        time.sleep(5)
if __name__ == '__main__':
    send_msg()
