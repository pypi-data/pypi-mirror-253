import argparse
from pathlib import Path
from ..command import RemoteCommand



class Command(RemoteCommand):
    @classmethod
    def get_help(cls) -> str:
        return """Loads all Recipe Entries from an extracted Paprika archive into a Notion DB."""

    @classmethod
    def add_arguments(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument("import_path", type=Path)

    def handle(self) -> None:
        remote = self.get_remote()

        self.options.export_path.mkdir(parents=True, exist_ok=True)

        for recipe in track(
            remote, total=remote.count(), description="Downloading Recipes"
        ):
            with open(
                self.options.export_path / Path(f"{recipe.name}.paprikarecipe.yaml"),
                "w",
            ) as outf:
                dump_recipe_yaml(recipe, outf)