import os


def move_file(command: str) -> None:
    if command.startswith("mv ") and len(command.split()) == 3:
        comm, source_file, destination_file = command.split()

        if len(destination_file.split("/")) == 1:
            os.rename(source_file, destination_file)

        if len(destination_file.split("/")) > 1:
            os.makedirs(destination_file.rsplit("/", 1)[0], exist_ok=True)

            with (open(source_file, "r") as source,
                  open(destination_file, "w") as destination):
                destination.write(source.read())

            os.remove(source_file)
