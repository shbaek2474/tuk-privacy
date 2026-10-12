# 툭 개인정보 처리방침

시행일: 2026년 10월 [일]

툭(이하 "앱")은 생각, 링크, 사진, 일정을 던져 두면 알아서 정리하고, 물어보면 꺼내 주는 개인용 서랍 앱입니다. 이 방침은 앱이 어떤 정보를 어디에서 다루는지 설명합니다.

툭의 기본 원칙은 세 가지입니다.

- **서랍 내용은 내 폰에만 저장됩니다.** 툭 서버에는 글, 사진, 질문, 답이 저장되지 않습니다.
- **정리하고 답할 때만 필요한 내용이 AI로 갑니다.** 처리가 끝나면 툭 서버에는 남지 않습니다.
- **🔒로 시작하는 줄은 어디로도 보내지 않습니다.** 서버, AI, 캘린더, 내보내기 파일 어디에도 들어가지 않습니다.

## 1. 폰에 저장되는 정보

다음 정보는 이용자의 폰 안에만 저장되며, 운영자는 볼 수 없습니다.

- 던진 글, 링크, 사진과 정리 결과(제목, 주제, 일정, 함께 나온 이름)
- 질문과 답, 목차, 그래프 위치, 설정
- 툭 서버 연결 키(아이폰 키체인, 안드로이드 Keystore에 보관)
- 🔒 줄을 잠그는 열쇠(아이폰 키체인, 안드로이드 Keystore에 보관)

아이폰은 iCloud나 컴퓨터로 폰을 백업할 때 이 정보도 백업에 포함됩니다. 🔒 줄은 암호화된 상태로만 저장됩니다. 아이폰에서는 🔒 열쇠가 iCloud 키체인을 통해 이용자의 다른 기기로 옮겨질 수 있습니다. 안드로이드에서는 열쇠가 기기 밖으로 나가지 않으므로, 폰을 바꾸면 🔒 줄을 열 수 없습니다.

앱을 지우면 폰에 저장된 정보도 함께 지워집니다.

## 2. 툭 서버와 AI로 보내는 정보

### 무엇을 보내나

| 언제 | 보내는 내용 |
| --- | --- |
| 던질 때(정리) | 글 원문, 링크 주소와 링크 미리보기(제목, 설명, 사이트 이름, 작성자, 대표 이미지 주소), 사진이면 줄인 사진과 찍은 시각, 주소(좌표는 보내지 않음), 지금 쓰는 목차 이름과 함께 나온 이름 목록, 현재 시각과 시간대 |
| 질문할 때 | 질문, 목차 이름, 질문과 관련된 저장 줄 일부(제목, 요약, 원문, 링크, 일정, 저장 시각) |
| 목록을 물을 때 | 질문, 관련 줄의 제목과 분류 |
| 일주일 정리(이번 주 툭) | 그 주에 던진 줄의 제목, 원문 일부, 상태 |
| 주제 묶기 | 목차 이름, 줄 수, 날짜, 대표 제목 몇 개 |

모든 요청에는 이 폰을 알아보는 연결 키가 함께 붙습니다. 🔒 줄은 어떤 요청에도 들어가지 않습니다.

### 어디로 가나

