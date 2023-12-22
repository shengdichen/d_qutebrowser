#!/usr/bin/env dash

SCRIPT_PATH="$(realpath "$(dirname "${0}")")"
cd "${SCRIPT_PATH}" || exit 3

__download_dicts() {
    (
        local _dict_dir="${HOME}/.local/share/qutebrowser/qtwebengine_dictionaries"
        mkdir -p "${_dict_dir}"
        cd "${_dict_dir}" || exit 3

        for l in "de-DE" "en-US" "es-ES" "fr-FR" "it-IT" "pt-BR" "ru-RU" "sv-SE"; do
            if ! find . -maxdepth 1 -printf "%P\n" | grep -q "^${l}-.*\.bdic$"; then
                echo "[qutebrowser-dict:${l}] Installing"
                python "/usr/share/qutebrowser/scripts/dictcli.py" install "${l}"
            fi
        done
    )
}

__stow() {
    (
        cd .. && stow -R "$(basename "${SCRIPT_PATH}")"
    )
}

main() {
    __download_dicts
    __stow

    unset SCRIPT_PATH
    unset -f __download_dicts __stow
}
main
unset -f main
