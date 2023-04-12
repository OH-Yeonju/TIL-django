**Django ORM 특징**

- 기본적으로 lazy loading
  
  \> orm함수를 호출할 때가 아닌 쿼리셋이 실제로 평가될 때 db를 호출한다
  
  \> 똑같은 데이터를 사용한다면 캐싱을 내부적으로 해둔다
  
  - lazy loading
    
    : data = Models.objects.all() > 이럴때는 아무런 콜 하지 않는다
    
    print(data), list(data)... 이럴 때만 데이터를 조회한다
    
    왜 이렇게 할까? *성능 개선을 위해서*,  비용 많이 드는 호출을 줄이고 해당 데이터가 필요한 시점에 데이터베이스 호출
    
    N+1 problem : 지연 로딩으로 인해 발생하는 문제
    
    \> 해결법 : 즉시 로딩으로...... 정참조시 select_related 역참조시 prefetch_related
  
  - select_related
    
    1 : 1 또는 N:1 참조 관계에서 사용
    
    SQL에서 INNER JOIN절을 활용
  
  - prefetch_related
    
    M:N또는 N:1 역참조 관계에서 사용
    
    SQL이 아닌 python 을 통한 JOIN이 진행됨
  
  - *limit 21* 



- django ORM - Caching
  
  - 특정 데이터를 불러온 후 재사용할경우 저장해둔 캐싱 사용
    
    \> 코드 순서에 따라 콜하는 횟수 달라질 수 있음
