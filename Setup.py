from pip._internal.cli.main import main
common_packages = [
    "colorama>=0.4.6",
    "selenium",
]

def install_packages(packages: list[str] = common_packages):
    for pkg in packages:
        main(["install", "-U", pkg])
    with open("SetupCompleted.txt", "w") as f:
        f.write("Setup successfully completed")

if __name__ == '__main__':
    install_packages(common_packages)
