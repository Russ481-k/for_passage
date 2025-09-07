#!/usr/bin/env bash
set -e
echo "[SQL] (sqlite3 필요)"; which sqlite3 && sqlite3 :memory: ".read sql/schema.sql" ".read sql/seed.sql"
echo "[Python]"; cd algorithms && pip install -r requirements.txt >/dev/null && pytest -q || true; cd ..
echo "[Java]"; cd programming-java && mvn -q -DskipTests=false test || true; cd ..
echo "[C]"; cd programming-c && make && make test || true; cd ..
echo "Done."
