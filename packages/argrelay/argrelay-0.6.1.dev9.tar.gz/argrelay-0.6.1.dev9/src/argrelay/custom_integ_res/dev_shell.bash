#!/usr/bin/env bash
# `argrelay` integration file: https://github.com/argrelay/argrelay

# This is just a wrapper to start a new shell with special config and stay in that shell.
# Implements FS_58_61_77_69 dev_shell.

if [[ -n "${dev_shell_old_opts+x}" ]] ; then exit 1 ; fi

# Save `set`-able options to restore them at the end of this source-able script:
# https://unix.stackexchange.com/a/383581/23886
dev_shell_old_opts="$( set +o )"
case "${-}" in
    *e*) dev_shell_old_opts="${dev_shell_old_opts}; set -e" ;;
      *) dev_shell_old_opts="${dev_shell_old_opts}; set +e" ;;
esac
# Set special env var used before passing control to nexted interactive shell.
# This env var is used by the script which is sourced this one:
# shellcheck disable=SC2034
user_shell_opts="${dev_shell_old_opts}"

# Debug: Print commands before execution:
#set -x
# Debug: Print commands after reading from a script:
#set -v
# Return non-zero exit code from commands within a pipeline:
set -o pipefail
# Exit on non-zero exit code from a command:
set -e
# Inherit trap on ERR by sub-shells:
set -E
# Error on undefined variables:
set -u

failure_color="\e[41m"
reset_color="\e[0m"

# Indicate failure by color:
function color_failure_only {
    exit_code="${?}"
    if [[ "${exit_code}" != "0" ]]
    then
        echo -e "${failure_color}FAILURE:${reset_color} ${BASH_SOURCE[0]}: exit_code: ${exit_code}" 1>&2
        exit "${exit_code}"
    fi
}

trap color_failure_only EXIT

script_source="${BASH_SOURCE[0]}"
# The dir of this script:
script_dir="$( cd -- "$( dirname -- "${script_source}" )" &> /dev/null && pwd )"
# FS_29_54_67_86 dir_structure: `@/exe/` -> `@/`:
argrelay_dir="$( dirname "${script_dir}" )"

cd "${argrelay_dir}" || exit 1

# Let some code know that it runs under `@/exe/dev_shell.bash` (e.g to run some tests conditionally):
ARGRELAY_DEV_SHELL="$(date)"
export ARGRELAY_DEV_SHELL

# The new shell executes `@/exe/init_shell_env.bash` script as its init file:
# https://serverfault.com/questions/368054
if [[ "$#" -eq "0" ]]
then
    # Interactive:
    bash --init-file <(echo "source ~/.bashrc && source ${argrelay_dir}/exe/init_shell_env.bash")
else
    # Non-interactive:
    # All args passed to `@/exe/dev_shell.bash` are executed as command line:
    bash --init-file <(echo "source ~/.bashrc && source ${argrelay_dir}/exe/init_shell_env.bash") -i -c "${*}"
fi

