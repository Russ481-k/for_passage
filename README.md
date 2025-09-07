# study-lab — LLM Assisted Learning

## Quickstart
1) Cursor로 이 폴더 열기
2) 터미널:
   - `python3 scripts/today.py` (오늘 범위 확인)
   - `bash scripts/run_all.sh` (전체 테스트 시동)
3) LLM에 `tasks/daily-run.md` 붙여 대화 시작:
   - 개념 요약 → 퀴즈 → 실패 테스트 → 패치 PR(패치 블록) 제시 → 재검증
4) 오답은 `review.md`에 날짜/키워드/링크 기록

## 폴더별 안내
- sql/: schema/seed 실행 후 exercises로 문제풀이
- algorithms/: pytest로 실패 항목부터 그린북 페치
- programming-java/: `mvn test`로 TDD
- programming-c/: `make && make test`

## 루틴
- 매일: today.py → daily-run
- 1D/3D/7D: review-loop로 재출제
