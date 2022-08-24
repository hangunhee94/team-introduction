# :pushpin: Team Introduction
>나의 팀원을 소개합니다!    
>https://github.com/hangunhee94/team-introduction   

</br>

## 1. 제작 기간 & 참여 인원
- 2022년 4월 20일 ~ 4월 22일
- 팀 프로젝트
- 4인  

</br>

## 2. 사용 기술
#### `Back-end`
  - Flask

#### `Front-end`
  - HTML5
  - CSS3
  
</br>

## 3. 핵심 기능
이 프로젝트의 핵심 기능은 웹페이지를 통해 프로젝트의 팀원을 소개하는 것입니다.  
사용자는 팀원들의 가벼운 인사말과 TMI를 제공받을 수 있습니다.  

## 4. 핵심 트러블 슈팅
### 4.1. flask 배포 후 캐시메모리 오류
- 배포 후 웹페이지를 접속하고 새로고침 or 기능을 실행 하였을 때, 무한 로딩에 갇히는 상황이 발생
![무한로딩](https://user-images.githubusercontent.com/104430302/186332226-19457837-b3e7-4a1b-a050-51fe76aeb360.png)

- 확인 결과 여러 플랫폼 중 Safari에서는 정상적으로 작동 하였고, 그 외 크롬,엣지,웨일 등 똑같은 오류가 발생    
  캐시 메모리가 초기화되지 않았을 때 발생하는 것으로 보여져 캐시 메모리 삭제 후 실행하니 정상 작동
  하지만, 정상 작동 후 다시 캐시 메모리가 생겨나 같은 오류 반복 발생

- flask 캐시 삭제 기능을 추가 하여 해결
```
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response
```
</br>

## 5. 회고 / 느낀점
>프로젝트 개발 회고 글: https://hee94.tistory.com/6  
