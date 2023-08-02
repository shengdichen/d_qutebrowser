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
        return " ".join(["set", item, Cmd._reformat_value(value)])

    @staticmethod
    def cycle_config_items(
        item_candidates_pairs: Iterable[tuple[str, Iterable[str | dict]]]
    ) -> str:
        return Cmd.concat(
            (
                Cmd.cycle_config_item(item, candidates)
                for item, candidates in item_candidates_pairs
            )
        )

    @staticmethod
    def cycle_config_item(item: str, candidates: Iterable[str | dict]) -> str:
        candidates_as_str = " ".join(
            (Cmd._reformat_value(value) for value in candidates)
        )
        return " ".join(["config-cycle", item, candidates_as_str])

    @staticmethod
    def _reformat_value(value) -> str:
        if isinstance(value, dict):
            return Cmd._reformat_dict(value)

        return str(value)

    @staticmethod
    def _reformat_dict(d: dict) -> str:
        return f'"{d}"'
