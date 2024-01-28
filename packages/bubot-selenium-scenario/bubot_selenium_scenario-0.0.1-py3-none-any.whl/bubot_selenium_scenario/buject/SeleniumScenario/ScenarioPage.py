class ScenarioPage:
    page_url = ''

    @classmethod
    def is_page(cls, driver, current_url):
        if isinstance(current_url, str):
            current_url = current_url
        else:
            current_url = current_url.page_url

        if cls.page_url[-1] == '*':
            return current_url.startswith(cls.page_url[:-1])
        else:
            return current_url == cls.page_url

    @classmethod
    def is_loaded(cls, driver, *, current_url=None, destination=None):
        raise NotImplementedError()

    @classmethod
    def on_after_loaded(cls, scenario, *, destination=None):
        return True
