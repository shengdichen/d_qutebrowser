from collections.abc import Iterable


class Cmd:
    @staticmethod
    def concat(commands: Iterable[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def set_config_items(items_values: Iterable[tuple[str, str | dict]]) -> str:
        return Cmd.concat(
            (Cmd.set_config_item(item, value) for item, value in items_values)
        )

    @staticmethod
    def set_config_item(item: str, value: str | dict) -> str:
        if isinstance(value, dict):
            value = Cmd._reformat_dict(value)

        return " ".join(["set", item, value])

    @staticmethod
    def _reformat_dict(d: dict) -> str:
        return f'"{d}"'
