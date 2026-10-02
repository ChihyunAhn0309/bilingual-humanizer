# 조사한 스킬과 설계 근거

확인일: 2026-10-02. 공개 GitHub 저장소의 SKILL.md 원문과 주요 지침을 비교했다. 아래는 원문 전체에 대한 성능 평가가 아니라 이번 설계에서 선택한 아이디어와 제외한 가정이다. 설치되어 있던 한국어 스킬 네 개도 확인했지만, 원격 최신 버전과 다르면 구분했다.

## 초기 공개 스킬 11개

| 원본과 고정 커밋 | 범위 | 채택한 관점 | 그대로 가져오지 않은 부분 |
| --- | --- | --- | --- |
| [blader/humanizer](https://github.com/blader/humanizer/blob/225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8/SKILL.md) · `225a6f39ac85` | 영어 중심 | 단어보다 문단의 반복·수사 구조를 살피고 원문 의미와 목소리를 보존 | 모든 장르에 같은 리듬을 강제하거나 검토 중간본을 기본 출력하지 않음 |
| [keez97/humanizer](https://github.com/keez97/humanizer/blob/2d9a116fa9caee2c3466a7c7d419cbe02b35a470/SKILL.md) · `2d9a116fa9ca` | 영어 중심 | 장르별 편집 강도, 표면 신호의 과해석 경계, 제한된 교정 반복 | 소수 사례의 탐지 실험을 모든 탐지기·재작성에 대한 불가능성 정리로 확대하지 않음 |
| [apoapostolov/humanizer](https://github.com/apoapostolov/humanizer/blob/51c5f43fc8619dcc658dcbff800265163906b80a/skills/humanizer/SKILL.md) · `51c5f43fc861` | 영어 중심 | 의미 보존, 실제 경험만 사용, 문체·용도에 따른 모드 분리 | 외부 sibling skill 의존, detector chase, 소셜 글에 특정 디테일을 요구하는 공식을 제외 |
| [ashgreat/humanizer](https://github.com/ashgreat/humanizer/blob/952c8a138e29eb2cbe637b8ae8e9f6c6e2f6d627/SKILL.md) · `952c8a138e29` | 영어 학술 중심 | 논지 단위 문단 구성, 전문 용어와 인과·통계적 강도 보존 | 저자가 설명한 제한된 학술 코퍼스의 규칙을 범용화하지 않고 대시 전면 금지·we 강제를 제외 |
| [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill/blob/a58df065367550b6ce40ff3f648335018d8e0589/skills/humanizer/SKILL.md) · `a58df0653675` | 영어 중심 | 문체 프로필, 맥락 판단, 비원어민 글의 오탐 경계 | 문장 길이 분산 목표, 대시 전면 금지, 자체 점수로 탐지 결과를 예측하는 규칙을 제외 |
| [DaleSeo/korean-skills](https://github.com/DaleSeo/korean-skills/blob/ae12ba27982ebeff03b46dc738365aaa34260d9a/skills/humanizer/SKILL.md) · `ae12ba27982e` | 한국어 | 띄어쓰기·품사·쉼표·번역투를 영어와 별도로 살피는 구성 | 94.88을 범용 정확도로 읽거나 단일 표현을 결정적 AI 증거로 삼는 규칙을 제외 |
| [choconyam/humanizer-ko](https://github.com/choconyam/humanizer-ko/blob/eeab53e7dc511eeebaa0c41acf850b269b26ff32/SKILL.md) · `eeab53e7dc51` | 한국어·영어 | 언어별 지침, 주체·부정·양태·근거 보존, 표면 검사와 의미 검토의 구분 | 현재 스킬은 별도 코드로 작성하고 전문용어 자료 전체를 복제하지 않음 |
| [monologg/humanizer-kr](https://github.com/monologg/humanizer-kr/blob/ba6b8b5ef08e36c88b6ce25d8ba488834cadf7be/SKILL.md) · `ba6b8b5ef08e` | 한국어 | 한국어 장르별 말투와 번역투 항목을 분리해서 검토 | 추정된 1990년대를 확정된 1994년으로 바꾸는 예시 같은 사실 추가, 고정 리듬 가정을 배제 |
| [dotoricode/korean-humanizer](https://github.com/dotoricode/korean-humanizer/blob/4fc566b7d7ded76887f7a85c0886e44796e5e38c/SKILL.md) · `4fc566b7d7de` | 한국어 | 문체·존댓말·정보 보존, 사용자 선호, 필요한 만큼 문장 재구성 | 현재 원격 버전은 고정 교정 비율을 제거했다. 로컬 설치본에 있던 20% 한도를 최신 원격 버전의 규칙으로 잘못 기재하지 않음 |
| [evergreentree97/K-Humanizer](https://github.com/evergreentree97/K-Humanizer/blob/324435d561ba48d53de6b7d3fb3dd72cf77030dc/skills/k-humanizer/SKILL.md) · `324435d561ba` | 한국어 | 이력서의 실제 기여 범위, 경험·시도·결과 구분, 지어낸 성과 금지 | 기본 이력서 중심 라우팅, 특수 문장부호 전면 금지, 고정 변경률 제한을 범용 규칙으로 넣지 않음 |

## 재현 가능한 출처 기록

추가 조사한 [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai/tree/2f3d943d08056b612a92e12bfb72ea94dd2acd18)는 한국어 대조·당위·추상 서술의 반복, 지칭 관계, 윤문 중 새 상투구가 생기는 문제를 검토하는 데 참고했다. [상세 검토](im-not-ai-review.md)에 반영한 아이디어, 적용하지 않은 고정 변경률·빈도 처방, 자체 실험의 한계를 구분했다. 원본 스킬이나 스크립트를 연쇄 실행하지 않는다.

각 파일의 원격 커밋, 파일 경로, SHA-256, 확인일은 [skill-sources.json](skill-sources.json)에 기록했다. 커밋 날짜와 조사 날짜는 다르다. GitHub 라이선스 API의 `NOASSERTION`은 라이선스가 없다는 단정이 아니라 API가 확정하지 못했다는 값이다. 상류 저장소의 완성된 규칙·코드·예문을 묶어 재배포하지 않고, 원리를 검토해 새 지침·예문·검사 코드를 작성했다. 특정 상류 파일을 후속 복제할 때는 해당 파일의 라이선스와 고지를 따로 확인해야 한다.

## 이번 설계의 선택

사용자의 선택은 범용 지원과 적극적 재작성이다. 따라서 문장·문단 재구성을 기본으로 두고, 편집 비율이나 길이 비율 대신 정보 보존 여부로 판단한다. 한국어와 영어를 별도 참조문서로 나눴으며 혼합 문서는 문장 단위로 해당 기준을 적용한다. 사실 보존, 장르 적합성, 작성자 말투는 탐지 점수와 분리한다.

여러 스킬의 명령을 차례로 모두 실행하면 서로 다른 금지어·출력 양식·문체 기본값이 충돌할 수 있다. 이 패키지는 상류 스킬을 연쇄 호출하지 않고 하나의 편집 계약으로 통합했다. 이는 설계 판단이며, 통계적으로 우월함을 입증한 실험 결과는 아니다.

## 연구와 공식 제품 자료

탐지 제품 12개 항목과 공개 연구 5개 계열의 근거는 [detectors-and-authorship.md](detectors-and-authorship.md)에 각 주장 옆에 연결했다. 제품 기능·지원 언어·정확도는 서로 다른 항목이다. 마케팅 수치를 공통 데이터셋의 비교 순위로 만들지 않았다.

한국어 연구는 [KatFishNet ACL 2025 논문](https://aclanthology.org/2025.acl-long.1030/)의 장르별 실험을 기준으로 범위를 제한했다. 사람이 쓴 것으로 보이게 하는 스킬의 검증과 탐지 모델의 AUROC는 다른 문제다. 이 연구가 스킬의 모든 어휘 목록이나 편집 규칙을 검증했다는 주장은 하지 않는다.

스킬의 폴더·SKILL.md·선택 참조 파일 구성은 [OpenAI 공식 스킬 작성 안내](https://developers.openai.com/plugins/build/skills)에 맞췄다. 설치 환경에서는 제공된 skill-creator의 검증기를 사용한다.

## 남은 검증 범위

영어·한국어 실제 사용자 문서의 블라인드 원어민 평가, 장르별 대규모 의미 보존 평가, 독립 에이전트 평가, 상용 탐지기 실측은 이번 조사·구현만으로 완료되지 않는다. 로컬 단위 테스트는 검사 코드의 동작을 확인하며 스킬의 자연스러움이나 탐지 통과율을 입증하지 않는다. [평가 절차](evaluation.md)는 이런 후속 검증을 구분해서 수행하도록 마련했다.

## v1.5 확장 조사

[추가 8개 출처 비교](v15-reference-review.md)에 채택·제외 이유와 기능 변경을 기록했다. 현재 출처 목록은 19개이며, 파생 관계 때문에 독립적인 방법 19개로 계산하지 않는다.
# Follow-up inspection

The 2026-10-03 [expanded review](further-reference-review.md) adds selected-section screening of 13 skill repositories and 3 research implementations. Its [separate manifest](further-sources.json) records exact commits, read scope and rejected assumptions. Keep the original 19-repository manifest as a historical record; do not count forks as independent experimental support.

