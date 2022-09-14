# Secured_Post

쇼핑몰 서비스 백엔드 데이터베이스 및 API 개발
<br>
<br>

## MVP Service
유저가 상품을 조회 / 주문 할 수 있으며 아래와 같은 기능을 제공한다.

- 유저
    
    유저는 이용자, 관리자로 나누어져 있으며 
    
    회원가입/회원정보 조회/회원정보수정/회원탈퇴/로그인/로그아웃 의 기능이 있음 
    
    - 정보
        - 이름
        - 비밀번호
        - 배송지
        - 사용자 유형
            - 이용자
            - 관리자(is_admin)
- 상품
    
    관리자는 상품 등록/수정/삭제 권한이 있으며, 이용자는 조회만 가능함
    
    - 정보
        - 상품 이름
        - 설명
        - 상품 금액
        - 배송비
        - 재고
        - 판매 상태
- 주문
    
    이용자는 판매중인 상품을 주문할 수 있으며 주문내역의 조회/취소가 가능함
    
    관리자는 이용자의 주문을 조회/수정/삭제될 수 있음
    
    - 정보
        - 주문자
        - 상품
        - 상품 수량
        - 주문날짜
        - 주문상태

<br>

## 💻 기술 스택

<div style='flex'>
<img src="https://img.shields.io/badge/Python3.9.5-3776AB?style=for-the-badge&logo=Python&logoColor=white" >
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<img src="https://img.shields.io/badge/Django REST framework-092E20?style=for-the-badge&logo=Django REST framework&logoColor=white">
</div>
<br>
<br>

## 👉 ERD

<img width="500" src="" />
<br>

## 🙏 API 명세서

<br>

## 📌 컨벤션

### ❓ Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링, 버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### ❓ Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### ❓ 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.

### 🚷 벼락치기의 규칙

- 컨벤션 지키기
- Commit 단위 지키기
- 말 이쁘게하기
- 문제를 마주하여 트러블을 겪었다면, 어떻게 해결을 했는지 공유를 해주기
- 각자의 작업을 미리 작성을 하여서 각자의 작업을 공유하기
<br>

## 💻 트러블슈팅