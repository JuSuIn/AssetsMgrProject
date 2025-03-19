from AssetsMgrToyProjectInternal.celery import debug_task

# Celery task를 호출
result = debug_task.apply_async(args=[1,2])  # self는 Celery가 자동으로 처리
print(result.get())  # 결과 확인