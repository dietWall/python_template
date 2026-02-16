#! /usr/bin/env python3

import argparse
import os.path

packages = \
{        
#python -m build.
#pip install .
#pytest test/
}

def main():
    """Main function to build Docker images and run containers"""
    
    parser = argparse.ArgumentParser(description="Builds and run different images and containers in this repo")
    ops = ["build", "test"]

    parser.add_argument("--package", "-p", help="selects a package", choices=packages, default=None, required=True)
    parser.add_argument("--operations", "-o", help="selects the operations", choices=ops, nargs="+")

    parser.add_argument("--keep_running", 
                        help="keeps the container running for debugging, if any started", 
                        action="store_true", 
                        default=False)

    args = parser.parse_args()
    helper = docktools(None)
    #todo: operations must be: build package, test package, release package,
    #  not build container, run container
    for op in args.operations:
        if op == "build":
            result, output = helper.execute(command=packages[args.package]["build"])
            if result.returncode != 0:
                print(f"build of {args.package} failed with {result.returncode}")
                for l in output:
                    print(l.strip())
            else:
                print(f"build successful")
                for l in output:
                    print(l.strip())
        elif op == "test":
            pass

    if args.keep_running == False:
        if helper.get_containers(args.package) != []:
            helper.stop_container(args.package)
            helper.remove_container(args.package)
    else:
        print(f"keeping the container {args.package} running, you can enter it with:")
        print(f"docker exec -it {args.package} bash")

if __name__ == "__main__":
    main()