- **툭 서버(Cloudflare Workers)**: 요청을 받아 AI로 전달하고 결과를 돌려줍니다. 요청 내용을 저장하지 않습니다.
- **Anthropic(Claude API)**: 정리와 답을 만듭니다. Anthropic은 API로 받은 입력과 출력을 받은 날로부터 30일 안에 자동으로 지우며, 법률 준수나 이용 정책 위반 검토 같은 예외가 있습니다([Anthropic 보관 정책](https://privacy.claude.com/en/articles/7996866-how-long-does-anthropic-store-my-organizations-data)). API로 받은 데이터는 Anthropic의 상업용 약관에 따라 기본적으로 모델 학습에 쓰이지 않습니다.

## 3. 툭 서버에 저장되는 정보

툭 서버는 연결 관리와 사용량 한도를 위해 다음만 저장합니다. 서랍 내용은 저장하지 않습니다.

| 항목 | 내용 | 보관 기간 |
| --- | --- | --- |
| 초대 코드 | 코드의 해시값, 폰 이름, 사용량 묶음, 쓸 수 있는 횟수와 쓴 횟수, 하루 한도, 심사용 여부, 만든 시각, 만료 시각, 다 쓴 시각 | 만료 후 30일 |
| 연결된 폰 | 폰 이름, 연결 키의 해시값, 사용량 묶음, 하루 한도, 관리자 여부, 연결 시각, 연결 끊은 시각 | 연결을 끊고 30일 |
| 하루 사용량 | 폰 이름, 날짜, 호출 횟수(내용 없음) | 90일 |
| 잘못된 코드 시도 | 접속 IP의 해시값, 틀린 횟수, 시작 시각. 그리고 IP 없이 전체 틀린 횟수만 세는 기록 하나 | 성공하면 즉시, 아니면 하루 |

"해시값"은 서버만 아는 비밀값을 섞어서, 원래 값을 알아낼 수 없게 바꾼 값입니다.

서버 기록(로그)은 저장하지 않습니다. 문제를 확인할 때만 실시간으로 폰 이름, 요청 종류, 결과 상태, 오류 종류, 요청 크기를 봅니다. 서랍 내용은 기록에도 남지 않습니다.

툭 서버는 Cloudflare에서 돌아가므로, 앱이 서버에 접속할 때 Cloudflare가 접속 IP 주소를 받습니다. 툭은 이 IP를 저장하지 않지만, Cloudflare는 자체 정책에 따라 서비스 운영과 보안을 위해 처리할 수 있습니다.

## 4. 폰에서 다른 곳으로 직접 가는 정보

- **링크 미리보기**: 던진 링크의 제목 등을 읽으려고 폰이 그 사이트에 직접 접속합니다. 링크의 대표 이미지와 유튜브 썸네일은 그 줄이 화면에 보일 때마다 그 사이트(유튜브는 YouTube 이미지 서버)에서 불러옵니다. 이때 그 사이트는 이용자의 IP 주소를 볼 수 있습니다.
- **사진 위치를 주소로 바꾸기**: 사진에 위치가 있으면 폰 운영체제의 기능으로 주소를 찾습니다. 이때 좌표가 Apple(아이폰) 또는 Google(안드로이드)로 갑니다.
- **지도에서 보기**: 줄 카드에서 "지도에서 보기"를 누르면 장소 이름이나 주소가 Apple 지도 또는 Google 지도로 갑니다.
- **캘린더(켠 경우)**: 약속과 그날 할 일의 제목, 시각, 장소, 툭으로 돌아오는 링크를 폰 캘린더에 넣습니다. 원문은 넣지 않습니다. 캘린더가 iCloud나 Google 계정과 동기화되어 있으면 이 내용도 Apple 또는 Google 서버로 동기화됩니다. 🔒 줄은 넣지 않습니다.
- **알림**: 폰 안에서만 예약되는 알림입니다. 푸시 서버를 쓰지 않습니다. 잠금 화면에 알림 내용이 보일 수 있습니다. 할 일과 약속 알림에는 그 줄의 제목이, 아침 브리핑에는 그날 줄의 제목 목록이, 이번 주 툭에는 정리 문장이 나옵니다. 잠금 화면에 보이지 않게 하려면 폰의 알림 설정에서 "미리보기 표시"를 끄면 됩니다.
- **앱 업데이트 확인**: 앱이 새 버전을 확인하려고 Expo(EAS Update) 서버에 접속합니다. 이때 플랫폼, 앱 버전, 업데이트 경로, 지금 쓰는 업데이트 번호, 설치마다 만들어지는 무작위 번호가 갑니다.
- **전체 내보내기**: 이용자가 직접 고른 곳으로만 파일을 보냅니다. 🔒 줄은 들어가지 않습니다.
- **TestFlight(베타 테스트 중)**: 앱이 멈추면 Apple이 충돌 기록을 모으고, 테스터가 직접 보낸 피드백과 스크린샷을 운영자에게 전달합니다.

광고, 분석, 추적 도구는 쓰지 않습니다.

## 5. 처리를 맡기는 곳과 국외 이전

툭은 아래 업체의 서비스를 이용합니다. 이 업체들의 서버는 대한민국 밖에 있을 수 있으며, 정보는 앱을 쓸 때 인터넷을 통해 전송됩니다.

| 업체 | 하는 일 | 가는 정보 | 위치 |
| --- | --- | --- | --- |
| Anthropic, PBC | AI 정리와 답 만들기 | 2절의 내용 | 미국 |
| Cloudflare, Inc. | 툭 서버 운영 | 2절과 3절의 내용 | 전 세계 데이터센터 |
| Expo(650 Industries, Inc.) | 앱 업데이트 배포 | 4절의 업데이트 확인 정보 | 미국 |
| Apple, Google | 주소 변환, 지도, 캘린더 동기화, TestFlight | 4절의 해당 정보 | 미국 등 |

이 정보 이전을 원하지 않으면 해당 기능을 끄거나(캘린더, 사진 위치), 🔒로 시작하는 줄로 저장하거나, 앱을 쓰지 않을 수 있습니다. 이 경우 정리와 질문 기능은 쓸 수 없습니다.

## 6. 이용자의 권리

- **보기와 내보내기**: 앱의 설정에서 "전체 내보내기"로 내 서랍 전체를 파일로 받을 수 있습니다.
- **지우기**: 줄은 앱에서 바로 지울 수 있고, 앱을 지우면 폰의 정보가 모두 지워집니다.
- **연결 끊기**: 설정의 "연결 끊기"를 누르면 폰의 연결 키가 지워지고 서버의 연결도 끊깁니다. 서버에 남은 연결 기록은 3절의 기간이 지나면 지워집니다.
- **문의**: 서버에 남은 내 기록을 바로 지우고 싶거나 궁금한 점이 있으면 아래 연락처로 알려 주세요.

## 7. 안전하게 지키는 방법

- 서버와의 모든 통신은 암호화(HTTPS)됩니다.
- 연결 키와 초대 코드는 서버에 해시값으로만 저장합니다.
- 🔒 줄은 폰 안에서 AES-256 방식으로 암호화해 저장하고, 열쇠는 운영체제의 보안 저장소에만 둡니다.
- 폰마다 하루 사용량에 한도가 있고, 잘못된 초대 코드를 여러 번 넣으면 막힙니다.

## 8. 어린이

툭은 만 14세 미만 어린이를 대상으로 하지 않습니다.

## 9. 방침이 바뀌면

내용이 바뀌면 이 페이지를 고치고 맨 위 시행일을 바꿉니다. 중요한 변경은 앱 안에서도 알립니다.

## 10. 운영자와 연락처

- 운영자: [이름]
- 이메일: [연락 이메일]

---

## Summary in English

Tuk is a personal "drawer" app. Your notes, links, photos and questions are stored only on your device.

- **What is sent**: When Tuk organizes an item or answers a question, only the text needed for that task (and a resized photo, if any) is sent through our server, which runs on Cloudflare Workers, to Anthropic's Claude API. Items starting with 🔒 are never sent anywhere.
- **What our server keeps**: Our server does not store your content. It keeps only hashed connection keys and invite codes, device names, and daily request counts.
- **Anthropic**: Anthropic deletes API inputs and outputs within 30 days, with exceptions such as legal or policy review, and does not use API data for model training by default.
- **Directly from your phone**: Link previews and thumbnails are loaded from the linked site directly. "Open in Maps" sends the place name to Apple or Google Maps. Photo locations are converted to addresses by Apple or Google. Calendar entries contain only the title, time, place and a link back to Tuk, and may sync to iCloud or Google. Update checks go to Expo.
- **Tracking**: Tuk has no ads, analytics or tracking.
- **Your control**: You can export or delete your data in the app at any time. Contact: [email]
