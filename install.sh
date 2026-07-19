#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"
BUILD_DIR="${ROOT_DIR}/build"
DIST_DIR="${ROOT_DIR}/dist"
APP_NAME="OMNI Checklist"
APP_ID="omni-checklist"
APPDIR="${BUILD_DIR}/${APP_ID}.AppDir"
APPIMAGE_TOOL="${BUILD_DIR}/tools/appimagetool"
ARCH="$(uname -m)"

case "${ARCH}" in
  x86_64 | amd64)
    APPIMAGE_ARCH="x86_64"
    ;;
  aarch64 | arm64)
    APPIMAGE_ARCH="aarch64"
    ;;
  *)
    echo "Unsupported AppImage architecture: ${ARCH}" >&2
    exit 1
    ;;
esac

has_command() {
  command -v "$1" >/dev/null 2>&1
}

ensure_setup() {
  if [[ ! -x "${VENV_DIR}/bin/python" ]]; then
    echo "Local Python environment not found. Running setup.sh first..."
    "${ROOT_DIR}/setup.sh"
  fi

  # shellcheck source=/dev/null
  source "${VENV_DIR}/bin/activate"

  if ! python - <<'PY'
import importlib.util
import sys

missing = [name for name in ("PyQt5", "PyInstaller") if importlib.util.find_spec(name) is None]
if missing:
    print("Missing Python packages: " + ", ".join(missing), file=sys.stderr)
    sys.exit(1)
PY
  then
    echo "Refreshing local Python environment..."
    deactivate 2>/dev/null || true
    "${ROOT_DIR}/setup.sh"
    # shellcheck source=/dev/null
    source "${VENV_DIR}/bin/activate"
  fi
}

download_appimagetool() {
  if [[ -x "${APPIMAGE_TOOL}" ]]; then
    return
  fi

  mkdir -p "$(dirname "${APPIMAGE_TOOL}")"
  local url="https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-${APPIMAGE_ARCH}.AppImage"
  echo "Downloading appimagetool for ${APPIMAGE_ARCH}..."

  if has_command curl; then
    curl -L "${url}" -o "${APPIMAGE_TOOL}"
  elif has_command wget; then
    wget -O "${APPIMAGE_TOOL}" "${url}"
  else
    echo "curl or wget is required to download appimagetool." >&2
    exit 1
  fi

  chmod +x "${APPIMAGE_TOOL}"
}

build_pyinstaller_app() {
  rm -rf "${BUILD_DIR}/pyinstaller" "${DIST_DIR}/${APP_ID}"
  mkdir -p "${BUILD_DIR}" "${DIST_DIR}"

  pyinstaller \
    --noconfirm \
    --clean \
    --onedir \
    --windowed \
    --name "${APP_ID}" \
    --distpath "${DIST_DIR}" \
    --workpath "${BUILD_DIR}/pyinstaller" \
    --add-data "${ROOT_DIR}/assets:assets" \
    "${ROOT_DIR}/main.py"
}

write_appdir_files() {
  rm -rf "${APPDIR}"
  mkdir -p "${APPDIR}/usr/bin" "${APPDIR}/usr/share/applications" "${APPDIR}/usr/share/icons/hicolor/256x256/apps"

  cp -a "${DIST_DIR}/${APP_ID}/." "${APPDIR}/usr/bin/"
  cp "${ROOT_DIR}/assets/betawhite.png" "${APPDIR}/${APP_ID}.png"
  cp "${ROOT_DIR}/assets/betawhite.png" "${APPDIR}/.DirIcon"
  cp "${ROOT_DIR}/assets/betawhite.png" "${APPDIR}/usr/share/icons/hicolor/256x256/apps/${APP_ID}.png"

  tee "${APPDIR}/AppRun" >/dev/null <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec "${HERE}/usr/bin/omni-checklist" "$@"
EOF
  chmod +x "${APPDIR}/AppRun"

  tee "${APPDIR}/${APP_ID}.desktop" >/dev/null <<EOF
[Desktop Entry]
Type=Application
Name=${APP_NAME}
Exec=${APP_ID}
Icon=${APP_ID}
Categories=Utility;
Terminal=false
EOF
  cp "${APPDIR}/${APP_ID}.desktop" "${APPDIR}/usr/share/applications/${APP_ID}.desktop"
}

build_appimage() {
  rm -f "${DIST_DIR}/${APP_ID}-${APPIMAGE_ARCH}.AppImage"
  ARCH="${APPIMAGE_ARCH}" APPIMAGE_EXTRACT_AND_RUN=1 "${APPIMAGE_TOOL}" "${APPDIR}" "${DIST_DIR}/${APP_ID}-${APPIMAGE_ARCH}.AppImage"
  chmod +x "${DIST_DIR}/${APP_ID}-${APPIMAGE_ARCH}.AppImage"
}

ensure_setup
download_appimagetool
build_pyinstaller_app
write_appdir_files
build_appimage

echo
echo "AppImage created:"
echo "${DIST_DIR}/${APP_ID}-${APPIMAGE_ARCH}.AppImage"
