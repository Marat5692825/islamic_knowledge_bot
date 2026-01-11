from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    bot_token: str
    admin_ids: str = ""
    database_url: str = "sqlite+aiosqlite:///db.sqlite3"

    @property
    def admin_id_set(self) -> set[int]:
        raw = [x.strip() for x in self.admin_ids.split(",") if x.strip()]
        result: set[int] = set()
        for item in raw:
            try:
                result.add(int(item))
            except ValueError:
                continue
        return result


settings = Settings()
