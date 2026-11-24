# 모든 프로젝트에서 쓰는 기본 스킬

이 저장소와 이 세션에 설치된 스킬을 **사용자 전역(`~/.claude/skills`)**에 설치하는 방법입니다.
전역에 설치한 스킬은 어느 프로젝트를 열어도 Claude Code가 자동으로 불러옵니다.

## 한 번에 설치 (macOS / Linux)

새 컴퓨터나 새 환경에서 아래를 그대로 실행하세요. 이미 있는 스킬은 덮어쓰기만 합니다.

```bash
# 1. 이 저장소에서 직접 만든 스킬 5개
npx -y skills add zs2vynrn2r-tech/- -g -y -s 67 aura-farming china-maxing crash-out larp

# 2. 외부 스킬
npx -y skills add vercel-labs/agent-browser -g -y -s agent-browser
npx -y skills add vercel-labs/skills       -g -y -s find-skills
npx -y skills add Leonxlnx/taste-skill     -g -y -s design-taste-frontend
npx -y skills add anthropics/skills        -g -y -s mcp-builder
npx -y skills add nutlope/hallmark         -g -y
npx -y skills add heygen-com/hyperframes   -g -y

# 3. Graphify (uv 필요: curl -LsSf https://astral.sh/uv/install.sh | sh)
uv tool install graphifyy && graphify install

# 4. Ponytail 플러그인
claude plugin marketplace add DietrichGebert/ponytail --scope user
claude plugin install ponytail@ponytail --scope user

# 5. 확인
npx -y skills ls -g
claude plugin list
```

저장소가 비공개라면 1번은 GitHub에 로그인된 컴퓨터에서만 됩니다.

## 스킬 목록

| 스킬 | 언제 쓰나 | 출처 |
|---|---|---|
| `67` | 중요한 결과물을 6가지 방식으로 만들어 비교한 뒤 가장 좋은 것으로 합칠 때 | 이 저장소 |
| `aura-farming` | 광고, 슬라이드, 포스터 같은 시각물이 "AI가 만든 티" 없이 나와야 할 때 | 이 저장소 |
| `china-maxing` | 하위 에이전트를 많이 쓰는 작업에서 토큰을 아낄 때 | 이 저장소 |
| `crash-out` | 사실 확인, 디버깅, 조사처럼 틀리면 손해가 큰 답을 낼 때 | 이 저장소 |
| `larp` | 창업 아이디어를 냉정하게 검증할 때 | 이 저장소 |
| `agent-browser` | 웹사이트 열기, 폼 작성, 스크린샷, 웹앱 테스트 | vercel-labs/agent-browser |
| `find-skills` | 필요한 기능의 스킬을 찾을 때 | vercel-labs/skills |
| `design-taste-frontend` | 랜딩 페이지, 웹사이트, 앱 화면 디자인 | Leonxlnx/taste-skill |
| `mcp-builder` | MCP 서버를 만들 때 | anthropics/skills |
| `hallmark` | 새 웹페이지를 디자인할 때 (`/hallmark`) | nutlope/hallmark |
| `hyperframes` 외 8개 | HTML로 영상, 슬라이드쇼 만들기 (`hyperframes`, `hyperframes-cli`, `hyperframes-registry`, `media-use`, `reverse-any-video`, `style-sampling`, `remotion-to-hyperframes`, `slideshow`, `figma`) | heygen-com/hyperframes |
| `graphify` | 프로젝트나 문서 묶음을 지식 그래프로 만들 때 (`/graphify .`) | graphifyy (uv) |
| `ponytail` | 코딩할 때 꼭 필요한 만큼만 바꾸기 (플러그인, 항상 켜짐) | DietrichGebert/ponytail |

디자인 스킬이 세 개(`design-taste-frontend`, `hallmark`, `aura-farming`)라서, 디자인을 요청할 때는 쓸 스킬 이름을 같이 말하는 게 좋습니다.

## 클라우드 세션(claude.ai/code)에서 쓰려면

클라우드 세션은 매번 새 컨테이너에서 시작해서, 위에서 설치한 것이 남지 않습니다.
claude.ai/code의 **환경 설정 → 설정 스크립트(setup script)**에 위 "한 번에 설치" 블록을 넣으면 그 환경의 모든 세션에서 기본으로 설치됩니다.

## Headroom (스킬은 아니지만 함께 쓰는 도구)

```bash
uv tool install --python 3.13 "headroom-ai[proxy,mcp]"
echo "alias claude='headroom wrap claude'" >> ~/.zshrc   # bash라면 ~/.bashrc
```
