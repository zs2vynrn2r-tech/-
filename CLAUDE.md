# 작업 규칙 (토큰 절약)

- **시험 대비 교재·모의고사 요청** → 먼저 `exam-pack` 스킬(`.claude/skills/exam-pack/SKILL.md`)을 읽고 그 렌더러·스키마를 그대로 쓴다. 새로 설계하지 않는다.
- 과목 자료는 `<과목>_기말/` 폴더: 결과 PDF, `source/`(원문 전사본 `*.md`, 최신 `guide.json`·`mock.json`). 다음 범위는 이 JSON을 이어서 작성한다.
- 저장소 구조 질문은 `graphify query "..."` / `graphify explain "..."`로 먼저 찾는다 (`graphify-out/graph.json`). 파일 추가 후 `graphify update .`(LLM 불필요).
- ponytail 플러그인 원칙: 꼭 필요한 만큼만 바꾼다. 수정 요청은 python 패치 → 재렌더로 끝낸다.
- 교재·모의고사에 **조문을 묻는 문제는 만들지 않는다** (조문 번호는 해설 근거로만).
- `/67`(에이전트 7개)은 사용자가 부를 때만 쓴다. 기본은 에이전트 0~1개.
- 큰 파일(JSON, PDF, 서브에이전트 출력)은 통째로 읽지 않고 필요한 부분만 출력한다.
