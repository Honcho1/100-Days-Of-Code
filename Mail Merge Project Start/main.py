from pathlib import Path


def main():
    project_dir = Path(__file__).resolve().parent
    names_path = project_dir / "Input" / "Names" / "invited_names.txt"
    template_path = project_dir / "Input" / "Letters" / "starting_letter.txt"
    output_dir = project_dir / "Output" / "ReadyToSend"

    template = template_path.read_text(encoding="utf-8")
    names = names_path.read_text(encoding="utf-8").splitlines()
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in names:
        name = name.strip()
        if not name:
            continue

        letter = template.replace("[name]", name)
        output_path = output_dir / f"letter_for_{name}.txt"
        output_path.write_text(letter, encoding="utf-8")


if __name__ == "__main__":
    main()
