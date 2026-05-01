from datetime import datetime, time


def main() -> None:
    print("Starting log generator... (Press Ctrl+C to stop)")

    try:
        while True:
            now = datetime.now()

            name_file = now.strftime("app-%H_%M_%S.log")

            content = now.strftime("%Y-%m-%d %H:%M:%S")

            with open(name_file, "w") as file:
                file.write(content)

            print(f"{content} {name_file}")

            time.sleep(1)

    except KeyboardInterrupt:
        print("\Application terminated by user.")


if __name__ == "__main__":
    main()
