def copy_file(command: str) -> None:
    file_names = command.split(" ")
    if file_names[1] != file_names[2]:
        with (open(file_names[1], "r") as file_in,
              open(file_names[2], "w") as file_out):
            lines = file_in.read()
            file_out.write(lines)
