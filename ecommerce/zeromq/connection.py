import zmq

if __name__ == '__main__':
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://64.227.143.218:32148")
    socket.setsockopt(zmq.SUBSCRIBE, b"runs")

    while True:
        message = socket.recv()
        print(f"Received: {message}")