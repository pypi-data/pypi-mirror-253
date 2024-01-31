import logging
import os
import sys
import argparse
import multiprocessing as mp

from grpc_cotea.cotea_gateway_server import CoteaGatewayServer
from grpc_cotea.worker_connecter import WorkerConnectorLocal
from grpc_cotea.worker_maker import WorkerMakerLocal


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(prog="grpc-cotea", formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-p', '--port',
                        metavar='<grpc_cotea_gateway_port>',
                        type=int,
                        help='grpc-cotea gateway port, default is 50151')
    
    parser.add_argument('--host',
                    metavar='<host_addr>',
                    type=str,
                    help="if grpc-cotea should be available not only at localhost (0.0.0.0 don't work)")

    parser.add_argument('-w', '--workers',
                        metavar='<workers_count>',
                        type=int,
                        help='grpc-cotea workers count, default is 5')

    parser.add_argument('-m', '--mitogen',
                        action='store_true',
                        help='more logs will be shown')


    parser.add_argument('-v',
                        action='store_true',
                        help='more logs will be shown')

    parser.add_argument('--not-merge-logs',
                    action='store_true',
                    help="grpc-cotea workers logs will be merged with ansible logs")
    
    parser.add_argument('--extra-workers-killing-timeout',
                        metavar='<secs>',
                        type=int,
                        help='number of seconds free extra workers will be killed, default is 300')

    (args, _) = parser.parse_known_args(args)

    os.environ["GRPC_ENABLE_FORK_SUPPORT"] = "0"
    os.environ["GRPC_POLL_STRATEGY"] = "poll"

    gateway_port = "50151"
    if args.port is not None:
        gateway_port = str(args.port)

    workers_to_spawn = 5
    if args.workers is not None:
        workers_to_spawn = int(args.workers)
    
    log_lvl = logging.INFO
    if args.v:
        log_lvl = logging.DEBUG
    
    host = "localhost"
    if args.host:
        host = args.host
    
    use_mitogen = False
    if args.mitogen:
        use_mitogen = True
    
    merge_logs = True
    if args.not_merge_logs:
        merge_logs = False

    workers_killing_timeout = 300
    if args.extra_workers_killing_timeout is not None:
        workers_killing_timeout = int(args.extra_workers_killing_timeout)

    # gateway will run on specified port
    # also n works will be launched
    # on n ports starting from the specified one
    # (n+1, n+2, ...)

    conn_connecter, conn_maker = mp.Pipe()

    workers_connecter = WorkerConnectorLocal(conn_connecter)
    workers_maker = WorkerMakerLocal(conn_maker, gateway_port=gateway_port, use_mitogen=use_mitogen, merge_logs=merge_logs)
    # workers = []

    # for _ in range(workers_to_spawn):
    #     w = worker_spawner.spawn()
    #     w.start_work()
    #     workers.append(w)

    maker_p = mp.Process(target=workers_maker.start)
    maker_p.start()

    cgs = CoteaGatewayServer(workers_connecter=workers_connecter, port=gateway_port, host=host, \
         log_lvl=log_lvl, workers_count=workers_to_spawn, workers_killing_timeout=workers_killing_timeout)
    cgs.start()
