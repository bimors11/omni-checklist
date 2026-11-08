#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"

APT_PACKAGES=(
  python3
  python3-pip
  python3-venv
  python3-dev
  build-essential
  patchelf
  file
  desktop-file-utils
  curl
  ca-certificates
  libgl1
  libglib2.0-0
  libxkbcommon-x11-0
  libxcb-cursor0
  libxcb-icccm4
  libxcb-image0
  libxcb-keysyms1
  libxcb-randr0
  libxcb-render-util0
  libxcb-shape0
  libxcb-xinerama0
  libxcb-xfixes0
)

DNF_PACKAGES=(
  python3
  python3-pip
  python3-devel
  gcc
  gcc-c++
  make
  patchelf
  file
  desktop-file-utils
  curl
  ca-certificates
  mesa-libGL
  glib2
  libxkbcommon-x11
  xcb-util-cursor
  fuse
)

PACMAN_PACKAGES=(
  python
  python-pip
  base-devel
  patchelf
  file
  desktop-file-utils
  curl
  ca-certificates
  libgl
  glib2
  libxkbcommon-x11
  xcb-util-cursor
  fuse2
)

has_command() {
  command -v "$1" >/dev/null 2>&1
}

run_sudo() {
  if [[ "${EUID}" -eq 0 ]]; then
    "$@"
  elif has_command sudo; then
    sudo "$@"
  else
    echo "Missing sudo. Re-run as root or install the missing dependencies manually." >&2
    return 1
  fi
}

install_system_packages() {
  if has_command apt-get; then
    echo "Checking system packages with apt..."
    local missing=()
    local package
    for package in "${APT_PACKAGES[@]}"; do
      if ! dpkg-query -W -f='${Status}' "$package" 2>/dev/null | grep -q "install ok installed"; then
        missing+=("$package")
      fi
    done
    if ((${#missing[@]})); then
      run_sudo apt-get update
      run_sudo apt-get install --no-remove -y "${missing[@]}"
    else
      echo "System packages already installed."
    fi
    return
  fi

  if has_command dnf; then
    echo "Checking system packages with dnf..."
    local missing=()
    local package
    for package in "${DNF_PACKAGES[@]}"; do
      if ! rpm -q "$package" >/dev/null 2>&1; then
        missing+=("$package")
      fi
    done
    if ((${#missing[@]})); then
      run_sudo dnf install -y "${missing[@]}"
    else
      echo "System packages already installed."
    fi
    return
  fi

  if has_command pacman; then
    echo "Checking system packages with pacman..."
    local missing=()
    local package
    for package in "${PACMAN_PACKAGES[@]}"; do
      if ! pacman -Q "$package" >/dev/null 2>&1; then
        missing+=("$package")
      fi
    done
    if ((${#missing[@]})); then
      run_sudo pacman -Sy --needed --noconfirm "${missing[@]}"
    else
      echo "System packages already installed."
    fi
    return
  fi

  echo "No supported package manager found. Install Python 3, pip, venv, curl, patchelf, and Qt/XCB runtime libraries manually." >&2
}

setup_python_env() {
  if ! has_command python3; then
    echo "python3 is required but was not found." >&2
    exit 1
  fi

  if [[ ! -d "${VENV_DIR}" ]]; then
    echo "Creating virtual environment at ${VENV_DIR}"
    python3 -m venv "${VENV_DIR}"
  fi

  # shellcheck source=/dev/null
  source "${VENV_DIR}/bin/activate"

  python -m pip install --upgrade pip setuptools wheel
  python -m pip install -r "${ROOT_DIR}/requirements.txt"
  python -m pip install pyinstaller
}

install_system_packages
setup_python_env

echo
echo "Setup complete."
echo "Run the app with: ${VENV_DIR}/bin/python ${ROOT_DIR}/main.py"
