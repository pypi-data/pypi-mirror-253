def main():
    import argparse

    parser = argparse.ArgumentParser(prog="redlite", description="CLI ops for redlite")
    subparsers = parser.add_subparsers(required=True, dest="cmd")

    parser_server = subparsers.add_parser("server", help="starts UI server")
    parser_server.add_argument("--port", "-p", type=int, default=8000, help="Server port")

    args = parser.parse_args()
    if args.cmd == "server":
        from .server.app import main as server_main

        print("*** HTTP UI server")
        server_main(args.port)


if __name__ == "__main__":
    main()
