from collections.abc import Iterable


class Cmd:
    @staticmethod
    def concat(commands: Iterable[str]) -> str:
        return ";; ".join(commands)

    @staticmethod
    def repeat(command: str, repeat_for: int) -> list[str]:
        return repeat_for * [command]

    @staticmethod
    def set_config_items(items_values: Iterable[tuple[str, str | dict]]) -> str:
        return Cmd.concat(
            (Cmd._set_config_item(item, value) for item, value in items_values)
        )

    @staticmethod
    def _set_config_item(item: str, value: str | dict) -> str:
        return " ".join(["set", item, Cmd._reformat_value(value)])

    @staticmethod
    def cycle_config_items(
        item_candidates_pairs: Iterable[tuple[str, Iterable[str | dict]]]
    ) -> str:
        return Cmd.concat(
            (
                Cmd._cycle_config_item(item, candidates)
                for item, candidates in item_candidates_pairs
            )
        )

    @staticmethod
    def _cycle_config_item(item: str, candidates: Iterable[str | dict]) -> str:
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

    @staticmethod
    def enter_as_prompt(cmd: str, append_space: bool = True) -> str:
        base = "set-cmd-text "
        if append_space:
            return f"{base}--space :{cmd}"

        return f"{base}:{cmd}"

    @staticmethod
    def do_in_new_tab(cmd: str) -> str:
        base = "open --tab"

        if not cmd:
            return base
        return Cmd.concat([base, cmd])
