import model_api

TEST_CONTENT = ['КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР', 'КОНТЕНТ ЗАПР']

def get_content_for_query(query: str) -> list[object]:
    model_api.find(query) # обработка запроса пользователя
    return TEST_CONTENT # временно

def get_content_for_recs() -> list[object]:
    return ['КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК', 'КОНТЕНТ РЕК']