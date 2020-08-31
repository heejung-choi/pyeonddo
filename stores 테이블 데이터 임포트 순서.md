# stores 테이블 데이터 임포트 순서

1. CU
2. seven
3. gs25
4. emart24

5. ministop

```
 python manage.py dumpdata [app_name].[model.name] --indent [INDENT] > [fixture_name].json
 python manage.py dumpdata stores.Store --indent 2 > Store_data.json
```

