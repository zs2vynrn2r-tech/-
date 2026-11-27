# Additions to schema.md (round 2)

## 1) Diagram on a list item
Any list item may carry "diagram". Use it on EVERY item tagged "필기" whose handwriting is a picture/arrow/계산 (and on other items where a picture beats prose).
"diagram": {
  "w": 640, "h": 240,                      // viewBox size in px; width ≤ 660. Keep text 11–13px; leave ≥16px margins.
  "caption": "한 문장으로 이 그림이 보여주는 것 (해요체)",
  "groups": [ {"x":10,"y":10,"w":420,"h":150,"label":"상호계산 기간 (1/1~6/30)", "fill":"none"} ],   // dashed frame with label top-left
  "nodes":  [ {"id":"A","x":40,"y":60,"w":110,"h":56,"label":"A (상인)","sub":"원재료 공급","tone":"main|accent|muted|plain","shape":"rect|pill"} ],
             // label: bold 12.5px, 1–2 lines ("\n"); sub: 10.5px small text. Box width ≈ 13px × longest line chars + 20.
  "edges":  [ {"from":"A","to":"B","label":"채권 ①","dir":"->|<->|-","style":"solid|dashed","tone":"plain|main|accent",
               "offset":-10,          // parallel shift in px (use ±10 for two opposite arrows between same pair)
               "lx":0,"ly":-6,        // label offset from midpoint
               "cross":true} ],       // draws ✕ on the edge = "불가/×" (e.g., 개입권 ×, 변제청구 불가)
  "notes":  [ {"x":470,"y":150,"text":"이자 10%","tone":"main|accent","size":11,"anchor":"start|middle|end","weight":400} ]
}
Rules (from the artifact-diagramming skill): draw the mechanism, not its name — who owes whom, which way money/claims/risk flow, what a third party can/can't reach, before/after. Label every arrow (양도, 압류, 출자, 이익분배, 손실분담, 대외적 책임…). Align to a grid (multiples of 10), even gaps. Accent tone (orange) only for the one thing the 필기 stresses (the ✕, the trap, the result). Follow the layout of the student's handwriting (look at the photo crops), but cleaner. One figure, one claim. Numbers from the 필기 (200/100 등) go in nodes/notes.
Render-check every diagram: nothing overlapping, nothing outside the viewBox, labels readable.

## 2) Boxed 사례 text
guide "cases" items and mock questions may carry "box": "갑은 …\n을은 …" — a boxed fact pattern (<사례>), shown between the stem and options. Use it for 사례형 and 판례 적용형 questions: put the facts in "box", the question in "q"/"stem". ㄱ·ㄴ·ㄷ 보기 can also go in box.
