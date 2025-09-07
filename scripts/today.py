#!/usr/bin/env python3
import datetime, yaml, sys, pathlib

p = pathlib.Path(__file__).resolve().parents[1] / "schedule.yaml"
d = yaml.safe_load(open(p, encoding="utf-8"))
today = datetime.date.today()


def in_range(r):
    a = r[0]
    b = r[1]
    return a <= today <= b


phase = next((ph for ph in d["phases"] if in_range(ph["range"])), None)
print(f"📅 Today: {today.isoformat()}")
if phase:
    print(f"🎯 Phase: {phase['label']}")
    print("✅ Focus:")
    for k, v in phase["focus"].items():
        print(f"  - {k}: {v}")
    print("\n추천 워크플로우:")
    print(
        "1) 개념 5문항 퀵체크 → 2) 관련 테스트 실행 → 3) 실패 분석/패치 → 4) 오답키워드 기록(review.md)"
    )
else:
    print("학습 구간 외 입니다. review.md 회독 또는 기출 1세트 권장.")
