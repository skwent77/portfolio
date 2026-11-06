# 신재현 · Portfolio

AI 연구와 백엔드 프로젝트를 소개하는 GitHub Pages 포트폴리오입니다.

참고한 디자인: [박재현 님의 Portfolio](https://hyun-je.github.io/Portfolio/). 여백, 세리프 타이포그래피와 2열 갤러리 구성을 참고했으며, 코드·문구·프로젝트 이미지는 새로 작성했습니다. 프로젝트 이미지는 실제 서비스 화면이 아닌 설명용 벡터 그래픽입니다.

## 로컬 실행

```sh
python3 -m http.server 4173
```

브라우저에서 http://localhost:4173 을 엽니다. 빌드나 패키지 설치가 필요 없습니다.

## 수정하기

- `index.html`: 소개, 프로젝트 목록, 이력, 연락 링크
- `projects.js`: 프로젝트 상세 내용과 GitHub 링크
- `styles.css`: 레이아웃, 타이포그래피, 모바일 스타일
- `script.js`: 상세 모달, 프로젝트 이동, URL 연동
- `assets/*.svg`: 직접 제작한 프로젝트 개념 그래픽

프로젝트 추가 시 `index.html`의 카드와 `projects.js`의 항목을 함께 추가하고 섹션의 작품 수를 수정하세요. 카드의 `data-project` 값과 상세 데이터의 `id`가 일치해야 합니다.

## GitHub Pages

저장소 **Settings → Pages → Deploy from a branch → main / (root)** 로 배포합니다. 모든 내부 리소스는 상대 경로이므로 프로젝트 하위 경로에서도 동작합니다.

글꼴은 Google Fonts에서 불러오며, 연결할 수 없는 경우 시스템 세리프·고정폭 글꼴로 표시됩니다. 외부 분석기, 쿠키, 수집용 폼은 사용하지 않습니다.
