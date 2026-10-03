# v1.5 추가 참고 자료와 기능 변경

확인일: 2026-10-02. 기존 11개에 8개 저장소를 추가해 총 19개 출처를 기록했다. 주로 진입 지침과 이번 문제에 관련된 구간을 검토했다. 저장소 전체, 모든 예시와 코드를 검증했다는 뜻은 아니다. 도구나 설치 스크립트를 실행하지 않았다.

일부 저장소는 blader/humanizer나 im-not-ai에서 파생되었고 비슷한 패턴을 반복한다. **19개 출처는 서로 독립적인 19개 방법이나 성능 검증 19건을 뜻하지 않는다.** 러시아어 스킬은 평가 설계와 과잉 교정의 비교 자료이며 한국어·영어 지원 근거가 아니다.

| 출처의 고정 버전 | 범위 | 참고한 판단 | 적용하지 않은 처방 |
| --- | --- | --- | --- |
| [hannsxpeter/humanizer](https://github.com/hannsxpeter/humanizer/blob/978116a9ac2b094b7a6bb5f6a482b0eee41f3084/SKILL.md) | 영어 | 문체를 먼저 정하고 이후 상투어를 정리; 교정이 만드는 새 획일성 점검 | 인위적 리듬 분산, 상위 폴더 자동 검색, 표면 신호로 작성 주체 추정 |
| [Aparnabuilds/humanizer](https://github.com/Aparnabuilds/humanizer/blob/fd9728f1a66a5338dff533c712dd44509900e065/SKILL.md) | 영어 | 문단이 실제로 새 내용을 더하는지 확인 | 문장부호 전면 금지, 검증되지 않은 주장 자동 삭제, 문단 수 고정 |
| [ryanmaule/humanize](https://github.com/ryanmaule/humanize/blob/4a8bbcf74984dad5bdad10177afe766e32bc7633/SKILL.md) | 영어 | 글의 목적과 소수의 실제 문체 특징을 먼저 파악; 과잉 교정 억제 | 모든 글에 최소 수정만 적용, 내용 추가가 가능한 일부 교정 예시 |
| [milock/humanizer](https://github.com/milock/humanizer/blob/ec66c203c0400481819fda9cb17a6f1c7977c975/SKILL.md) | 영어 | 구조 우선 검토와 긍정적인 완성 기준; 채널에 맞는 문체 근거 | 구두점 예산, 일정 비율 이상 변경 거부, 강제 보고서 양식 |
| [liam-nextdomain/humanizer-kr](https://github.com/liam-nextdomain/humanizer-kr/blob/77badef924fbb9488242b7073b0b2c5838573f91/humanizer-kr/SKILL.md) | 한국어 | 고유 비유와 주제어 보존, 교정 예시의 문체를 복제하지 않는 기준 | 어미 비율 고정, 필수 승인 단계, 고정 글자 수의 분할 |
| [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill/blob/9fade13b1066bc58fd820fe659145a9a21974138/korean-humanizer/instruction.md) | 한국어 | im-not-ai 계열의 수사·담화 분류를 대조 확인 | 근거 없는 개인 감정이나 정량 표현을 덧붙이는 예시, CLI 실행 |
| [TaewoooPark/personal-humanizer-maker](https://github.com/TaewoooPark/personal-humanizer-maker/blob/86b987d2c609e41854a43214c8868718b5b6acea/skills/personal-humanizer-maker/SKILL.md) | 한국어·영어 | 문체의 여러 축과 증거별 신뢰도, 샘플과 편집 대상의 구분 | 개인 프로필 자동 생성·설치, 빈도 목표 강제, 구조 변경 제한 |
| [ilyautov/humanizer-ru](https://github.com/ilyautov/humanizer-ru/blob/1e035ad6b64c56c6e770ed28d076e2cbda3d1aed/skills/humanizer-ru/SKILL.md) | 러시아어 비교자료 | 지어낸 감정·리듬의 부작용, 수정과 평가 분리 | 러시아어 규칙의 한영 이전, 자체 청결도 점수의 상용 탐지 점수 취급 |

## 실제 변경

1. 단어 제거보다 먼저 독자·목적·거리감·근거 있는 문체 특징을 짧게 정한다. 샘플이 없으면 저자 개인의 목소리를 지어내지 않는다.
2. 보존해야 하는 의미와 원래 문장의 수를 분리한다. 행위자·행위·대상·시점·강도로 반복 지시를 대조하고, 공통 대상을 공유해 재작성한다.
3. 도입·평가·이유의 기능을 독립 문장 유지, 실제 문장에 흡수, 이미 수행된 기능의 중복 제거로 구분한다. 사실과 평가를 함께 담은 예시를 추가했다.
4. 명사만 줄이는 수정에서 더 나아가 한국어 추상 술어와 영어 메타 설명을 구체적 관계로 고친다. 검토를 권고한 원문을 의무나 확정 결과로 바꾸지 않는다.
5. 별도 세션으로 기존 결과를 진단하고 새 장르의 원문을 동결해 버전 간 비교에 사용한다. 반복 횟수 상한은 늘리지 않았다.

이 변경의 출처는 공개 스킬의 편집 아이디어와 v1.4 원문/수정본의 독립 진단이다. 탐지기 내부 모델이나 비공개 기준을 알아낸 것은 아니다. 원본의 보장 문구·자체 청결도·고정 빈도·자체 검증 수치를 이 스킬의 성능으로 옮기지 않았다. 아래 실험 보고서의 관측만 실제 탐지 결과로 취급한다.
