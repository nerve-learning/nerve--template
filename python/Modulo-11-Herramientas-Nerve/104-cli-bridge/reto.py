import time
from nerve import NexusClient

# Client that listens for messages crossing the bridge
client = NexusClient()

try:
    print("Bridge client trying to connect...")
    client.connect("cliente_puente")
    print("Connection successful.")

    def on_message_received(data):
        print(f"Message received via bridge: {data}")

    # Listen for incoming messages
    client.listen(on_message_received)
    print("Listening for messages. Press Ctrl+C to exit.")

    while True:
        time.sleep(1)

except ConnectionRefusedError:
    print("Error: Could not connect to the Hub.")
    print("Make sure 'nerve start' is running.")
