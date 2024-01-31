# grpccotea



## Installation

```
pip install grpcio
pip install grpcio-tools
```

## Run server

In the server env:
```
export GRPC_ENABLE_FORK_SUPPORT=0
export GRPC_POLL_STRATEGY=poll
```

Run the server:
```
python grpc_server.py
```

## Client example
File client.py contains client example.