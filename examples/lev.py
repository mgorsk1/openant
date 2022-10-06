from ant.easy.node import Node
from ant.devices.lev import Lev, LevData

# standard ANT+ network key
NETWORK_KEY = [0xB9, 0xA5, 0x21, 0xFB, 0xBD, 0x72, 0xC3, 0x45]

def main(device_id=0):
    node = Node()
    node.set_network_key(0x00, NETWORK_KEY)

    device = Lev(node, device_id=device_id)

    def on_found():
        print(f"Device {device} found and receiving")

    def on_device_data(page: int, page_name: str, data):
        if isinstance(data, LevData):
            print(f"Lev {page_name} ({page}) update: {data}")

    device.on_found = on_found
    device.on_device_data = on_device_data

    try:
        print(f"Starting {device}, press Ctrl-C to finish")
        node.start()
    except KeyboardInterrupt:
        print(f"Closing ANT+ device...")
    finally:
        device.close_channel()
        node.stop()

if __name__ == "__main__":
    main()
