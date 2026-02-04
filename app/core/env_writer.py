from pathlib import Path

ENV_PATH = Path("/app/.env")


def write_env(key: str, value: str):
    if not ENV_PATH.exists():
        ENV_PATH.write_text("")

    lines = ENV_PATH.read_text().splitlines()
    new_lines = []
    found = False

    for line in lines:
        if line.startswith(f"{key}="):
            new_lines.append(f"{key}={value}")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{key}={value}")

    ENV_PATH.write_text("\n".join(new_lines) + "\n")

def read_env():
    from app.core.config import settings
    if settings.LOGGING_ENABLED:
        print(f"[알림] : env를 정보를 불러오는 중입니다.")

    data = {}
    if not ENV_PATH.exists():
        return data

    content = ENV_PATH.read_text()

    for line in content.splitlines():
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        data[k] = v
    if settings.LOGGING_ENABLED:
        print(f"[알림] : env를 정보를 모두 불러왔습니다.")
    return data